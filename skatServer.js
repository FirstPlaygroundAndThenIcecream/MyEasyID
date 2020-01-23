const express = require('express')
const app = express()

const mongoOperation = require('./mongodbOperation')

const csv = require('csv-parser')
const fs = require('fs')
const user_array = []

const jwt = require('jsonwebtoken')

app.use(express.static('./static'))


app.get('/login-form', function(req, res){
    res.sendFile(__dirname + '/html/loginForm-skat.html');
})


app.get('/get-user-taxes', function(req, res){
    let token = req.query.token;
    let secret = 'example_key'
    try{
        let decoded_token = jwt.verify(token, secret)
        let userEmail = {"email": decoded_token["email"]}
        mongoOperation.findUserByEmil(userEmail, function(foundUser){
            let msg = {
                name: foundUser.name, //decoded_token["name"] is decoding directly from the token, user b@b.com has name A in the token
                email: decoded_token["email"],
                tax: foundUser.taxes
            }
            console.log(msg)
            res.status(200).send(msg)
        })        
    } catch(err){
        res.send("Sorry, something is wrong.")
    }
})


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