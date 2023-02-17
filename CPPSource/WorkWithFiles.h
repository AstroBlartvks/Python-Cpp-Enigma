#pragma once
#include <string>
using namespace std;
extern "C" __declspec(dllexport) int EncryptValues(int*, int, int*, int);
extern "C" __declspec(dllexport) int EncryptFile(char*, int*, int);