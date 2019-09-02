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
            res.then((api_respond) => {
                let db_res = agent.updateDB(asset.DB, api_respond);
                db_res.then((db_respond) => {
                    callback(null, {api_log: api_respond, db_log: db_respond})
                }).catch((db_error) => {
                    callback(null, {api_log: api_respond, db_log: db_error})
                })
            }).catch((api_error) => {
                callback(null, {api_log: api_error, db_log: null})
            })
        }
    });
    server.bind('localhost:50051', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();