#!/usr/local/bin/node
/**
 * lowercase.js
 * Created by cparrish on 2/27/15.
 *  Given a string write a program to convert it into lowercase.
 */


var fs  = require('fs');
var myArgv = process.argv;
var fileName = myArgv[2];
var buffer = fs.readFileSync(fileName, 'utf8');
var lines = buffer.split('\n');
lines.forEach(function(line){
    if(line !== ""){
        line.toLowerCase();
    }
});
