const request = require('request');
const grpc = require('grpc');
const protoDescriptor = require('./grpcLoader');

function callAPI(asset_struct) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021', (err, body, res) => {
            if (err) reject(err);
            resolve(res);
        });
    })
}

function callDB(api_log) {
    return new Promise((resolve, reject) => {
        let asset = protoDescriptor.asset;
        let client = new asset.DB('localhost:50051', grpc.credentials.createInsecure());
        client.update({text: api_log}, (err, db_log) => {
            if (err) reject(err);
            resolve({api_log: api_log, db_log: db_log});
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
            company_code: this.companyCode,
            asset_number: this.assetNumber,
            description: this.description
        });
        return promise
            .then(callAPI)
            .then(callDB);
    }
}

module.exports = AssetAgent;