def main():
    c11 = 9
    ans = ''
    num4_chunk = ''
    mul_chunk4 = ''
    while ans != '2020':
        throw = True
        throw_mul = True
        time.sleep(1)
        chunk4 = four_digit_numbers[c0:c1]
        mul_chunk4 = four_digit_number[c00:c11]
        print(f'debug - raw chunk- {chunk4}')
        chunk4 = ''.join([str(x) for x in chunk4])
        c0 += 1
        c1 += 1
        for x in chunk4: # not working' :( - [throw == True for x in chunk4 if x.isspace() or x.isdigit() == False]
            if x.isspace() or x.isdigit() == False:
                throw = False
        if throw == True:
            print(f'debug - good answer - {chunk4} - throw - {throw}')
            for x in range(len(four_digit_numbers)):
                for x in mul_chunk4:
                    if x.isspace() or isdigit() == False:
                        throw_mul = False
            if throw_mul == True:
                pass # ASIGDL IAUSHD ASJDA SJDASJD ASDKBASDKJ
            if throw_mul == False:
                pass
    
        if throw == False:
                pass
if __name__ == '__main__':
    main()
