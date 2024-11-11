// Logs out
async function logout() {
    
    // Requests options for logout
    const requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        }
    };


    // Fetches route that logs out
    // Clears session
    // Returns url of homepage (refreshes page)
    await fetch('/logout', requestOptions)
        .then((response) => {

            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            return response.url;

        })
        .then((url) => {
            window.location.href = url;
        })
        .catch((error) => {
            console.log(`Could not log out: ${error}`);
        });
}




// Adds add form when the add button is clicked
function showFields() {
    document.getElementById("add-icon").classList.toggle("rotate");
    document.getElementById("add-fields").classList.toggle("hide");
}