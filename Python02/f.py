nums_str = input('請輸入三個數，數字之間加入空格：').split()

nums = [] 

while True:
    for n in nums_str:
        if n.isdigit():   
            nums += [int(n)]

        if len(nums) == 3:
            break

    if len(nums) < 3:
        nums_str = input('請繼續輸入：').split()
    else:
        break

print(nums)