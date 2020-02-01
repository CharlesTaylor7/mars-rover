import React from 'react';
import './ControlPanel.css';
import { rovers, cameras } from '../api';
import ArrowButton from './ArrowButton';

const ControlPanel = ({
  setRover, setCamera, prevPhoto, nextPhoto,
}) => (
  <div className="control-panel">
    <select onChange={(event) => setRover(event.target.value)}>
      {rovers.map((rover, index) => (
        <option key={index}>{rover}</option>
      ))}
    </select>
    <select
      disabled={!cameras || !cameras.length}
      onChange={(event) => setCamera(event.target.value)}
    >
      {cameras.map((camera, index) => (
        <option key={index} value={camera.name}>{camera.full_name}</option>
      ))}
    </select>
    <div className="navigation-buttons">
      <ArrowButton direction="left" handleClick={prevPhoto} />
      <ArrowButton direction="right" handleClick={nextPhoto} />
    </div>
  </div>
);

export default ControlPanel;
