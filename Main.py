import Counting

def strNum2NumList(seq: str):        
        return [int(num) for num in seq.strip().split(' ')]

def is_continuous(num_list):
    for i in range(1, len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            return False

    return True

def main():
    init = Counting.Counting_AI()
    turn = 0
    num_list = []
    start_point = 0
    while True:
        if turn == 0:
            user_input = input(f'Enter your sequence {turn}: ')
            num_list = strNum2NumList(user_input)

            if not is_continuous(num_list) or len(num_list) > 3 or num_list[0] != start_point + 1:
                continue

        if turn == 1:
            num_list = init.ai(num_list)

        start_point = num_list[-1]
        if turn == 1:
            turn = 0
        else:
            turn = 1

        print(num_list)
        if init.is_win(num_list):
            print(f'{turn} is win')
            break
if __name__ == '__main__':
    main()