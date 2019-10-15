const request = require('request');
const grpc = require('grpc');
const protoDescriptor = require('./grpcLoader');

function callS4CreateAssetAPI(value) {
    return new Promise((resolve, reject) => {
        request('https://gsrestservicei333288trial.hanatrial.ondemand.com/gs-rest-service/asset/',
            {
                json: {
                    companyCode: value.company_code,
                    assetClass: value.asset_class,
                    assetNum: "",
                    description: value.description
                }
            },
            (err, res, body) => {
                console.log('create asset');
                if (err) reject(err);
                console.log(res);
                resolve({
                    company_code: body.companyCode,
                    asset_class: body.assetClass,
                    asset_number: body.assetNum,
                    description: body.description
                });
            });
    })
}

function updateAsset2DB(value) {
    return new Promise((resolve, reject) => {
        const dbEnv = process.env.DB_SERVER_ADDRESS;
        const dbAddress = dbEnv ? dbEnv : 'localhost:50051';

        let assetDB = protoDescriptor.asset;
        let client = new assetDB.DBapi(dbAddress, grpc.credentials.createInsecure());

        //get date
        let dateObj = new Date();
        let month = dateObj.getUTCMonth() + 1; //months from 1-12
        let day = dateObj.getUTCDate();
        let year = dateObj.getUTCFullYear();

        client.insertAsset(
            {
                asset_id: "9",
                asset_class: value.asset_class,
                description: value.description,
                picture: "/root/",
                company_code: value.company_code,
                assert_number: value.asset_number,
                asset_subno: "0",
                cost_center: "CC_A001",
                acquisition_date: {
                    year: year,
                    month: month,
                    day: day
                },
                amount: 1000.10,
                ul_year: 10,
                ul_period: 12,
                user_id: "i333463"
            }, (err, res) => {
                if (err) reject(err);
                console.log(typeof res);
                //TODO: i need asset number not id here
                resolve({
                    error: res.error,
                    asset_id: res.asset_id,
                    log: res.log
                });
            })
    })
}

function callS4DisplayAssetAPI(value) {
    return new Promise((resolve, reject) => {
        // const dbEnv = process.env.DB_SERVER_ADDRESS;
        // const dbAddress = dbEnv ? dbEnv : 'localhost:50051';
        // //TODO: align with frontend and DB
        // let assetDB = protoDescriptor.asset;
        // let client = new assetDB.DBapi(dbAddress, grpc.credentials.createInsecure());
        // client.selectAssetById({asset_id})
        // request('https://jcodemoi333288trial.hanatrial.ondemand.com/jco_demo', (err, res, body) => {
        //     console.log('inside diplay asset');
        //     if (err) reject(err);
        //     let bodyJSON = JSON.parse(body);
        //     resolve({
        //         company_code: bodyJSON.companyCode,
        //         asset_number: bodyJSON.assetMainNumber,
        //         description: undefined
        //     })
        // });
    })
}

function AssetAgent() {
    let args = (arguments.length === 1 ? [arguments[0]] : Array.apply(null, arguments));
    if (args.length === 1) {
        this.assetNumber = args[0]
    } else if (args.length === 3) {
        this.companyCode = args[0];
        this.assetClass = args[1];
        this.description = args[2]
    }
}

AssetAgent.prototype.createAsset = () => {
    let promise = Promise.resolve({
        company_code: this.companyCode,
        asset_class: this.assetClass,
        description: this.description
    });
    return promise
        .then(callS4CreateAssetAPI)
        .then(updateAsset2DB);
};

AssetAgent.prototype.displayAsset = () => {
    let promise = Promise.resolve({
        company_code: this.companyCode,
    });
    return promise.then(callS4DisplayAssetAPI)
};


module.exports = AssetAgent;