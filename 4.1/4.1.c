#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void Uniformadd(char *str1,char *str2,char *str,int len)
{
uniform(str1, 1000000);
uniform(str2, 1000000);
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
temp = x+y;
fprintf(fp,"%lf\n",temp);
}
fclose(fp1);
fclose(fp2);
fclose(fp);
}


int main(){

Uniformadd("uni1.dat","uni2.dat", "fourth.dat",1000000);
return 0;}
