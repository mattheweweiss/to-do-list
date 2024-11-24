// Disallows use of certain characters
// Allowed characters are a-z, A-Z, 0-9, !, @, #, $, &, *, ?
function preventBadCharacter(event) {

    // Prevents bad character from being added to password
    if (!passwordCharacters.includes(event.key)) {
        event.preventDefault();

        // In Internet Explorer
        return false;
    }

    return true;

}




// Checks if passwords match
// Prevents form from being submitted if passwords do not match
function checkPasswordsMatch() {

    // Gets password input
    const passwordElement = document.getElementById("create-account-password");
    const password = passwordElement.value;


    // Gets confirm password input
    const confirmPasswordElement = document.getElementById("create-account-confirm-password");
    const confirmPassword = confirmPasswordElement.value;



    // Checks if passwords match
    if (password != confirmPassword) {
        // Adds event handler, input color, pop-up
        passwordsDoNotMatch();
    } else {
        // Removes event handler, input color, pop-up
        passwordsMatch();
    }

}




// Prevents form from being submitted
function preventFormSubmission(event) {
    event.preventDefault();
    window.alert("Passwords must match");
}




// if passwords do not match
// Adds event handler that prevents form submission
// Makes password inputs red
// Adds pop-up stating that passwords do not match
function passwordsDoNotMatch() {

    console.log("don't match");

    // Gets form
    const createAccountForm = document.getElementById("create-account-form");


    // Gets password input
    const passwordElement = document.getElementById("create-account-password");


    // Gets confirm password input
    const confirmPasswordElement = document.getElementById("create-account-confirm-password");


    // Prevents form submission
    createAccountForm.addEventListener("submit", preventFormSubmission);

        
    // Makes inputs red
    if (!passwordElement.classList.contains("no-submit")) {
        passwordElement.classList.add("no-submit");
    }

    if (!confirmPasswordElement.classList.contains("no-submit")) {
        confirmPasswordElement.classList.add("no-submit");
    }


    // Creates pop-up if not exists
    if (!document.getElementById("passwords-do-not-match-popup")) {
        createPasswordsDoNotMatchPopup();
    }

}




// Creates pop-up for passwords not matching
function createPasswordsDoNotMatchPopup() {
    
    // Gets password input
    // Pop-up will be inserted after this element
    const passwordElement = document.getElementById("create-account-password");


    // Creating the passwords do not match pop-up
    const passwordsDoNotMatchPopup = document.createElement("div");
    passwordsDoNotMatchPopup.id = "passwords-do-not-match-popup";
    passwordsDoNotMatchPopup.className = "hide password-popup";
    passwordsDoNotMatchPopup.innerText = "Passwords do not match";


    passwordElement.after(passwordsDoNotMatchPopup);


    // Allows for transition animation
    setTimeout(() => {
        passwordsDoNotMatchPopup.classList.remove("hide");
    }, 100);

}




// if passwords match
// Removes event handler that prevents form submission
// Returns password inputs to normal color
// Removes pop-up stating that passwords do not match
function passwordsMatch() {

    // Gets form
    const createAccountForm = document.getElementById("create-account-form");


    // Gets password input
    const passwordElement = document.getElementById("create-account-password");


    // Gets confirm password input
    const confirmPasswordElement = document.getElementById("create-account-confirm-password");


    // Allows form submission
    createAccountForm.removeEventListener("submit", preventFormSubmission);


    // Returns inputs to normal
    if (passwordElement.classList.contains("no-submit")) {
        passwordElement.classList.remove("no-submit");
    }

    if (confirmPasswordElement.classList.contains("no-submit")) {
        confirmPasswordElement.classList.remove("no-submit");
    }


    // Removes pop-up if exists
    if (document.getElementById("passwords-do-not-match-popup")) {
        document.getElementById("passwords-do-not-match-popup").remove();
    }

}