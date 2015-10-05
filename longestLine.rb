input = []
File.open(ARGV[0]).each_line do |line|
	input.push(line)
end
count = input.shift
input.sort! { |a,b| b.length <=> a.length}
count.to_i.times {|i| puts input[i]}   
