from OpenSSL.CommandSet import OpensslGenpkey

a = r'E:\me\certificate\openssl\localhost\First'

genpkey = OpensslGenpkey(target_dir=a, option='genpkey', filename='localhost')
genpkey.set_option()
genpkey.set_filename('localhost')
genpkey.set_out_file()
genpkey.set_pub_file()
genpkey.set_rsa_numbits()
genpkey.set_rsa_primes(3)
ssl_list = genpkey.get_arg()
