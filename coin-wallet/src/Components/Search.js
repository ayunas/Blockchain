import React,{useState} from 'react';

export default function Search(props) {
    const {filterQuery} = props;
    const [query,setQuery] = useState();

    const handleChange = (e) => {
        const query = e.target.value;
        filterQuery(query);
    }

    return (
        <label>
            <span>Block Number: </span>
            <input name="search" type="number" value={query} onChange={handleChange} />
        </label>
        
    )
}