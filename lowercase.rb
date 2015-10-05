#!/usr/bin/ruby
=begin
Given a string write a program to convert it into lowercase.
 The frist argument will be a text file containg sentences, one per line. You 
 can assume all characters are from the english language
=end
File.open(ARGV[0]).each_line do |line|
	puts line.downcase unless line.nil?
end