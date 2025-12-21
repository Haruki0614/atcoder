n, m = gets.split(" ").map(&:to_i)

s = []

n.times do |i|
  s[i] = gets.split("")
end

count = []
(n-m+1).times do |l|
  (n-m+1).times do |k|
    temp = ''
    m.times do |i|
      m.times do |j|
        temp += s[l+i][k+j]
      end
    end

    unless count.include?(temp)
      count.push(temp)
    end
  end
end

puts count.length
