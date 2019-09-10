const redis = require('redis');
const crypto = require('crypto');
let client = redis.createClient();
let token = crypto.randomBytes(32).toString('hex');

client.on("error", function (err) {
    console.log("Error " + err);
});
client.set('transactonKey', token, redis.print);
client.get('transactonKey', (err, reply) => {
    console.log(reply.toString())
});
client.quit();

