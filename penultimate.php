#!/usr/bin/php
<?php

$file_name = $argv[1]; 


$buffer = file($file_name);

foreach ($buffer as $line) 
{
	$line_array = explode(" ", trim($line));
	#$last_word = array_pop($line_array);
	#$penultimate = array_pop($line_array);
	$penultimate = array_slice($line_array,-2,1);
	
	#print "{$penultimate} \n";
	var_dump($penultimate) . "\n";
}


	