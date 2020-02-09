import React from 'react';
import './Slideshow.css';
import ControlPanel from './control-panel/ControlPanel';
import useSlideshow from '../hooks/useSlideshow';

const Slideshow = () => {
  const {
    setRover, setCamera, photo, navigation,
  } = useSlideshow();
  return (
    <div className="slideshow">
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
        navigation={navigation}
      />
      { photo
        && (
          <img className="rover-photo" src={photo.url} />
        )}
    </div>
  );
};

export default Slideshow;
