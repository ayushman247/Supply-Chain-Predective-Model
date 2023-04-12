const firebaseApp= firebase.initializeApp({
    apiKey: "AIzaSyAeOhmREceHofpS0AAUBjdve1OyJ-SfHUo",
    authDomain: "out-of-form.firebaseapp.com",
    databaseURL: "https://out-of-form-default-rtdb.firebaseio.com",
    projectId: "out-of-form",
    storageBucket: "out-of-form.appspot.com",
    messagingSenderId: "472855709137",
    appId: "1:472855709137:web:afbc831a4993ef9abfccf0"
});
const db=firebaseApp.firestore();
const auth= firebaseApp.auth();

// Sign up function
const signUp = () => {
    const name = document.getElementById("signupName").value;
    const email = document.getElementById("signupEmail").value.trim();
    const password = document.getElementById("signupPassword").value;

    console.log(email, password)
    // firebase code
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in 
            document.write("You are Signed Up")
            console.log(result)
            // ...
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
            // ..
        });
}

// Sign In function
const signIn = () => {
    const name = document.getElementById("signInName").value;
   // const email = document.getElementById("email").value;
    const password = document.getElementById("signInPassword").value;
    // firebase code
    firebase.auth().signInWithEmailAndPassword(name, password)
        .then((result) => {
            // Signed in 
            document.write("You are Signed In")
            console.log(result)
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
        });
}