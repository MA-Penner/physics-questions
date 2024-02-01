function sendEquation() {
    var userEquation = document.getElementById('userEquation').value;
    fetch('/compare', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ equation: userEquation }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.message;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
