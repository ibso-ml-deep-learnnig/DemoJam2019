const request = require('request');

function callAPI(companyCode, assetNumber, description) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021', (err, body, res) => {
            if (err) reject(err);
            console.log('in promise: %s', res);
            resolve(res);
        });
    })
}

async function asyncCall(companyCode, assetNumber, description) {
    let res = await callAPI(companyCode, assetNumber, description);
    console.log('in async: %s', res);
    return res
}

class AssetAgent {
    constructor(companyCode, assetNumber, description) {
        this.companyCode = companyCode;
        this.assetNumber = assetNumber;
        this.description = description;
    }

    callAPI() {
        return asyncCall(this.companyCode, this.assetNumber, this.description);
    }
}

module.exports = AssetAgent;