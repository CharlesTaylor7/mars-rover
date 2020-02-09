export const rovers = [
  'Curiosity',
  'Opportunity',
  'Spirit',
];

export const fetchCameras = (rover) => fetch(`mars_rover/cameras/?rover=${rover}`).then((res) => res.json());

export const fetchPhotos = ({ rover, camera, method = 'ORM' }) => fetch(
  `mars_rover/photos/${rover}/${camera}/?method=${method}`,
).then((res) => res.json());
