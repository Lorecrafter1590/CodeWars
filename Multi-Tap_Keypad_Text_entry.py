def presses(phrase):
    phrase = phrase.lower()
    tap_counter = []
    one_tap_array = ['a','d','g','j','m','p','t','w','*',' ','#','1']
    two_tap_array = ['b','e','h','k','n','q','u','x','0']
    three_tap_array = ['c','f','i','l','o','r','v','y']
    four_tap_array = ['2','3','4','5','6','s','8','z']
    five_tap_array = ['7','9']
    for x in phrase:
        if any(element in x for element in one_tap_array):
            tap_counter.append(1)
        elif any(element in x for element in two_tap_array):
            tap_counter.append(2)
        elif any(element in x for element in three_tap_array):
            tap_counter.append(3)
        elif any(element in x for element in four_tap_array):
            tap_counter.append(4)
        elif any(element in x for element in five_tap_array):
            tap_counter.append(5)
    return sum(tap_counter)

print(presses('HakunaMatata'))