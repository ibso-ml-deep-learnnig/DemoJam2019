const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./createAsset');
const OS = require('os');

let asset = protoDescriptor.asset;

function main() {
    let server = new grpc.Server();
    server.addService(asset.CRUD.service, {
        create: (call, callback) => {
            let agent = new assetAgent(call.asset.company_code, call.asset.asset_number, call.asset.description);
            agent.callAPI();
            callback(null, {message: call.request.name + "say hi!"})
        }
    });
    server.bind('localhost:50051', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();