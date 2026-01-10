n, m = gets.chomp.split(" ").map(&:to_i)

average = Array.new(m, 0.0)
count = Array.new(m, 0)
(0...n).each do |i|
  a, b = gets.chomp.split(" ").map(&:to_i)

  average[a - 1] += b
  count[a - 1] += 1
end

(0...m).each do |i|
  puts average[i] / count[i]
end
