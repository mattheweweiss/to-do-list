// Adds add form when the add button is clicked
function showFields() {
    document.getElementById("add-icon").classList.toggle("rotate");
    document.getElementById("add-fields").classList.toggle("hide");
}




// Adds task
async function addTask() {

    // Retrieves body to post to route
    const task = document.getElementById("task-input").value;
    const priority = document.getElementById("priority-input").value;


    // Adds task if task field has a value
    if (task) {

        // Creates dictionary of body data
        const body = {
            "task": task,
            "priority": priority
        };


        // Request options for adding task
        const requestOptions = {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify(body)
        };


        // Fetches route that adds task
        fetch('/add_task', requestOptions)
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
                console.log(`Could not add task: ${error}`);
            });

    }


}




// Marks task as complete
async function checkTask(event) {

    console.log(event);

    // Retrieves body to post to route
    const taskId = event.target.value;


    // Creates a dictionary of body data
    const body = {
        "taskId": taskId
    };


    // Request options for adding task
    const requestOptions = {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(body)
    };


    // Fetches route that marks task as complete
    fetch('/complete_task', requestOptions)
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
            console.log(`Could not mark task as complete: ${error}`)
        });


}