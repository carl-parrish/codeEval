#!/usr/bin/php
<?php
/**
 * Data Recovery - Your task is to write a program which reconstructs each
 * sentence out of a set of words and prints out the original sentences.
 *
 *
 * Your program should accept a path to a filename as its first argument.
 * Each line is a test case which consists of a set of words and a sequence of
 * numbers separated by a semicolon. The words within a set and the numbers
 * within a sequence are separated by a single space.
 * @author Carl Parrish <'cparrish@carlparrish.com'>
 */
class secretData{
  private $words = array();
  private $positions = array();

  public function arrangeWords($input){

    $output = array();

    /*Format data in Arrays so we can work with them */
    $this->formatArrays($input);

    $hiddenWord = array_pop($this->words);

      for($index=0; $index < count($this->positions); $index++){
        $position = $this->positions[$index] -1;
        $output[$position] = $this->words[$index];
      }

      ksort($output, SORT_NUMERIC);
      $output = $this->insertHiddenWord($hiddenWord, $output);
      ksort($output, SORT_NUMERIC);
      $sentence = $this->toString($output);
      return $sentence;
  }

  private function formatArrays($input) {
    list($words, $indexes) = explode(";", $input);
    $this->words = explode(' ', $words);
    $this->positions = explode(' ', $indexes);
  }

  private function insertHiddenWord($lastWord, $wordArray){
      for ($index = 0; $index <= count($wordArray); $index++ ){
          if(!array_key_exists($index, $wordArray)){
              $wordArray[$index] = $lastWord;
              return $wordArray;
          }
      }
  }

  private function toString($elements){
    return join(' ', $elements);
  }
}

$data = new secretData();
$file_name = $argv[1];

$lines = file($file_name);
foreach($lines as $line){
  $result =  $data->arrangeWords($line);
  print ($result . "\n");
}

