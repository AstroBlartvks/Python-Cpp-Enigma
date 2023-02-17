#pragma once
extern "C" __declspec(dllexport) void set_rus_reflector(int*);
extern "C" __declspec(dllexport) void set_rus_rotor(int*, int, int);
extern "C" __declspec(dllexport) int encryptRus(int, int, int, int);
extern "C" __declspec(dllexport) void set_eng_reflector(int*);
extern "C" __declspec(dllexport) void set_eng_rotor(int*, int, int);
extern "C" __declspec(dllexport) int encryptEng(int, int, int, int);