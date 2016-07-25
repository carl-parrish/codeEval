#!/usr/local/bin/node
'use strict';

var fs = require('fs');
var myArgv = process.argv;
var fileName = myArgv[2];
var buffer = fs.readFileSync(fileName, 'utf8');
var lines = buffer.split('\n');
lines.forEach(function (line) {
  if (line != null){
    let [haystack, needle] = line.split(',');
    //var input = line.split(',');
    //var haystack = input[0];
    //var needle = input[1].trim();
    if(haystack.endsWith(needle.trim())){
      console.log(1);
    }else {
      console.log(0);
    }
  }
});
