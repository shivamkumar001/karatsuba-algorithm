def karatsuba_algo(num_1, num_2):
    num1Str = str(num_1)
    num2Str = str(num_2)
    if (num_1 < 10) or (num_2 < 10):
        return num_1*num_2

    maxLength = max(len(num1Str), len(num2Str))
    pos = maxLength // 2
   
    a1, b1= int(num1Str[:-pos]), int(num1Str[-pos:])
    c1, d1= int(num2Str[:-pos]), int(num2Str[-pos:])
    z2 = karatsuba_algo(b1, d1)
    z3 = karatsuba_algo((b1 + a1), (d1 + c1))
    z1 = karatsuba_algo(a1, c1)
    z4=z3-z2-z1
  

    return (z1*10**(2*pos)) + ((z4)*10**(pos))+z2
a=int(input("enter 1 no"))
b=int(input("enter 2 no"))
ans=karatsuba_algo(a,b)


print(ans)