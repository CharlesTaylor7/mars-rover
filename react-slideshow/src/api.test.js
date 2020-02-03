import { fetchPhotos } from './api';

describe('fetchPhotos', () => {
  test('integration test', async () => fetchPhotos({
    rover: 'Curiosity',
    camera: 'FHAZ',
  })
    .then((photos) => expect(photos).toMatchSnapshot()));
});
