n, q = gets.split(" ").map(&:to_i)

machines = Array.new(n, 1)
head = 0

q.times do
  x, y = gets.split(" ").map(&:to_i)

  count = 0
  while head < x
    count += machines[head]
    machines[head] = 0
    head += 1
  end

  puts count
  machines[y-1] += count
end
