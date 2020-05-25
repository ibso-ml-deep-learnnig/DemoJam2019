function syncFunct () {
    setTimeout(() => {
        console.log("we are in another funct");
    }, 3000);
};

console.log("start");

syncFunct();

console.log("end");

//------------------------------------------------------------------
// email is undefined in output
//------------------------------------------------------------------
/* function login (email, password) {
    setTimeout(() => {
        return email;
    }, 3000);
};

console.log("bigin login");

const email = login("xxx@gmail.com");
console.log(email);


console.log("end login"); */

//------------------------------------------------------------------
// callback function
//------------------------------------------------------------------
/* function login (email, callback) {
    setTimeout(() => {
        callback(email);
    }, 3000);
};

console.log("bigin login");

const email = login("xxx@gmail.com",(mail) => {
    console.log(mail);
    
});


console.log("end login"); */
