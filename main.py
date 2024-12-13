# 1=misol
# class SimpleIterator:
#     def __init__(self):
#         self.joriy = 1
#         self.end = 10
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.joriy <= self.end:
#             val = self.joriy
#             self.joriy += 1
#             return val
#         else:
#             raise StopIteration
# a = SimpleIterator()
# for raqam in a:
#   print(raqam)


# 2-misol
# my_list = [1, 2, 3, 4, 5]
# a = iter(my_list)
#
# for b in a:
#     print(b)

# 3-misol
# class ReverseIterator:
#     def __init__(self, list):
#         self.list = list
#         self.index = len(list)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index > 0:
#             self.index -= 1
#             return self.list[self.index]
#         else:
#             raise StopIteration
#
# my_list = [1, 2, 3, 4, 5]
# for a in ReverseIterator(my_list):
#     print(a)

# 4-misol
# string = "Python"
# a = iter(string)
#
# for char in a:
#     print(char)


# 5-misol
# class EvenIterator:
#     def __init__(self, list):
#         self.list = list
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.list):
#             a = self.list[self.index]
#             self.index += 1
#             if a % 2 == 0:
#                 return a
#         raise StopIteration
#
# raqam = [1, 2, 3, 4, 5, 6]
# for b in EvenIterator(raqam):
#     print(b)


# 6-misol
# raqamlar = [1, 2, 3, 4, 5]
# a = iter(raqamlar)
# qigindi = sum(a)
# print("Yig'indisi:", qigindi)


# 7-misol
# raqam = [1, 2, 3, 4, 5]
# b = iter(raqam)
#
# element = 6
# a = any(num == element for num in b)
# print(f"{element} ro'yxatda {'bor' if a else 'yo‘q'}.")



# Generatorlarga oid
# 1-misol
# def simple_range(start, end):
#     a = start
#     while a <= end:
#         yield a
#         a += 1
#
# for b in simple_range(1, 10):
#     print(b)


# 2-misol
# def soz_uuzunligi(text):
#     for soz in text.split():
#         yield len(soz)
#
# text = "Python va django"
# for a in soz_uuzunligi(text):
#     print(a)


# 3-misol
# def toq_sonlar(limit):
#     for toq in range(1, limit + 1, 2):
#         yield toq
#
# for a in toq_sonlar(10):
#     print(a)


# 4-misol
# def juft_sonlar(limit):
#     for a in range(2, limit + 1, 2):
#         yield a
# for juft in juft_sonlar(10):
#     print(juft)


# 5-misol
# def cheksis_son():
#     num = 1
#     while True:
#         yield num
#         num += 1
#
# for num in cheksis_son():
#     print(num)
#     if num > 10:
#         break


# 6-misol
# def kvadrat_son(a):
#     for num in range(1, a + 1):
#         yield num ** 2
#
# for kvadrat in kvadrat_son(5):
#     print(kvadrat)


# 7-misol
# def raqam_yigind(raqam):
#     son = 0
#     for num in raqam:
#         son += num
#         yield son
#
# for s in raqam_yigind([1, 2, 3, 4]):
#     print(s)

# 8-misol
# def filtirlash(raqam):
#     for num in raqam:
#         if num > 0:
#             yield num
#
# for a in filtirlash([-2, 0, 3, -5, 7]):
#     print(a)

# 9-misol
# import random
#
# def tasodiv_raqam(boshlash, start=1, end=100):
#     for _ in range(boshlash):
#         yield random.randint(start, end)
# for a in tasodiv_raqam(5):
#     print(a)

# 10-misol
# def tup_son(n):
#     boshlash = 0
#     num = 2
#     while boshlash < n:
#         if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#             yield num
#             boshlash += 1
#         num += 1
# for a in tup_son(5):
#     print(a)

# 11-misol
# def teskari_harf(text):
#     for a in reversed(text):
#         yield a
# for b in teskari_harf("Python"):
#     print(b)

# 12-misol
# def kopaytirmas(n):
#     mahsulot = 1
#     for i in range(1, n + 1):
#         mahsulot *= i
#         yield mahsulot
#
# for a in kopaytirmas(6):
#     print(a)
