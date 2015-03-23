#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <math.h>
union ip{
	char str_ip[16];
	long int int_ip[2];
};
int main()
{
	union ip ip;
	strcpy(ip.str_ip,"192.168.1.100");
	printf("%ld,%ld\n",ip.int_ip[0],ip.int_ip[1]);//save in long int
	printf("ip = %s\n",(char*)ip.int_ip);
	return 0;
}