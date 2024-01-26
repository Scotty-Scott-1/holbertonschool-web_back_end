export default function uploadPhoto(fileName = '') {
  const result = `${fileName} cannot be processed`;
  return Promise.reject(new Error(result));
}
