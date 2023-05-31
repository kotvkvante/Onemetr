#include <iostream>

int main(int argc, char *argv[])
{
  int a;
  cout << argc << std::endl;
  if (argc < 2)
  {
    std::cout << "Need 7 arguments!" << std::endl;
  }

  std::cout << "Hello World!" << std::endl;

  std::cin >> a;

  std::cout << "Int a = " << a << std::endl;

  return 0;
}
