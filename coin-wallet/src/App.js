import React,{useState, useEffect} from 'react';
import './App.scss';
import {Route,Link,Switch} from 'react-router-dom';
import Chain from './Components/Chain';
import Mine from './Components/Mine';
import Transactions from './Components/Transactions';
import lambdashield from './assets/Lambda_Avatar_Red.jpg'


function App() {
  const base_url = 'http://localhost:5000'

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <img src={lambdashield}/>
          <h1>Lambda School (LS) Coin</h1>
        </div>
        <nav className="header-links">
          <Link to="/">Home</Link>
          <Link to="/chain">BlockChain</Link>
          <Link to="/mine">Mine Coin</Link>
          <Link to="/transaction/new">Add Transaction</Link>
        </nav>
      </header>
      <main>
        <Route path="/mine">
          <Mine base_url={base_url}/>
        </Route>
        <Route path="/transactions/new">
          <Transactions base_url={base_url}/>
        </Route>
        <Route path="/chain">
          <Chain base_url={base_url}/>
        </Route>
      </main>
    </div>
  );
}

export default App;
