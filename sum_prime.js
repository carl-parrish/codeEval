#!/usr/local/bin/node

/*
Sum of Primes

Description:
Write a program to determine the sum of the first 1000 prime numbers
 */

function isPrime(num){
    for(let i = 2; i< num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return num > 1;
}

function sumPrimes(){
    let primes = [...Array(10000).keys()].filter(val => isPrime(val));
    primes = primes.slice(0,1000);
    return primes.reduce( (a,b) => { return a+ b;}, 0);
}

console.log(sumPrimes());