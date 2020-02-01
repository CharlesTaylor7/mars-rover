import React from 'react';
import './Arrow.css';

const Arrow = ({ direction, handleClick }) => (
  <button className="arrow" onClick={handleClick} type="button">
    { direction === 'left' ? '<' : '>'}
  </button>
);

export default Arrow;
