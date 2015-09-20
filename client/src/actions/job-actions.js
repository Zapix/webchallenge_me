import request from 'superagent'

import appDispatcher from '../dispatcher/app-dispatcher';
import {API_END_POINT} from '../constants/app-settings';
import {JOB_ACTION_TYPES} from '../constants/action-types';

export default {
  loadJobList(page=1) {
    console.log(API_END_POINT + '/job/');
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
              'type': JOB_ACTION_TYPES.JOB_LIST_LOAD_SUCCEEDED,
              'results': res.body.results,
              'next': res.body.next
            }
          );
        } else {
          appDispatcher.dispatch(
            {
              'type': JOB_ACTION_TYPES.JOB_LIST_LOAD_FAILED
            }
          );
        }
      }
    );
  },

  clearJobList() {
    appDispatcher.dispatch({'type': JOB_ACTION_TYPES.JOB_LIST_CLEAR});
  }
};