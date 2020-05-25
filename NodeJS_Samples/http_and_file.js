const http = require("http");
const fs = require("fs");
const server = http.createServer(function (req, res) {
  //Read data from file and write to page
  fs.readFile("http.txt", async (err, data) => {
    if (err) {
      console.log("error");
    } else {
      console.log(data);
      res.write(data);
      res.end();
    }
  });
  console.log("first");
});

server.listen(9999);
