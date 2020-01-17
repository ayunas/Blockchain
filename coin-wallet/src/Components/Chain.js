import React, {useState, useEffect} from 'react';
import axios from 'axios';

export default function Chain({base_url}) {
    
    const [chain, setChain] = useState([])

    useEffect(() => {
        axios.get(`${base_url}/chain`)
        .then(res => {
            console.log(res.data)
            setChain(res.data.chain)
        })
        .catch(err => console.log(err))
    },[])

    return (
        <div>
            <ul>
                {chain.map(block => (
                    <div className="chain">
                        {/* <li>{JSON.stringify(block)}</li> */}
                        <li>Block Index: {block.index}</li>
                        <li>Previous Hash: {block.prev_hash}</li>
                        <li>Proof: {block.proof}</li>
                        <li>Timestamp: {block.timestamp}</li>
                        {block.transactions.map((tx,i) => (
                        <div className="tx">
                            <h2>Transaction: {i+1}</h2>
                            <li>Sender: {tx.sender ? tx.sender : 'network'}</li>
                            <li>Receiver: {tx.receiver}</li>
                            <li>Amount: {tx.amount}</li>
                        </div>
                        ))}
                    </div>
                    )
                )}
            </ul>
        </div>
    )
}
