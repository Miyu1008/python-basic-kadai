
var = 77

#3の倍数かつ5の倍数
if var % 15 ==0:
    print("FizzBuzz")

#3の倍数
elif var % 3 ==0:
    print("Fizz")

#5の倍数
elif var % 5 ==0:
    print("Buzz")

#該当なし
else:
    print(var)