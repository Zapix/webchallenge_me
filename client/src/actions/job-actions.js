import request from 'superagent';

import appDispatcher from '../dispatcher/app-dispatcher';
import {API_END_POINT} from '../constants/app-settings';
import {JOB_ACTION_TYPES} from '../constants/action-types';

export default {
  loadJobList(page=1) {
    request
    .get(`${API_END_POINT}/job/`)
    .query(
      {
        page: page
      }
    )
    .end(
      (err, res) => {
        if (res.ok) {
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_LIST_LOAD_SUCCEEDED,
              results: res.body.results,
              next: res.body.next
            }
          );
        } else {
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_LIST_LOAD_FAILED
            }
          );
        }
      }
    );
  },

  clearJobList() {
    appDispatcher.dispatch({type: JOB_ACTION_TYPES.JOB_LIST_CLEAR});
  },

  loadJobDetail(jobId) {
    request
    .get(`${API_END_POINT}/job/${jobId}`)
    .end(
      (err, res) => {
        if (res.ok) {
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_DETAIL_LOAD_SUCCEEDED,
              job: res.body
            }
          );
        } else {
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_DETAIL_LOAD_FAILED
            }
          );
        }
      }
    );
  },

  createJob(url) {
    request
    .post(`${API_END_POINT}/job/`)
    .send(
      {
        url: url
      }
    )
    .end(
      (err, res) => {
        if(res.ok) {
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_CREATE_SUCCEEDED,
              job: res.body,
              status: res.status
            }
          );
        } else {
          console.log(res.body, res.status);
          appDispatcher.dispatch(
            {
              type: JOB_ACTION_TYPES.JOB_CREATE_FAILED,
              errors: res.body,
              status: res.status
            }
          );
        }
      }
    );
  },

  clearCreateJob() {
    appDispatcher.dispatch(
      {
        type: JOB_ACTION_TYPES.JOB_CREATE_CLEAR
      }
    )
  }
};