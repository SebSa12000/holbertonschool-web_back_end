export default function getListStudentsIds(studentsList) {
  if (!Array.isArray(studentsList)) return 0;
  var arr = studentsList.map((studentsList) => studentsList.id);
  return arr.reduce(
  (total, arr) => total + arr,
  0,
);
}
