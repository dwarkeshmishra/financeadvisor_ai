import React, { useState } from 'react';
import axios from 'axios';

const Advisor = () => {
  const [input, setInput] = useState('');
  const [advice, setAdvice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/getAdvice', { input });
      setAdvice(response.data.advice);
    } catch (error) {
      console.error('Error fetching advice', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter your financial query"
        />
        <button type="submit">Get Advice</button>
      </form>
      {advice && <p>{advice}</p>}
    </div>
  );
};

export default Advisor;
