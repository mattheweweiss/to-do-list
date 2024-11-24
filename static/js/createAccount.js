// Disallows use of certain characters
// Allowed characters are a-z, A-Z, 0-9, !, @, #, $, &, *, ?
function stopBadCharacter(event) {

    // Prevents bad character from being added to password
    if (!passwordCharacters.includes(event.key)) {
        event.preventDefault();

        // In Internet Explorer
        return false;
    }

    return true;

}




// Prevents form from being submitted
function preventFormSubmission(event) {
    event.preventDefault();
    window.alert("Passwords must match");
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


    // Gets submit button
    const createAccountForm = document.getElementById("create-account-form");



    // Adds event handler that prevents form submission if passwords do not match
    // Removes event handler that prevents form submission if password match
    if (password != confirmPassword) {

        // Prevents form submission
        createAccountForm.addEventListener("submit", preventFormSubmission);

    } else {

        // Allows form submission
        createAccountForm.removeEventListener("submit", preventFormSubmission);

    }

}