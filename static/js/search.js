// async function fetchCourseData() {
//   try {
//     const response = await fetch('/package.json');
//     const data = await response.json();
//     return data.courses || []; // Handle potential missing "courses" property
//   } catch (error) {
//     console.error('Error fetching course data:', error);
//     // Handle fetching errors (display message, disable search functionality)
//   }
//   return []; // Return empty array on error or missing data
// }

// function searchCourses() {
//   async function performSearch() {
//     const courseData = await fetchCourseData(); // Get course data

//     const searchQuery = document.querySelector('.text-field').value.toLowerCase();
//     const tableBody = document.querySelector('tbody');
//     tableBody.innerHTML = ''; // Clear existing table content

//     const courses = courseData;

//     const matchingCourses = courses.filter(course => {
//       const courseNameLower = course.name?.toLowerCase() || ""; // Handle optional name
//       return courseNameLower.includes(searchQuery);
//     });

//     if (matchingCourses.length > 0) {
//       // Display matching courses in the table
//       // ... (implement logic to display matching courses in the table body)
//     } else {
//       // No matching courses found
//       // ... (display message or handle empty results)
//     }
//   }

//   performSearch(); // Call the search logic asynchronously
// }

// function createCell(text) {
//   const cell = document.createElement('td');
//   cell.textContent = text;
//   return cell;
// }

// document.addEventListener('DOMContentLoaded', () => {
//   const cells = document.querySelectorAll('.clickable-cell');
//   cells.forEach(cell => {
//     cell.addEventListener('click', () => {
//         window.location.href = cell.dataset.href;
//     });
//   });

//   const searchInput = document.querySelector('.text-field');
//   searchInput.addEventListener('keyup', searchCourses);
// });