const express = require('express')
const app = express()

const csv = require('csv-parser')
const fs = require('fs')
const user_array = []

const jwt = require('jsonwebtoken')

app.use(express.static('./static'))

fs.createReadStream('users.csv')
    .pipe(csv())
    .on('data', (data) => user_array.push(data))
    .on('end', () => {
        console.log(user_array);
    })

// fs.createReadStream('users.csv')
//     .pipe(csv())
//     .on('headers', (headers) =>{
//         console.log(`First headers: ${headers[0]}`)
//     })

app.get('/', function(req, res){
    res.send("Hello ID");
})

app.get('/login-form', function(req, res){
    res.sendFile(__dirname + '/html/loginForm.html');
})

app.get('/get-user-taxes', function(req, res){

})

app.post('/login/:email/:password', function(req, res){
    let user_email = req.params.email;
    let user_password = req.params.password;
    let token = jwt.sign({
        "email" : user_email,
        "password" : user_password 
    }, 'secret');
    res.status(200).send(token);
})

app.listen('80', function(err){
    if(err){
        console.log("Can't listen to port 80.");
        return;
    }
    console.log("Server is listening to port 80...")
})