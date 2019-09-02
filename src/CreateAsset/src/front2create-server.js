const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./createAsset');

let asset = protoDescriptor.asset;

function main() {
    let server = new grpc.Server();
    server.addService(asset.CRUD.service, {
        create: (call, callback) => {
            let agent = new assetAgent(call.asset.company_code, call.asset.asset_number, call.asset.description);
            let res = agent.callAPI();
            res.then(value => {
                callback(null, {api_log: value.api_log, db_log: value.db_log})
            }).catch(error => {
                callback(null, {api_log: error, db_log: error})
            })
        }
    });
    server.bind('localhost:50051', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();