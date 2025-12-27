s = gets.chomp.split("")
s.delete_at((s.length - 1) / 2)
s.each { |str| print str }
