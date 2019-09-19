const request = require('request');

request('https://jcodemoi333288trial.hanatrial.ondemand.com/jco_demo', (err, res, body) => {
    bodyJSON = JSON.parse(body);
    console.log(bodyJSON)
});

