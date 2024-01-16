export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  this.addNeighborhood = (newNeighbourhood) => {
    this.sanFranciscoNeighborhoods.push(newNeighbourhood);
    return this.sanFranciscoNeighborhoods;
  };
}
