n = gets.to_i

a = gets.chomp.split(" ").map(&:to_i)

count = 0
(0...a.length).each do |i|
  sum = 0
  (i...a.length).each do |j|
    flag = 0
    sum += a[j] 
    (i..j).each do |k|
      if sum % a[k] == 0
        flag = 1
        break
      end
    end
    count += 1 if flag == 0
  end
end

puts count
