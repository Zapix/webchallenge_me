# -*- coding: utf-8 -*-
import os
import random
import datetime
import mimetypes
from StringIO import StringIO
from urlparse import urlparse
from HTMLParser import HTMLParser

import requests

from django.core.files.images import ImageFile


class ImagesHTMLParser(HTMLParser):

    _image_links = []

    @property
    def image_links(self):
        return self._image_links

    def handle_startendtag(self, tag, attrs):
        if tag == 'img':
            self._image_links.append(dict(attrs)['src'])


def get_image_links_from_html(response):
    parser = ImagesHTMLParser()
    parser.feed(response.content.decode(response.encoding))
    return parser.image_links


def get_image_links_from_response(response):
    content_type = response.headers.get('content-type')

    if 'image' in content_type:
        return [response.request.url]
    if 'text/html' in content_type:
        return get_image_links_from_html(response)
    return []


def prepare_image_link(image_link, response):
    """
    Prepare link.
    If links starts from http:// or https:// then it is a full image link.
    If links starts from // then add scheme to link
    If link starts from / then add scheme and netloc
    If response.request.path finishes with '/' then add link
    Else get dirname for reqponse.request.path and join with link
    :param image_link:
    :param response:
    :return:
    """
    parsed_url = urlparse(response.request.url)

    if image_link.startswith('http://') or image_link.startswith('https://'):
        return image_link

    if image_link.startswith('//'):
        return '{}:{}'.format(parsed_url.scheme, image_link)

    if image_link.startswith('/'):
        return '{}://{}{}'.format(
            parsed_url.scheme,
            parsed_url.netloc,
            image_link
        )

    if parsed_url.path[-1] == '/':
        return '{}{}'.format(
            response.request.url,
            image_link
        )

    return '{}/{}'.format(
        os.path.dirname(response.request.url),
        image_link
    )


def get_image_links_from_url(url):
    """
    Get the resopnse for current url
    If url is html/text then parse it
    If url is image then return current url
    Else return empty list
    :param url:
    :return:
    """

    response = requests.get(url)

    return {
        prepare_image_link(image_link, response)
        for image_link in get_image_links_from_response(response)
    }


def get_image_filename_from_response(response):
    """
    Get image by url path.
    If there is no filename, then generate it.
    If filename hasn't got extension then try to get it from content type
    :param url:
    :return:
    """
    image_name = os.path.basename(
        urlparse(response.request.url).path
    )
    if not image_name:
        image_name = '{}-{}'.format(
            datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            random.randint(1, 100)
        )

    _, split_ext = os.path.splitext(image_name)

    if not split_ext:
        image_name = '{}{}'.format(
            image_name,
            mimetypes.guess_extension(
                response.headers.get('content-type'),
                False
            )
        )

    return image_name


def get_image_by_url(url):
    """
    Get image by url.
    If url status is 200 and response is image then return django image file
    and genereated name.
    Else return None
    :param url:
    :return:
    """
    response = requests.get(url)

    if (
        response.status_code != 200 or
        'image' not in response.headers.get('content-type')
    ):
        return None

    return (
        ImageFile(StringIO(response.content)),
        get_image_filename_from_response(response)
    )
