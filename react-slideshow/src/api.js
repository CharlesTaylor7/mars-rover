export const rovers = [
  'Curiosity',
  'Opportunity',
  'Spirit',
];

export const cameras = [{ name: 'FHAZ', full_name: 'Front Hazard Avoidance Camera' }, { name: 'NAVCAM', full_name: 'Navigation Camera' }, { name: 'PANCAM', full_name: 'Panoramic Camera' }, { name: 'MINITES', full_name: 'Miniature Thermal Emission Spectrometer (Mini-TES)' }, { name: 'ENTRY', full_name: 'Entry, Descent, and Landing Camera' }, { name: 'RHAZ', full_name: 'Rear Hazard Avoidance Camera' }];

export const fetchPhotos = ({ rover, camera, method = 'ORM' }) => fetch(
  `photos/${rover}/${camera}/?method=${method}`,
).then((res) => res.json());
