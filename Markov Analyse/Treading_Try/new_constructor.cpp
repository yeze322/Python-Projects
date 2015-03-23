/*************************************************************************
	> File Name: new_constructor.cpp
	> Author: Yeze
	> Mail: 2295905420@qq.com
	> Created Time: 2015年03月21日 星期六 00时13分42秒
 ************************************************************************/

#include<iostream>
#include<cstdio>
class tst {
public:
    int a;
    int b;

    tst():a(4),b(5){};
};
int main(int argc,char *argv[])
{
    tst *A = new tst;
    std::cout<<A->a<<A->b;
    char c = 10;
    printf("123%d\n",c);
    char a = '\72';
    std::cout<<a;
    int n = 0 , i;
    printf("argv = %d\n",'0');
    for(i = 1 ; i < argc ; i++){
        std::cout<<*argv[i]-'0'<<std::endl;
        n = n * 10 + *argv[i]-'0';
    }
    printf("%d\n",n);
    return 0;
}
