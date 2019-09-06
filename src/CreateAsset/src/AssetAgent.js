const request = require('request');
const grpc = require('grpc');
const protoDescriptor = require('./grpcLoader');

function callS4CreateAssetAPI(value) {
    return new Promise((resolve, reject) => {
        request('http://localhost:50021', (err, body, res) => {
            //TODO: mock S4 API
            if (err) reject(err);
            resolve(res);
        });
    })
}

function callDB(value) {
    return new Promise((resolve, reject) => {
        let asset = protoDescriptor.asset;
        let client = new asset.DB('localhost:50051', grpc.credentials.createInsecure());
        client.update({text: value}, (err, res) => {
            if (err) reject(err);
            resolve({api_log: api_log, db_log: res.text});
        })
    })
}

function callS4DisplayAssetAPI() {
    return new Promise((resolve, reject) => {
        request('http://localhost:55021', (err, body, res) => {
            // TODO: mock S4 API
            if (err) reject(err);
            resolve(res);
        })
    })
}

class AssetAgent {
    constructor(companyCode, assetNumber, description) {
        this.companyCode = companyCode;
        this.assetNumber = assetNumber;
        this.description = description;
    }

    createAsset() {
        let promise = Promise.resolve({
            company_code: this.companyCode,
            asset_number: this.assetNumber,
            description: this.description
        });
        return promise
            .then(callS4CreateAssetAPI)
            .then(callDB);
    }

    displayAsset() {
        let promise = Promise.resolve({
            company_code: this.companyCode,
            asset_number: this.assetNumber,
            description: this.description
        });
        return promise.then(callS4DisplayAssetAPI)
    }
}

module.exports = AssetAgent;