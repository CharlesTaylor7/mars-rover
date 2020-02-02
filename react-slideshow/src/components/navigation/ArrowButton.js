import React from 'react';
import './ArrowButton.css';

const ArrowButton = ({ direction, handleClick }) => (
  <button className="arrow-button" onClick={handleClick} type="button">
    { direction === 'left' ? '<' : '>'}
  </button>
);

export default ArrowButton;
