#!/usr/bin/php
<?php
function sum()
{
    $sum = 0;
    for($i = 0; $i <= 100; $i++){
        $sum += $i;
    }
    
    return $sum;
}
print sum();
?>
