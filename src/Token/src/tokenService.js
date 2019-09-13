const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const redis = require('redis');
const crypto = require('crypto');

let token = protoDescriptor.tokenProto.token;
let health = protoDescriptor.healthProto.grpc.health.v1;

let port = process.env.PORT;
const address = port ? `0.0.0.0:${port}` : 'localhost:50051';

function main() {
    let server = new grpc.Server();
    server.addService(token.CRUD.service, {
        getToken: (call, callback) => {
            console.log("get token called");
            let key = call.request.keyValue ? call.request.keyValue : 'CreateAsset';
            let token = crypto.randomBytes(32).toString('hex');
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(undefined, {tokenValue: undefined, error: undefined, isSuccess: false});
            });
            // set key token pair to redis
            redisClient.set(key, token);
            redisClient.quit();
            callback(undefined, {tokenValue: token, error: undefined, isSuccess: true});
        },
        checkToken: (call, callback) => {
            console.log("check token called");
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(undefined, {tokenValue: undefined, error: err, isSuccess: false});
            });
            redisClient.get(call.request.keyValue, (err, reply) => {
                if (err) callback(undefined, {return: false});
                if (reply.toString() === call.request.tokenValue) {
                    callback(undefined, {tokenValue: call.request.tokenValue, error: undefined, isSuccess: true})
                }
            });
            redisClient.quit();
        },
        deleteToken: (call, callback) => {
            console.log("delete token called");
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(undefined, {tokenValue: undefined, error: err, isSuccess: false});
            });
            redisClient.del(call.redisKey.keyValue, (err, response) => {
                if (response === 1) {
                    callback(undefined, {tokenValue: call.redisKey.keyValue, error: undefined, isSuccess: true});
                } else {
                    callback(undefined, {tokenValue: undefined, error: err, isSuccess: false})
                }
            });
            redisClient.quit();
        }
    });
    server.addService(health.Health.service, {
        Check: (call, callback) => {
            callback(undefined, {status: 'SERVING'})
        }
    });
    server.bind(address, grpc.ServerCredentials.createInsecure());
    server.start();
    console.log(`Token service on: ${address}`);
}

main();