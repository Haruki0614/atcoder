s, a, b, x = gets.split(" ").map(&:to_i)

sec = 0
total = 0
while sec < x do 
  a.times do |i|
    break unless sec < x
    total += s
    sec += 1
  end

  b.times do |i|
    sec += 1
  end
end

puts total
