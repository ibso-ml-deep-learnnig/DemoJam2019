const protoDescriptor = require('./grpcLoader');
const grpc = require('grpc');
const redis = require('redis');
const crypto = require('crypto');

let token = protoDescriptor.token;

function main() {
    let server = new grpc.Server();
    server.addService(token.CRUD.service, {
        getToken: (call, callback) => {
            let key = "";
            call.key.value ? key = call.key.value : key = 'CreateAsset';
            let token = crypto.randomBytes(32).toString('hex');
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {token: null, error: err});
            });
            // set key token pair to redis
            redisClient.set(key, token);
            redisClient.quit();
            callback(null, {token: token, error: null});
        },
        checkToken: (call, callback) => {
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {token: null, error: err});
            });
            redisClient.get(call.check_value.key, (err, reply) => {
                if (err) callback(null, {return: false});
                if (reply.toString() === call.check_value.token) {
                    callback(null, {return: true})
                } else {
                    callback(null, {return: false});
                }
            });
            redisClient.quit();
        },
        deleteToken: (call, callback) => {
            let redisClient = redis.createClient();
            redisClient.on("error", (err) => {
                callback(null, {token: null, error: err});
            });
            redisClient.del(call.key.value);
            redisClient.quit();
        }
    })
}