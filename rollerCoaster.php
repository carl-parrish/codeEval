#!/usr/bin/php
<?php
/**
 * Roller Coaster
 * You are given a piece of text. Your job is to write a program that sets the case of
 * text characters according to the following rules:
 * The first letter of the line should be in uppercase.
 * The next letter should be in lowercase.
 * The next letter should be in uppercase, and so on.
 * Any characters, except for the letters, are ignored during determination of letter case.
 * @author Carl Parrish <cparrish@carlparrish.com>
 */

function isSpecialChar($char){
    if(strtolower($char) === strtoupper($char)){
        return true;
    } else {
        return false;
    }
}

$file_name = $argv[1];

$lines = file($file_name);

foreach($lines as $line){
    $line = strtolower($line);
    for ($current=0; $current < strlen($line); $current ++){
        if($current){ // Not the first char
            $previous = $current - 1;
            while(isSpecialChar($line[$previous]) && ($previous > 0 )){ // make sure last char tested was a letter
                $previous--;
            }
        } else {
            $previous = false;
        }

        if($previous){
            if($line[$previous] == strtolower($line[$previous])){ // previous is lowercase
                $line[$current] = strtoupper($line[$current]);
            }
        } elseif($current == 0) { //This is the first char

            $line[$current] = strtoupper($line[$current]);
        }
    }
    print $line;
}