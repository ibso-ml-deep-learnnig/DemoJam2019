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
            let agent = new AssetAgent(
                "create",
                call.request.asset_class,
                call.request.description,
                call.request.picture,
                call.request.company_code,
                call.request.cost_center,
                call.request.acquisition_date,
                call.request.amount,
                call.request.ul_year,
                call.request.ul_period,
                call.request.user_id
            );
            let res = agent.createAsset();
            res.then(value => {
                if (value.error === true) {
                    let logMsg = `${value.asset_id} with error ${value.log}`;
                    callback(undefined, {api_log: undefined, db_log: logMsg, has_error: true});
                    return;
                }
                let log = value.asset_id;
                callback(undefined, {
                    api_log: log, db_log: log, has_error: false
                })
            }).catch(error => {
                callback(undefined, {api_log: error, db_log: error, has_error: true})
            });
        },
        display: (call, callback) => {
            let agent = new AssetAgent(
                "display",
                call.request.value
            );
            console.log("display");
            console.log(call.request.value);
            let res = agent.displayAsset();
            res.then(value => {
                console.log(value);
                callback(undefined, {
                    asset_id: value.asset_id,
                    asset_class: value.asset_class,
                    description: value.description,
                    picture: value.picture,
                    company_code: value.company_code,
                    asset_number: value.asset_number,
                    asset_subno: value.asset_subno,
                    cost_center: value.cost_center,
                    acquisition_date: value.acquisition_date,
                    amount: value.amount,
                    ul_year: value.ul_year,
                    ul_period: value.ul_period,
                    user_id: value.user_id,
                    create_date: value.create_date,
                    create_time: value.create_time,
                    log: undefined
                })
            }).catch(error => {
                callback(undefined, {
                    asset_id: undefined,
                    asset_class: undefined,
                    description: undefined,
                    picture: undefined,
                    company_code: undefined,
                    asset_number: undefined,
                    asset_subno: undefined,
                    cost_center: undefined,
                    acquisition_date: undefined,
                    amount: undefined,
                    ul_year: undefined,
                    ul_period: undefined,
                    user_id: undefined,
                    create_date: undefined,
                    create_time: undefined,
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