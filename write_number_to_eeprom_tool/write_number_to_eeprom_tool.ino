#include <EEPROM.h>

#define startRunCount 20000

void writeNumberToEEPROM(long number) {
    EEPROM.put(0, number);
    }

void setup() {
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);

    // Clear all EEPROM values
    for (int i = 0 ; i < EEPROM.length() ; i++) {
    EEPROM.write(i, 0);
    }

    // Write startRunCount to EEPROM
    writeNumberToEEPROM(startRunCount);

    // Turn on builtin LED to show finished
    digitalWrite(13, HIGH);
}

void loop() {
}