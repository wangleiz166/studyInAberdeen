import express from 'express';

const app = express();

app.get('/test', function(req, res) {
    res.status(200);
    res.send('hello')
});

app.listen(8000);
console.log('Server is listening on port 8000');