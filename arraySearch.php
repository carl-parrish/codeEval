#!/usr/bin/php
<?php

function is_in($value,$array){
    $pattern = '/$value/';
   foreach ($array as $index){
	if($index === $value){
		return "True";
	   }
}
   return "False"; 
}

$myArray = array("123", "abc", 123);

print is_in("abc", $myArray);
?>
