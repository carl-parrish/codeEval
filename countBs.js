function countBs(input){
    var source = input.split('');
    return countChars(input, 'B');
}

function countChars(haystack, needle){
    let count = 0;
    haystack.split('').forEach(function(value){
        if(value == needle){
            count++;
        }
    });
    return count;
}

console.log(countBs('RuBBer BaBBY Bumpers'));