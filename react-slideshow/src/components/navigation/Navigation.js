import React from 'react';
import ArrowButton from './ArrowButton';

const Navigation = ({ prevPhoto, nextPhoto, prevDisabled, nextDisabled }) => (
  <div className="navigation-buttons">
    <ArrowButton direction="left" handleClick={prevPhoto} disabled={prevDisabled} />
    <ArrowButton direction="right" handleClick={nextPhoto} disabled={nextDisabled} />
  </div>
);

export default Navigation;
