object = {
    '0': [1, 2, 3, 4, 'a', 'b'], 
    'kdjfdkfjd': [1, 2, 3, 4, 5],
    '1': [5, 2, 4, 1] 
}
def calculate_avarage(obj):
    result = {}
    for key, value in obj.items():
        if key.isdigit() and isinstance(value, list):
            nums = []
            for x in value:
                if isinstance(x, int or float):
                    nums.append(x)
            if nums:
                avg = int(sum(nums)/len(nums))
                result[key] = avg
    return result


result = calculate_avarage(object)
print(result)