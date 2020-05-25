// const EventEmitter = require('events');
const logger = require('./logger');
const log = new logger;
// const emitter = new EventEmitter()
//Register listener
log.on('messageLogged', async (arg) =>{
    console.log('Listener called', arg);
    
})
//Raise event
//emitter.emit('messageLogged',{ id:1, url: 'http://' })
log.log('trigger event');