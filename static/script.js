document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const location = event.target.querySelector('input[type="text"]').value;
    
    if (location) {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<p>Searching for properties in ${location}...</p>`;
        
        // Simulate an API call
        setTimeout(() => {
            resultsDiv.innerHTML = `<p>Found some properties in ${location}.</p>`;
        }, 2000);
    }
});