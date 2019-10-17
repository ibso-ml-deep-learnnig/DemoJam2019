const protoDescriptor = require('../src/grpcLoader');
const grpc = require('grpc');

let assetService = protoDescriptor.assetProto.asset;

function main() {
    let client = new assetService.s4api('localhost:50051',
        grpc.credentials.createInsecure());
    client.create({
        company_code: 'A001',
        asset_class: '00003100',
        description: 'Test By gRPC'
    }, (err, response) => {
        if (err) console.error(err);
        console.log(response);
    })
}

main();