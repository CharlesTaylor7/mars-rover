export const rovers = [
  'Curiosity',
  'Oppurtunity',
  'Spirit',
];

export const cameras = [{ name: 'FHAZ', full_name: 'Front Hazard Avoidance Camera' }, { name: 'NAVCAM', full_name: 'Navigation Camera' }, { name: 'PANCAM', full_name: 'Panoramic Camera' }, { name: 'MINITES', full_name: 'Miniature Thermal Emission Spectrometer (Mini-TES)' }, { name: 'ENTRY', full_name: 'Entry, Descent, and Landing Camera' }, { name: 'RHAZ', full_name: 'Rear Hazard Avoidance Camera' }];

/* eslint-disable-next-line */
export const fetchPhotos = async ({ rover, camera }) => [
  {
    img_src: 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG',
    earth_date: '2015-05-30',
    rover: {
      id: 5, name: 'Curiosity', landing_date: '2012-08-06', launch_date: '2011-11-26', status: 'active', max_sol: 2540, max_date: '2019-09-28', total_photos: 366206, cameras: [{ name: 'FHAZ', full_name: 'Front Hazard Avoidance Camera' }, { name: 'NAVCAM', full_name: 'Navigation Camera' }, { name: 'MAST', full_name: 'Mast Camera' }, { name: 'CHEMCAM', full_name: 'Chemistry and Camera Complex' }, { name: 'MAHLI', full_name: 'Mars Hand Lens Imager' }, { name: 'MARDI', full_name: 'Mars Descent Imager' }, { name: 'RHAZ', full_name: 'Rear Hazard Avoidance Camera' }],
    },
  }, {
    id: 102694,
    sol: 1000,
    camera: {
      id: 20, name: 'FHAZ', rover_id: 5, full_name: 'Front Hazard Avoidance Camera',
    },
    img_src: 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG',
    earth_date: '2015-05-30',
    rover: {
      id: 5, name: 'Curiosity', landing_date: '2012-08-06', launch_date: '2011-11-26', status: 'active', img_src: 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/rcam/RLB_486265291EDR_F0481570RHAZ00323M_.JPG', earth_date: '2015-05-30',
    },
  },
];
