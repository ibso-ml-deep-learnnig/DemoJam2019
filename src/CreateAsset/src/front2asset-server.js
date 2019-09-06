const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./AssetAgent');

let asset = protoDescriptor.asset;

function main() {
    let server = new grpc.Server();
    server.addService(asset.s4api.service, {
        create: (call, callback) => {
            let agent = new assetAgent(call.assetInputs.company_code, call.assetInputs.asset_number, call.assetInputs.description);
            let res = agent.createAsset();
            res.then(value => {
                callback(null, {api_log: value.api_log, db_log: value.db_log, error: null})
            }).catch(error => {
                callback(null, {api_log: null, db_log: null, error: error})
            });
        },
        display: (call, callback) => {
            let agent = new assetAgent(call.assetNumber.value);
            let res = agent.displayAsset();
            res.then(value => {
                callback(undefined, {
                    company_code: value.company_code,
                    asset_number: value.asset_number,
                    description: value.description
                })
            }).catch(error => {
                callback(undefined, {
                    company_code: undefined,
                    asset_number: undefined,
                    description: undefined,
                    log: error
                })
            });
        }
    });
    server.bind('localhost:50051', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();