// FUNCTIONS FOR INDEX

// Función para obtener número de participantes apuntados
function obtenerNumeroParticipantes(event_id) {
    return fetch(`/obtener_participantes/${event_id}`)
        .then(response => response.json())
        .then(participantes => participantes.length)
        .catch(error => console.error('Error:', error));
}

// Función para saber si el usuario está apuntado al evento
function obtenerEstadoParticipacion(event_id, user_id) {
    return fetch(`/obtener_estado_participacion/${event_id}/${user_id}`)
        .then(response => response.json())
        .then(data => data.participa)
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
    // Realiza la solicitud DELETE
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
        console.log('Respuesta del servidor:', data);
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function addUserEvent(event_id, user_id, max_participantes) {
    obtenerNumeroParticipantes(event_id)
    .then(numero_participantes => {
        if (numero_participantes < max_participantes) {
            // Realiza la solicitud POST
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
                console.log('Respuesta del servidor:', data);
                location.reload();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        } else {
            alert('El evento ya tiene el número máximo de participantes');
        }
    });
}

function deleteEvent(event_id) {
    // Realiza la solicitud DELETE
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
        console.log('Respuesta del servidor:', data);
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}


// FUNCTIONS FOR MANAGE GROUPS

function deleteUser(user_id, group_id) {
    // Realiza la solicitud DELETE
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
        console.log('Respuesta del servidor:', data);
        // Refresh the list of users inside the group
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function deleteGroup(group_id) {
    // Realiza la solicitud DELETE
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
        console.log('Respuesta del servidor:', data);
        // Refresh the list of users inside the group
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}