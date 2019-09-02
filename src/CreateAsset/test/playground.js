let assetAgent = require('./createAsset');

let agent = new assetAgent('0001', '0001', 'Test');
let result = agent.callAPI();

result.then((value => {
        console.log(value)
    }
));