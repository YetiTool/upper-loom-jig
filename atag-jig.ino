step = 23;
dir = 25;

void step () {
    for (int i = 0; i < 100; i++) {
        digitalWrite(step, HIGH);
        delay(100);
        digitalWrite(step, LOW);
        delay(100);
    }
}

void setup() {
pinMode(step, OUTPUT);
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