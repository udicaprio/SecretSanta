import copy
import random

def generate_combinations(member_list):
    #This part of the code is to add some favour to the allocations
    shift_key = 3
    if len(member_list)<=3:
        shift_key = 1
    
    #This part of the code is to generate the allocations
    random.shuffle(member_list)
    receiver_list = copy.copy(member_list)
    to_append = receiver_list[:shift_key]
    receiver_list = receiver_list[shift_key:]
    receiver_list+=to_append

    return member_list, receiver_list