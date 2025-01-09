import React, { useState, useEffect, useCallback } from "react";
import "./Slideshow.css";
import ControlPanel from "./control-panel/ControlPanel";
import useOnKeyDown from "../hooks/useOnKeyDown";
import { rovers, fetchCameras, fetchPhotos } from "../api";

export default function Slideshow() {
  const [rover, setRover] = useState(rovers[0]);
  const [camera, setCamera] = useState();
  const [cameras, setCameras] = useState([]);
  const [photos, setPhotos] = useState([]);
  const [photoIndex, setPhotoIndex] = useState(0);
  const prevDisabled = photoIndex <= 0;
  const nextDisabled = photoIndex >= photos.length - 1;

  const slideToNext = useCallback(
    () => setPhotoIndex((i) => Math.min(i + 1, photos.length - 1)),
    [setPhotoIndex, photos],
  );

  const slideToPrevious = useCallback(
    () => {
      setPhotoIndex((i) => Math.max(i - 1, 0))
      setClasses(["slide-rtl-in",])
      setCurrentClass("slide-rtl-in")
    }
    [setPhotoIndex],
  );

  useOnKeyDown(({ key }) => {
    if (key === "ArrowRight") {
      slideToNext();
    } else if (key === "ArrowLeft") {
      slideToPrevious();
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

  return (
    <div className="slideshow">
      <ControlPanel
        setRover={setRover}
        setCamera={setCamera}
        cameras={cameras}
        navigation={{
          prevDisabled,
          nextDisabled,
          prevPhoto: slideToPrevious,
          nextPhoto: slideToNext,
        }}
      />
      <Photo
        key={`slide-rtl-out-${photoIndex - 1}`}
        photo={photos[photoIndex - 1]}
        className="slide-out"
      />
      <Photo
        key={`slide-rtl-in-${photoIndex}`}
        photo={photos[photoIndex]}
        className="slide-in"
      />
    </div>
  );
}

function Photo(props) {
  return props.photo ? (
    <img className={`rover-photo ${props.className}`} src={props.photo.url} />
  ) : null;
}
