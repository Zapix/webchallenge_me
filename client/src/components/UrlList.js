import React from 'react';
import {
  Link
} from 'react-router';
import {
  Table
} from 'react-bootstrap';

import Header from './Header';

import jobActions from '../actions/job-actions';


export default class UrlList extends React.Component {
  constructor() {
    super();
    jobActions.loadJobList();
  }

  render() {
    return (
      <div>
        <Header title="Url List"/>
        <div
          className="col-md-12"
          >
          <div className="pull-right">
            <Link
              className="btn btn-primary"
              to="/add-job"
              >
              Add Job
            </Link>
          </div>
        </div>
        <Table hover>
          <thead>
            <tr>
              <th>Link</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
          </tbody>
        </Table>
      </div>
    );
  }
}
