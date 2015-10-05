#!/usr/bin/php

<?php
$my_array = array("602-699-4564", "(480) 270-4295", "6234802792", "abpc1234", "yeap_that-sucks");

$pattern = '/^\(?\d{3}\)?[-\s]?\d{3}[-|\s]?\d{3}/';

foreach ($my_array as $number)
{
	 if( preg_match($pattern, $number)) {
	 	$stored_number = preg_replace('/[\s-\(\)]/',"", $number);
	 	print $number . " is a now the valid phone number {$stored_number} \n";	
	}else{
		print $number . " is an invalid phone number \n";
	}
}
 
