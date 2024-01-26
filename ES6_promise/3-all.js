import { uploadPhoto as promise1, createUser as promise2 } from './utils';

export default function handleProfileSignup() {
  return Promise.all([promise1(), promise2()])
    .then((results) => {
      const result = `${results[0].body} ${results[1].firstName} ${results[1].lastName}`;
      console.log(result);
    })
    .catch(() => console.log('Signup system offline'));
}
