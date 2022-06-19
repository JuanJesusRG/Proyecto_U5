#define DRV_1 6
#define DRV_2 7
#define DRV_LEDS 5

#define EXPO 600
#define PERIOD 5000
#define DEF_OFFSET 100   //Entre 100 y 250


boolean flashState, motorState;
uint8_t valColor;
uint16_t flashDelay, lightTimer;
uint32_t lightPrev, motorPrev;


void setup() {
  pinMode(DRV_1, OUTPUT);
  pinMode(DRV_2, OUTPUT);
  pinMode(DRV_LEDS, OUTPUT);
  delay(500);
  bitWrite(PORTD, DRV_LEDS, 1);
  flashDelay = PERIOD * 2 + DEF_OFFSET;
  delay( 3000 ); // power-up safety delay
}

void loop() {

  if (micros() - lightPrev >= lightTimer) {
    lightPrev = micros();
    flashState = !flashState;
    bitWrite(PORTD, DRV_LEDS, flashState);
    if (flashState) lightTimer = EXPO;
    else lightTimer = flashDelay - EXPO;
  }

  if (micros() - motorPrev >= PERIOD){
    motorPrev = micros();
    motorState = !motorState;

    bitWrite(PORTD, DRV_1, motorState);
    bitWrite(PORTD, DRV_2, !motorState);
  }
}
