=begin
=end
contact_collection =["602-699-4564", "(480) 270-4295", "6234802792", "abpc1234", "yeap_that-sucks"]

pattern = '/^\(?\d{3}\)?[-\s]?\d{3}[-|\s]?\d{3}/';

re = Regexp.new(pattern)
contact_collection.each {|phone_number|
	puts "#{phone_number} is an invalid phone number" unless phone_number =~ re
	} 