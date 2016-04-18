def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError :
        print('err inval arg')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
