import { useState, useCallback, useEffect } from 'react';
import { fetchPhotos } from '../api';

export default () => {
  const [rover, setRover] = useState('');
  const [camera, setCamera] = useState('');
  const [photos, setPhotos] = useState([]);
  const [photoIndex, setPhotoIndex] = useState(0);

  useEffect(() => {
    (async () => {
      const newPhotos = await fetchPhotos(rover, camera);
      setPhotoIndex(0);
      setPhotos(newPhotos);
    })();
  },
  [rover, camera, setPhotos, setPhotoIndex]);

  const nextPhoto = useCallback(
    () => setPhotoIndex((i) => Math.min(i + 1, photos.length - 1)),
    [setPhotoIndex, photos],
  );

  const prevPhoto = useCallback(
    () => setPhotoIndex((i) => Math.max(i - 1, 0)),
    [setPhotoIndex],
  );

  const photo = photos[photoIndex];
  return {
    setRover, setCamera, photo, nextPhoto, prevPhoto,
  };
};
