import React, { useState, useCallback } from 'react';
import './Slideshow.css';
import ControlPanel from './ControlPanel';

const Slideshow = () => {
  const url = 'https://cdn.theatlantic.com/assets/media/img/mt/2019/07/PIA22486_MAIN/lead_720_405.jpg?mod=1562072594';
  const [rover, setRover] = useState('');
  const [cameras, setCameras] = useState([]);
  const [camera, setCamera] = useState('');
  const [photos, setPhotos] = useState([1,2,3]);
  const [photoIndex, setPhotoIndex] = useState(0);
  const nextPhoto = useCallback(
    () =>
      setPhotoIndex(i => Math.min(i + 1, photos.length - 1))
    ,
    [setPhotoIndex, photos]
  );
  const prevPhoto = useCallback(
    () =>
      setPhotoIndex(i => Math.max(i - 1, 0))
    ,
    [setPhotoIndex]
  );
  console.log(photoIndex)
  const photoUrl = photos[photoIndex];
  return (
    <>
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
        prevPhoto={prevPhoto}
        nextPhoto={nextPhoto}
      />
      <img className="rover-photo" src={photoUrl || url} />
    </>
  );
}

export default Slideshow;
