#!/usr/bin/php
<?php
/**
 * Longest Lines
 * Write a program which reads a file and prints to stdout the specified
 * number of the longest lines that are sorted based on their length in
 * descending order.
 * @author: Carl Parrish <cparrish@carlparrish.com>
 */

function size_compare($a,$b){
    $size_of_a = strlen($a);
    $size_of_b = strlen($b);
    if($size_of_a == $size_of_b){
        return 0;
    }
    return ($size_of_b < $size_of_a) ? -1 : 1;

}

$file_name = $argv[1];

$lines = file($file_name);

$count = array_shift($lines);

usort($lines, "size_compare");

for($i=0; $i < $count; $i++){
    echo $lines[$i];
}