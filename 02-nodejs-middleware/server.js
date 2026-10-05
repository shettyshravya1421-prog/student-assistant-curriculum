    var express = require("express");
    var app = express();
    
   function sayRequestCameIn(request, response, next) {
      console.log("A request came in!");
      next(); 
    }
    
    app.use(sayRequestCameIn);
    
    app.get("/student", function (request, response) {
      response.json({ name: "Sample Student", gpa: 8.7 });
    });
    
    app.listen(3001, function () {
      console.log("Server is running now");
    });