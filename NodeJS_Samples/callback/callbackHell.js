console.log("start");
//Get email
function loginUser (email, callback) {
    setTimeout(() => {
        console.log("Now we have the data");
        callback({userEmail: email});
    }, 2000);
};
//get vedio
function getVedios (email, callback) {
    setTimeout(() => {
        callback( ["vedio1","vedio2","vedio3"] );
    });
};
//get vedio details
function getVediosDetail (vedio, callback) {
    setTimeout(() => {
        callback( {name: "vedio details"} );
    });
};
//callback hell
const user = loginUser("xxx@gmail.com", user => {
    getVedios(user.userEmail, (vedio) => {
        getVediosDetail(vedio, (vedioDetails) => {
            console.log(vedioDetails.name);         
        })
    });
});

console.log("Finish");
