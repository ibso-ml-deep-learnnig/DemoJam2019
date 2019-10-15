const request = require('request');

// request('https://jcodemoi333288trial.hanatrial.ondemand.com/jco_demo', (err, res, body) => {
//     bodyJSON = JSON.parse(body);
//     console.log(bodyJSON)
// });

request.post('https://gsrestservicei333288trial.hanatrial.ondemand.com/gs-rest-service/asset/', {
    json: {
        companyCode: "A001",
        assetClass: "00003100",
        assetNum: "",
        description: "Test By PostMan4324"
    }
}, (error, res, body) => {
    if (error) {
        console.error(error);
        return;
    }
    console.log(`statusCode: ${res.statusCode}`);
    console.log(body);
});

