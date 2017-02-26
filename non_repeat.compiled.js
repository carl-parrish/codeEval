'use strict';

var fs = require("fs");

function non_repeat(str) {
    var inputArray = str.split('');
    var unique = inputArray.filter(function (val, indx, arr) {
        if (arr.indexOf(val) === arr.lastIndexOf(val)) {
            return val;
        }
    });
    return unique[0];
}

fs.readFileSync(process.argv[2]).toString().split('\n').map(function (line) {
    console.log(non_repeat(line));
});