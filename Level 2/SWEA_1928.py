if __name__ == '__main__':
    T = int(input())

    #index는 값, 원소는 문자를 의미
    decode = []
    for i in range(ord('A'), ord('Z') + 1):
        decode.append(chr(i))
    for i in range(ord('a'), ord('z') + 1):
        decode.append(chr(i))
    for i in range(0, 10):
        decode.append(str(i))
    decode.append('+')
    decode.append('/')

    for test_case in range(1, T + 1):
        string = input()

        origin_bit = ''
        for s in string:
            #encoding 과정에서 숫자를 문자로 변환했으니 decoding 과정에서는 문자를 숫자로 변환
            #bin을 통해 10진수를 2진수(bit)로 변환, 슬라이싱을 통해 0b는 제거
            #2진수가 여섯 자리가 아니면 0으로 채움
            origin_bit += bin(decode.index(s))[2:].zfill(6)

        origin_string = ''
        #2진수(bit)를 8개씩 끊어서 10진수로 변환 후 문자로 변환
        for i in range(0, len(origin_bit), 8):
            origin_string += chr(int(origin_bit[i:i+8], 2))

        print(f"#{test_case} {origin_string}")
