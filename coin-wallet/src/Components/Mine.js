import React, {useState, useEffect} from 'react';
import axios from 'axios';


export default function Mine({base_url}) {
    const [mined,setMined] = useState({})

    useEffect(() => {
        axios.get(`${base_url}/mine`)
        .then(res => {
            console.log(res.data);
            setMined(res.data)
        })
        .catch(err => console.log(err.response))
    },[])

    return (
        <div>
            {JSON.stringify(mined)}
        </div>
    )
}
