var { initializeApp } = require("firebase/app");
var { getAuth, createUserWithEmailAndPassword } = require("firebase/auth");
var firebaseConfig = require("./firebaseConfig.js");


var app = initializeApp(firebaseConfig);
var auth = getAuth(app);


function makeNewStudent(email, password) {
  createUserWithEmailAndPassword(auth, email, password)
    .then(function (result) {
      console.log("New student was created");
    })
    .catch(function (error) {
      console.log("Something went wrong");
      console.log(error.message);
    });
}
    
