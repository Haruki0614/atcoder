n, m = gets.split(" ").map(&:to_i)
a = gets.split(" ").map(&:to_i)

sum = a.sum

n.times do |i|
  if sum - a[i] == m
    puts 'Yes'
    exit
  end
end

puts 'No'
