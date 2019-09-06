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

function updateAsset2DB(value) {
    return new Promise((resolve, reject) => {
        let assetDB = protoDescriptor.asset;
        let client = new assetDB.DBapi('localhost:50051', grpc.credentials.createInsecure());
        client.update({text: value}, (err, res) => {
            if (err) reject(err);
            resolve({api_log: api_log, db_log: res.text});
        })
    })
}

function callS4DisplayAssetAPI(value) {
    return new Promise((resolve, reject) => {
        request('http://localhost:55021', (err, body, res) => {
            // TODO: mock S4 API
            if (err) reject(err);
            resolve(res);
        })
    })
}

function AssetAgent() {
    let args = (arguments.length === 1 ? [arguments[0]] : Array.apply(null, arguments));
    if (args.length === 1) {
        this.assetNumber = args[0]
    } else if (args.length === 3) {
        this.companyCode = args[0];
        this.assetNumber = args[1];
        this.description = args[2]
    }
}

AssetAgent.prototype.createAsset = () => {
    let promise = Promise.resolve({
        company_code: this.companyCode,
        asset_number: this.assetNumber,
        description: this.description
    });
    return promise
        .then(callS4CreateAssetAPI)
        .then(updateAsset2DB);
};

AssetAgent.prototype.displayAsset = () => {
    let promise = Promise.resolve({
        company_code: this.companyCode,
    });
    return promise.then(callS4DisplayAssetAPI)
};


module.exports = AssetAgent;