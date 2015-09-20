import React from 'react/addons';
import reactMixin from 'react-mixin';
import {Button} from 'react-bootstrap'

import Header from './Header';
import ErrorList from './ErrorList';
import jobActions from '../actions/job-actions';
import jobCreateStore from '../stores/job-create';


let LinkedStateMixin = React.addons.LinkedStateMixin;


class AddJob extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: '',
      isCreated: jobCreateStore.isCreated,
      job: jobCreateStore.job,
      errors: jobCreateStore.errors
    };
  }

  componentDidMount() {
    jobCreateStore.addChangeListener(
      this.jobCreateStoreChangeHandler.bind(this)
    );
  }

  componentWillUnmount() {
    jobCreateStore.removeChangeListener(
      this.jobCreateStoreChangeHandler.bind(this)
    );
    jobActions.clearCreateJob();
  }

  renderForm() {
    let renderedErrorList;

    if (this.state.errors) {
      renderedErrorList = <ErrorList errors={this.state.errors.url} />
    }
    return (
      <div>
        <Header title="Add job" />
        <form onSubmit={(event) => {this.addJob(event);}}>
          <div>
            <input
              className="form-control"
              placeholder="Url"
              valueLink={this.linkState('url')}
              />
          </div>
          {renderedErrorList}
          <div>
            <Button
              bsStyle="success"
              type="submit"
              >
              Add job
            </Button>
          </div>
        </form>
      </div>
    );
  }

  renderSuccessMessage() {
    return (
      <div>
        <Header title="Job started" />
        <p>Please check job list</p>
      </div>
    );
  }

  render() {
    if (this.state.isCreated) {
      return this.renderSuccessMessage();
    }
    return this.renderForm();
  }

  addJob() {
    event.preventDefault();
    jobActions.createJob(this.state.url);
  }

  jobCreateStoreChangeHandler() {
    this.setState(
      {
        isCreated: jobCreateStore.isCreated,
        job: jobCreateStore.job,
        errors: jobCreateStore.errors
      }
    )
  }
}
reactMixin(AddJob.prototype, LinkedStateMixin);

export default AddJob
