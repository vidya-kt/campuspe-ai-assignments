count = int(input("How many numbers do you want to add? "))

number = int(input("Enter number 1: "))
min_val = number
max_val = number
sum = number

nums = [number]   # for median and mode

for i in range(count-1):
    number = int(input(f"Enter number {i+2}: "))

    nums.append(number)

    if number > max_val:
        max_val = number

    if number < min_val:
        min_val = number

    sum += number

avg = sum/count

print("1. Sum =",sum)
print("2. Average =",avg)
print("3. Maximum =",max_val)
print("4. Minimum =",min_val)


#Median
nums.sort()

if count % 2 == 1:
    median = nums[count//2]
else:
    median = (nums[count//2 - 1] + nums[count//2]) / 2

print("5. Median =", median)


#Mode
mode = nums[0]
max_count = 0

for i in nums:
    freq = nums.count(i)

    if freq > max_count:
        max_count = freq
        mode = i

if max_count == 1:
    print("6. Mode = No mode")
else:
    print("6. Mode =", mode)