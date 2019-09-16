const path = require('path');
const PROTO_PATH = path.resolve(__dirname, '../proto/token.proto');
const HEALTH_PROTO_PATH = path.join(__dirname, '../proto/grpc/health/v1/health.proto');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const tokenPackageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

const healthPackageDefinition = protoLoader.loadSync(
    HEALTH_PROTO_PATH,
    {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    });

let tokenProtoDescriptor = grpc.loadPackageDefinition(tokenPackageDefinition);
let healthProtoDescriptor = grpc.loadPackageDefinition(healthPackageDefinition);

module.exports = {
    tokenProto: tokenProtoDescriptor,
    healthProto: healthProtoDescriptor
};