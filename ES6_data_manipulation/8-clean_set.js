export default function cleanSet(set, startString) {
  let myStr = '';
  const len = startString.length;
  if (len === 0 || typeof startString !== 'string') {
    return myStr;
  }
  for (const element of set) {
    const sliced = element.slice(0, len);
    if (sliced === startString) {
      const newSlice = element.slice(len);
      myStr += newSlice;
      myStr += '-';
    }
  }
  const myNewStr = myStr.slice(0, -1);
  return myNewStr;
}
