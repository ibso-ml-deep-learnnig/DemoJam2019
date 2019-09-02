const request = require('request');
const grpc = require('grpc');

function callAPI(companyCode, assetNumber, description) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021', (err, body, res) => {
            if (err) reject(err);
            resolve(res);
        });
    })
}

function callDB(dbGRPC, apiLog) {
    return new Promise((resolve, reject) => {
        let client = new dbGRPC('localhost:50051', grpc.credentials.createInsecure());
        client.update({text: apiLog}, (err, res) => {
            if (err) reject(err);
            resolve(res.text);
        })

    })
}

async function asyncCallAPI(companyCode, assetNumber, description) {
    return await callAPI(companyCode, assetNumber, description);
}

async function asyncCallDB(dbGRPC, apiLog) {
    return await callDB(dbGRPC, apiLog)
}

class AssetAgent {
    constructor(companyCode, assetNumber, description) {
        this.companyCode = companyCode;
        this.assetNumber = assetNumber;
        this.description = description;
    }

    callAPI() {
        return asyncCallAPI(this.companyCode, this.assetNumber, this.description);
    }

    updateDB(dbGRPC, apiLog) {
        return asyncCallDB(dbGRPC, apiLog)
    }
}

module.exports = AssetAgent;