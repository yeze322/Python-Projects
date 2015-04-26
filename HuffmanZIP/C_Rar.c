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
int main(int argc,char *argv[])
{
    if(argc!=2){
        printf("Error Input!\n");
        exit(1);
    }
    char srcfile[100]="";
    strcpy(srcfile,argv[1]);
    FILE *fr = fopen(srcfile,"r");
    strcat(srcfile,".hzip");
    FILE *fw = fopen(srcfile,"w");
    char buf[32]="";
    int count = 0;
    do{
        memset(buf,0,32);
        count = fread(buf,sizeof(char),32,fr);
        transfer.num = str_to_bit_int(buf);
        fwrite(transfer.str,sizeof(char),4,fw);
        transfer.num = 0;
    }
    while(count==32);
    printf("last one : %#X,%d",transfer.num,count);
    fclose(fr);
    fclose(fw);
    return 0;
}

int str_to_bit_int(char str[N])
{
    int ret = 0;
    for(int i=0; i<N; i++)
    {
        ret = (ret<<1)|(str[i]-'0');
    }
    return ret;
}
