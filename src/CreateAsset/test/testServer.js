const express = require('express');
let app = express();

app.get('/', (req, res) => {
    res.send('Hello World!');
    res.end();
});

app.post('/', (req, res) => {
    console.log('Hello POST!');
    res.end();
});

let server = app.listen(50021, () => {
        let host = server.address().address;
        let port = server.address().port;

        console.log("http://%s:%s", host, port);
    })
;
