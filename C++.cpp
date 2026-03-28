#include <iostream>
#include <string>
#include <random>
#include <ctime>
#include <sstream>
#include <vector>
#include <bitset>
#include <cstdlib>

using namespace std;

// -----------------------------
// Password Generator
// -----------------------------
string generatePassword(int length) {
    string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    string password = "";
    srand(time(0));
    for(int i=0;i<length;i++){
        password += chars[rand() % chars.size()];
    }
    return password;
}

// -----------------------------
// Simple Hash Generator (ASCII sum as simple hash)
// -----------------------------
string simpleHash(string text){
    int sum = 0;
    for(char c : text){
        sum += int(c);
    }
    stringstream ss;
    ss << hex << sum;
    return ss.str();
}

// -----------------------------
// Base64 Encode (simplified)
// -----------------------------
string base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

string base64Encode(string input) {
    string result;
    int val=0, valb=-6;
    for (unsigned char c : input) {
        val = (val<<8) + c;
        valb += 8;
        while (valb>=0) {
            result.push_back(base64_chars[(val>>valb)&0x3F]);
            valb-=6;
        }
    }
    if (valb>-6) result.push_back(base64_chars[((val<<8)>>(valb+8))&0x3F]);
    while (result.size()%4) result.push_back('=');
    return result;
}

// -----------------------------
// Main Menu
// -----------------------------
int main() {
    int choice;
    do {
        cout << "\n=== Zohaib Cyber Security Toolkit (C++) ===" << endl;
        cout << "1. Generate Random Password" << endl;
        cout << "2. Simple Hash Generator" << endl;
        cout << "3. Base64 Encode" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;
        cin.ignore(); // clear buffer

        if(choice==1){
            int len;
            cout << "Enter password length: ";
            cin >> len;
            cin.ignore();
            cout << "Generated Password: " << generatePassword(len) << endl;
        }
        else if(choice==2){
            string text;
            cout << "Enter text to hash: ";
            getline(cin, text);
            cout << "Simple Hash: " << simpleHash(text) << endl;
        }
        else if(choice==3){
            string text;
            cout << "Enter text to encode: ";
            getline(cin, text);
            cout << "Base64 Encoded: " << base64Encode(text) << endl;
        }
        else if(choice==4){
            cout << "Exiting... Stay Secure!" << endl;
        }
        else{
            cout << "Invalid choice! Try again." << endl;
        }

    } while(choice != 4);

    return 0;
}