#include <EEPROM.h>

#define test_pin 2
#define run_pin 7
long run_count = 0;
volatile bool fail = false;
bool triggered = false;
bool loggedCount = false;

void log_fail() {
    fail = true;
}

void writeNumberToEEPROM(long number) {
    EEPROM.put(0, number);
}

long readNumberFromEEPROM() {
  long number;
  EEPROM.get(0, number);
  return number;
}

void setup() {
    Serial.begin(115200);
    pinMode(test_pin, INPUT_PULLUP);
    pinMode(run_pin, INPUT);
    attachInterrupt(digitalPinToInterrupt(test_pin), log_fail, RISING);
    long storedNumber = readNumberFromEEPROM();
    run_count = storedNumber;
}

void loop() {
    // FAILURE REPORTING
    if (fail == true) {
        Serial.print("Cable 3 FAIL - RUN: ");
        Serial.print(run_count);
        Serial.println(",");
        delay(300);
        fail = false;
    }

    //  RUN COUNT HANDLING
    bool pin_state = digitalRead(run_pin);
    if (pin_state == HIGH && !triggered) {
        triggered = true;
        run_count++;
    }
    if (pin_state == LOW && triggered) {
        triggered = false;
    }
    delay(50);
    if (run_count % 500 == 0) {
        if (!loggedCount) {
            writeNumberToEEPROM(run_count);
            Serial.print("Run Count: ");
            Serial.print(run_count);
            Serial.println(",");
            loggedCount = true;
        }
    }else {
        loggedCount = false;
    }
}