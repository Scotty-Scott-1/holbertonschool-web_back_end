export default function getStudentIdsSum(students) {
  const sum = students.reduce((acumulator, student) => student.id + acumulator, 0);
  return sum;
}
