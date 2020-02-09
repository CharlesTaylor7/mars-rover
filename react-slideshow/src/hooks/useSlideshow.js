import { useState, useCallback, useEffect } from 'react';
import { fetchPhotos, cameras, rovers } from '../api';

const loadImage = (src) => new Promise((resolve) => {
  const image = document.createElement('img');
  image.src = src;
  image.addEventListener('load', () => resolve(image));
});

export default () => {
  const [rover, setRover] = useState(rovers[0]);
  const [camera, setCamera] = useState(cameras[0].name);
  const [photos, setPhotos] = useState([]);
  const [photoIndex, setPhotoIndex] = useState(0);
  const prevDisabled = photoIndex <= 0;
  const nextDisabled = photoIndex >= photos.length - 1;

  const nextPhoto = useCallback(
    () => setPhotoIndex((i) => Math.min(i + 1, photos.length - 1)),
    [setPhotoIndex, photos],
  );

  const prevPhoto = useCallback(
    () => setPhotoIndex((i) => Math.max(i - 1, 0)),
    [setPhotoIndex],
  );

  const photo = photos[photoIndex];

  useEffect(() => {
    (async () => {
      const newPhotos = await fetchPhotos({ rover, camera });
      setPhotoIndex(0);
      setPhotos(newPhotos);
    })();
  },
  [rover, camera, setPhotos, setPhotoIndex]);

  useEffect(() => {
    (async () => {
      /* eslint-disable */
      for (const photo of photos) {
        await loadImage(photo.url);
      }
    })();
  },
  [photos]);

  return {
    setRover,
    setCamera,
    photo,
    navigation: {
      nextPhoto,
      prevPhoto,
      prevDisabled,
      nextDisabled,
    },
  };
};
