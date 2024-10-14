#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double Wt(){
    int num = 10;
    double w = (rand() % (2*num + 1));
    return fmin(w/100.0, 0.99);
}

int main()
{
    srand(time(NULL));

    double S0 = 160.00;
    double mu = 0.07;
    double vol = 0.4;
    double t = 1.0/12.0;
    double St;
    for(int t = 0; t < 10; ++t){
        St = S0*exp((mu - 0.5*pow(vol, 2))*t + vol*Wt());
        printf("Initial Stock Price: %f | New Stock Price: %f\n", S0, St);
        S0 = St;
    }


    return 0;
}