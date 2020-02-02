import React from 'react';
import './Slideshow.css';
import ControlPanel from './control-panel/ControlPanel';
import useSlideshow from '../hooks/useSlideshow';
import Navigation from './navigation/Navigation';

const Slideshow = () => {
  const {
    setRover, setCamera, photo, nextPhoto, prevPhoto,
  } = useSlideshow();
  return (
    <div className="slideshow">
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
      />
      { photo &&
        <>
          <img className="rover-photo" src={photo.url} />
          <Navigation
            prevPhoto={prevPhoto}
            nextPhoto={nextPhoto}
          />
        </>
      }
    </div>
  );
};

export default Slideshow;
