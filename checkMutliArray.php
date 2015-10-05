#!/usr/bin/php
<?php
function check_value($array, $value, $match = false)
{
	foreach ($array as $index){
		if (is_array($index)) {
    	   $result = check_value($index, $value, &$match);
    	}elseif ($index === $value){
    		$match = true;
    	} 
    	
	}

 return $match;
}
$myArray = array("carl",array('parrish','louis',"abc"), "whatever","123" );


var_dump( check_value($myArray, "whatever"));
?>
