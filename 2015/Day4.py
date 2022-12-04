import hashlib

def day4():
    input = 'bgvyzdsv'
    start = 99999
    result = hashlib.md5((input+str(start)).encode())
 
    while not (result.hexdigest()[0] == '0' and result.hexdigest()[1] == '0' and result.hexdigest()[2] == '0' and result.hexdigest()[3] == '0' and result.hexdigest()[4] == '0'):
        start += 1
        result = hashlib.md5((input+str(start)).encode())
    
    part1 = start
    start = 99999
    result = hashlib.md5((input+str(start)).encode())

    while not (result.hexdigest()[0] == '0' and result.hexdigest()[1] == '0' and result.hexdigest()[2] == '0' and result.hexdigest()[3] == '0' and result.hexdigest()[4] == '0'and result.hexdigest()[5] == '0'):
        start += 1
        result = hashlib.md5((input+str(start)).encode())
    part2 = start

    return part1, part2

print(day4())
