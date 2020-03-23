import React from 'react';
import wallet from '../assets/wallet.png';

export default function Wallet({base_url}) {

    return (
        <div class="wallet">
            <img id="wallet-img" src={wallet} />
            <div>This is Your Lambda School Coin Wallet</div>
        </div>
    )
}

