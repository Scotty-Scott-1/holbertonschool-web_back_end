export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8array = new Int8Array(buffer);
  try {
    int8array[position] = value;
    const dataView = new DataView(buffer);
    return {
      byteLength: dataView.byteLength,
      byteOffset: int8array.byteOffset,
      buffer,
    };
  } catch (error) {
    throw new Error('Position outside range');
  }
}
