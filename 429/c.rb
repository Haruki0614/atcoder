n = gets.to_i
a = gets.split(" ").map(&:to_i)

total = 0
count = Array.new(n, 0)

a.each do |value|
  count[value-1] += 1
end

count.each do |i|
  next if i == 0 || i == 1

  total += ((i * (i - 1)) / 2) * (n - i)
end

puts total
