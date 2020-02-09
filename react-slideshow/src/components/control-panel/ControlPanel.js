/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import './ControlPanel.css';
import { rovers, cameras } from '../../api';
import Dropdown from './Dropdown';
import Navigation from '../navigation/Navigation';

const roverOptions = rovers.map((rover) => ({ value: rover, display: rover }));
const cameraOptions = cameras.map((camera) => ({ value: camera.name, display: camera.full_name }));

const ControlPanel = ({
  setRover, setCamera, navigation,
}) => (
  <div className="control-panel">
    <Dropdown label="Rover" handleSelect={setRover} options={roverOptions} />
    <Dropdown label="Camera" handleSelect={setCamera} options={cameraOptions} />
    <Navigation {...navigation} />
  </div>
);

export default ControlPanel;
