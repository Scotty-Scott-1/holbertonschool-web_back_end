export default function updateStudentGradeByCity(students, city, grades) {
  let myArray = [];
  let newArray = [];
  myArray = students.filter((student) => student.location === city);

  newArray = myArray.map((student) => {
    const matchingGrade = grades.find((grade) => grade.studentId === student.id);

    if (matchingGrade) {
      const studentupdated = { ...student, grade: matchingGrade.grade };
      return studentupdated;
    }
    const studentupdated = { ...student, grade: 'N/A' };
    return studentupdated;
  });
  return newArray;
}
