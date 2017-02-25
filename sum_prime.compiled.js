#!/usr/local/bin/node
"use strict";

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

/*
Sum of Primes

Description:
Write a program to determine the sum of the first 1000 prime numbers
 */

function isPrime(num) {
    for (var i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return num > 1;
}

function sumPrimes() {
    var primes = [].concat(_toConsumableArray(Array(10000).keys())).filter(function (val) {
        return isPrime(val);
    });
    primes = primes.slice(0, 1000);
    return primes.reduce(function (a, b) {
        return a + b;
    }, 0);
}

console.log(sumPrimes());
