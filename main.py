def get_bingo_letter(n):
    if 1 <= n <= 15:return 'B'
    elif 16 <= n <= 30:return 'I'
    elif 31 <= n <= 45:return 'N' 
    elif 46 <= n <= 60:return 'G' 
    elif 61 <= n <= 75:return 'O' 

if __name__ == '__main__':
    print(get_bingo_letter(75))
    print('-----')
    print(get_bingo_letter(54))
    print('-----')
    print(get_bingo_letter(25))
    print('-----')
    print(get_bingo_letter(38))
    print('-----')
    print(get_bingo_letter(11))