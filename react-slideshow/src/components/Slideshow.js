/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import './Slideshow.css';
import ControlPanel from './control-panel/ControlPanel';
import useSlideshow from '../hooks/useSlideshow';
import Navigation from './navigation/Navigation';

const Slideshow = () => {
  const {
    setRover, setCamera, photo, navigation,
  } = useSlideshow();
  return (
    <div className="slideshow">
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
      />
      { photo
        && (
          <>
            <img className="rover-photo" src={photo.url} />
            <Navigation {...navigation} />
          </>
        )}
    </div>
  );
};

export default Slideshow;
