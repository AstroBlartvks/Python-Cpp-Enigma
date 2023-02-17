#include <iostream>

using namespace std;

int GlobalRusModule = 33;
int GlobalReflectorRus[33];

int GlobalRotor1RusForward[33];
int GlobalRotor1RusBack[33];

int GlobalRotor2RusForward[33];
int GlobalRotor2RusBack[33];

int GlobalRotor3RusForward[33];
int GlobalRotor3RusBack[33];

int GlobalEngModule = 26;
int GlobalReflectorEng[26];

int GlobalRotor1EngForward[26];
int GlobalRotor1EngBack[26];

int GlobalRotor2EngForward[26];
int GlobalRotor2EngBack[26];

int GlobalRotor3EngForward[26];
int GlobalRotor3EngBack[26];


extern "C" __declspec(dllexport) void set_rus_reflector(int* array) {
	for (int i = 0; i < GlobalRusModule; i++) {
		GlobalReflectorRus[i] = array[i];
	}
}

extern "C" __declspec(dllexport) void set_rus_rotor(int* array, int rotorNumber, int mode) {
	for (int i = 0; i < GlobalRusModule; i++) {
		if (rotorNumber == 1){
			if (mode == 0) {
				GlobalRotor1RusForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor1RusBack[i] = array[i];
			}
		}else if (rotorNumber == 2) {
			if (mode == 0) {
				GlobalRotor2RusForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor2RusBack[i] = array[i];
			}
		}else if (rotorNumber == 3) {
			if (mode == 0) {
				GlobalRotor3RusForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor3RusBack[i] = array[i];
			}
		}

	}
}

extern "C" __declspec(dllexport) int encryptRus(int symbol, int rotor1, int rotor2, int rotor3) {
	symbol = (symbol + rotor1) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor1RusForward[symbol];
	symbol = (symbol + (rotor2 - rotor1)) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor2RusForward[symbol];
	symbol = (symbol + (rotor3 - rotor2)) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor3RusForward[symbol];
	symbol = (symbol - rotor3) % GlobalRusModule;
	if(symbol < 0) symbol += GlobalRusModule;

	symbol = GlobalReflectorRus[symbol];

	symbol = (symbol + rotor3) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor3RusBack[symbol];
	symbol = (symbol - (rotor3 - rotor2)) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor2RusBack[symbol];
	symbol = (symbol - (rotor2 - rotor1)) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;
	symbol = GlobalRotor1RusBack[symbol];
	symbol = (symbol - rotor1) % GlobalRusModule;
	if (symbol < 0) symbol += GlobalRusModule;

	return symbol;
}


extern "C" __declspec(dllexport) void set_eng_reflector(int* array) {
	for (int i = 0; i < GlobalEngModule; i++) {
		GlobalReflectorEng[i] = array[i];
	}
}

extern "C" __declspec(dllexport) void set_eng_rotor(int* array, int rotorNumber, int mode) {
	for (int i = 0; i < GlobalEngModule; i++) {
		if (rotorNumber == 1) {
			if (mode == 0) {
				GlobalRotor1EngForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor1EngBack[i] = array[i];
			}
		}
		else if (rotorNumber == 2) {
			if (mode == 0) {
				GlobalRotor2EngForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor2EngBack[i] = array[i];
			}
		}
		else if (rotorNumber == 3) {
			if (mode == 0) {
				GlobalRotor3EngForward[i] = array[i];
			}
			else if (mode == 1) {
				GlobalRotor3EngBack[i] = array[i];
			}
		}

	}
}

extern "C" __declspec(dllexport) int encryptEng(int symbol, int rotor1, int rotor2, int rotor3) {
	symbol = (symbol + rotor1) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor1EngForward[symbol];
	symbol = (symbol + (rotor2 - rotor1)) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor2EngForward[symbol];
	symbol = (symbol + (rotor3 - rotor2)) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor3EngForward[symbol];
	symbol = (symbol - rotor3) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;

	symbol = GlobalReflectorEng[symbol];

	symbol = (symbol + rotor3) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor3EngBack[symbol];
	symbol = (symbol - (rotor3 - rotor2)) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor2EngBack[symbol];
	symbol = (symbol - (rotor2 - rotor1)) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;
	symbol = GlobalRotor1EngBack[symbol];
	symbol = (symbol - rotor1) % GlobalEngModule;
	if (symbol < 0) symbol += GlobalEngModule;

	return symbol;
}