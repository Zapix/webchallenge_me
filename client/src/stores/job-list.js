import BaseStore from './base';
import {JOB_ACTION_TYPES} from '../constants/action-types';


class JobListStore extends BaseStore {
  constructor() {
    super();
    this._jobList = [];
    this._next = null;

    this._addHandler(
      JOB_ACTION_TYPES.JOB_LIST_LOAD_SUCCEEDED,
      this.listLoadSucceeded.bind(this)
    );
    this._addHandler(
      JOB_ACTION_TYPES.JOB_LIST_CLEAR,
      this.listClear.bind(this)
    );
  }

  listLoadSucceeded(action) {
    this._jobList.push(...action.results);
    this._next = action.next;
    this.emitChange();
  }

  listClear() {
    this._jobList = [];
    this._next = null;
    this.emitChange();
  }

  get jobList() {
    return this._jobList;
  }

  get hasNext() {
    return !!this._next;
  }
}

export default new JobListStore();
