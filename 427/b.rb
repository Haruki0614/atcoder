n = gets.to_i

a = []
a[0] = 1
a[1] = 1
a[2] = 2

sum = a[0] + a[1]
(n - 1).times do |i|
  temp = 0
  copy = a[i+2]
  while copy > 0
    temp += copy % 10
    copy /= 10
  end

  a[i+3] = sum + temp
  sum = a[i+3]
end

puts a[n]
