def get_next_collatz(prev):
    if prev % 2 == 0:
        return prev / 2
    else:
        return 3 * prev + 1

chain_lengths = {}
chain_lengths[1] = 1

def calc_collatz_length(num):
    if num in chain_lengths:
        return chain_lengths[num]
    collatz_length = calc_collatz_length(get_next_collatz(num)) + 1
    chain_lengths[num] = collatz_length
    return collatz_length

for i in range(1, 1000000):
    calc_collatz_length(i)

max_chain = 0
max_value = 0
for key in chain_lengths:
    cur_length = chain_lengths[key]
    if cur_length > max_chain:
        max_chain = cur_length
        max_value = key

def get_answer():
    return max_value
    
if __name__ == '__main__':
    print(get_answer())