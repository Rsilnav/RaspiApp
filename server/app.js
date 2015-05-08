var express = require('express');
var app = express();
var fs = require('fs');

app.get('/', function(req, res) {
  res.type('text/plain'); // set content-type
  var temperature = fs.readFileSync("/sys/class/thermal/thermal_zone0/temp");
  temperature = ((temperature/1000).toPrecision(3)) + "°C";
  res.send(temperature);
});

app.listen(process.env.PORT || 3000, function() {
	console.log("Node server up and running.");
});
