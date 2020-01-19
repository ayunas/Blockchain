import React, {useEffect, useState} from 'react';
import axios from 'axios';

export default function Transaction({base_url}) {
    const [transaction, setTransaction] = useState({sender: '', receiver: '', amount: ''})
    const [isPosting, setIsPosting] = useState(false)
    const [message, setMessage] = useState({message : null})

    const postTransaction = (e) => {
        setIsPosting(true)
        console.log('e', e)
        e.preventDefault()
        console.log('transaction', transaction);
        axios.post(`${base_url}/transactions/new`, transaction)
        .then(res => {
            console.log(res.data)
            setMessage(res.data)
            setIsPosting(false)   
            setTransaction({sender: '', receiver: '', amount: ''})         
        })
        .catch(err => console.log(err.response))
    }

    const handleChange = (e) => {
        console.log('e', e.target.name, e.target.value)
        setTransaction({
            ...transaction,     
            [e.target.name] : e.target.value
        })
        console.log('transaction', transaction)
    }

    return (
        <div id="transaction">
           <form onSubmit={postTransaction}>
                <label>
                    <span>Sender: </span>
                    <input name="sender" type="text" value={transaction.sender} onChange={handleChange} />
                </label><br/>
                <label>
                    <span>Receiver:</span>
                    <input name="receiver" type="text"value={transaction.receiver} onChange={handleChange} />
                </label><br/>
                <label>
                    <span>Amount:</span>
                    <input name="amount" type="number" value={transaction.amount} onChange={handleChange} />
                </label><br/>
                <button type="submit">Add Transaction</button>
           </form>
           <div id="post-message">{message.message}</div>
        </div>
    )
}

