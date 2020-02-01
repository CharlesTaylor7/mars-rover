import React from 'react';
import './ControlPanel.css';
import { rovers, cameras } from '../api';
import Arrow from './Arrow';

const ControlPanel = ({ setRover, setCamera, prevPhoto, nextPhoto}) => (
<div className="control-panel">
  <select onChange={(event) => console.log(event.target)}>
    {rovers.map((rover, index) => (
      <option key={index}>{rover}</option>
    ))
    }
  </select>
  <select disabled>
    {/* {cameras.map((camera, index) => (
      <option key={index}>{camera}</option>
    ))} */}
  </select>
  <div className="navigation-buttons">
    <Arrow direction="left" onClick={prevPhoto} />
    <Arrow direction="right" onClick={nextPhoto} />
  </div>
</div>
)



export default ControlPanel;
