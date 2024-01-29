export default function getListStudentIds(students) {
  let myArray = [];

  if (Array.isArray(students) === false) {
    return myArray;
  }

  myArray = students.map((student) => student.id);
  return myArray;
}
