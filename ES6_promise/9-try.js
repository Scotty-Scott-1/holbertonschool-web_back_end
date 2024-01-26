export default function guardrail(mathFunction) {
  const queue = [];
  const message = 'Guardrail was processed';
  const error = 'Error: cannot divide by 0';

  try {
    const result = mathFunction();
    queue.push(result);
  } catch (err) {
    queue.push(error);
  } finally {
    queue.push(message);
  }
  return queue;
}
