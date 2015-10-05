#! /usr/bin/php
<?php
/**************************************************************************
**  Given a string write a program to convert it into lowercase.		***
**
**
**
**
**************************************************************************/

$file_name = $argv[1];

$lines = file($file_name);

foreach ($lines as $line){
	print strtolower($line);
}

?>
	