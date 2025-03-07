// JavaScript file for the Real Estate Finder website

// Function to fetch and display properties
function fetchProperties() {
    fetch('/api/properties')
        .then(response => response.json())
        .then(properties => displayProperties(properties))
        .catch(error => console.error('Error fetching properties:', error));
}

// Function to display properties on the page
function displayProperties(properties) {
    const propertyList = document.getElementById('propertyList');
    propertyList.innerHTML = '';

    properties.forEach(property => {
        const listItem = document.createElement('li');
        listItem.textContent = `${property.name} - ${property.location} - $${property.price}`;
        propertyList.appendChild(listItem);
    });
}

// Initialize the app
function initApp() {
    fetchProperties();
}

// Event listener for document ready
document.addEventListener('DOMContentLoaded', initApp);