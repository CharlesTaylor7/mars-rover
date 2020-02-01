import React, { useState, useCallback } from 'react';
import './Slideshow.css';
import { rovers, cameras } from '../api';
import Arrow from './Arrow';
import ControlPanel from './ControlPanel';

const Slideshow = () => {
  const url = 'https://cdn.theatlantic.com/assets/media/img/mt/2019/07/PIA22486_MAIN/lead_720_405.jpg?mod=1562072594';
  const [rover, setRover] = useState('');
  const [cameras, setCameras] = useState([]);
  const [camera, setCamera] = useState('');
  const [photos, setPhotos] = useState([1,2,3]);
  const [photoIndex, setPhotoIndex] = useState(0);
  const nextPhoto = useCallback(
    () => setPhotoIndex(i => Math.min(i + 1, photos.length - 1)),
    [photos]
  );
  const prevPhoto = useCallback(
    () => setPhotoIndex(i => Math.max(i - 1, 0)),
    []
  );
  console.log(photoIndex)
  const photoUrl = photos[photoIndex];
  const controlPanelProps = { setRover, setCamera, prevPhoto, nextPhoto};
  return (
    <>
      <ControlPanel {...{controlPanelProps}} />
      <img className="rover-photo" src={photoUrl || url} />
    </>
  );
}

export default Slideshow;
