const protoDescriptors = require('./grpcLoader');
const grpc = require('grpc');
const AssetAgent = require('./AssetAgent');

const port = process.env.PORT;
const address = port ? `0.0.0.0:${port}` : 'localhost:50051';

let asset = protoDescriptors.assetProto.asset;
let health = protoDescriptors.healthProto.grpc.health.v1;

function main() {
    let server = new grpc.Server();
    server.addService(asset.s4api.service, {
        create: (call, callback) => {
            let agent = new AssetAgent(call.assetInputs.company_code, call.assetInputs.asset_class, call.assetInputs.description);
            let res = agent.createAsset();
            res.then(value => {
                if (value.error === true) {
                    let logMsg = `${value.asset_id} with error ${value.log}`;
                    callback(undefined, {api_log: undefined, db_log: logMsg, has_error: true});
                    return;
                }
                callback(undefined, {api_log: undefined, db_log: undefined, error: true})
            }).catch(error => {
                callback(undefined, {api_log: error, db_log: error, error: true})
            });
        },
        display: (call, callback) => {
            let agent = new AssetAgent(call.AssetId.asset_id);
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
        Check: (call, callback) => {
            callback(undefined, {status: 'SERVING'})
        }
    });
    server.bind(address, grpc.ServerCredentials.createInsecure());
    server.start();
    console.log(`Asset service on: ${address}`);
}

main();