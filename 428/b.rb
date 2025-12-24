n, k = gets.split(" ").map(&:to_i)
s = gets

counts = Hash.new(0)

(0..n - k).each do |i|
  counts[s[i, k]] += 1
end

max = counts.values.max

puts max

str = []
counts.each do |strings, i|
  if i == max
    str << strings
  end
end

str = str.sort

str.each do |strings|
  print "#{strings} "
end
