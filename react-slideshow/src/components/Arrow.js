import React, { useState } from 'react';
import './Arrow.css';
import { rovers, cameras } from '../api';

const Arrow = ({ direction, onClick }) => {
  return (
    <button className="arrow" onClick={onClick}>
      { direction === 'left' ? '<' : '>'}
    </button>
  );
}

export default Arrow;
