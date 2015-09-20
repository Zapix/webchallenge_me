import React from 'react';

import jobStore  from '../stores/job-detail';
import jobActions from '../actions/job-actions';
import ImageTable from './ImageTable';


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
          Job url: {job.url}
        </h2>
        <div>
          <strong>Status:</strong>
          {job.state}
        </div>
        <ImageTable jobId={job.id} />
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
