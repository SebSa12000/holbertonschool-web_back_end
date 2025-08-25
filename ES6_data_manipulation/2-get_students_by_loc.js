export default function getListStudentsIds(studentsList, location) {
    return studentsList.filter((name) => name.location === location);
}
