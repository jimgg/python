# -*- coding: utf-8 -*-

# 参考wiki的伪代码：https://en.wikipedia.org/wiki/Mersenne_Twister

MT = [0 for i in range(624)]


class IndexGlb(object):
    def __init__(self):
        self.index = 0

indexGlb = IndexGlb()


def initialize_generator(seed):
    i = 0
    MT[0] = seed & 0xffffffff
    for i in range(1, 624):  # 遍历剩下的每个元素 1..623
        MT[i] = (1812433253 * (MT[i-1] ^ (MT[i-1] >> 30)) + i) & 0xffffffff


def extract_number():
    index = indexGlb.index
    if index == 0:
        generate_numbers()

    y = MT[index]
    y = y ^ (y >> 11)
    y = y ^ (y << 7 & 0x9d2c5680)  # 2636928640
    y = y ^ (y << 15 & 0xefc60000)  # 4022730752
    y = y ^ (y >> 18)

    indexGlb.index = (index + 1) % 624
    return y


def generate_numbers():
    for i in range(624):
        y = (MT[i] & 0x80000000) + (MT[(i+1) % 624] & 0x7fffffff)
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if (y % 2):
            MT[i] = MT[i] ^ 0x9908b0df  # 2567483615


if __name__ == '__main__':
    seed = 4098487615
    initialize_generator(seed)
    for i in range(1024):
        print extract_number()
