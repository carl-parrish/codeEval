File.open(ARGV[0]).each_line do |line|
	haystack, needle = line.split(',')
	pattern = "[#{needle.strip!}]"
	re = Regexp.new(pattern)
	haystack.gsub!(re, '')
	puts haystack
end