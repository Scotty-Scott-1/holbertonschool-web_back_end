import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  try {
    const promise1 = signUpUser(firstName, lastName);
    const promise2 = uploadPhoto(fileName);
    const result = await Promise.allSettled([promise1, promise2]);
    const results = [
      {
        status: result[0].status,
        value: result[0].status === 'fulfilled' ? result[0].value : result[0].reason,
      },
      {
        status: result[1].status,
        value: result[1].status === 'fulfilled' ? result[1].value : result[1].reason,
      },
    ];
    return results;
  } catch (error) {
    return error.message;
  }
}
