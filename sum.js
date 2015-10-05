var sum = 0;
var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (number) {
    if (number !== false) {
 		 sum += parseInt(number);
    }
});
console.log(sum);