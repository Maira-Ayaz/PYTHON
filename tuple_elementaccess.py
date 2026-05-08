def get_element(a,b):
        

        if b < len(a):
          return a[b]
        else:
           return -1

print(get_element((1,4,5,6,7),8))