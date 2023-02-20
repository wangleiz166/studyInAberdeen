const express = require('express');

const app = express();

//处理静态资源,把public目录设置为静态资源
app.use(express.static('public'))

app.get('/test', function(req, res) {
    res.status(200);
    res.send('hello')
});

app.listen(5000);
console.log('Server is listening on port 5000');