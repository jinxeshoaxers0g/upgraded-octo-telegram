#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

int main() {
    int minutes;
    cout << "⏰ Enter alarm time in minutes: ";
    cin >> minutes;

    cout << "⏳ Alarm set for " << minutes << " minutes...\n";
    this_thread::sleep_for(chrono::minutes(minutes));

    cout << "\a🚨 ALARM! Time's up! 🚨\n";
    return 0;
}
