import React, { useState } from 'react';
import './Slideshow.css';
import { rovers, cameras } from '../api';

const Slideshow = () => {
  const url = 'https://cdn.theatlantic.com/assets/media/img/mt/2019/07/PIA22486_MAIN/lead_720_405.jpg?mod=1562072594';
  const [rover, setRover] = useState('');
  const [cameras, setCameras] = useState([]);

  const onChange = event => {
    console.log(event)
    setRover(event.target.value);
  }
  return (
    <div className="rover-slideshow">
      <div className="control-panel">
      <select onChange={onChange}>
        {rovers.map((rover, index) => (
          <option key={index}>{rover}</option>
        ))
        }
      </select>

      <select disabled>
         {cameras.map((camera, index) => (
          <option key={index}>{camera}</option>
        ))}
      </select>

      </div>

      <img className="rover-photo" src={url} />
    </div>
  );
}

export default Slideshow;
