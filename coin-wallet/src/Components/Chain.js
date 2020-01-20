import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Search from './Search';

export default function Chain({base_url}) {
    
    const [chain, setChain] = useState([]);
    const [filtered,setFiltered] = useState([]);
    const [query, setQuery] = useState(null);
    // const [noResults, setNoResults] = useState(false);
    // const [displayChain, setDisplayChain] = useState(true);
    const [blockModal, setBlockModal] = useState({});
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        getChain()
    },[])   

    function getChain() {
        axios.get(`${base_url}/chain`)
        .then(res => {
            setChain(res.data.chain)
        })
        .catch(err => console.log(err))
    }

    useEffect(()=>{
        console.log('filtered', filtered)
    },[filtered])

    const filterQuery = (q) => {
        setQuery(q)
        console.log('query', query);
        // if (query > chain.length || !query) {
        //     setNoResults(true)
        // }
        console.log('query in filterQuery', query);
        const queryResult = chain.filter(b => b.index == q)[0];
        console.log('query result', queryResult);
        if (!queryResult) {
            setFiltered([])
        } else {
            setFiltered(queryResult);
        }
    }

    const blockDetail = (i) => {
        console.log(`blockdetail ${i} clicked`);
        setShowModal(!showModal)
        const shown = chain.find(b => b.index == i)
        const blockModalLength = Object.values(blockModal).length;
        if (blockModalLength) {
            setBlockModal({})
        } else {
            setBlockModal(shown)
        }
        
    }

    const filteredLength = Object.entries(filtered).length;
    


    return (
        <>
            <Search chain={chain} 
                    setChain={setChain} 
                    getChain={getChain}
                    filtered={filtered}
                    setFiltered={setFiltered}
                    filterQuery={filterQuery} 
            />
            <ul>
                {showModal && 
                            <div id="modal">
                                <li>Block {blockModal.index}</li>
                                <li>Previous Hash: {blockModal.prev_hash}</li>
                                <li>Proof: {blockModal.proof}</li>
                                <li>Timestamp: {blockModal.timestamp}</li>
                                {blockModal.transactions && blockModal.transactions.map((tx,i) => (
                                    <div className="tx">
                                        <h2>Transaction: {i+1}</h2>
                                        <li>Sender: {tx.sender ? tx.sender : 'network'}</li>
                                        <li>Receiver: {tx.receiver}</li>
                                        <li>Amount: {tx.amount}</li>
                                    </div>
                                ))}
                            </div>
                }
                {filteredLength ? 
                    <div className="block">
                        {/* <li>{JSON.stringify(block)}</li> */}
                        <li>Block Index: {filtered.index}</li>
                        <li>Previous Hash: {filtered.prev_hash}</li>
                        <li>Proof: {filtered.proof}</li>
                        <li>Timestamp: {filtered.timestamp}</li>
                        {filtered.transactions.map((tx,i) => (
                        <div className="tx">
                            <h2>Transaction: {i+1}</h2>
                            <li>Sender: {tx.sender ? tx.sender : 'network'}</li>
                            <li>Receiver: {tx.receiver}</li>
                            <li>Amount: {tx.amount}</li>
                        </div>
                        ))}
                    </div> : 
                    query > filteredLength || query < 0 || query === '0' ? <span>'No results found'</span> : 
                        chain.map( (block,i) => (
                        <div key={i} onClick={() => blockDetail(i+1)} className="block">
                            {/* <li>{JSON.stringify(block)}</li> */}
                            <li>Block {block.index}</li>
                            {/* <li>Previous Hash: {block.prev_hash}</li>
                            <li>Proof: {block.proof}</li>
                            <li>Timestamp: {block.timestamp}</li>
                            {block.transactions.map((tx,i) => (
                            <div className="tx">
                                <h2>Transaction: {i+1}</h2>
                                <li>Sender: {tx.sender ? tx.sender : 'network'}</li>
                                <li>Receiver: {tx.receiver}</li>
                                <li>Amount: {tx.amount}</li>
                            </div>
                            ))} */}
                        </div>
                        )
                )}
                
            </ul>
        </>
    )
}
