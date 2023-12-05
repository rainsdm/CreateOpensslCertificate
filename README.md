# CreateOpensslCertificate
这是一个全新的项目，主要为OpenSSL加了一层Python的外壳。目前支持的Openssl版本是v3.2。

## 安装方法：
```bash
git clone git@github.com:rainsdm/CreateOpensslCertificate.git
```

# 主要功能
执行v3.2版本的以下指令 ：
```bash
openssl genpkey -out filename -outpubkey filename -algorithm RSA -pkeyopt rsa_keygen_bits:numbits
-pkeyopt rsa_keygen_primes:numprimes
```
