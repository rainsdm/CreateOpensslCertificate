import GenerateKey
import subprocess
import os
import typing
import time

ssl_Key = GenerateKey.ssl_list


def ssl_genpkey(out: typing.TextIO):
    """
    执行已经生成的openssl genpkey指令。具体的方法见GenerateKey.py。
    :param out:
    :return:
    """
    s = time.time()
    subprocess.run(args=ssl_Key, stdout=out, timeout=10.0)
    e = time.time()
    c = e - s
    out.write('用时%.3f秒。\n' % c)


output_file = open(os.getcwd() + '\\genpkey_info.txt', 'w')
if __name__ == '__main__':
    ssl_genpkey(output_file)
