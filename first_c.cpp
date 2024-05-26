#include <iostream>
#include <math.h>
#include <vector>

int main()
{

    std::cout << "This is a test" << std::endl;

    return 0;
}

class Vector2D
{
public:
    float x;
    float y;

    Vector2D(float a, float b)
    {
        x = a;
        y = b;
    }
};

void createFirstVector(float x, float y)
{
    const int X = static_cast<int>(std::floor(x)) & 255;
    const int Y = static_cast<int>(std::floor(y)) & 255;
    int xf = x - std::floor(x);
    int yf = y - std::floor(y);

    Vector2D topRight(xf - 1.0, yf - 1.0);
}