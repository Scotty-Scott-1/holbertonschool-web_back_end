export default function signUpUser(firstName, lastName) {
  const result = { firstName, lastName };
  return Promise.resolve(result);
}
