const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const redis = require('redis');
const crypto = require('crypto');

let token = protoDescriptor.token;

function main() {
    let server = new grpc.Server();
    server.addService(token.CRUD.service, {
        getToken: (call, callback) => {
            console.log("get token called");
            let key = "";
            call.redisKey.keyValue ? key = call.redisKey.keyValue : key = 'CreateAsset';
            let token = crypto.randomBytes(32).toString('hex');
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {tokenValue: null, error: err, isSuccess: false});
            });
            // set key token pair to redis
            redisClient.set(key, token);
            redisClient.quit();
            callback(null, {tokenValue: token, error: null, isSuccess: true});
        },
        checkToken: (call, callback) => {
            console.log("check token called");
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {tokenValue: null, error: err, isSuccess: false});
            });
            redisClient.get(call.checkValue.keyValue, (err, reply) => {
                if (err) callback(null, {return: false});
                if (reply.toString() === call.checkValue.tokenValue) {
                    callback(null, {tokenValue: call.checkValue.tokenValue, error: null, isSuccess: true})
                }
            });
            redisClient.quit();
        },
        deleteToken: (call, callback) => {
            console.log("delete token called");
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {tokenValue: null, error: err, isSuccess: false});
            });
            redisClient.del(call.redisKey.keyValue, (err, response) => {
                if (response === 1) {
                    callback(null, {tokenValue: call.redisKey.keyValue, error: null, isSuccess: true});
                } else {
                    callback(null, {tokenValue: null, error: err, isSuccess: false})
                }
            });
            redisClient.quit();
        }
    });
    server.bind('localhost:50052', grpc.ServerCredentials.createInsecure());
    server.start();
}

main();