fetch('http://127.0.0.1:5000/analyse/average/feeling')
    .then(function (response) {
        return response.json();
    })
    .then(html => {
        document.getElementById("data").innerHTML = html;
    })
