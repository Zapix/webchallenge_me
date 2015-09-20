import keyMirror from 'keyMirror';

export const JOB_ACTION_TYPES = keyMirror(
  {
    JOB_LIST_LOAD_SUCCEEDED: null,
    JOB_LIST_LOAD_FAILED: null,
    JOB_LIST_CLEAR: null,
    JOB_CREATE_SUCCEEDED: null,
    JOB_CREATE_FAILED: null,

    JOB_DETAIL_LOAD_SUCCEEDED: null,
    JOB_DETAIL_LOAD_FAILED: null
  }
);
