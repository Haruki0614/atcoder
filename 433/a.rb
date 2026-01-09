x, y, z = gets.split(" ").map(&:to_i)

i = 0
while i < 100 do
  if x+i == (y+i) * z
    puts 'Yes'
    exit
  end
  i += 1
end

puts 'No'
