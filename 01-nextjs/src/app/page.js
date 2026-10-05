import SearchBar from "./SearchBar";

export default function HomePage() {
  var course1 = "Data Structures";
  var course2 = "Web Development";
  var course3 = "Linear Algebra";
  var courseList = [course1, course2, course3];

  return (
    <main style={{ padding: "40px" }}>
      <h1>Student Course Catalog</h1>
      <ul>
        <li>{courseList[0]}</li>
        <li>{courseList[1]}</li>
        <li>{courseList[2]}</li>
      </ul>
      <h2>Search Courses</h2>
      <SearchBar />
    </main>
  );
}