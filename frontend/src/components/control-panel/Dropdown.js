import React from 'react';
import './Dropdown.css';

const Dropdown = ({ handleSelect, options, label }) => (
  <div className="dropdown">
    <div className="dropdown-label">
      {label}
      :
    </div>
    <select
      className="dropdown-select"
      onChange={(event) => handleSelect(event.target.value)}
    >
      {options.map((option, index) => (
        <option key={index} value={option.value}>{option.display}</option>
      ))}
    </select>
  </div>
);

export default Dropdown;
