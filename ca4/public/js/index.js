   //Connect to socketio port:8080
   let socket = io('http://127.0.0.1:8080');

   //Define two global variables to hold username and avatar
   var username;
   var avatar;

   //Login click event
   $('#loginSubmit button').on('click', function() {
       //console.log($('#loginBox'))
       //console.log($('#loginUserName').val())
       //console.log($('#login_avatar li.now img').attr('src'))

       //Determine that the username and avatar selection cannot be empty
       if ($('#loginUserName').val() == "") {
           $('.nameTip').show()
       } else if ($('#login_avatar li.now img').attr('src') == undefined) {
           $('.avatarTip').show()
       } else {
           //Get the address of your username and avatar
           let username = $('#loginUserName').val().trim();
           let avatar = $('#login_avatar li.now img').attr('src');

           //Communicate with the server, transferring username and avatar to the server
           socket.emit('login', {
               username: username,
               avatar: avatar
           });

           //Login box hidden, dialog box displayed
           $('#loginBox').hide()
           $('#containerBox').show()
       }
   });

   //Send button click event
   $("#sendBox button").on("click", function() {
       //Get the value of an input
       var sendMessageValue = $("#sendMessage").val()
           //console.log(chatBox)
           //Determine that the message cannot be empty
       if (sendMessageValue == "") {
           alert("The message sent cannot be empty!")
       } else {
           //Send to server
           socket.emit('sendMessage', {
               msg: sendMessageValue,
               username: username,
               avatar: avatar
           })

           //Empty input content after sending
           $("#sendMessage").val("");
       }
   });

   //Screen capture carriage return event
   $(document).keyup(function(event) {
       if (event.keyCode == 13) {
           //Get the value of an input
           var sendMessageValue = $("#sendMessage").val()
               //Determine that the message cannot be empty
           if (sendMessageValue == "") {
               alert("The message sent cannot be empty!")
           } else {
               //console.log(chatBox)
               //Send to server
               socket.emit('sendMessage', {
                   msg: sendMessageValue,
                   username: username,
                   avatar: avatar
               })

               //Empty input content after sending
               $("#sendMessage").val("");
           }
       }
   });

   //Select the avatar, register a click event on the li, add the now class addClass:add a class siblings:remove the other classes on the li
   $('#login_avatar li').on('click', function() {
       $(this).siblings('li').removeClass('now');
       $(this).addClass('now');
   });

   //Time output method, user dialog box display using
   function getFormatDate() {
       var nowDate = new Date();
       var month = nowDate.getMonth() + 1 < 10 ? "0" + (nowDate.getMonth() + 1) : nowDate.getMonth() + 1;
       var date = nowDate.getDate() < 10 ? "0" + nowDate.getDate() : nowDate.getDate();
       var hour = nowDate.getHours() < 10 ? "0" + nowDate.getHours() : nowDate.getHours();
       var minute = nowDate.getMinutes() < 10 ? "0" + nowDate.getMinutes() : nowDate.getMinutes();
       var second = nowDate.getSeconds() < 10 ? "0" + nowDate.getSeconds() : nowDate.getSeconds();
       return month + "-" + date + " " + hour + ":" + minute + ":" + second;
   }

   $(function() {
       //Flashing status
       setInterval('set_word_bili()', 2000);
   })

   //Add blinking text effect to group chat
   function set_word_bili() {

       var color = ['red', 'green', 'black', 'blue'];

       $('.content').css('color', color[parseInt(Math.random() * color.length)]);

   }

   //Listen for failed login messages
   socket.on('loginError', data => {
       alert('Login failed, username already exists');
       $('#loginBox').show()
       $('#containerBox').hide()
   });

   //Listening for successful login messages
   socket.on('loginSuccess', data => {
       //Set up user information after successful login
       username = data.username;
       avatar = data.avatar;
   });

   //Listening to user list messages and creating connections for each user
   socket.on('userList', data => {
       $('.people-list ul').html(''); //Set the list to empty after each loop, otherwise it will be repeatedly stacked
       data.forEach(item => {
           //Add a system message from the tail
           $('.people-list ul').append(
               `<li class="clearfix">
                           <img src="${item.avatar}" alt="avatar">
                           <div class="about">
                               <div class="name">${item.username}</div>
                           </div>
                       </li>`
           )
       })
   });

   //Listening for new users joining
   socket.on('addUser', data => {
       //console.log(data)
       //Add a system message from scratch
       if (data.username != undefined) {
           $('.system').prepend(
               `<p class="message_system">
                <span class="content">${data.username} Joined the group chat</span>
            </p>`
           )
       }

   });

   //Listening for new users leaving
   socket.on('delUser', data => {
       //console.log(data)
       // Add a system message
       if (data.username != undefined) {
           $('.system').prepend(
               `<p class="message_system">
               <span class="content">${data.username} left the group chat</span>
           </p>`
           )
       }
   });


   //Listening to chat messages
   socket.on('receiveMessage', data => {
       var chatBox = $("#chatBox");
       var timeStr = getFormatDate();
       //Show received messages in the chat window
       //Determining whether a message is your own or someone else's
       if (data.username === username) {
           //Your own message
           chatBox.append(
               `<li class="clearfix">
                   <div class="message-data text-right">
                        <span class="message-data-time">${data.username}, ${timeStr}</span>
                   </div>
                   <div class="message my-message float-right">   
                       ${data.msg} 
                   </div>
               </li>`
           );
       } else {
           //Other people's news
           chatBox.append(
               `<li class="clearfix">
                   <div class="message-data">
                       <span class="message-data-time"> ${data.username}, ${timeStr}</span>
                   </div>
                   <div class="message other-message">
                       ${data.msg}   
                   </div>
               </li>`
           );
       }

       $('#chatHistory').scrollTop($('#chatHistory')[0].scrollHeight); //Keep the scrollbar always at the bottom
   })