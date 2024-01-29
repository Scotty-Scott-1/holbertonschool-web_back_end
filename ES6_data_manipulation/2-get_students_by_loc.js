export default function getStudentsByLocation(students, city) {
  let myArray = [];
  myArray = students.filter((student) => student.location === city);
  return myArray;
}
