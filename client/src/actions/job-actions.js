import request from 'superagent'

import {API_END_POINT} from '../constants/app-settings'
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
        console.log(err, res);
        if (res.ok) {
          console.log("Ok");
          console.log(res);
        } else {
          console.log("Error");
          console.log(err);
        }
      }
    );
  }
};