r"""
使用Python新建的OpenSSL基本类，目前仅支持v3.2版本里的openssl genpkey指令，之后将逐步添加新的内容。

一共有以下的类：
 - OpensslCommand
 - OpensslGenpkey（继承自OpensslCommand）
"""

import os

'''
第一步：执行openssl genpkey命令，在指定文件夹下生成*.key文件作为默认的密钥。
完整指令格式如下：
openssl genpkey -out filename -outpubkey filename -algorithm RSA -pkeyopt rsa_keygen_bits:numbits
-pkeyopt rsa_keygen_primes:numprimes
对应的字典格式数据为：
['openssl', 'genpkey', '-out', 'filename', '-outpubkey', 'filename', '-algorithm', 'RSA', '-pkeyopt', 
'rsa_keygen_bits:numbits', '-pkeyopt', 'rsa_keygen_primes:numprimes']
'''
workdir = os.getcwd()  # 当前文件夹所在的目录
# print(workdir)


class OpensslCommand(object):
    """
    所有类的基类。以后所有Openssl命令共有的部分将放到一起，其他的方法类基于此派生。
    """
    __arg_genpkey = ['openssl', 'genpkey', '-out', 'filename', '-outpubkey', 'filename', '-algorithm', str, '-pkeyopt',
                     'rsa_keygen_bits:numbits', '-pkeyopt', 'rsa_keygen_primes:numprimes']
    separator = '\\'

    def __init__(self, target_dir: str, option: str, filename: str):
        self.targetdir = target_dir
        self.filename = filename
        self.option = option

    def __filetype(self, type_name: str) -> str:
        """
        用于设定文件名的类型。
        :param type_name: 指定的文件类型。\n仅限key,pub,csr和crt四种。
        :return: 如果文件类型在允许的范围内，就返回对应的文件名。否则，返回空字符串。
        """
        self.type_name = type_name
        typename = ['key', 'pub', 'csr', 'crt']
        if self.type_name in typename:
            return self.type_name
        else:
            return ''

    def set_option(self):
        """
        用于设置__arg_list中的实际选项。
        :return: 该方法无返回值。
        """
        OpensslCommand.__arg_genpkey[1] = self.option

    def set_filename(self, filetype: str):
        """
        设置输出密钥的文件名，并将其存储到列表中。
        :param filetype: 指定的文件类型。仅限key,pub,csr,crt四种。
        :return: 文件的绝对路径。
        """
        name = self.targetdir + OpensslCommand.separator + self.filename + '.' + OpensslCommand.__filetype(self,
                                                                                                           filetype)
        return name


class OpensslGenpkey(OpensslCommand):
    __arg = ['openssl', 'genpkey', '-out', 'filename', '-outpubkey', 'filename', '-algorithm', 'RSA', '-pkeyopt',
             'rsa_keygen_bits:numbits', '-pkeyopt', 'rsa_keygen_primes:numprimes']

    @staticmethod
    def get_arg():
        """
        获取最终的命令列表。
        :return: 完成修改的arg列表。
        """
        result = OpensslGenpkey.__arg
        return result

    def set_out_file(self):
        OpensslGenpkey.__arg[3] = OpensslGenpkey.set_filename(self, 'key')

    def set_pub_file(self):
        OpensslGenpkey.__arg[5] = OpensslGenpkey.set_filename(self, 'pub')

    @staticmethod
    def set_rsa_numbits(numbits=4096):
        """
        设置rsa公钥的模数
        :param numbits: 推荐使用4096作为默认大小。此外，也可以使用1024、2048、8192等值。
        :return: 无返回值。
        """
        if type(numbits) is not int:
            numbits = 4096
        OpensslGenpkey.__arg[9] = f'rsa_keygen_bits:{numbits}'

    @staticmethod
    def set_rsa_primes(numprimes: int):
        """
        设置RSA公钥的质数
        :param numprimes:RSA公钥的质数。不能大于5.
        :return:
        """
        if (type(numprimes) is not int) or numprimes > 5:
            numprimes = 2
        OpensslGenpkey.__arg[11] = f'rsa_keygen_primes:{numprimes}'
