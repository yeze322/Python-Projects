#include<iostream>
#include<vector>
#include<sys/stat.h>
#include<fcntl.h>
using std::vector;
using std::cout;
using std::cin;
#include<unistd.h>
#include<string>
#include<string.h>
using std::string;

class Huffman
{
public:
    int freqset[255];
    vector<char> sortedchar;
	Huffman();
	int openfile(const char* filename);
    void wordanalyse(int fd);
};
Huffman::Huffman(){
    memset(freqset,0,sizeof(int)*255);
}
int Huffman::openfile(const char* filename){
    int fd1 = open(filename,0,O_RDONLY);
    return fd1;
}
void Huffman::wordanalyse(int fd){
    char buf[1024];
    int readnum;
    do{
        readnum = read(fd,buf,1024);
        for(int i=0;i<1024;i++){
            freqset[buf[i]]++;
        }
    }
    while(readnum==1024);
    int charsort[255]={0};
    index_sort = 0;
    for(int i=0;i<255;i++){
        if(freqset[i]==0)
            continue;

    }
    return;
}

int main()
{

}
