#define test_pin 43
#define run_pin 3
int run_count = 0;
#define fail_pin 12


void log_fail() {
    digitalWrite(fail_pin, HIGH);
}

void add_to_run_count() {
    run_count += 1;
}

void setup() {
    Serial.begin(115200);
    pinMode(test_pin, INPUT);
    pinMode(run_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(test_pin), log_fail, FALLING);
    attachInterrupt(digitalPinToInterrupt(run_pin), add_to_run_count, RISING);
    digitalWrite(fail_pin, LOW);
}

void loop() {
    Serial.println("running...");
    delay(1000);
    if (digitalRead(fail_pin) == HIGH) {
        Serial.println("Cable 1 FAIL - RUN:" + String(run_count) + ",\n");
    }
}