import React from 'react';
import { Router, Route } from 'react-router';
import App from './components/App';
import JobList from './components/JobList';
import AddJob from './components/AddJob';
import About from './components/About';


window.React = React;


React.render(
  <Router>
    <Route path="/" component={App}>
      <Route path="/about" component={About}/>
      <Route path="/job-list" component={JobList}/>
      <Route path="/add-job" component={AddJob}/>
    </Route>
  </Router>
  , document.getElementById('content')
);
