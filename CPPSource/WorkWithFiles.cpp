#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int Module = 256;

int FrontMassive_1[256] = {218, 139, 94, 95, 205, 152, 42, 204, 108, 140, 25, 223, 47, 43, 226, 83, 12, 97, 99, 251, 15, 173, 201, 107, 214, 127, 90, 67, 118, 238, 216, 198, 150, 76, 202, 56, 234, 6, 126, 22, 93, 110, 169, 112, 163, 81, 170, 21, 55, 133, 158, 74, 225, 151, 73, 58, 172, 155, 229, 34, 85, 154, 9, 235, 32, 75, 168, 145, 246, 135, 131, 116, 66, 178, 1, 46, 221, 147, 190, 84, 189, 10, 188, 232, 30, 236, 219, 255, 45, 8, 149, 231, 78, 195, 24, 182, 123, 242, 194, 132, 61, 60, 2, 111, 19, 39, 183, 115, 210, 237, 248, 193, 77, 206, 181, 215, 101, 28, 240, 136, 103, 23, 125, 153, 11, 179, 156, 157, 13, 92, 191, 177, 253, 16, 184, 89, 224, 200, 186, 69, 122, 230, 3, 166, 138, 185, 247, 91, 68, 164, 37, 31, 79, 249, 26, 146, 142, 167, 120, 144, 87, 143, 208, 117, 192, 228, 82, 14, 212, 245, 119, 57, 250, 41, 109, 227, 104, 241, 7, 141, 17, 88, 102, 100, 176, 217, 252, 114, 49, 0, 65, 105, 62, 48, 59, 71, 98, 72, 134, 165, 86, 171, 148, 203, 124, 211, 244, 44, 40, 70, 38, 35, 180, 222, 239, 175, 160, 121, 220, 33, 5, 130, 137, 207, 159, 36, 129, 4, 113, 209, 63, 54, 213, 196, 50, 20, 233, 162, 18, 96, 53, 29, 199, 174, 52, 80, 161, 27, 187, 197, 51, 128, 254, 243, 106, 64};
int BackMassive_1[256] = {189, 74, 102, 142, 227, 220, 37, 178, 89, 62, 81, 124, 16, 128, 167, 20, 133, 180, 238, 104, 235, 47, 39, 121, 94, 10, 154, 247, 117, 241, 84, 151, 64, 219, 59, 211, 225, 150, 210, 105, 208, 173, 6, 13, 207, 88, 75, 12, 193, 188, 234, 250, 244, 240, 231, 48, 35, 171, 55, 194, 101, 100, 192, 230, 255, 190, 72, 27, 148, 139, 209, 195, 197, 54, 51, 65, 33, 112, 92, 152, 245, 45, 166, 15, 79, 60, 200, 160, 181, 135, 26, 147, 129, 40, 2, 3, 239, 17, 196, 18, 183, 116, 182, 120, 176, 191, 254, 23, 8, 174, 41, 103, 43, 228, 187, 107, 71, 163, 28, 170, 158, 217, 140, 96, 204, 122, 38, 25, 251, 226, 221, 70, 99, 49, 198, 69, 119, 222, 144, 1, 9, 179, 156, 161, 159, 67, 155, 77, 202, 90, 32, 53, 5, 123, 61, 57, 126, 127, 50, 224, 216, 246, 237, 44, 149, 199, 143, 157, 66, 42, 46, 201, 56, 21, 243, 215, 184, 131, 73, 125, 212, 114, 95, 106, 134, 145, 138, 248, 82, 80, 78, 130, 164, 111, 98, 93, 233, 249, 31, 242, 137, 22, 34, 203, 7, 4, 113, 223, 162, 229, 108, 205, 168, 232, 24, 115, 30, 185, 0, 86, 218, 76, 213, 11, 136, 52, 14, 175, 165, 58, 141, 91, 83, 236, 36, 63, 85, 109, 29, 214, 118, 177, 97, 253, 206, 169, 68, 146, 110, 153, 172, 19, 186, 132, 252, 87};

int FrontMassive_2[256] = {191, 61, 56, 48, 180, 36, 123, 94, 110, 78, 22, 120, 33, 86, 102, 106, 223, 185, 15, 147, 31, 159, 46, 29, 72, 41, 176, 133, 51, 144, 136, 69, 201, 219, 14, 224, 30, 2, 225, 229, 43, 95, 241, 81, 153, 70, 169, 122, 146, 99, 58, 203, 243, 213, 190, 52, 212, 209, 108, 112, 128, 174, 7, 57, 173, 5, 184, 91, 54, 53, 42, 64, 0, 60, 195, 34, 40, 4, 66, 67, 38, 129, 141, 230, 152, 247, 160, 59, 32, 158, 196, 165, 16, 181, 200, 192, 103, 10, 63, 101, 210, 157, 208, 9, 222, 100, 161, 71, 109, 142, 221, 89, 65, 143, 25, 39, 206, 1, 242, 126, 253, 246, 87, 77, 116, 166, 151, 83, 3, 85, 140, 26, 138, 8, 104, 244, 13, 233, 234, 214, 98, 27, 47, 249, 55, 75, 251, 119, 168, 186, 204, 235, 28, 183, 217, 162, 175, 220, 154, 49, 21, 150, 155, 6, 24, 216, 88, 11, 187, 18, 115, 236, 92, 17, 194, 135, 113, 198, 117, 238, 84, 125, 76, 132, 127, 111, 167, 37, 163, 107, 197, 74, 171, 232, 124, 45, 182, 97, 118, 121, 62, 170, 90, 179, 93, 226, 227, 231, 20, 44, 68, 202, 73, 250, 96, 239, 254, 23, 12, 50, 248, 207, 114, 188, 35, 193, 82, 137, 130, 215, 134, 105, 131, 228, 252, 211, 245, 19, 237, 240, 199, 148, 189, 218, 149, 177, 156, 139, 164, 205, 80, 255, 79, 178, 172, 145 };
int BackMassive_2[256] = {72, 117, 37, 128, 77, 65, 163, 62, 133, 103, 97, 167, 218, 136, 34, 18, 92, 173, 169, 237, 208, 160, 10, 217, 164, 114, 131, 141, 152, 23, 36, 20, 88, 12, 75, 224, 5, 187, 80, 115, 76, 25, 70, 40, 209, 195, 22, 142, 3, 159, 219, 28, 55, 69, 68, 144, 2, 63, 50, 87, 73, 1, 200, 98, 71, 112, 78, 79, 210, 31, 45, 107, 24, 212, 191, 145, 182, 123, 9, 252, 250, 43, 226, 127, 180, 129, 13, 122, 166, 111, 202, 67, 172, 204, 7, 41, 214, 197, 140, 49, 105, 99, 14, 96, 134, 231, 15, 189, 58, 108, 8, 185, 59, 176, 222, 170, 124, 178, 198, 147, 11, 199, 47, 6, 194, 181, 119, 184, 60, 81, 228, 232, 183, 27, 230, 175, 30, 227, 132, 247, 130, 82, 109, 113, 29, 255, 48, 19, 241, 244, 161, 126, 84, 44, 158, 162, 246, 101, 89, 21, 86, 106, 155, 188, 248, 91, 125, 186, 148, 46, 201, 192, 254, 64, 61, 156, 26, 245, 253, 203, 4, 93, 196, 153, 66, 17, 149, 168, 223, 242, 54, 0, 95, 225, 174, 74, 90, 190, 177, 240, 94, 32, 211, 51, 150, 249, 116, 221, 102, 57, 100, 235, 56, 53, 139, 229, 165, 154, 243, 33, 157, 110, 104, 16, 35, 38, 205, 206, 233, 39, 83, 207, 193, 137, 138, 151, 171, 238, 179, 215, 239, 42, 118, 52, 135, 236, 121, 85, 220, 143, 213, 146, 234, 120, 216, 251 };

int FrontMassive_3[256] = {137, 104, 159, 58, 164, 167, 111, 122, 25, 219, 76, 240, 186, 79, 54, 2, 183, 40, 143, 199, 160, 56, 162, 185, 89, 152, 32, 93, 224, 43, 201, 7, 139, 73, 215, 148, 18, 116, 165, 0, 225, 234, 113, 200, 85, 59, 140, 15, 175, 195, 242, 53, 205, 68, 136, 153, 188, 251, 196, 101, 138, 29, 110, 203, 127, 214, 172, 91, 211, 10, 254, 194, 90, 74, 125, 23, 197, 45, 20, 221, 230, 82, 252, 253, 135, 107, 117, 176, 112, 105, 247, 19, 114, 236, 51, 78, 67, 36, 243, 81, 154, 69, 92, 50, 64, 179, 235, 1, 141, 39, 144, 63, 99, 102, 22, 86, 166, 100, 213, 3, 192, 33, 149, 8, 216, 223, 62, 168, 232, 174, 5, 206, 57, 31, 37, 126, 237, 80, 75, 170, 16, 145, 151, 222, 21, 34, 13, 17, 121, 106, 173, 146, 191, 109, 83, 150, 208, 246, 255, 156, 244, 118, 218, 46, 158, 11, 157, 115, 248, 231, 155, 238, 190, 189, 163, 77, 202, 207, 70, 108, 60, 14, 120, 9, 180, 119, 72, 124, 65, 44, 71, 103, 184, 204, 84, 38, 181, 250, 161, 52, 35, 209, 131, 30, 171, 249, 177, 24, 233, 226, 55, 182, 229, 88, 169, 97, 27, 96, 130, 42, 6, 212, 61, 87, 147, 28, 95, 210, 129, 94, 133, 220, 193, 41, 187, 241, 227, 132, 49, 4, 178, 128, 66, 123, 48, 47, 217, 98, 12, 142, 26, 134, 239, 198, 228, 245};
int BackMassive_3[256] = {39, 107, 15, 119, 239, 130, 220, 31, 123, 183, 69, 165, 248, 146, 181, 47, 140, 147, 36, 91, 78, 144, 114, 75, 207, 8, 250, 216, 225, 61, 203, 133, 26, 121, 145, 200, 97, 134, 195, 109, 17, 233, 219, 29, 189, 77, 163, 245, 244, 238, 103, 94, 199, 51, 14, 210, 21, 132, 3, 45, 180, 222, 126, 111, 104, 188, 242, 96, 53, 101, 178, 190, 186, 33, 73, 138, 10, 175, 95, 13, 137, 99, 81, 154, 194, 44, 115, 223, 213, 24, 72, 67, 102, 27, 229, 226, 217, 215, 247, 112, 117, 59, 113, 191, 1, 89, 149, 85, 179, 153, 62, 6, 88, 42, 92, 167, 37, 86, 161, 185, 182, 148, 7, 243, 187, 74, 135, 64, 241, 228, 218, 202, 237, 230, 251, 84, 54, 0, 60, 32, 46, 108, 249, 18, 110, 141, 151, 224, 35, 122, 155, 142, 25, 55, 100, 170, 159, 166, 164, 2, 20, 198, 22, 174, 4, 38, 116, 5, 127, 214, 139, 204, 66, 150, 129, 48, 87, 206, 240, 105, 184, 196, 211, 16, 192, 23, 12, 234, 56, 173, 172, 152, 120, 232, 71, 49, 58, 76, 253, 19, 43, 30, 176, 63, 193, 52, 131, 177, 156, 201, 227, 68, 221, 118, 65, 34, 124, 246, 162, 9, 231, 79, 143, 125, 28, 40, 209, 236, 254, 212, 80, 169, 128, 208, 41, 106, 93, 136, 171, 252, 11, 235, 50, 98, 160, 255, 157, 90, 168, 205, 197, 57, 82, 83, 70, 158};

int* AnotherEncryptValues(int* Arraybytes, int length, int* rotors, int every) {
	int rotor_1 = rotors[0];
	int rotor_2 = rotors[1];
	int rotor_3 = rotors[2];
	for (int NowByte = 0; NowByte < length; NowByte += every) {
		int ItByte = Arraybytes[NowByte];
		ItByte = (ItByte + rotor_1) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_1[ItByte];
		ItByte = (ItByte + (rotor_2 - rotor_1)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_2[ItByte];
		ItByte = (ItByte + (rotor_3 - rotor_2)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_3[ItByte];
		ItByte = (ItByte - rotor_3) % Module;
		if (ItByte < 0) ItByte += Module;

		ItByte = Module - ItByte - 1;

		ItByte = (ItByte + rotor_3) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_3[ItByte];
		ItByte = (ItByte - (rotor_3 - rotor_2)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_2[ItByte];
		ItByte = (ItByte - (rotor_2 - rotor_1)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_1[ItByte];
		ItByte = (ItByte - rotor_1) % Module;
		if (ItByte < 0) ItByte += Module;

		if (rotor_1 + 1 >= Module) {
			rotor_1 = 0;
			if (rotor_2 + 1 >= Module) {
				rotor_2 = 0;
				if (rotor_3 + 1 >= Module) {
					rotor_3 = 0;
					rotor_2 = 0;
					rotor_1 = 0;
				}
				else { rotor_3++; }
			}
			else { rotor_2++; }
		}
		else { rotor_1++; }

		Arraybytes[NowByte] = ItByte;
	}
	rotors[0] = rotor_1;
	rotors[1] = rotor_2;
	rotors[2] = rotor_3;
	return rotors;
}

extern "C" __declspec(dllexport) int EncryptFile(char* path_to_file, int* rotors, int every) {
	cout << path_to_file << endl;
	ifstream FILE(path_to_file, ios::binary);
	if (!FILE)
	{
		cout << "Error!" << endl;
		system("pause");
		return 0;
	}

	FILE.seekg(0, ios::end);
	size_t SizeFile = FILE.tellg();
	FILE.seekg(0, ios::beg);
	char* CharText = new char[SizeFile];
	int* intText = new int[SizeFile];
	int length = 0;
	FILE.read(CharText, SizeFile);
	for (int i = 0; i < SizeFile; ++i) {
		intText[i] = CharText[i];
		length++;
	}

	FILE.close();
	int* NewRotors = AnotherEncryptValues(intText, length, rotors, every);
	rotors = NewRotors;

	for (int i = 0; i < SizeFile; i++) {
		CharText[i] = (char)intText[i];
	}

	delete[] intText;

	ofstream FILE2(path_to_file, ios::binary);
	FILE2.write(CharText, length);
	FILE2.close();
	delete[] CharText;

	return 0;
}

extern "C" __declspec(dllexport) int EncryptValues(int* Arraybytes, int length, int* rotors, int every) {
	int rotor_1 = rotors[0];
	int rotor_2 = rotors[1];
	int rotor_3 = rotors[2];
	for (int NowByte = 0; NowByte < length; NowByte += every) {
		int ItByte = Arraybytes[NowByte];
		ItByte = (ItByte + rotor_1) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_1[ItByte];
		ItByte = (ItByte + (rotor_2 - rotor_1)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_2[ItByte];
		ItByte = (ItByte + (rotor_3 - rotor_2)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = FrontMassive_3[ItByte];
		ItByte = (ItByte - rotor_3) % Module;
		if (ItByte < 0) ItByte += Module;

		ItByte = Module - ItByte - 1;

		ItByte = (ItByte + rotor_3) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_3[ItByte];
		ItByte = (ItByte - (rotor_3 - rotor_2)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_2[ItByte];
		ItByte = (ItByte - (rotor_2 - rotor_1)) % Module;
		if (ItByte < 0) ItByte += Module;
		ItByte = BackMassive_1[ItByte];
		ItByte = (ItByte - rotor_1) % Module;
		if (ItByte < 0) ItByte += Module;

		if (rotor_1 + 1 >= Module) {
			rotor_1 = 0;
			if (rotor_2 + 1 >= Module) {
				rotor_2 = 0;
				if (rotor_3 + 1 >= Module) {
					rotor_3 = 0;
					rotor_2 = 0;
					rotor_1 = 0;
				}
				else { rotor_3++; }
			}
			else { rotor_2++; }
		}
		else { rotor_1++; }

		Arraybytes[NowByte] = ItByte;
	}
	rotors[0] = rotor_1;
	rotors[1] = rotor_2;
	rotors[2] = rotor_3;
	return 0;
}