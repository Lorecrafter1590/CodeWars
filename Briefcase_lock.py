def min_turns(current_lock, target_lock):
    movements_array = []
    current_lock = [int(x) for x in str(current_lock)]
    target_lock = [int(x) for x in str(target_lock)]
    
    for element in range(0,4):
        current = current_lock[element]
        target = target_lock[element]
        if (current + 5) == target or (current - 5) == target:
            movements_array.append(5)
        elif current == target:
            movements_array.append(0)
        elif (current > (target - 5) and current < target):
            movements_array.append(target - current)
        elif (current > target and current < (target + 5)):
            movements_array.append(current - target)
        elif current > (target + 5):
            movements_array.append(10 - current + target) 
        elif current < (target - 5): 
            movements_array.append(10 - target + current) 
            
    sum_movements = sum(movements_array)
    print(movements_array)
    return sum_movements

min_turns(4234,5682)