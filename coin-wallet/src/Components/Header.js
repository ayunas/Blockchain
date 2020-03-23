import React from 'react';
import lambdashield from '../assets/Lambda_Avatar_Red.jpg';
import {NavLink} from 'react-router-dom';

export default function Header() {

    return (
        <header className="App-header">
          <div>
            <img id="lambdashield" src={lambdashield}/>
            <h1>Lambda School (LS) Coin</h1>
          </div>
          <nav className="header-links">
            {/* <Link to="/">Home</Link> */}
            <NavLink to="/chain">BlockChain</NavLink>
            <NavLink to="/mine">Mine Coin</NavLink>
            <NavLink to="/transactions/new">Add Transaction</NavLink>
            <NavLink to="/wallet">Wallet</NavLink>
          </nav>
      </header>
    )
}