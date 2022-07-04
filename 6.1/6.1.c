
void gaussianadd(char *str1,char *str2,char *str,int len)
{
int i=0,c;
FILE *fp1;
double x, temp=0.0;

fp1 = fopen(str1,"r");

FILE *fp2;
double y;
fp2 = fopen(str2,"r");

FILE *fp;
fp = fopen(str,"w");

//get numbers from file
while(fscanf(fp1,"%lf",&x)!=EOF && (fscanf(fp2,"%lf",&y)!=EOF))
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = x*x+y*y;
fprintf(fp,"%lf\n",temp);
}
fclose(fp1);
fclose(fp2);
fclose(fp);
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "6.h"


int main(){
gaussian("gau1.dat", 1000000);
gaussian("gau2.dat", 1000000);
gaussianadd("gau1.dat","gau2.dat","gau3.dat",1000000);

return 0;}
