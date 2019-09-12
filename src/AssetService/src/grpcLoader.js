const path = require('path');
const ASSET_PROTO_PATH = path.resolve(__dirname, '../proto/createAsset.proto');
const HEALTH_PROTO_PATH = path.join(__dirname, '../proto/grpc/health/v1/health.proto');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const assetPackageDefinition = protoLoader.loadSync(
    ASSET_PROTO_PATH,
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

let assetProtoDescriptor = grpc.loadPackageDefinition(assetPackageDefinition);
let healthProtoDescriptor = grpc.loadPackageDefinition(healthPackageDefinition);

module.exports = {
    assetProto: assetProtoDescriptor,
    healthProto: healthProtoDescriptor
};