import React from 'react';
import ArrowButton from './ArrowButton';

const Navigation = ({ prevPhoto, nextPhoto }) => (
  <div className="navigation-buttons">
    <ArrowButton direction="left" handleClick={prevPhoto} />
    <ArrowButton direction="right" handleClick={nextPhoto} />
  </div>
);

export default Navigation;
