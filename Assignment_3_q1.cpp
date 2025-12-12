#include <iostream>
using namespace std;
class Shape {
public:
    virtual double calculateArea() const = 0;
    virtual double calculatePerimeter() const = 0;
};

class Rectangle:public Shape {
private:
    double width;
    double height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double calculateArea() const override {
        return width * height;
    }
    double calculatePerimeter() const override {
        return 2 * (width + height);
    }
};
class Circle:public Shape{
private:
    double radius;
public:
    Circle(double r) : radius(r) {}

    double calculateArea() const override {
        return 3.14 * radius * radius;
    }

    double calculatePerimeter() const override {
        return 2 * 3.14 * radius;
    }
};

int main() {
    Rectangle rectangle(5, 6);
    cout << "Rectangle area: " << rectangle.calculateArea() << endl;
    cout << "Rectangle perimeter: " << rectangle.calculatePerimeter() << endl;

    Circle circle(5);
    cout << "Circle area: " << circle.calculateArea() << endl;
    cout << "Circle perimeter: " << rectangle.calculatePerimeter() << endl;
    return 0;}