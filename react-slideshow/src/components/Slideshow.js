import React from 'react';
import './Slideshow.css';
import ControlPanel from './ControlPanel';
import useSlideshow from '../hooks/useSlideshow';

const Slideshow = () => {
  const {
    setRover, setCamera, photo, nextPhoto, prevPhoto,
  } = useSlideshow();
  return (
    <>
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
        prevPhoto={prevPhoto}
        nextPhoto={nextPhoto}
      />
      { photo && <img className="rover-photo" src={photo.url} />}
    </>
  );
};

export default Slideshow;
