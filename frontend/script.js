// Function that creates events
function createEvents(apiUrl) {
    return function(e) {
        e.preventDefault();
        
        const eventName = document.getElementById('eventName').value;
        const eventDate = document.getElementById('eventDate').value;

        fetch(`${apiUrl}/api/events`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: eventName, date: eventDate }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            listEvents(apiUrl);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };
}

// Function that list events
function listEvents(apiUrl) {
    fetch(`${apiUrl}/api/events`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        const eventsList = document.getElementById('eventsList');
        eventsList.innerHTML = '';
        data.events.forEach(event => {
            const listItem = document.createElement('li');
            listItem.textContent = `${event.name} on ${event.date}`;
            eventsList.appendChild(listItem);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Load configuration from config.json
fetch('config.json')
    .then(response => response.json())
    .then(config => {
        const apiUrl = config.API_URL;
        
        // Create an Event
        document.getElementById('eventForm').addEventListener('submit', createEvents(apiUrl));

        // List Events
        listEvents(apiUrl);
    })
    .catch(error => console.error('Failed to load configuration:', error));
