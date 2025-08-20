export default function createEmployeesObject(departmentName, employees) {
  const list = [];
  for (const emp of employees) list.push(emp);
  return { [departmentName]: list };
}
