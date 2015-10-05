File.open(ARGV[0]).each_line do |line|
	words = line.split(" ")
	sentence = words.map! {|word|
		if word =~ /^([a-z])|\s+([a-z])/
			word[0] = word[0].upcase
		end
		 word

	}.join(' ')
	print sentence
	puts
	 
end