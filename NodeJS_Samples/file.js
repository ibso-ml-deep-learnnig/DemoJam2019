const fs = require("fs");

//Read data from file
fs.readFile("http.txt", (err, data) => {
  if (err) {
    console.log("error");
  } else {
    console.log(data);
  }
});

//Create file
//-----------------------------------------------------------------------------------------------------------
//create new file
fs.appendFile("testfile.txt", "Hello content", (err) => {
  if (err) throw err;
  else console.log("saved");
});

//creat new empty file
fs.open('testfile2.txt', 'w' , err => {
    if (err) throw err;
    else console.log('testfile2 created');
    
});

// replaces the specified file and content if it exists. If the file does not exist, a new file, containing the specified content, will be created
fs.writeFile('testfile3.txt', 'hello content3' , err => {
    if (err) throw err;
    else console.log('testfile3 created');
    
});
//-----------------------------------------------------------------------------------------------------------

//Update file
//-----------------------------------------------------------------------------------------------------------
//Append "This is my text." to the end of the file "mynewfile.txt":
fs.appendFile("testfile.txt", "This is my text", (err) => {
    if (err) throw err;
    else console.log("updated");
  });

  //Replace the content of the file "mynewfile3.txt":
fs.writeFile("testfile3.txt", "This is my text", (err) => {
    if (err) throw err;
    else console.log("Replaced");
  });
  //-----------------------------------------------------------------------------------------------------------

  //Rename file(Use Promise to make sure rename firstly and then delete file)
  //-----------------------------------------------------------------------------------------------------------
  const promise = new Promise((resolve, reject) => {
    fs.rename('testfile2.txt', 'testfile4.txt', err =>{
        if (err) {
            reject(err)
        }
        else {
            resolve('testfile4.txt')
            console.log("Renamed")
        };      
      });
  });
  //-----------------------------------------------------------------------------------------------------------

  //Delete file
  //-----------------------------------------------------------------------------------------------------------
  promise.then(function (filename) {
    fs.unlink(filename, err => {
        if (err) throw err;
        else console.log(`${filename} is deleted`);
    });
  })

  //-----------------------------------------------------------------------------------------------------------

