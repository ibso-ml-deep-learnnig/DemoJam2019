let assetAgent = require('./createAsset');

let agent = new assetAgent('0001', '0001', 'Test');
let res = agent.callAPI();
res.then((value) => {
    console.log(value)
});

