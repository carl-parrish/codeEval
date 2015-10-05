#!/usr/bin/php
<?php
function search_array($array, $value)
{
    foreach ($array as $first_level){
        if (is_array($first_level){
            foreach ($first_level as $next_level_index){
                if ($next_leve_index === $value) {
                    return true;
                }
            }
        }else{
            if($first_level === $value) {
                return true;
            }
        }
    }
    return false;
}
?>
