export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const message = { status: 200, body: 'success' };
      return message;
    })
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
