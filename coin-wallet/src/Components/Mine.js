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
            {isLoading ? <Spinner animation="grow"/> : mined.transactions &&                       mined.transactions.map((tx,i) => (
                    <div className="tx">
                        <h2>Earned {tx.amount} Lambda Coin!</h2>
                        <img id="lambdashield" src={lambdashield} />
                    </div>
                ))
            }
            <button onClick={mine}>{isLoading ? 'Mining Coin' : 'Mine Coin'}</button>
        </div>
    )
}




        