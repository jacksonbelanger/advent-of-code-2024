def part1(lines):
    safe_reports = 0
    
    for line in lines:
        nums = [int(num) for num in line.split()]

        safe_reports += is_safe(nums)
    
    return safe_reports

def part2(lines):
    nums = [int(num) for num in line.split()]

    safe_reports += is_really_safe(nums)

def is_safe(nums):
    direction = 0
    unsafe_levels = 0

    for i in range(1, len(nums)):
        cur_direction = 1
        if nums[i] < nums[i - 1]:
            cur_direction = -1
        
        diff = abs(nums[i] - nums[i - 1])

        if (-1 * cur_direction == direction or diff < 1 or diff > 3):
            return False

        direction = cur_direction
    
    return True

def is_really_safe(nums):
    direction = 0
    unsafe_levels = 0

    for i in range(1, len(nums)):
        cur_direction = 1
        if nums[i] < nums[i - 1]:
            cur_direction = -1
        
        diff = abs(nums[i] - nums[i - 1])

        if (-1 * cur_direction == direction or diff < 1 or diff > 3):
            return False

        direction = cur_direction
    
    return True


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        lines = file.readlines()
    
    print("Part 1", part1(lines))