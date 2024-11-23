// Logs out
async function logout() {
    
    // Request options for logout
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