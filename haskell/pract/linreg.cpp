#include <iostream>
#include <vector>
#include <chrono>
#include <sys/time.h>
#include <ctime>
float linreg(std::vector<float> x, std::vector<float> y, float bias){
    std::vector<float> z;
    for (int i = 0; i < x.size(); i++){
        z.push_back(x[i] * y[i]);
        
    }
    float sum = 0;
    for (float i: z)
        sum += i;
    return sum + bias;

}
int main(){
    struct timeval time_now{};
    gettimeofday(&time_now, nullptr);
    time_t start = (time_now.tv_sec * 1000) + (time_now.tv_usec / 1000);

    for (int i = 0; i < 1000000; i++){
        linreg({2.4,6.9},{2.9,4.4}, 2); 
    }
    struct timeval time_end{};
    gettimeofday(&time_end, nullptr);
    time_t end = (time_end.tv_sec * 1000) + (time_end.tv_usec / 1000);

    std::cout <<"Miliseconds: " << end - start << std::endl;
    return 0;
}
