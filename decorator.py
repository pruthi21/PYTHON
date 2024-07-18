'''def shop(watch):
    def wrap():
        print('before the function is callled')
        watch()
        print('after the function is callled')
    return wrap

@shop
def watch():
    print("watches")
#watch= shop(watch)
watch()
print()'''


def add(num):
    def wrap():
        a=10
        r=a+num()
        return r
    return wrap

def mul(num):
    def wrap():
        x=5
        r=x*num()
        return r
    return wrap
@add
@mul
def num():
    return 20

# num =mul(add(num))
print(num())