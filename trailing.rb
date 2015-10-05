File.open(ARGV[0]).each_line do |line|
	unless line == ''
		haystack, needle = line.split(',')
		haystack = haystack.split(" ")
		tail = haystack.pop
		puts tail.chomp == needle.chomp ? 1 : 0
	end
end