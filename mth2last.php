#!/usr/bin/php
<?php
/**
 * Mth to Last Element
 * Write a program which determines the Mth to the last element in a list.
 * @author Carl Parrish <cparrish@carlparrish.com>
 */

function mthElement($input){
    $array = explode(" ", $input);
    $m = array_pop($array);
    if ($m > count($array)){
            return;
    }
    $m *= -1;
    $answer = array_slice($array, $m, 1);
    return $answer[0];

}

$file_name = $argv[1];

$lines = file($file_name);

foreach($lines as $line){
    echo mthElement($line). "\n";
}