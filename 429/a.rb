n, m = gets.split(" ").map(&:to_i)

if n > m 
  m.times do |i|
    puts 'OK'
  end

  (n - m).times do |i|
    puts 'Too Many Requests'
  end
else
  n.times do |i|
    puts 'OK'
  end
end
