// FUNCTIONS FOR INDEX

// Function to get the number of registered participants
function getNumberOfParticipants(event_id) {
    return fetch(`/get_participants/${event_id}`)
        .then(response => response.json())
        .then(participants => participants.length)
        .catch(error => console.error('Error:', error));
}

// Function to check if the user is registered for the event
function getParticipationStatus(event_id, user_id) {
    return fetch(`/get_participation_status/${event_id}/${user_id}`)
        .then(response => response.json())
        .then(data => data.participates)
        .catch(error => console.error('Error:', error));
}

function exportParticipants(event_id) {
    var url = "/export_participants/" + event_id;

    // Create a hidden link element
    var link = document.createElement("a");
    link.href = url;
    link.download = "participants.xlsx";
    
    // Append the link to the document body
    document.body.appendChild(link);
    
    // Simulate a click on the link to trigger the download
    link.click();

    // Remove the link from the document body
    document.body.removeChild(link);
}

function deleteUserEvent(event_id, user_id) {
    // Send a DELETE request
    fetch('/delete_user_event', {
        method: 'DELETE',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        user_id: user_id,
        event_id: event_id,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function addUserEvent(event_id, user_id, max_participants) {
    getNumberOfParticipants(event_id)
    .then(number_of_participants => {
        if (number_of_participants < max_participants) {
            // Send a POST request
            fetch('/add_user_event', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: user_id,
                    event_id: event_id,
                }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Server response:', data);
                location.reload();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else {
            alert('The event has reached the maximum number of participants');
        }
    });
}

function deleteEvent(event_id) {
    if (confirm('Are you sure you want to delete this event?')) {
        // Send a DELETE request
        fetch('/delete_event', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                event_id: event_id,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data);
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}


// FUNCTIONS FOR MANAGE GROUPS

function deleteUser(user_id, group_id) {
    if (confirm('Are you sure you want to remove this user from the group?')) {
        // Send a DELETE request
        fetch('/delete_user_group', {
            method: 'DELETE',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            user_id: user_id,
            group_id: group_id,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data);
            // Refresh the list of users inside the group
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

function deleteGroup(group_id) {
    if (confirm('Are you sure you want to delete this group?')) {
        // Send a DELETE request
        fetch('/delete_group', {
            method: 'DELETE',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            group_id: group_id,
            }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data);
            // Refresh the list of users inside the group
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

function isButtonChecked(buttonId) {
    const button = document.getElementById(buttonId);
    if (button) {
      return true;
    }
    return false; // Return false if the button with the given ID doesn't exist
  }