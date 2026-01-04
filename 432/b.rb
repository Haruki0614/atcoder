x = gets.chomp.split("").map(&:to_i)

sort_x = x.sort

result = ""
count = 0

sort_x.each do |num|
  if num == 0
    count += 1
    next
  end

  result = result + num.to_s

  count.times do
    result = result + '0'
  end

  count = 0
end

puts result
