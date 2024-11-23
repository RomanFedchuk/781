my_list = [1, 2, 3]
iterator = iter(my_list)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

my_list = [1, 2, 3]
iterator = iter(my_list)
for item in iterator:
    print(item)

for item in iterator:
    print(item)

class Counter:

    def __init__(self, max_number):
        self.i = 0
        self.maxnumber = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i






counter = Counter(5)
for i in counter:
    print(i)

def raise_to_degree(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

for i in raise_to_degree(123345, 500):
    print(i)



    class Car:

        def __init__(self, brand):
            self.brand = brand

            def __call__(self, *args, **kwargs):
                return f'It is a Car {self.brand} with {passengers}'

car = Car('BMW')
print(car(4)
      )

def helper(work):

    work_in_memory = work

    def helper(work):
        return f"I will help you with {work_in_memory}, after i will help with {work}"

    return helper




help = helper('homework')
print(help_('cleaning'))
print(help_('playing football'))


print(
    helper('homeworl')('cleaning')
)

def checker(func, *args, **kwargs):
    tr:
    result = func(*args, **kwargs)
    except Exception as ex:
    print(f'we have problem: {ex}')
    else:
    print(f'no problems. result: {result}')

def calculate(expression):
    return eval(expression)

calculate = checker(calculate('2+2'))
print(calculate)