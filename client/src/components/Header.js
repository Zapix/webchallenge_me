import React from 'react';

const {PropTypes} = React;


class Header extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="page-header">
        <h1>{this.props.title}</h1>
      </div>
    );
  }
}
Header.propTypes = {
  'title': PropTypes.string.isRequired
};

export default Header;
