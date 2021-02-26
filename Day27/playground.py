def add(*args):
    output = 0
    for n in args:
        output += n
    print(output)
    return output

add(3,4,5,6,7,8)