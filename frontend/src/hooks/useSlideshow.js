/* eslint-disable */
import { useState, useCallback, useEffect } from "react";
import { fetchPhotos, fetchCameras, rovers } from "../api";
import useOnKeyDown from "./useOnKeyDown";

export default () => {
  const [rover, setRover] = useState(rovers[0]);
  const [camera, setCamera] = useState();
  const [cameras, setCameras] = useState([]);
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
  useOnKeyDown(({ key }) => {
    if (key === "ArrowRight") {
      nextPhoto();
    } else if (key === "ArrowLeft") {
      prevPhoto();
    }
  }, []);

  useEffect(() => {
    fetchCameras(rover).then((cameras) => {
      setCameras(cameras);
      if (cameras.length) {
        setCamera(cameras[0].name);
      }
    });
  }, [rover]);

  useEffect(() => {
    if (camera === undefined) return;
    fetchPhotos({ rover, camera }).then((photos) => {
      setPhotoIndex(0);
      setPhotos(photos);
    });
  }, [rover, camera, setPhotos, setPhotoIndex]);

  return {
    cameras,
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
