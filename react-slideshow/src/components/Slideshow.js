import React from 'react';
import './Slideshow.css';

const Slideshow = () => {
  const url = 'https://cdn.theatlantic.com/assets/media/img/mt/2019/07/PIA22486_MAIN/lead_720_405.jpg?mod=1562072594'
  return (
    <div className="rover-slideshow">
      <img className="rover-photo" src={url} />
    </div>
  );
}

export default Slideshow;
