import React from 'react';
import {
  Link
} from 'react-router';
import {
  Table,
  Button
} from 'react-bootstrap';

import Header from './Header';
import JobItem from './JobItem';

import jobActions from '../actions/job-actions';
import jobListStore from '../stores/job-list';


class JobList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      jobList: jobListStore.jobList,
      hasNext: jobListStore.hasNext,
      nextPage: 1
    }
  }

  componentDidMount() {
    jobListStore.addChangeListener(
      this.listStoreChangeHandler.bind(this)
    );
    jobActions.loadJobList(this.state.nextPage);
  }

  componentWillUnmount() {
    jobActions.clearJobList();
    jobListStore.removeChangeListener(
      this.listStoreChangeHandler
    );
  }

  render() {
    if (this.props.children) {
      return <div>{this.props.children}</div>
    }
    let loadMoreButton = null;

    if (this.state.hasNext) {
      loadMoreButton = (
        <Button
          bsStyle="success"
          onClick={() => {this.loadMore()}}
          >
          Load more
        </Button>
      )
    }

    let jobRenderedList = this.state.jobList.map(
      (item) => {
        return <JobItem job={item} />
      }
    );

    return (
      <div>
        <Header title="Job List"/>
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
            {jobRenderedList}
          </tbody>
        </Table>
        <div>
          {loadMoreButton}
        </div>
      </div>
    );
  }

  listStoreChangeHandler() {
    this.setState(
      {
        jobList: jobListStore.jobList,
        hasNext: jobListStore.hasNext,
        nextPage: jobListStore.hasNext ? ++this.state.nextPage: null
      }
    );
  }

  loadMore() {
    jobActions.loadJobList(this.state.nextPage);
  }
}
//UrlList.getStores = function() {
//  return [jobListStore]
//};

export default JobList;
