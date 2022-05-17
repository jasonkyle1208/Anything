#include <stdio.h>

void jump()
{
    __asm__("jmp %esp");
}
void init()
{
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}
int vuln()
{
    char s[0x20];
    puts("Welcome to the game1");
    puts("What's your name?");
    fflush(stdout);
    fgets(&s,55,stdin);
    printf("Hello %s!",&s);
    fflush(stdout);
    return 1;
}
int main()
{
    init();
    vuln();
}