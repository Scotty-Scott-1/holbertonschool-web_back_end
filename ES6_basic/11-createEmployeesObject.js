export default function createEmployeesObject(departmentName, employees) {
  const myDict = {
    [departmentName]: employees,
  };
  return myDict;
}
