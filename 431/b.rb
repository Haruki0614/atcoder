x = gets.to_i
n = gets.to_i
w = gets.split(" ").map(&:to_i)
q = gets.to_i

weight = x
flag = Array.new(n, false)

q.times do |n|
  p = gets.to_i

  if flag[p - 1] == true
    flag[p - 1] = false
    weight -= w[p - 1]
  else
    flag[p - 1] = true
    weight += w[p - 1]
  end

  puts weight
end
