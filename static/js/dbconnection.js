  
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-app.js";
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyCXrmzmNOaHIsoonCqILsDW1ONA_uXuJWU",
    authDomain: "careerhub-database.firebaseapp.com",
    databaseURL: "https://careerhub-database-default-rtdb.firebaseio.com",
    projectId: "careerhub-database",
    storageBucket: "careerhub-database.appspot.com",
    messagingSenderId: "910229715948",
    appId: "1:910229715948:web:3a42a1a1d0d6210cd99ec9",
    measurementId: "G-9XQVRH5D3J"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
 
document.getElementById("signup-form").addEventListener("submit", function(e){
    e.preventDefault();
    const userData = {
        firstName: document.getElementById("first-name").value,
        secondName: document.getElementById("second-name").value,
        surname: document.getElementById("surname").value,
        school: document.getElementById("school-attended").value,
        grade: document.getElementById("kcse-grade").value,
        password: document.getElementById("password").value,
        confirmPassword: document.getElementById("password1").value,
        email: document.getElementById("email").value,
        residence: document.getElementById("residence").value
    };

    if (userData.password !== userData.confirmPassword) {
        alert("Passwords do not match");
        return;
    }
    set(ref(db, 'users/' + userData.email.replace('.', '_')), userData)
        .then(() => {
            alert("Signup successful");
            window.location.href = '{{ url_for("display") }}';
        })
        .catch((error) => {
            alert("Error: " + error);
        });
});