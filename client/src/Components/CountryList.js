import React, { useEffect, useState } from 'react';

function CountryList() {
  const [countries, setCountries] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/countries')
      .then(response => response.json())
      .then(data => setCountries(data));
  }, []);

  return (
    <div>
      <h1>Countries</h1>
      <ul>
        {countries.map(country => (
          <li key={country.id}>{country.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CountryList;
