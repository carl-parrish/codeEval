#!/usr/bin/php
<?php
class Singleton {
    private static $instance = false; 
    public $property;
    
    private function __construc() {}
    
    public static function getInstance()
    {
        if(self::$instance === false){
            self::$instance = new Singleton;
        }
    return self::$instance;
    }
}

$first = Singleton::getInstance();
$next =  Singleton::getInstance();
$first->property = "hello world";
print $next->property;

?>
