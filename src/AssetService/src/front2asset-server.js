const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const assetAgent = require('./AssetAgent');

const port = process.env.PORT;
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
            let response = JSON.stringify({
                company_code: call.assetInputs.company_code,
                asset_number: call.assetInputs.asset_number,
                description: call.assetInputs.description
            });
            callback(undefined, {api_log: response, db_log: "here is db log", error: undefined})
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
    server.bind(`0.0.0.0:${port}`, grpc.ServerCredentials.createInsecure());
    console.log()
    server.start();
}

main();