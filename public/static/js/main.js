function login() {
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginpassword').value
    var csrf = document.getElementById('csrf').value

    if (username == '' && password == '') {
        alert('You must enter both')
    }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf,
            },

            'body': JSON.stringify(data)
        }).then(result => result.json())
        .then(response => {
            if (response.status == 200) {
                window.location.href = '/'
            } else {
                alert(response.message)
            }
        })
}

function register() {
    var username = document.getElementById('registerUsername').value
    var password = document.getElementById('registerpassword').value
    var csrf = document.getElementById('csrf').value

    if (username == '' && password == '') {
        alert('You must enter both')
    }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf,
            },

            'body': JSON.stringify(data)
        }).then(result => result.json())
        .then(response => {
            console.log(response)
            if (response.status == 200) {
                alert('You have successfully created your profile!')
                window.location.href = '/'

            } else {
                alert(response.message)
            }
        })
}