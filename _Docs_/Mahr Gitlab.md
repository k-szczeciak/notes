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


```
ssh-keygen -t ed25519 -C "<comment>"
```
```
ssh-keygen -t rsa -b 2048 -C "<comment>"
```
eval $(ssh-agent -s) 
ssh-add ~/.ssh/id_rsa 

[info](https://docs.gitlab.com/ee/user/ssh.html)

example:
$ git clone oauth2:1AbCDe F _ g2HIJKLMNOPqr@gitlab.com/yourusername/project.git project

my:
nsUwG5HiYYL1zJ2bJvSf:

git clone https://oauth2:nsUwG5HiYYL1zJ2bJvSf@gitlab.mahr.com/Szczeciak/MarCator.git

git remote add origin git@gitlab.mahr.com:precision-gages/marcator/marcator-firmware-main-mcu.git




git config --global user.name "Krzysztof Szczeciak"
git config --global user.email "krzysztof.szczeciak@mahr.com"

##### Create a new repository

git clone git@gitlab.mahr.com:precision-gages/marcator/marcator-firmware-main-mcu.git
cd marcator-firmware-main-mcu
git switch -c main
touch README.md
git add README.md
git commit -m "add README"
git push -u origin main

##### Push an existing folder

cd existing_folder
git init --initial-branch=main
git remote add origin git@gitlab.mahr.com:precision-gages/marcator/marcator-firmware-main-mcu.git
git add .
git commit -m "Initial commit"
git push -u origin main

##### Push an existing Git repository

cd existing_repo
git remote rename origin old-origin
git remote add origin git@gitlab.mahr.com:precision-gages/marcator/marcator-firmware-main-mcu.git
git push -u origin --all
git push -u origin --tags

git remote add origin  https://oauth2:nsUwG5HiYYL1zJ2bJvSf@gitlab.mahr.com:precision-gages/marcator/marcator-firmware-main-mcu.git

check log ssh:
ssh -vvvT ‘git@gitlab.mahr.com

```
ssh -T git@gitlab.mahr.com
```


token office pc:
j24UuzJPUA6AT_MxqSzx
feed token:
_MJ5oFcWdAJHFwEroPGP

resetowanie tokena:
git config --global credential.helper cache
git config --global --unset credential.helper

klonowanie z historia:
- ```
git clone --bare <url>
git clone --bare https://github.com/k-szczeciak/C1202.git
cd C1202.git
git push --mirror https://gitlab.mahr.com/precision-gages/millimar-c1202/millimar-c1202-firmware-main-mcu.git


projekty do importu:
- MarCator
- A1701
- C102
- MillimarTool
|   #   |   projekt    |       status        | office PC |             home PC             | laptop | image,other |
| :---: | :----------: | :-----------------: | :-------: | :-----------------------------: | :----: | :---------: |
|   1   |   MarCator   | ported folder only  |     -     | remote set, updated, 05.01.2023 |   -    |      -      |
|   2   |    C1202     | cloned with history |     -     | remote set, updated, 05.01.2023 |   -    |      -      |
|   3   | MillimarTool | cloned with history |     -     | remote set, updated, 05.01.2023 |   -    |      -      |
|   4   |    A1701     |   ported from svn   |     -     | remote set, updated, 05.01.2023 |   -    |      -      |




pytania:
- ssh - connections
- yubikey add
- git gui tool (git kraken, git tower, git fork, git s...)
- gitlab application server
WN 6741R




dodac Tagi
cleanup
poczytac o gitflow
rebase
fork
mirroring repos
inne:
- CI/CD (unit testing, automation tetsing)
- deployments apps

new remote



remove remote:
> git remote remove old-origin

> git remote add origin https://Szczeciak:<token>@gitlab.mahr.com/precision-gages/marcator/marcator-firmware-main-mcu.git
> git push --set-upstream origin master


lub wszystkie origin-y:
> git push -u origin all


inne:
- [resetowanie origin-a](https://www.freecodecamp.org/news/git-reset-to-remote-head-how-to-reset-a-remote-branch-to-origin/)

> `git remote show origin`

git log --oneline
last 5 commits



to be removed projects:
https://gitlab.mahr.com/precision-gages/marcator-firmware-touch
https://gitlab.mahr.com/precision-gages/marcator/marcator
https://gitlab.mahr.com/precision-gages/marcator-firmware-touch-mcu

https://gitlab.mahr.com/precision-gages/c1202-basic-demo-csharp
https://gitlab.mahr.com/rd-precision-gages-public-repositories/C1202-basic-demo-csharp
