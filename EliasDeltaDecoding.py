import math
from copy import deepcopy

def decoding(sequence,position):
    for i in range(position,len(sequence)):
        if sequence[i] == '0':
            if i == position:
                result.append(0)
                return decoding(sequence, i + 1)
            else:
                dd = len(sequence[position:i])
                dd_length = dd + 1
                dr_base2 = sequence[i+1:i+1 + dd]
                dr_length = len(str(dr_base2))
                dr = int(dr_base2,2)
                d = dr - 1 + 2 ** dd
                length = d + 2 * dd + 1
                kr_length = length - dd_length - dr_length
                part = sequence[position:position+length]
                print("Partial Code:",part)
                kr = int(part[-kr_length:],2)
                print("Result: d = %d,r = %d,dd = %d,dr = %d\n" %(d,kr,dd, dr))
                output = 2 ** d + kr
                result.append(output)
                return decoding(sequence,position+length)

result = list()
in_ = input()
sequence = str(in_)
decoding(sequence,0)
print(result)

