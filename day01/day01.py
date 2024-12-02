def getLists(lines):
    list1 = []
    list2 = []

    for line in lines:
        nums = line.strip().split("   ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
    
    return (list1, list2)

def part1(list1, list2):
    list1.sort()
    list2.sort()

    ans = 0

    for i in range(len(list1)):
        ans += abs(list1[i] - list2[i])

    return ans

def part2(list1, list2):
    list2_count = {}

    for num in list2:
        if num in list2:
            list2[num] += 1
        else:
            list2[num] = 1
    
    similarity_score = 0

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        lines = file.readlines()
    
    list1, list2 = getLists(lines)

    print("Part 1:", part1(list1, list2))