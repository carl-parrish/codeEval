<?php
$sum = 0;
$numbers = file($argv[1]);

foreach ($numbers as $num){
	$sum += trim($num);
}
print $sum;