#define step_pin 23
#define dir 25
#define travel_mm 1100
#define steps_per_mm 5
#define steps travel_mm * steps_per_mm

void step () {
    digitalWrite(step_pin, HIGH);
    delay(100);
    digitalWrite(step_pin, LOW);
    delay(100);
}

void setup() {
    pinMode(step_pin, OUTPUT);
    pinMode(dir, OUTPUT);
}

void loop () {
    digitalWrite(dir, not(digitalRead(dir)));
    delay(100);
    for (int i = 0; i < steps; i++) {
        step();
    }
}