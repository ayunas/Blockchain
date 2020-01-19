import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Spinner from 'react-bootstrap/Spinner';
import lambdashield from '../assets/Lambda_Avatar_Red.jpg'

export default function Mine({base_url}) {
    const [mined,setMined] = useState({});
    const [mineIt, setMineIt] = useState(false)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        axios.get(`${base_url}/mine`)
        .then(res => {
            console.log(res.data);
            setIsLoading(false)
            setMined(res.data)
        })
        .catch(err => console.log(err.response))
    },[mineIt])

    const mine = () => {
        setMineIt(!mineIt)
        setIsLoading(true)
    }

    return (
        <div className="mine">
            {isLoading ? <Spinner id="spinner" animation="grow" size="lg"/> : (
                    <div className="earn">
                        <h2>Earned One Lambda Coin!</h2>
                        <img id="lambdashield" src={lambdashield} />
                        <div className="mine-txs"> 
                            <span><strong>{mined.message}</strong></span><br/>
                            <span><strong>Transactions on Block {mined.index}: </strong></span>
                            {mined.transactions && mined.transactions.map(tx => (  
                            <div className="mine-tx">
                                <div><strong>Sender: </strong> {tx.sender == '0' ? 'LS Blockchain' : tx.sender}</div>
                                <div><strong>Receiver: </strong>{tx.receiver.length > 20 ? 'Miner' : tx.receiver}</div>
                                <div><strong>Amount: </strong>{tx.amount}</div>
                            </div>
                            )
                            )}
                        </div>
                    </div>
                )
            }
            <button onClick={mine}>{isLoading ? 'Mining Coin... Please Wait...' : 'Mine Another Coin'}</button>
        </div>
    )
}




        