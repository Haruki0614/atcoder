x, y = gets.split(" ")

if x == 'Ocelot'
  x = 0
elsif x == 'Serval'
  x = 1
else
  x = 2
end

if y == 'Ocelot'
  y = 0
elsif y == 'Serval'
  y = 1
else
  y = 2
end

if x >= y
  puts 'Yes'
else
  puts 'No'
end
