#!/usr/bin/env ruby
# regular expression must be exactly matching a string
# that starts with h ends with n and can have any single character in between
puts ARGV[0].scan(/^h\wn$/).join
