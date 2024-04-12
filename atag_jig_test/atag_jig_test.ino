#include <EEPROM.h>

#define test_pin 2
#define run_pin 3
long run_count = 0;
volatile bool fail = false;
bool triggered = false;

void log_fail() {
    fail = true;
}

void writeNumberToEEPROM(long number) {
  // Split the number into bytes
  byte byte1 = (number >> 16) & 0xFF;
  byte byte2 = (number >> 8) & 0xFF;
  byte byte3 = number & 0xFF;

  // Write each byte to EEPROM
  EEPROM.write(0, byte1);
  EEPROM.write(1, byte2);
  EEPROM.write(2, byte3);
}

long readNumberFromEEPROM() {
  // Read each byte from EEPROM and combine into a long number
  byte byte1 = EEPROM.read(0);
  byte byte2 = EEPROM.read(1);
  byte byte3 = EEPROM.read(2);

  long number = (byte1 << 16) | (byte2 << 8) | byte3;
  return number;
}

void setup() {
    Serial.begin(115200);
    pinMode(test_pin, INPUT_PULLUP);
    pinMode(run_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(test_pin), log_fail, RISING);
    long storedNumber = readNumberFromEEPROM();
    run_count = storedNumber;
}

void loop() {
    if (fail == true) {
        Serial.print("Cable 2 FAIL - RUN: ");
        Serial.print(run_count);
        Serial.println(",");
        delay(300);
        fail = false;
    }
    bool pin_state = digitalRead(run_pin);
    if (pin_state == HIGH && !triggered) {
        triggered = true;
        run_count++;
    }
    if (pin_state == LOW && triggered) {
        triggered = false;
    }
    delay(50);
    if (run_count % 50 == 0) {
        writeNumberToEEPROM(run_count);
    }
}