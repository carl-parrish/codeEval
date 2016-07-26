/*********
 * @source: Eloquent Javascript
 * Write a program that uses console.log to print all the numbers from 1 to 100
 * with two exceptions. For numbers divisble by 3, print "Fizz" instead of the 
 * number, and for numbers divisible by 5 (and not 3), print "Buzz"
 * *****************************************************************/
 
 for(let i=1; i<=100; i++){
     if((i % 5 == 0 )&& (i % 3 == 0)){
        console.log("FizzBuzz");
     }else if(i % 3 == 0){
         console.log("Fizz");
     }else if(i % 5 == 0 ){
         console.log("Buzz");
     }else{
         console.log(i);
     }
 }