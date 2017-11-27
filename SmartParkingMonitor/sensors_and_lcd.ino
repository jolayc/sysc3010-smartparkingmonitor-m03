/* SYSC3010 M03
 * This sketch performs the following:
 * i. Each node check if something is within its range
 * ii. Node identification and distance detected
 * is sent through serial port to RPi
 */
#include <Wire.h>
#include <LiquidCrystal_I2C.h> // LCD I2C library
#include <TimeLib.h> // Time keeping library
#include <NewPing.h> // Distance sensor library

#define SONAR_NUM 3 // number of sensors
#define MAX_DISTANCE 8 // max detection distance is 10 cm
#define PING_INTERVAL 33 // used for pinging distance sensors

boolean newData = false; // new data available flag
unsigned long pingTimer[SONAR_NUM];
unsigned int cm[SONAR_NUM]; // distance detected
uint8_t currentSensor = 0;

time_t start[3]; // start time for each node
time_t timers[3]; // timer values for each node

LiquidCrystal_I2C lcd(0x20,16,2); // set up LCD

NewPing sonar[SONAR_NUM] = { // array of distance sensors
  NewPing(2,3,MAX_DISTANCE), // node A
  NewPing(4,5,MAX_DISTANCE), // node B
  NewPing(6,7,MAX_DISTANCE) // node C
};

void setup() {
    lcd.init();
    lcd.backlight();
    Serial.begin(9600);
    pingTimer[0] = millis() + 75;
    for(uint8_t i = 1; i < SONAR_NUM; i++) {
      pingTimer[i] = pingTimer[i - 1] + PING_INTERVAL;
    }
  }

void loop() {
  for (uint8_t i = 0; i < SONAR_NUM; i++) { // Loop through all the sensors.
    if (millis() >= pingTimer[i]) {         // Is it this sensor's time to ping?
      pingTimer[i] += PING_INTERVAL * SONAR_NUM;  // Set next time this sensor will be pinged.
      if (i == 0 && currentSensor == SONAR_NUM - 1) oneSensorCycle(); // Sensor ping cycle complete, do something with the results.
      sonar[currentSensor].timer_stop();          // Make sure previous timer is canceled before starting a new ping (insurance).
      currentSensor = i;                          // Sensor being accessed.
      cm[currentSensor] = 0;                      // Make distance zero in case there's no ping echo for this sensor.
      sonar[currentSensor].ping_timer(echoCheck); // Do the ping (processing continues, interrupt will call echoCheck to look for echo).
    }
  }
  lcd.setCursor(0,0);
  lcd.print("A ");
  lcd.print(minute(timers[0]));
  lcd.print(":");
  lcd.print(second(timers[0]));
  
  lcd.print(" ");
  
  lcd.print("B ");
  lcd.print(minute(timers[1]));
  lcd.print(":");
  lcd.print(second(timers[1]));
  
  lcd.setCursor(0,1);
  
  lcd.print("C ");
  lcd.print(minute(timers[2]));
  lcd.print(":");
  lcd.print(second(timers[2]));
}

void echoCheck() { // If ping received, set the sensor distance to array.
  if (sonar[currentSensor].check_timer())
    cm[currentSensor] = sonar[currentSensor].ping_result / US_ROUNDTRIP_CM;
  newData = true;
}

void oneSensorCycle() { // Sensor ping cycle complete, do something with the results.
  if(newData) {
    for(uint8_t i = 0; i < SONAR_NUM; i++) {
      Serial.print(i);
      Serial.print(" ");
      Serial.print(cm[i]);
      Serial.print(" ");
      checkNode(i, cm[i]);
    }
    newData = false;
    Serial.println();
  }
}

time_t setTimer(time_t start) {
 return now() - start; 
}

time_t startTimer() {
 return now(); 
}

void checkNode(uint8_t ID, unsigned int distance) {
 if(distance > 0 && distance <= MAX_DISTANCE) {
   if(start[ID] == 0) {
     start[ID] = startTimer();
   }
   timers[ID] = setTimer(start[ID]);
 } else {
  start[ID] = 0;
  timers[ID] = 0; 
 }
}
