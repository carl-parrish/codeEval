#!/usr/bin/php
<?

$file_name = $argv[1];

$inputs = file($file_name);

foreach ($inputs as $input) {
	if (strlen($input) <= 1) { continue; }
	
	list($srcString, $scrub) = explode(",", $input);
	$intab		=	"#"; //place holder for removed chars
	$srcString 	= trim($srcString);
	$scrub 		= trim($scrub);
	$replace 	= "";
	// Add as many whitespace chars to replace as there are chars in $scrub
	$replace 	= str_pad($replace, strlen($scrub)+1, "#");
	
	$translation =  strtr($srcString, $scrub, $replace);
	$translation = str_replace("#","", $translation);
	print $translation . "\n";
}

?>