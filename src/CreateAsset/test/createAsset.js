const request = require('request');

function callAPI(asset) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021', (err, body, res) => {
            if (err) reject(err);
            resolve({
                res: res,
                des: asset.des,
                an: asset.an,
                cc: asset.cc
            });
        });
    })
}

function callAPI2(api_one) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021/abc', (err, body, res) => {
            console.log('i am here');
            if (err) reject(err);
            resolve({
                res1: api_one.res,
                res2: res,
                cc: api_one.cc,
                an: api_one.an,
                des: api_one.des
            })
        })
    })
}

class AssetAgent {
    constructor(companyCode, assetNumber, description) {
        this.companyCode = companyCode;
        this.assetNumber = assetNumber;
        this.description = description;
    }

    callAPI() {
        let promise = Promise.resolve({
            cc: this.companyCode,
            an: this.assetNumber,
            des: this.description
        });
        return promise
            .then(callAPI)
            .then(callAPI2);
    }
}

module.exports = AssetAgent;