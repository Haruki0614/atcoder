h, b = gets.split(" ").map(&:to_i)

ans = h - b

if ans > 0
  puts ans
else
  puts 0
end
