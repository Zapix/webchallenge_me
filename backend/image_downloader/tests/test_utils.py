# -*- coding: utf-8 -*-
import os

import mock
from mock import MagicMock

from django.test import TestCase

from .. import utils


class GetImagesFromResponseTestCase(TestCase):

    def test_image_response(self):
        fake_url = 'http://fake-domain.com/img/test1.png'

        mock_response = MagicMock()

        mock_response.headers = {
            'content-type': 'image/jpeg'
        }
        mock_response.request = MagicMock()
        mock_response.request.url = fake_url

        links = utils.get_image_links_from_response(mock_response)

        self.assertEquals(len(links), 1)
        self.assertEquals(links[0], fake_url)

    def test_html_response(self):
        mock_response = MagicMock()

        mock_response.headers = {
            'content-type': 'text/html'
        }

        mock_parse_html = MagicMock()
        mock_parse_html.return_value = [
            'http://fake-url.com/img1.jpg',
            'http://fike-url.com/img2.png'
        ]

        get_images_from_html_patch = mock.patch(
            'image_downloader.utils.get_image_links_from_html',
            mock_parse_html
        )

        with get_images_from_html_patch:
            links = utils.get_image_links_from_response(
                mock_response
            )
            self.assertEquals(len(links), 2)

    def test_other_response(self):
        mock_response = MagicMock()

        mock_response.headers = {
            'content-type': 'text/plain'
        }

        links = utils.get_image_links_from_response(mock_response)

        self.assertEquals(len(links), 0)


class ImageHTMLParserTestCase(TestCase):

    def test_html_parsing(self):
        current_dir = os.path.dirname(__file__)
        html_file = open(os.path.join(current_dir, 'data/simple.html'), 'r')
        data = html_file.read()

        parser = utils.ImagesHTMLParser()
        parser.feed(data)

        image_links = parser.image_links
        self.assertEquals(len(image_links), 3)


class GetImageLinksFromHtmlTestCase(TestCase):

    def test_get_image_links_from_html(self):
        parser = MagicMock()
        parser.feed = MagicMock()
        parser.image_links = [
            'http://fake-domain.com/img/123.jpg',
            '/img/123.png'
        ]

        parser_class = MagicMock()
        parser_class.return_value = parser

        response = MagicMock()

        with mock.patch('image_downloader.utils.ImagesHTMLParser',
                        parser_class):
            links = utils.get_image_links_from_html(response)
            self.assertEquals(len(links), 2)


class PrepareImageLink(TestCase):

    def test_full_http_link(self):
        full_link = 'http://habrahabr.ru/img/test.jpg'
        response = MagicMock()

        prepared_link = utils.prepare_image_link(
            full_link,
            response
        )

        self.assertEquals(prepared_link, full_link)

    def test_full_https_link(self):
        full_link = 'https://habrahabr.ru/img/test.jpg'
        response = MagicMock()

        prepared_link = utils.prepare_image_link(
            full_link,
            response
        )

        self.assertEquals(prepared_link, full_link)

    def test_link_without_scheme(self):
        link = '//habrastorage.org/1/1231.png'

        response = MagicMock()
        response.request.url = 'http://webchallenge.me/test'

        prepared_link = utils.prepare_image_link(
            link,
            response
        )

        self.assertEquals(prepared_link, 'http:' + link)

    def test_absolute_link(self):
        link = '/img/src/test.png'

        response = MagicMock()
        response.request.url = 'https://docs.python.org/2/library/urlpars.html'

        prepared_link = utils.prepare_image_link(link, response)

        self.assertEquals(prepared_link, 'https://docs.python.org' + link)

    def test_relative_link_with_dir_url_end(self):
        link = 'img/src/test.png'

        response = MagicMock()
        response.request.url = 'https://docs.python.org/2/library/'

        prepared_link = utils.prepare_image_link(link, response)

        self.assertEquals(prepared_link, response.request.url + link)

    def test_relate_link_with_file_end(self):
        link = 'img/src/test.png'

        response = MagicMock()
        response.request.url = 'https://docs.python.org/2/library/urlpars.html'

        prepared_link = utils.prepare_image_link(link, response)

        self.assertEquals(
            prepared_link,
            'https://docs.python.org/2/library/' + link
        )


class GetImageLinksFromUrlTestCase(TestCase):

    def test_success(self):
        mock_requests = MagicMock()

        mock_requests.get = MagicMock()
        requests_patch = mock.patch(
            'image_downloader.utils.requests',
            mock_requests
        )

        mock_get_image_links_from_response = MagicMock()
        mock_get_image_links_from_response.return_value = [
            'http://fake_url.com/1.jpg',
            'http://fake_url.com/2.png'
        ]
        get_image_links_patch = mock.patch(
            'image_downloader.utils.get_image_links_from_response',
            mock_get_image_links_from_response
        )

        fake_prepeare_image_link = lambda image_link, response: image_link
        prepare_image_link_patch = mock.patch(
            'image_downloader.utils.prepare_image_link',
            fake_prepeare_image_link
        )

        with requests_patch, get_image_links_patch, prepare_image_link_patch:
            image_links = utils.get_image_links_from_url('http://fake_url.com')
            self.assertEquals(len(image_links), 2)


class GetImageFilenameFromResponseTestCase(TestCase):

    def test_get_filename_from_url(self):
        response = MagicMock()
        response.request.url = 'http://vk.com/test/image1.png'

        filename = utils.get_image_filename_from_response(response)

        self.assertEquals(filename, 'image1.png')

    def test_generate_filename(self):
        strftime_mock = MagicMock()
        strftime_mock.return_value = "20150916000000"
        mock_datetime = MagicMock()
        mock_datetime.datetime.now.return_value.strftime = strftime_mock
        patch_datetime = mock.patch(
            'image_downloader.utils.datetime',
            mock_datetime
        )

        mock_random = MagicMock()
        mock_random.randint.return_value = 1
        patch_random = mock.patch(
            'image_downloader.utils.random',
            mock_random
        )

        mock_mimetypes = MagicMock()
        mock_mimetypes.guess_extension.return_value = '.jpg'
        patch_mimetypes = mock.patch(
            'image_downloader.utils.mimetypes',
            mock_mimetypes
        )

        response = MagicMock()
        response.request.url = 'http:/google.com/test/dir/'

        with patch_datetime, patch_random, patch_mimetypes:
            filename = utils.get_image_filename_from_response(response)
            self.assertEquals(filename, '20150916000000-1.jpg')


class GetImageByUrlTestCase(TestCase):

    def get_requests_patch(self, response):
        """
        Return requests module patch with response for get request
        :param response:
        :return:
        """
        mock_requests = MagicMock()
        mock_requests.get.return_value = response
        return mock.patch(
            'image_downloader.utils.requests',
            mock_requests
        )

    def test_404_response(self):
        response = MagicMock()
        response.status_code = 404

        requests_patch = self.get_requests_patch(response)

        with requests_patch:
            image = utils.get_image_by_url('http://wrong-url.com/img/test.png')

            self.assertIsNone(image)

    def test_200_html_response(self):

        response = MagicMock()
        response.status_code = 200
        response.headers = {
            'content-type': 'text/html'
        }

        requests_patch = self.get_requests_patch(response)

        with requests_patch:
            image = utils.get_image_by_url('http://google.com')

            self.assertIsNone(image)

    def test_200_image_response(self):
        data_file = open(
            os.path.join(
                os.path.dirname(__file__),
                'data/googlelogo_color_272x92dp.png'
            ),
            'rb'
        )

        response = MagicMock()
        response.status_code = 200
        response.headers = {
            'content-type': 'image/png'
        }
        response.content(data_file.read())

        requests_patch = self.get_requests_patch(response)

        get_filename_fake = MagicMock()
        get_filename_fake.return_value = '1.png'
        get_filename_patch = mock.patch(
            'image_downloader.utils.get_image_filename_from_response',
            get_filename_fake
        )

        with requests_patch, get_filename_patch:
            image, filename = utils.get_image_by_url(
                'http://existing-image.com/img/1.png'
            )

            self.assertEquals(filename, '1.png')
