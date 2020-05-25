
console.log("start");

//Get email
function loginUser (email) {
    return new Promise( (resolve, reject) => {
        setTimeout(() => {
            console.log("user login");
            resolve({userEmail: email})
        }, 2000);
    });
};
//get vedio
function getVedios (email) {
    return new Promise( (resolve, reject) => {
        setTimeout(() => {
            console.log("read vedios");
            resolve( ["vedio1","vedio2","vedio3"] );
        }, 1000);
    } );
};
//get vedio details
function getVediosDetail (vedio) {
    return new Promise( (resolve, reject) => {
        setTimeout(() => {
            resolve( {name: "vedio details"} );
        }, 1000);
    } );    

};
//await statement to resolve callback hell
async function asyncfun (email ){
    const user = await loginUser(email);
    const vedio = await getVedios(user.userEmail);
    const detail = await getVediosDetail(vedio[0]);
    console.log(detail.name);
};

asyncfun("xxx@gmail.com")
console.log("Finish");




