export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      const message = { status: 200, body: 'Success' };
      resolve(message);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
