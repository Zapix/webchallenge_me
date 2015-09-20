import {Component, PropTypes} from 'react';


class ErrorList extends Component {
  render() {
    let renderedErrorList = this.props.errors.map(
      (item) => {
        return (
          <div
            className="alert alert-warning"
            >
            {item}
          </div>
        )
      }
    );
    return (
      <div>
        {renderedErrorList}
      </div>
    );
  }
}
ErrorList.propTypes = {
  errors: PropTypes.array.isRequired
};

export default ErrorList;