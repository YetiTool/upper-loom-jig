#define step_pin = 23;
#define dir = 25;

void step () {
    for (int i = 0; i < 100; i++) {
        digitalWrite(step_pin, HIGH);
        delay(100);
        digitalWrite(step_pin, LOW);
        delay(100);
    }
}

void setup() {
    pinMode(step_pin, OUTPUT);
    pinMode(dir, OUTPUT);
}

void loop () {
    digitalWrite(dir, LOW);
    delay(100);
    step();
    digitalWrite(dir, HIGH);
    delay(100);
    step();
}