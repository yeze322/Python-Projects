#include <stdio.h>
#include <stdlib.h>
#include <string.h>
union int_to_char
{
    int num;
    char str[4];
} transfer;
#define N 32
int str_to_bit_int(char [N]);
int main()
{
    printf("sizeof int  = %lu\n",sizeof(int));
    char str[33]="";
    for(int i=0;i<4;i++){
        strcat(str,"1111");
        strcat(str,"0000");
    }
    transfer.num = str_to_bit_int(str);
    printf("transfer num = %#X\ntransfer str = %s\n",transfer.num,transfer.str);
    FILE *fp = fopen("cwrite.txt","w");
    fwrite(transfer.str,1,8,fp);
    fclose(fp);
    fp = fopen("cwrite.txt","r");
    fread(transfer.str,1,8,fp);
    fclose(fp);
    printf("decode = %#X",transfer.num);
    return 0;
}

int str_to_bit_int(char str[N])
{
    int ret = 0;
    printf("str = %s,size = %lu\n",str,strlen(str));
    for(int i=0; i<N; i++)
    {
        putchar(str[i]);
        ret = (ret<<1)|(str[i]-'0');
    }
    printf("\nretval = %x\n",ret);
    return ret;
}
