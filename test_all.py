import importlib
import sys

answers = [
    233168,
    4613732,
    6857,
    906609,
    232792560,
    25164150,
    104743,
    23514624000,
    31875000,
    142913828922,   # 10
    70600674,
    -1,
    5537376230,
    837799,
    137846528820,
    1366,
    21124,
    1074,
    171,
    648,            # 20
    31626,
    871198282,
    4179871,
    2783915460,
    4782,
    ]
    
ignore = [
    12
    ]

if __name__ == '__main__':
    test_pass = True
    for i in range(len(answers)):
        if i+1 in ignore:
            continue
        mod = importlib.import_module(str(i+1).zfill(3))
        print(str(i+1).rjust(3) + ':', end='', flush=True)
        cur_answer = mod.get_answer()
        if cur_answer == answers[i]:
            print(' OK: ' + str(cur_answer))
        else:
            print(' WRONG: Got ' + str(cur_answer) + ' instead of ' + str(answers[i]))
            test_pass = False
            
    print('==========')
    if test_pass == True:
        print('OK')
    else:
        print('FAIL')
        sys.exit(1)
        