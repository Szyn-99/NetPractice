"""a very basic CIDR to Mask and vice versa"""
from sys import argv, exit
if len(argv) == 1:
    print("Usage example:\npython3 cidr /24")
    exit(1)
if argv[1] == 'cidr':
    cidr = argv[2].strip('/')
    mask = str("1" * int(cidr)).zfill(32)
    print(f"CIDR: /{argv[2]}\nMask: {'.'.join(reversed([str(int(mask[:8], 2)), str(int(mask[8:16], 2)), str(int(mask[16:24], 2)), str(int(mask[24:32], 2))]))}")
elif argv[1] == 'mask':
    mask = argv[2].split('.')
    mask = str(bin(int(mask[0]))+ bin(int(mask[1]))+ bin(int(mask[2])) + bin(int(mask[3]))).zfill(32)
    mask = mask.replace('0b', '')
    count_ones = 0
    print(f'Mask: {argv[2]}\nCIDR: /{sum(1 for digit in mask if digit == "1")}')
