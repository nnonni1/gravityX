// GravityX prototype vibration alarm, preserved from the technical report.
const uint8_t VIB_PIN = 2;
const uint8_t BUZZER = 8;
const unsigned long BEEP_MS = 120;
volatile bool vibTriggered = false;

void vibISR() { vibTriggered = true; }

void setup() {
  pinMode(VIB_PIN, INPUT_PULLUP);
  pinMode(BUZZER, OUTPUT);
  noTone(BUZZER);
  attachInterrupt(digitalPinToInterrupt(VIB_PIN), vibISR, FALLING);
  Serial.begin(9600);
  Serial.println("System ready: Vibration monitoring active...");
}

void loop() {
  if (vibTriggered) {
    vibTriggered = false;
    tone(BUZZER, 1500, BEEP_MS);
    Serial.println("Vibration detected -> Path deviation alarm!");
  }
}
