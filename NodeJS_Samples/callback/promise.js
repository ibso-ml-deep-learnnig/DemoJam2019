//promise
console.log("start");

const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("we are in another funct");       
        resolve("end");
    }, 2000);
});

promise.then(end => {
    console.log(end);    
})


/* console.log("start");

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
//promist to resolve callback hell
loginUser("xxx@gmail.com")
.then(user => getVedios(user.userEmail))
.then(vedios => getVediosDetail(vedios[0]))
.then(vedioDetail => console.log(vedioDetail.name));

console.log("Finish"); */


//Promise all
/* const yt = new Promise( resolve => {
    setTimeout(() => {
        console.log("get vedio from yotube");
        resolve({videos: [1,2,3,4,5]});
    }, 5000);
});

const fb = new Promise( resolve => {
    setTimeout(() => {
        console.log("get photo from facebook");
        resolve({photos: ['a','b','c','d','e']});
    }, 2000);
});

Promise.all([yt, fb]).then(result => console.log(result)); */




