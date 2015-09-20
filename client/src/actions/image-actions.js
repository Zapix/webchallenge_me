import request from 'superagent';

import appDispatcher from '../dispatcher/app-dispatcher';
import {API_END_POINT} from '../constants/app-settings';
import {IMAGE_ACTION_TYPES} from '../constants/action-types';

export default {
  loadImageList(jobId, page=1) {
    request
    .get(`${API_END_POINT}/job/${jobId}/image/`)
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
              type: IMAGE_ACTION_TYPES.IMAGE_LIST_LOAD_SUCCEEDED,
              results: res.body.results,
              next: res.body.next
            }
          );
        } else {
          appDispatcher.dispatch(
            {
              type: IMAGE_ACTION_TYPES.IMAGE_LIST_LOAD_FAILED
            }
          );
        }
      }
    );
  },

  clearImageList() {
    appDispatcher.dispatch(
      {
        type: IMAGE_ACTION_TYPES.IMAGE_LIST_CLEAR
      }
    );
  }
}