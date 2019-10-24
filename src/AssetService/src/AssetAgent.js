const request = require('request');
const grpc = require('grpc');
const protoDescriptor = require('./grpcLoader');

function callS4CreateAssetAPI(value) {
    return new Promise((resolve, reject) => {
        console.log('call s4');
        console.log(value);
        request.post('https://gsrestservicei333288trial.hanatrial.ondemand.com/gs-rest-service/asset/',
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
                console.log(body);
                if (err) reject(err);
                resolve({
                    asset_class: body.assetClass,
                    description: body.description,
                    picture: value.picture,
                    company_code: body.companyCode,
                    asset_number: body.assetNum,
                    cost_center: value.cost_center,
                    acquisition_date: value.acquisition_date,
                    amount: value.amount,
                    ul_year: value.ul_year,
                    ul_period: value.ul_period,
                    user_id: value.user_id
                });
            });
    })
}

function updateAsset2DB(value) {
    return new Promise((resolve, reject) => {
        console.log('call db');
        console.log(value);
        const dbEnv = process.env.DB_SERVER_ADDRESS;
        const dbAddress = dbEnv ? dbEnv : 'localhost:50051';

        console.log(dbAddress);

        let db = protoDescriptor.dbProto.demojam2019;
        let client = new db.DBService(dbAddress, grpc.credentials.createInsecure());
        client.insertAsset(
            {
                asset: {
                    asset_id: "/new",
                    asset_class: value.asset_class,
                    description: value.description,
                    picture: value.picture,
                    company_code: value.company_code,
                    assert_number: value.asset_number,
                    asset_subno: "0",
                    cost_center: value.cost_center,
                    acquisition_date: {
                        year: value.acquisition_date.year,
                        month: value.acquisition_date.month,
                        day: value.acquisition_date.day
                    },
                    amount: value.amount,
                    ul_year: value.ul_year,
                    ul_period: value.ul_period,
                    user_id: value.user_id
                }
            }, (err, response) => {
                if (err) reject(err);
                console.log("Response");
                console.log(Date());
                resolve({
                    error: response.error,
                    asset_id: response.asset_id,
                    log: response.log
                });
            })
    })
}

function callS4DisplayAssetAPI(value) {
    return new Promise((resolve, reject) => {
        const dbEnv = process.env.DB_SERVER_ADDRESS;
        const dbAddress = dbEnv ? dbEnv : 'localhost:50051';

        let assetDB = protoDescriptor.asset;
        let client = new assetDB.DBapi(dbAddress, grpc.credentials.createInsecure());
        client.selectAssetById({asset_id: value.asset_id}, (err, res) => {
            if (err) reject(err);
            console.log(res);
            resolve({
                asset_id: res.asset_id,
                asset_class: res.asset_class,
                description: res.description,
                picture: res.picture,
                company_code: res.company_code,
                asset_number: res.asset_number,
                asset_subno: res.asset_subno,
                cost_center: res.cost_center,
                acquisition_date: res.acquisition_date,
                amount: res.amount,
                ul_year: res.ul_year,
                ul_period: res.ul_period,
                user_id: res.user_id,
                create_date: res.create_date,
                create_time: res.create_time
            })
        });
    })
}

function AssetAgent() {
    let args = Array.apply(null, arguments);
    if (args[0] === "create") {
        this.assetClass = args[1];
        this.description = args[2];
        this.picture = args[3];
        this.companyCode = args[4];
        this.costCenter = args[5];
        this.acquisitionDate = args[6];
        this.amount = args[7];
        this.ulYear = args[8];
        this.ulPeriod = args[9];
        this.userID = args[10]
    }
    if (args[0] === "display") {
        this.assetID = args[0]
    }
}

AssetAgent.prototype = {
    createAsset: function () {
        let promise = Promise.resolve({
            asset_class: this.assetClass,
            description: this.description,
            picture: this.picture,
            company_code: this.companyCode,
            cost_center: this.costCenter,
            acquisition_date: this.acquisitionDate,
            amount: this.amount,
            ul_year: this.ulYear,
            ul_period: this.ulPeriod,
            user_id: this.userID
        });
        return promise
            .then(callS4CreateAssetAPI)
            .then(updateAsset2DB);
    },
    displayAsset: function () {
        let promise = Promise.resolve({
            asset_id: this.assetID,
        });
        return promise.then(callS4DisplayAssetAPI)
    }
};

module.exports = AssetAgent;