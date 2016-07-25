#!/usr/bin/ruby

File.open(ARGV[0]).each_line do |line|
    unless line.chomp.nil?
        haystack, needle = line.split(',')
        puts haystack =~ %r{#{needle.chomp}\z} ? 1 : 0
    end
end
