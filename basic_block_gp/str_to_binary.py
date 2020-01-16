

def str_to_binary(s: str) -> str:
    # if not s.ascii():
    #     raise ValueError('ASCII characters only allowed')

    return ' '.join(f"{ord(i):08b}" for i in s)


x  = str_to_binary('hello world')
