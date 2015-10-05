#!/usr/bin/php
<?php
function even_sum()
{
    $sum = 0; 
    for($i = 0; $i <=100; $i++){
        if ($i % 2 == 0 ) {
            $sum += $i;
        }
    }
        return $sum;
}
print even_sum(). "\n";;
?>
