export default function updateUniqueItems(myMap) {
  if (myMap instanceof Map) {
    for (const [item, amount] of myMap) {
      if (amount === 1) {
        myMap.set(item, 100);
      }
    }
    return myMap;
  }
  throw new Error('Cannot process');
}
