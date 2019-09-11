const protoDescriptor = require('../src/grpcLoader');
const grpc = require('grpc');

let assetService = protoDescriptor.asset;

function main() {
    let client = new assetService.s4api('localhost:50051',
        grpc.credentials.createInsecure());
    client.create({
        company_code: '0001',
        asset_number: '60051',
        description: 'I am tester'
    }, (err, response) => {
        if (err) console.error(err);
        console.log(response);
    })
}

main();