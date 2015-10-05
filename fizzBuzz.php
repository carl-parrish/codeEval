#!/usr/bin/php
<?php
/**********************************************************
**  Fizz Buzz											 
**	Players generally sit in a circle. The player		  
**	designated to go first says the number "1", and each 
** 	player thenceforth counts one number in turn. 		 
** 	However, any number divisible by 'A' e.g. three is    
**	replaced by the word fizz and any divisible by 'B' 	 
**	e.g. five by the word buzz. Numbers divisible by both
**	become fizz buzz. A player who hesitates or makes a  
**	mistake is either eliminated.						 
** Write a program that prints out the the pattern
** generated by such a scenario given the values of 
** 'A'/'B' and 'N' which are read from an input text file.
** The input text file contains three space delimited
** numbers i.e. A, B, N. The program should then print 
** out the final series of numbers using 
** 'F' for fizz, 'B' for 'buzz' and 'FB' for fizz buzz.
**	@package CodeEval									 
**  @author Carl Parrish								 	
**********************************************************/

$file_name = $argv[1];

$lines = file($file_name);

foreach ($lines as $line)
{
	list($fizz, $buzz, $max) = explode(" ",$line);
	
	$fizzBuzz = $fizz * $buzz;
	
	for ($i = 1; $i <= $max; $i++) {
		
		if ($i % $fizzBuzz 		== 0) {
			print ("FB ");
		}	elseif ($i % $buzz 	== 0) {
			print ("B "); 
		}	elseif ($i % $fizz 	== 0) {
			print ("F ");
		}	else {
			print $i . " ";
		}
	
	}
	print "\n";
}

?>	