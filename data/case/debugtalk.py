import hashlib
import random
import string

def gen_random_string(str_len):
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))

def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()
if __name__ == '__main__':
    print(gen_random_string(5))  # => A2dEx

    TOKEN = "debugtalk"
    data = '{"name": "user", "password": "123456"}'
    random = "A2dEx"
    print(gen_md5(TOKEN, data, random))  # => a83de0ff8d2e896dbd8efb81ba14e17d