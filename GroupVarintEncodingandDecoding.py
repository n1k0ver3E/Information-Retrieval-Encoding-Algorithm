import math

def encode_per_group(group):
    encoded = list()  
    tags = 0 
    offset = 6
    for i in range(len(group)):
        temp = group[i]
        count = 0x0
        if(temp != 0):
            current_byte = 0xFF
            while(temp != 0):
                 current_byte = current_byte & temp
                 count = count + 1
                 encoded.append(current_byte)
                 temp = temp >> 8
                 current_byte = 0xFF
            tags = tags | (count-1 << offset)
        else:
            encoded.append(0x00) 
            tags = tags | (count << offset)
        offset -= 2
    tag = tags
    res = list()
    res.append(tag)
    temp = [bin(code)[2:].zfill(8)for code in encoded]
    return res + encoded

def encode(posting_list):
    res = list()
    groups = [[0 for i in range(4)] for j in range(math.ceil(len(posting_list) / 4))]
    groups[0][0] = posting_list[0]
    for i in range(1, len(posting_list)):
        temp = posting_list[i] - posting_list[i-1]
        index = i // 4
        offset = i % 4
        groups[index][offset] = temp
    for group in groups:
        res = res + (encode_per_group(group))
    
    return bytearray(res)


def decode(encoded_list):
    decoded = list()
    encoded_list = [bin(code)[2:].zfill(8)for code in encoded_list]
    # print(encoded_list)
    index = 0
    while (index< len(encoded_list)):
        tags = encoded_list[index]
        index = index + 1
        # print(tags)
        offset = 6
        while(offset >= 0 and index < len(encoded_list)):
            selecter = ((int(tags,2) >> offset) & 3) + 1
            value = 0
        
            for i in range(selecter):
                trans = int(encoded_list[index],2)
                value = value | (trans << i*8)
                index = index + 1
                
            decoded.append(value)
            offset = offset - 2
        # print(value)
    res = list()
    total = 0
    for i in decoded:
        total = total + i
        if len(res)>0 and total == res[-1]:
            pass
        else: 
            res.append(total)
    return res

    
if __name__ == "__main__":
    
    # Encoding Process
    posting_list = [
        [1,16,257],
        [9, 22, 26, 31, 104, 234, 272, 325, 390, 456, 554, 605, 665],
        [138, 238, 273, 292, 341, 387, 458, 502, 531, 578, 613, 621, 777, 963, 1138, 1154, 1158, 1252, 1363, 1500, 1622, 1781, 1793, 1870, 2059, 2136, 2399, 2592, 2615, 2625, 2743, 2754, 2810, 2903, 2961, 3024, 3080, 3283, 3371, 3425, 3475, 3565, 3614, 3656, 3692, 3761, 4088, 4134, 4152, 4181, 4182, 4233, 4401, 4471, 4607, 4756, 4824, 4880, 4892, 5019, 5084, 5111, 5263, 5275, 5625, 5643, 5684, 6192, 6333, 6470, 6509, 6818, 6896, 6984, 6990, 7072, 7301, 7386, 7421, 7449, 7550, 7762, 8134, 8295, 8337, 8357, 8463, 8583, 8640, 8924, 9023, 9028, 9186, 9255, 9343, 9434, 9575, 9676, 9828, 9922]]
    for posting_set in posting_list:
        encoding_res = encode(posting_set)
        print(posting_set)
        print(encoding_res,"\n")
    
    # Decoding Process
    encoded_list = [
        bytearray(b'\x04\x01\x0f\xff\x01\x00'),
        bytearray(b'\x00\t\r\x04\x05\x00I\x82&5\x00ABb3\x00<\x00\x00\x00'),
        bytearray(b"\x00\x8ad#\x13\x001.G,\x00\x1d/#\x08\x00\x9c\xba\xaf\x10\x00\x04^o\x89\x00z\x9f\x0cM\x04\xbdM\x07\x01\xc1\x00\x17\nv\x0b\x008]:?\x008\xcbX6\x002Z1*\x04$EG\x01.\x00\x12\x1d\x013\x00\xa8F\x88\x95\x00D8\x0c\x7f\x00A\x1b\x98\x0cA^\x01\x12)\xfc\x01\x01\x8d\x89\'5\x01\x00NX\x06R\x00\xe5U#\x1c\x04e\xd4t\x01\xa1\x00*\x14jx\x109\x1c\x01c\x05\x00\x9eEX[\x00\x8de\x98^")]
    for encoded_set in encoded_list:
        decoding_res = decode(encoded_set)
        print(encoded_set)
        print(decoding_res,"\n")
