export default function createReportObject(employeesList) {
  const allEmployees = {
    allEmployees: { ...employeesList },
    getNumberOfDepartments: () => {
      const departments = Object.keys(employeesList);
      return departments.length;
    },

  };
  return allEmployees;
}
