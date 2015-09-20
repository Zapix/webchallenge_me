import BaseStore from './base';
import {JOB_ACTION_TYPES} from '../constants/action-types';


class JobCreateStore extends BaseStore {
  constructor() {
    super();
    this._responseStatus = null;
    this._errors = null;
    this._job = null;

    this._addHandler(
      JOB_ACTION_TYPES.JOB_CREATE_SUCCEEDED,
      this.jobCreateSucceeded.bind(this)
    );
    this._addHandler(
      JOB_ACTION_TYPES.JOB_CREATE_FAILED,
      this.jobCreateFailed.bind(this)
    );
    this._addHandler(
      JOB_ACTION_TYPES.JOB_CREATE_CLEAR,
      this.jobCreateClear.bind(this)
    );
  }

  jobCreateSucceeded(action) {
    this._responseStatus = action.status;
    this._job = action.job;
    this._errors = null;
    this.emitChange();
  }

  jobCreateFailed(action) {
    this._responseStatus = action.status;
    this._job = null;
    this._errors = action.errors;
    this.emitChange();
  }

  jobCreateClear(action) {
    this._responseStatus = null;
    this._job = null;
    this._errors = null;
  }

  get isCreated() {
    return this._responseStatus == 201;
  }

  get errors() {
    return this._errors;
  }

  get job() {
    return this._job;
  }
}

export default new JobCreateStore();
