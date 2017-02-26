const fs = require("fs");

function non_repeat(str) {
    let inputArray = str.split('');
    let unique = inputArray.filter((val,indx,arr) => {
        if ((arr.indexOf(val)) === (arr.lastIndexOf(val))){
            return val;
        }
    });
    return unique[0];
}

fs.readFileSync(process.argv[2]).toString().split('\n').map((line)=>{
    console.log(non_repeat(line));
});