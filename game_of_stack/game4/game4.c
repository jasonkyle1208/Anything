#include <stdio.h>
#include <unistd.h>

void init()
{
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}
int getshell()
{
    return system('/bin/sh');
}
int main()
{
    init();
    char buf[40];

    memset(0,buf,sizeof(buf));
    puts("What's your name?");
    read(0,buf,0x30);
    printf("Hello %s:\n",buf);
    read(0,buf,0x60);
    return 0;
}