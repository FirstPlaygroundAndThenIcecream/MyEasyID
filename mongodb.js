const mongo = require('mongodb')
var MongoClient = mongo.MongoClient

let path = "mongodb://localhost:27017"; 

const dbName = "node1"
const collectionName = "skat"

// // //make connection to the server
// MongoClient.connect(path, ({useNewUrlParser: true, useUnifiedTopology: true}), function(err, client){
//     if (err) console.log("sorry, something is wrong...")
//     console.log("Connected to the server at 27017...")
//     const db = client.db(dbName)
//     client.close()
// })

// // //create a new collection which is called 'skat'
// MongoClient.connect(path, ({useNewUrlParser: true, useUnifiedTopology: true}), function(err, db) {
//     if (err) throw err;
//     let dbo = db.db(dbName);
//     dbo.createCollection(collectionName, function(err, res) {
//       if (err) throw err;
//       console.log("Collection created!");
//       db.close();
//     });
// }); 

// // //insert one doc which contains one user info
// MongoClient.connect(path, ({useNewUrlParser: true, useUnifiedTopology: true}), function(err, db){
//     if(err) throw err;
//     let dbo = db.db(dbName);
//     let user_info = {
//         name: "b", 
//         email: "b@b.com",
//         taxes: 200
//     };
//     dbo.collection(collectionName).insertOne(user_info, function(err, res){
//         if (err) throw err;
//         console.log("one doc is inserted");
//         db.close();
//     });
// });

//db operation can not return a value directly, therefore a callback function to handle the return value
module.exports.findUserByEmil = function(userEmail, callback){
    MongoClient.connect(path, ({useNewUrlParser: true, useUnifiedTopology: true}), function(err, db){
        if(err) throw err;
        let dbo = db.db(dbName);
        dbo.collection(collectionName).findOne(userEmail, function(err, user){
            if(err) throw err;
            db.close();
            return callback(user);
        });
    });
}
