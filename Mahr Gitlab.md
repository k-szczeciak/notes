- URL 
- auth codes:
1d2f4127def62281
c1a98a62e01fa362
c57dc3b5cfdf1371
faf35505174e9da9
f2a12e7c5a4937db
8ea66963650945cd
a45c5188ededc1ad
831450e1cd625cd7
5b1c60016e3b6bc1
eb41a2e5e0932a26

- login: szczeciak
- pass: as for main comp (Taboret11.2022#)
- email: krzysztof.szczeciak@mahr.com
- url: [gitlab.mahr.com](gitlab.mahr.com)
- [generateKey in PS](https://docs.oracle.com/en/cloud/cloud-at-customer/occ-get-started/generate-ssh-key-pair.html)
- [putty keygen](https://www.howtogeek.com/762863/how-to-generate-ssh-keys-in-windows-10-and-windows-11/)
- [online key gen](https://cryptotools.net/rsagen)


github:
git config --global user.email krzysztof.szczeciak@icloud.com
git config --global user.name k-szczeciak

git config --global user.name "Krzysztof Szczeciak"
git config --global user.email "krzysztof.szczeciak@mahr.com"


eval $(ssh-agent -s) 
ssh-add ~/.ssh/id_rsa 

[info](https://docs.gitlab.com/ee/user/ssh.html)
