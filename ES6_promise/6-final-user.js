import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  const results = [];
  try {
    const promise1 = await signUpUser(firstName, lastName);
    results.push({
      status: 'fulfilled',
      value: promise1,
    });

    const promise2 = await uploadPhoto(fileName);
    results.push({
      status: 'fulfilled',
      value: promise2,
    });
  } catch (error) {
    results.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return results;
}
