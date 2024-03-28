#define test_pin 2
#define run_pin 3

int run_count = 0;


void log_fail() {
    Serial.println("Cable 1 FAIL - RUN:" + String(run_count) + ",\n");
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
}

void loop() {
}