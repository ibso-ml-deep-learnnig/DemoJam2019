const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./AssetAgent');

const port = process.env.PORT;
const address = port ? `0.0.0.0:${port}` : 'localhost:50051';
const HEALTH_PROTO_PATH = path.join(__dirname, './proto/grpc/health/v1/health.proto');
const healthProto = _loadProto(HEALTH_PROTO_PATH).grpc.health.v1;
let asset = protoDescriptor.asset;

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
    server.bind(address, grpc.ServerCredentials.createInsecure());
    server.addService(healthProto.Health.service, {check});
    server.start();
    console.log(`Asset service on: ${address}`);
}

main();