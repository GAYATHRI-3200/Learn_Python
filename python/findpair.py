#Find the pair with a given number in a list

nums = [8,7,2,5,3,1]
target = 10

num_len = len(nums)
for i in range(num_len):
    for j in range(i+1,num_len):
        if (nums[i] + nums[j]) == target:
            print(nums[i],nums[j])