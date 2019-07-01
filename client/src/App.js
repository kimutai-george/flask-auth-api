import React,{Component} from 'react'
//import React from 'react';
import logo from './logo.svg';
//import './App.css';

import {BrowserRouter as Router, Route} from 'react-router-dom'

import Navbar from './components/Navbar'
import Landing from './components/Landing'
import Login from './components/Login'
import Register from './components/Register'
import Profile from './components/Profile'

class App extends Component {
  render() {


    return (
          <Router>
          <div className = "App">
          <Navbar/>
          <Route exact path = "/" component = {Landing}/>
            <div className="container">
              <Route exact path = "/Login" component = {Login}/>
              <Route exact path = "/Register" component = {Register}/>
              <Route exact path = "/Profile" component = {Profile}/>
            </div>
          </div>
          </Router>
          
  );
  }
 
}

export default App;
