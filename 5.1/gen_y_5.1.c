#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "5.h"

int main(){
uniform_Bernolli("ber5.dat", 1000000);
gaussian("gau5.dat",1000000);
int A=5;//A=5dB
var_Y("ber5.dat","gau5.dat","Var_Y.dat",1000000,A);


    return 0;
}
