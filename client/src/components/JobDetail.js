import React from 'react';

import jobStore  from '../stores/job-detail';
import jobActions from '../actions/job-actions';


class JobDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      job: jobStore.job
    };
  }

  componentDidMount() {
    jobStore.addChangeListener(
      this.jobStoreChangeHandler.bind(this)
    );
    jobActions.loadJobDetail(this.props.params.id);
  }

  componentWillUnmount() {
    jobStore.removeChangeListener(
      this.jobStoreChangeHandler
    );
  }

  render() {
    let job = this.state.job;
    if (!job) {
      return (
        <div></div>
      );
    }

    return (
      <div>
        <h2>
          Job Detail: {this.props.params.id}
        </h2>
        <div>
          <strong>Url:</strong>
          {job.url}
        </div>
        <div>
          <strong>Status:</strong>
          {job.state}
        </div>
      </div>
    );
  }

  jobStoreChangeHandler() {
    this.setState(
      {
        job: jobStore.job
      }
    )
  }
}

export default JobDetail;
