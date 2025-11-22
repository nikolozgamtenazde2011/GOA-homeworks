#6)შექმენით ფუნქცია რომელსაც გადაეცემა რენდომ სია , ამ ფუნქციამ უნდა დააბრუნოს თავდაპირველი სია ოღონდ რევერსულად(შებრუნებული) ([1,4,7] → [7,4,1]
random_LIST = [3, 5, 7, 9, 11]
def reverse_list(random_LIST):
    reversed_LIST = []
    for i in range(len(random_LIST)-1, -1, -1):
        reversed_LIST.append(random_LIST[i])
    return reversed_LIST
print(reverse_list(random_LIST))