fetch('http://127.0.0.1:5000/analyse/average/feeling')
    .then(function (response) {
        return response.json();
    })
    .then(html => {
        document.getElementById("data").innerHTML = html;
    })


//https://stackoverflow.com/questions/55057801/how-can-i-use-fetch-api-to-populate-a-div