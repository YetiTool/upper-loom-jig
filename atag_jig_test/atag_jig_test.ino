#define test_pin 2
#define run_pin 3
int run_count = 0;
volatile bool fail = false;
bool triggered = false;


void log_fail() {
    fail = true;
}

void setup() {
    Serial.begin(115200);
    pinMode(test_pin, INPUT_PULLUP);
    pinMode(run_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(test_pin), log_fail, RISING);
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
}