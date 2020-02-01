import React, { useState } from 'react';
import './Slideshow.css';
import { rovers, cameras } from '../api';
import Arrow from './Arrow';
import ControlPanel from './ControlPanel';

const Slideshow = () => {
  const url = 'https://cdn.theatlantic.com/assets/media/img/mt/2019/07/PIA22486_MAIN/lead_720_405.jpg?mod=1562072594';
  const [rover, setRover] = useState('');
  const [cameras, setCameras] = useState([]);

  const onChange = event => {
    console.log(event)
    setRover(event.target.value);
  }
  return (
    <>
      <ControlPanel />
      <img className="rover-photo" src={url} />
    </>
  );
}

export default Slideshow;
