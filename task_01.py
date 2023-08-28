# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Функция должна возвращать логическое значение и быть нечувствительным к регистру.
# Строка может содержать любые символы.

# Примеры ввода/вывода:
#   XO("ooxx") => true
#   XO("xooxx") => false
#   XO("ooxXm") => true
#   XO("zpzpzpp") => true # когда нет "x" и "o", должно быть возвращено значение true
#   XO("zzoo") => false

# Решение

def xo(s):
    cx = s.lower().count('x')
    co = s.lower().count('o')

    if cx == co:
        return True
    else:
        return False

# вызов
if __name__ == "__main__":
    print(xo("ooxx"))
    print(xo("xooxx"))
    print(xo("zpzpzpp"))
