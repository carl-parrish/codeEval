#!/usr/bin/php
<?php
/***************************************************
** Simple Sorting
**
** Write a program which sorts numbers. 
**
****************************************************/


$file_name = $argv[1];

$buffer = file($file_name);

foreach ($buffer as $input) 
{
	$numbers = explode(" ", trim($input));
	sort($numbers, SORT_NUMERIC);
	
	foreach ($numbers as $num) {
		print("$num ");
	}
	
	print "\n";
}
