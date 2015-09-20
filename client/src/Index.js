import React from 'react';
import { Router, Route } from 'react-router';
import App from './components/App';
import UrlList from './components/UrlList';
import AddJob from './components/AddJob';
import About from './components/About';


window.React = React;


console.log('Environment:', process.env.NODE_ENV);
console.log('Environment:', process.env.API_END_POINT);


React.render(
  <Router>
    <Route path="/" component={App}>
      <Route path="/about" component={About}/>
      <Route path="/url-list" component={UrlList}/>
      <Route path="/add-job" component={AddJob}/>
    </Route>
  </Router>
  , document.getElementById('content')
);
