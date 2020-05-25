const EventEmitter = require('events');
module.exports = class Logger extends EventEmitter{
    log(url){
        console.log(url);
        this.emit('messageLogged', {id:1, url:url});
    }
}