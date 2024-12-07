def part1(lines):
    safe_reports = 0
    
    for line in lines:
        nums = [int(num) for num in line.split()]

        safe_reports += is_safe(nums, -1)[0]
    
    return safe_reports

def part2(lines):
    safe_reports = 0
    
    for line in lines:
        nums = [int(num) for num in line.split()]

        safe_reports += is_really_safe(nums)
    
    return safe_reports

def is_safe(nums, indexToSkip):
    if len(nums) <= 1:
        return (True, -1)

    direction = None
    start = 1 if indexToSkip == 0 else 0
    prev = nums[start]

    for i in range(start + 1, len(nums)):
        if indexToSkip == i:
            continue

        cur_direction = 1
        if nums[i] < prev:
            cur_direction = -1
        
        diff = abs(nums[i] - prev)

        if ((direction is not None and cur_direction != direction) or diff < 1 or diff > 3):
            return (False, i)
        else:
            direction = cur_direction

            # update prev
            prev = nums[i]
    
    return (True, -1)

def is_really_safe(nums):
    if is_safe(nums, -1)[0]:
        return True

    for i in range(len(nums)):
        if is_safe(nums, i)[0]:
            return True
    
    return False

    # safe = is_safe(nums, -1)

    # if (safe[0]):
    #     return True
    
    # if is_safe(nums, safe[1])[0] or (safe[1] > 0 and is_safe(nums, safe[1] - 1)[0]) or (safe[1] > 1 and is_safe(nums, 0)[0]):
    #     return True

    # return False    

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        lines = file.readlines()
    
    print("Part 1", part1(lines))
    print("Part 2:", part2(lines))