/*********
 * @source: Eloquent Javascript
 * Write a program that uses process.stdout.write to print all the numbers from 1 to 100
 * with two exceptions. For numbers divisble by 3, print "Fizz" instead of the 
 * number, and for numbers divisible by 5 (and not 3), print "Buzz"
 * *****************************************************************/
 var fs = require("fs");
 fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {
     if(line !=""){
         let fizz, buzz, max;
         [fizz, buzz, max] = line.split(' ');
         let fizzBuzz = fizz * buzz;
         for(let i = 1; i <= max; i++){
             if(i % fizzBuzz == 0 ){
                process.stdout.write("FB ");
             }else if(i % fizz == 0){
                 process.stdout.write("F ");
             }else if(i % buzz == 0 ){
                 process.stdout.write("B ");
             }else{
                 process.stdout.write(i + " ");
             }
         }
         console.log(" ");
     }
 });
 