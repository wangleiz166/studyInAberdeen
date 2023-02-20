const express = require('express');

const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

//Save all logged in users
const users = [];

server.listen(8080, () => {
    console.log('Server started successfully');
});


//Handle static resources, set the public directory as a static resource
app.use(express.static('public'))

app.get('/', function(req, res) {
    res.redirect('/index.html');
});

//Listening for user connections
io.on('connection', (socket) => {
    //console.log('New user connection');
    //Listening for login requests from clients
    socket.on('login', data => {
        //Determine if there is a duplicate name by looking in the array to see if the name is present
        let user = users.find(item => item.username === data.username);
        if (user) {
            //This user exists, login failed
            socket.emit('loginError', { msg: 'Login failed' });
        } else {
            //The user does not exist, login was successful Store the user in the array first
            users.push(data);
            socket.emit('loginSuccess', data);

            //Broadcast message that someone has joined the chat room io.emit broadcast event
            io.emit('addUser', data);

            //Show people currently in the chat room
            io.emit('userList', users);

            //Save information about the user after successful login
            socket.username = data.username;
            socket.avatar = data.avatar;
        }
    });

    //Listening for user disconnect disconnect events
    socket.on('disconnect', () => {
        //Remove the current user from users,findIndex to find the subscript of the current user
        let idx = users.findIndex(item => item.username === socket.username);
        //Delete
        users.splice(idx, 1);
        //Broadcast someone leaving the chat room
        io.emit('delUser', {
            username: socket.username,
            avatar: socket.avatar
        })

        //Update userList
        io.emit('userList', users);
    })

    //Listening to chat messages
    socket.on('sendMessage', data => {
        //console.log(data);
        //Broadcast News
        io.emit('receiveMessage', data);
    })
});