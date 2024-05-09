word = input("Введите слово: ")

array = []
array1 =['a', 'e', 'i', 'o', 'u']

for i in word:
    array.append(i)
 
a = array.count("a")
e = array.count("e")
i = array.count("i")
o = array.count("o")
u = array.count("u")

if (a+e+i+o+u) != 0:
    print("Ваше слово содержит гласные:")
    print("Количество гласных a =", a)
    print("Количество гласных e =", e)
    print("Количество гласных i =", i)
    print("Количество гласных o =", o)
    print("Количество гласных u =", u)
elif (a+e+i+o+u) == 0:
    print("False")
print("Количество гласных = ", a+e+i+o+u)
print("Количество согласных = ",(len(array) - (a+e+i+o+u)))
