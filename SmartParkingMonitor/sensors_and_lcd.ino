/* https://github.com/jolayc/sysc3010-smartparkingmonitor/blob/master/SmartParkingMonitor/sensors_and_lcd.ino
   @author Joseph Laycano
   SYSC3010 M03
   This sketch performs the following:
   i. Each node check if something is within its range
   ii. Node identification and distance detected
   is sent through serial port to RPi
   iii. Timer values are displayed on LCD connected to Arduino (buggy)
*/

#include <Wire.h> //I2C connection Library
#include <LiquidCrystal_I2C.h> // LCD I2C library
#include <TimeLib.h> // Time keeping library
#include <NewPing.h> // Distance sensor library

#define SONAR_NUM 3 // Number of sensors
#define MAX_DISTANCE 8 // Max detection distance is 8 cm
#define PING_INTERVAL 33 // Used for pinging distance sensors

boolean newData = false; // New data available flag
unsigned long pingTimer[SONAR_NUM];
unsigned int cm[SONAR_NUM]; // Distance detected for each node
uint8_t currentSensor = 0; // Node identification for loops
time_t start[3]; // Start time for each node
time_t timers[3]; // Timer values for each node
long baud = 9600; // Baud rate

LiquidCrystal_I2C lcd(0x20, 16, 2); // LCD object

NewPing sonar[SONAR_NUM] = { // Array of distance sensors
  NewPing(2, 3, MAX_DISTANCE), // Node A
  NewPing(4, 5, MAX_DISTANCE), // Node B
  NewPing(6, 7, MAX_DISTANCE) // Node C
};

void setup() {
  // Initialize LCD
  lcd.begin();
  lcd.backlight();
  // Initialize serial communication
  Serial.begin(baud);
  pingTimer[0] = millis() + 75;
  for (uint8_t i = 1; i < SONAR_NUM; i++) {
    pingTimer[i] = pingTimer[i - 1] + PING_INTERVAL;
  }
}

/* This loop function was taken from NewPing library examples */
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
  // Bring LCD cursor to home position (0,0) and print node ID and call printLCD to print timer value
  lcd.home();
  lcd.print("A");
  printLCD(0);
  lcd.print(" B");
  printLCD(1);
  lcd.setCursor(0, 1);
  lcd.print("C");
  printLCD(2);
}

/* If ping is received, set the sensor distance to array */
void echoCheck() {
  if (sonar[currentSensor].check_timer())
    cm[currentSensor] = sonar[currentSensor].ping_result / US_ROUNDTRIP_CM; // Convert distance to cm
  newData = true; // Set flag
}

/* Sensor ping cycle in complete, print distance values to serial and call checkNode() */
void oneSensorCycle() {
  if (newData) { // New data/reading was received
    for (uint8_t i = 0; i < SONAR_NUM; i++) { // Print all distances values to serial
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

/* Print timer value to LCD based on ID0. */
void printLCD(int ID) {
  if (cm[ID] == 0 || cm[ID] > MAX_DISTANCE) {
    lcd.print("  :  ");
  } else {
    lcd.print(minute(timers[ID]));
    lcd.print(":");
    lcd.print(second(timers[ID]));
  }
}

/* Set timer value */
time_t setTimer(time_t start) {
  return now() - start;
}

/* Set start timer value */
time_t startTimer() {
  return now();
}

/* 
 * Check distance of node and
 * modify timer value based on readings
 */
void checkNode(uint8_t ID, unsigned int distance) {
  if (distance > 0 && distance <= MAX_DISTANCE) { // Check if distance is within range
    if (start[ID] == 0) {
      start[ID] = startTimer();
    }
    timers[ID] = setTimer(start[ID]);
  }
  else { // Reset values otherwise
    start[ID] = 0;
    timers[ID] = 0;
  }
}
