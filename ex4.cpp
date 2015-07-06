#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char * args[]) {

	srand(time(0));
	for (int k = 0; k < 100; ++k) {
		for (int i = 0; i < 6; ++i) {
			int n = rand()%16;
			if (n <= 9) {
				cout << n;
			}
			if (n == 10) {
				cout << "A";
			}
			if (n == 11) {
				cout << "B";
			}
			if (n == 12) {
				cout << "C";
			}
			if (n == 13) {
				cout << "D";
			}
			if (n == 14) {
				cout << "E";
			}
			if (n == 15) {
				cout << "F";
			}
		}
		cout << endl;
	}
}
