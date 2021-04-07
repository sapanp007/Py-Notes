"""
simple generator
"""


def gen1():
    for i in range(100):
        yield i


def muutable_args(d=[]):
    d.append(99)
    return d


if __name__ == "__main__":
    # print(gen1())
    print(muutable_args())
    print(muutable_args())
    print(muutable_args())
    print(muutable_args([108]))
    print(muutable_args([90]))
    print(muutable_args())
    print(muutable_args())

"""
[99]
[99, 99]
[99, 99, 99]
[108, 99]
[90, 99]
[99, 99, 99, 99]
[99, 99, 99, 99, 99]
"""