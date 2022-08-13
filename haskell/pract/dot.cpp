#include <iostream>
#include <vector>

float dot(std::vector<float> x, std::vector<float> y){
    std::vector<float> z;
    for (int i = 0; i < x.size(); i++){
        z.push_back(x[i] + y[i]);
        
    }
    float sum = 0;
    for (float i: z)
        sum += i;
    return sum;

}
int main(){
    std::vector<float> x{2.4,6.9};
    std::vector<float> y{2.9, 4.4};
    std::cout << dot(x,y) << std::endl;
    return 0;
}
