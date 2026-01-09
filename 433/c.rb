s = gets.chomp.split("").map(&:to_i)
length = s.length

count = 0
(0...length-1).each do |i|
  j = i 
  k = i + 1

  if s[j] + 1 == s[k]
    j_count = 0
    k_count = 0

    while j-1 >= 0 && s[j-1] == s[j] do
      j_count += 1
      j -= 1
    end

    while k+1 < length && s[k] == s[k+1] do
      k_count += 1
      k += 1
    end

    count += [j_count, k_count].min + 1
  end
end


puts count
