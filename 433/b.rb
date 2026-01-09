n = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)

(0...n).each do |i|
  index = false
  (0...i).each do |j|
    index = j+1 if a[i] < a[j]
  end

  puts index ? index : -1
end
