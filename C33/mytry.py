try:
    print('我还在执行')
except:
    print('捕捉到异常')
finally:
    raise IndexError

print()
print('继续执行')
