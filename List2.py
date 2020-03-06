
def reemove_adjacent(nums):
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
        return result


def linear_merge(list11, list2):
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

        result.extent(list1)
        result.extend(list2)
        return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '
        print '%s got
