```Javascript
'use strict';

document.addEventListener('DOMContentLoaded', (event) => {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const resultContainer = document.getElementById('results');
    
    searchForm.addEventListener('submit', (event) => {
        event.preventDefault();
        searchProperties(searchInput.value);
    });

    async function searchProperties(keyword) {
        try {
            resultContainer.innerHTML = '';
            const response = await fetch(`/search?keyword=${keyword}`);
            const properties = await response.json();
            displayProperties(properties);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    function displayProperties(properties) {
        if (properties.length === 0) {
            resultContainer.innerHTML = '<p>No properties found.</p>';
            return;
        }

        properties.forEach((property) => {
            const propertyElement = document.createElement('div');
            const propertyHTML = `
                <h2>${property.name}</h2>
                <img src="${property.image}" alt="${property.name}">
                <p>${property.description}</p>
                <p>${property.price}</p>
                <a href="/property/${property.id}">View More</a>
            `;
            propertyElement.innerHTML = propertyHTML;
            resultContainer.appendChild(propertyElement);
        });
    }
});
```