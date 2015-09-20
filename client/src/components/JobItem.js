import React from 'react';
import {PropTypes} from 'react';
import {Link} from 'react-router';


class JobItem extends React.Component {
  render() {
    let job = this.props.job;
    let viewJobButton = null;

    if (job.state == 'finished') {
      viewJobButton = (
        <Link
          to={`/job-list/${job.id}`}
          >
          View results
        </Link>
      )
    }

    return (
      <tr>
        <td>{job.url}</td>
        <td>{job.state}</td>
        <td>{viewJobButton}</td>
      </tr>
    );
  }
}
JobItem.propTypes = {
  'job': PropTypes.object.isRequired
};

export default JobItem;
