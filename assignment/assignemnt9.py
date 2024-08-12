start = 100
end = 200
total_sum =0

while start<= end:
    if start % 2==0:
        total_sum += start
    start += 1
print('the sum of all the number between 100 to 200 is:', total_sum)