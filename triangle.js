#!/usr/local/bin/node

/***********************
* @source: Eloquent Javascript pg #37
* Write a loop that makes seven calls to console.log to output the following triangle:
* #
* ##
* ###
* ####
* #####
* ######
* ####### 
**************************/ 

for (var count = 1; count < 8; count++) {
  var output = "";
  do {
    output += "#"
  } while (output.length < count);

  console.log(output);
}
