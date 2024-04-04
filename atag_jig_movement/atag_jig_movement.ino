#define step_pin 12
#define dir 13
#define run_pin 11
#define steps 7500

void step() {
    digitalWrite(step_pin, HIGH);
    delayMicroseconds(700);
    digitalWrite(step_pin, LOW);
    delayMicroseconds(700);
}

void setup() {
    pinMode(step_pin, OUTPUT);
    pinMode(dir, OUTPUT);
    pinMode(run_pin, OUTPUT);
}
void loop() {
    digitalWrite(dir, LOW);
    delay(1000);
    for (int i = 0; i < steps; i++) {
        step();
    }
    delay(1000);
    digitalWrite(dir, HIGH);
    delay(1000);
    for (int i = 0; i < steps; i++) {
        step();
    }
    delay(1000);
    digitalWrite(run_pin, HIGH);
    delay(500);
    digitalWrite(run_pin, LOW);
    delay(500);
}