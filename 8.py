import random
import math
import array
numbers = array.array('i', [random.randint(1, 10) for _ in range(1, random.randint(1, 10000) + 1)])
powtwo = math.ceil(math.log(len(numbers), 2))
print("Длина массива {}\n{}".format(len(numbers), numbers))
print("Ближайшая верхняя степень двойки: {}\nДвойка в этой степени {}\nНулей надо добавить: {}".format(powtwo, 2 ** powtwo, 2 ** powtwo - len(numbers)))
numbers += array.array('i', [0] * (2 ** powtwo - len(numbers)))
print(numbers)