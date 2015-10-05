sum = 0
File.open(ARGV[0]).each_line do |num|
	sum += num.chomp.to_i unless num.chomp.nil?
end
puts sum