import React from 'react';
import {PropTypes} from 'react';
import {Button, Table} from 'react-bootstrap';

import imageActions from '../actions/image-actions';
import imageStore from '../stores/image-list';
import ImageTableRow from './ImageTableRow';

class ImageTable extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      imageList: imageStore.imageList,
      hasNext: imageStore.hasNext,
      nextPage: 1
    };
  }

  componentDidMount() {
    imageStore.addChangeListener(
      this.imageListStoreChangeHandler.bind(this)
    )
    imageActions.loadImageList(this.props.jobId, this.state.nextPage);
  }

  componentWillUnmount() {
    imageStore.removeChangeListener(
      this.imageListStoreChangeHandler
    );
    imageActions.clearImageList()
  }

  render() {
    let loadMoreButton;
    if (this.state.hasNext) {
      loadMoreButton = (
        <Button
          bsStyle="success"
          onClick={() => {this.loadMore()}}
          >
          Load more
        </Button>
      );
    }

    let renderedImageList = this.state.imageList.map(
      (item) => {
        return <ImageTableRow image={item}/>
      }
    );

    return (
      <div>
        <Table hover>
          <thead>
            <tr>
              <th>Img name</th>
              <th>Sizes</th>
              <th>Size in bytes</th>
            </tr>
          </thead>
          <tbody>
            {renderedImageList}
          </tbody>
        </Table>
        <div>
          {loadMoreButton}
        </div>
      </div>
    )
  }

  imageListStoreChangeHandler() {
    this.setState(
      {
        imageList: imageStore.imageList,
        hasNext: imageStore.hasNext,
        nextPage: imageStore.hasNext ? ++this.state.nextPage : null
      }
    );
  }

  loadMore() {
    imageActions.loadImageList(this.props.jobId, this.state.nextPage);
  }
}
ImageTable.propTypes = {
  'jobId': PropTypes.number.isRequired
};

export default ImageTable
