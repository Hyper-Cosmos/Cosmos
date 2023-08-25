#include <iostream>
#include <string>

int main() {
    std::string string_input = "algoritma dan pemrograman";
    int first_a_index = -1;
    int second_a_index = -1;
    int a_count = 0;

    for (int index = 0; index < string_input.length(); ++index) {
        if (string_input[index] == 'a') {
            a_count++;
            if (a_count == 1) {
                first_a_index = index;
            } else if (a_count == 2) {
                second_a_index = index;
                break;
            }
        }
    }

    std::cout << "Indeks huruf 'a' pertama: " << first_a_index << std::endl;
    std::cout << "Indeks huruf 'a' kedua: " << second_a_index << std::endl;

    return 0;
}
