import BaseStore from './base';
import {JOB_ACTION_TYPES} from '../constants/action-types';


class JobDetailStore extends BaseStore {
  constructor() {
    super();
    this._job = null;

    this._addHandler(
      JOB_ACTION_TYPES.JOB_DETAIL_LOAD_SUCCEEDED,
      this.jobLoadSucceeded.bind(this)
    );
  }

  jobLoadSucceeded(action) {
    this._job = action.job;
    this.emitChange();
  }

  get job() {
    return this._job;
  }
}

export default new JobDetailStore()