# Самостоятельная работа по уроку "Рекурсия"

def get_multiplying_digits(number: int):
    str_number = str(number)
    first=int(str_number[0])
    if len(str_number) > 1:
        # print(f' pop: {str_number[0]}, remain: {int(str_number[1:])} ')
        return first * get_multiplying_digits(int(str_number[1:]))
    else:
        return first


# result=get_multiplying_digits(40203)
result=get_multiplying_digits(96205)
print(result)