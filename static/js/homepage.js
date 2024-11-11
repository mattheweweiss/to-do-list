// Redirects to login page
async function login() {

    // Fetches route that renders login page
    await fetch('/login')
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
            console.error(`Could not load login page: ${error}`);
        });

}