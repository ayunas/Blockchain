import React,{useState, useEffect} from 'react';
import './App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

import {Route,Switch} from 'react-router-dom';
import Chain from './Components/Chain';
import Mine from './Components/Mine';
import Transactions from './Components/Transactions';
import Header from './Components/Header';

function App() {
  const base_url = 'http://localhost:5000'

  return (
  <>
    
    <div className="App">
        <Route path="/">
          <Header/>
        </Route>
        <Route path="/mine">
            <Mine base_url={base_url}/>
        </Route>
        <Route path="/transactions/new">
          <Transactions base_url={base_url}/>
        </Route>
        <Route path="/chain">
          <Chain base_url={base_url}/>
        </Route>
    </div>
  </>
  );
}

export default App;
