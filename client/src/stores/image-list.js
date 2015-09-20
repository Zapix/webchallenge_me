import BaseStore from './base';

import {IMAGE_ACTION_TYPES} from '../constants/action-types';


class ImageListStore extends BaseStore {
  constructor() {
    super();
    this._imageList = [];
    this._next = null;

    this._addHandler(
      IMAGE_ACTION_TYPES.IMAGE_LIST_LOAD_SUCCEEDED,
      this.imageListLoadSucceeded.bind(this)
    );
    this._addHandler(
      IMAGE_ACTION_TYPES.IMAGE_LIST_CLEAR,
      this.imageListClear.bind(this)
    );

  }

  imageListLoadSucceeded(action) {
    this._imageList.push(...action.results);
    this._next = action.next;
    this.emitChange();
  }

  imageListClear() {
    this._imageList = [];
    this._next = null
  }

  get imageList() {
    return this._imageList
  }

  get hasNext() {
    return !!this._next;
  }
}

export default new ImageListStore();