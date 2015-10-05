#!/usr/bin/php
<?php

function multiply(){
$multi_num1 = 12;
$multi_num2 = 12;
#outerloop
for($i =1; $i <= 12; $i++){
   #inner loop
    
    for ($j=1; $j <= 12; $j++){
        $ans = $j * $i;
        printf ("%4d", $ans);
    }
    print "\n";
}
}
multiply();
?>
