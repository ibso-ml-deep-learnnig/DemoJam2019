const protoDescriptor = require('../src/grpcLoader');
const grpc = require('grpc');

let assetService = protoDescriptor.assetProto.asset;

function main() {
    let client = new assetService.s4api('localhost:50051',
        grpc.credentials.createInsecure());
    client.create({
        asset_class: '00003100',
        description: 'Test By gRPC',
        picture: '/root',
        company_code: 'A001',
        cost_center: 'C001',
        acquisition_date: {
            year: 2019,
            month: 12,
            day: 31
        },
        amount: 10000,
        ul_year: 2019,
        ul_period: 12,
        user_id: 'I072179'
    }, (err, response) => {
        if (err) console.error(err);
        console.log(response);
    })
}

main();