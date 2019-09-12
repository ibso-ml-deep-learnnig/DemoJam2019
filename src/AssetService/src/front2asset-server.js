const protoDescriptors = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./AssetAgent');

const port = process.env.PORT;
const address = port ? `0.0.0.0:${port}` : 'localhost:50051';

let asset = protoDescriptors.assetProto.asset;
let health = protoDescriptors.healthProto.grpc.health.v1;

function main() {
    let server = new grpc.Server();
    server.addService(asset.s4api.service, {
        create: (call, callback) => {
            // let agent = new assetAgent(call.assetInputs.company_code, call.assetInputs.asset_number, call.assetInputs.description);
            // let res = agent.createAsset();
            // res.then(value => {
            //     callback(undefined, {api_log: value.api_log, db_log: value.db_log, error: undefined})
            // }).catch(error => {
            //     callback(undefined, {api_log: undefined, db_log: undefined, error: undefined})
            // });
            // Mock create API
            console.log(call.request);
            let response = JSON.stringify({
                company_code: call.request.company_code,
                asset_number: call.request.asset_number,
                description: call.request.description
            });
            callback(undefined, {api_log: response, db_log: "here is db log", error: undefined})
        },
        display: (call, callback) => {
            let agent = new assetAgent(call.request.value);
            let res = agent.displayAsset();
            res.then(value => {
                callback(undefined, {
                    company_code: value.company_code,
                    asset_number: value.asset_number,
                    description: value.description,
                    log: undefined
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
    server.addService(health.Health.service, {
        check: (call, callback) => {

        }
//    server.addService(health.Health.service, {check});
    server.bind(address, grpc.ServerCredentials.createInsecure());
    server.start();
    console.log(`Asset service on: ${address}`);
}

main();