const path = require('path');
const PROTO_PATH = path.resolve(__dirname, '../proto/token.proto');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

// TODO: error load proto

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

let protoDescriptor = grpc.loadPackageDefinition(packageDefinition);

module.exports = protoDescriptor;