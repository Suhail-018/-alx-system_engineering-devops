#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\W?\w+)|to:(\W?\w+)|flags:(\S+1)/).flatten.compact.join(',')
