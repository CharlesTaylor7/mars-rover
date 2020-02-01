import { useState, useCallback, useEffect } from 'react';
import { fetchPhotos } from '../api';

export default () => {
  const [rover, setRover] = useState('');
  const [camera, setCamera] = useState('');
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
      (async () => {
        const newPhotos = await fetchPhotos(rover, camera);
        setPhotos(newPhotos);
      })();
    },
    [rover, camera, setPhotos]
  );

  const [photoIndex, setPhotoIndex] = useState(0);

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
