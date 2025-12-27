s = gets.chomp.split("")

(1...(s.length-1)).each do |i|
  unless s[i-1] == s[i] && s[i] == s[i+1]
    if s[i-1] == s[i]
      puts s[i+1]
    elsif s[i] == s[i+1]
      puts s[i-1]
    else
      puts s[i]
    end

    exit
  end
end
