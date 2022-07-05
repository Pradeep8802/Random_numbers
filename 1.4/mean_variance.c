
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
double var(char* str,int Mean)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x*x;
}
fclose(fp);
temp = temp/(i);
return temp;
}
int main(){

    double Mean = mean("uni.dat");
    

//Var(X)= E[X^2] - (E[X])^2 
    double Variance=var("uni.dat",Mean)-Mean*Mean;
printf("%f %f",Mean,Variance);
}
