export default function createEmployeesObject(departmentName, employees) {
    var list = [];
    for (let emp of employees)
        list.push(emp);
    return { departmentName : list };
}