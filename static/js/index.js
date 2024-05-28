function filterTable() {
    // Get the input value and convert it to lower case for case-insensitive comparison
    const query = document.getElementById('search-input').value.toLowerCase();

    // Get all rows of the table body
    const rows = document.querySelectorAll('#institutions-table tbody tr');

    // Loop through the rows and hide those that don't match the query
    rows.forEach(row => {
        const code = row.cells[1].textContent.toLowerCase();
        const name = row.cells[2].textContent.toLowerCase();
        if (code.includes(query) || name.includes(query)) {
            row.style.display = ''; // Show row
        } else {
            row.style.display = 'none'; // Hide row
            }
        });
}


function validateForm(){
    var email = document.myform.email.value;
    var password = document.myform.password.value;
    var atpostion = email.indexOf("@");
    var dotposition = email.lastIndexOf(".");

    if (password==null || password==""){
        alert("Password cant be blank");
        return false;
    }
    else if (password.length < 8){
        alert("password must be atleast 8 character long");
        return false;
    }
    else if (atpostion < 1 || dotposition < atpostion + 2 || dotposition + 2 >= email.length){
        alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
        return false;
    }
}

// document.addEventListener('DOMContentLoaded', (event) => {
//     document.getElementById('signUpButton').addEventListener('click', () => {
//         const url = document.getElementById('signUpButton').getAttribute('data-url');
//         window.location.href = url;
//     });
// });