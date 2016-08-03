var fs = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line){
    var round = line.split(' ');
    var unqueArray = round.filter(unqueNumbers,round);
    var lowest = Math.min.apply(Math, unqueArray);
    var indx = round.indexOf(String(lowest)) || 0;
    console.log(indx + 1);
});

function unqueNumbers(value, index, source){
    return source.indexOf(value) === source.lastIndexOf(value);
    
}

