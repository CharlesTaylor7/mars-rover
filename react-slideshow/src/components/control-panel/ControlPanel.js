import React from 'react';
import './ControlPanel.css';
import { rovers, cameras } from '../../api';
import Dropdown from './Dropdown';

const roverOptions = rovers.map(rover => ({ value: rover, display: rover }));
const cameraOptions = cameras.map(camera => ({ value: camera.name, display: camera.full_name }));

const ControlPanel = ({
  setRover, setCamera,
}) => (
  <div className="control-panel">
    <Dropdown label="Rover" handleSelect={setRover} options={roverOptions} />
    <Dropdown label="Camera" handleSelect={setCamera} options={cameraOptions} />
  </div>
);

export default ControlPanel;
