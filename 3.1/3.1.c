#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void gaussianV(char *str1,char *str,int len)
{
int i=0,c;
FILE *fp1;
double x, temp=0.0;

fp1 = fopen(str1,"r");


FILE *fp;
fp = fopen(str,"w");

//get numbers from file
while(fscanf(fp1,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//apply -2 ln ( 1 - U ) to all numbers in file
//-2 ln ( 1 - U )
temp = -2*log(1-x);
fprintf(fp,"%lf\n",temp);
}
fclose(fp1);
fclose(fp);
}
int main(){
gaussianV("uni.dat","V.dat",1000000);

return 0;}