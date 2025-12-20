n, m, k = gets.split(" ").map(&:to_i)
h = gets.split(" ").map(&:to_i)
b = gets.split(" ").map(&:to_i)

h = h.sort
b = b.sort

count = 0
j = 0

h.each do |i|
  if j >= b.length 
    break
  end 

  if i > b[j] 
    j += 1
    redo
  end

  j += 1
  count += 1
end

if count >= k
  puts 'Yes'
else
  puts 'No'
end
