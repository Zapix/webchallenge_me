import {Component, PropTypes} from 'react';


class ImageTableRow extends Component {
  render() {
    let image = this.props.image;
    return (
      <tr>
        <td>
          <a
            href={image.image}
            target="_blank"
            >
            {image.filename}
          </a>
        </td>
        <td>
          {image.width}x{image.height}
        </td>
        <td>
          {image.size}
        </td>
      </tr>
    );
  }
}
ImageTableRow.propTypes = {
  'image': PropTypes.object.isRequired
};

export default ImageTableRow;
