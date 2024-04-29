//  PIN DEFINITION
#define step_pin 12
#define dir 13
#define run_pin 11

//  TRAVEL PARAMS
#define stepsPerMM 7.075
#define travelMM 300
#define steps (stepsPerMM * travelMM) //  7500 steps = 1060mm

void step() {
    digitalWrite(step_pin, HIGH);
    delayMicroseconds(500);
    digitalWrite(step_pin, LOW);
    delayMicroseconds(500);
}

void setup() {
    pinMode(step_pin, OUTPUT);
    pinMode(dir, OUTPUT);
    pinMode(run_pin, OUTPUT);
}
void loop() {
    //  MOVEMENT
    digitalWrite(dir, LOW);
    delay(500);
    for (int i = 0; i < steps; i++) {
        step();
    }
    delay(500);
    digitalWrite(dir, HIGH);
    delay(500);
    for (int i = 0; i < steps; i++) {
        step();
    }
    delay(500);

    //  RUN COUNT INCREMENT
    digitalWrite(run_pin, HIGH);
    delay(500);
    digitalWrite(run_pin, LOW);
    delay(500);
} 