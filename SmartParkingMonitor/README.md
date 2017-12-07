# Smart Parking Monitoring System
The Smart Parking Monitoring System was a project by group M03 for SYSC 3010

## Getting Started
Files used for system: 
  - Main.py <- Main script run on RPi 3
  - MonitoringNode.py <- General Utility class
  - sensors_and_lcd.ino <- Arduino sketch code, handled lcd and distance sensors
  - Server.py <- Server/Database side on RPi 2
  
Files used for testing:
  - TestDistributedSystem.py <- Used for testing Server.py
  - TestMonitoringNode.py <- Used for testing MonitoringNode.py
  
Files excluded from system:
  - udpRecevier.py <- Integrated into Server.py
  - UDPSender.py <- Integrated into Main.py
  - _pycache_ <- Cache created when running code 
  - Old folder was older code that was not initially uploaded to Github
  
  ### Prerequisites
  **Make sure all files are in the same directory.**
  Each Arduino board has a different address for I2C communication, you must run
  I2C_scanner to find the address and replace it in sensors_and_lcd.ino where the
  LCD object is initialized
  ```
  LiquidCrystal_I2C lcd(0x##, 16, 2) - replace ## with I2c address
  ```
  ```
  I2c Scanner sketch: https://playground.arduino.cc/Main/I2cScanner
  ```
  The Arduino IDE needs the following libraries installed:
  ```
  NewPing library: https://bitbucket.org/teckel12/arduino-new-ping/downloads/
  ```
  ```
  LiquidCrystal_I2C library: http://image.dfrobot.com/image/data/TOY0046/LiquidCrystal_I2Cv1-1.rar
  ```
  ```
  TimeLib: https://www.pjrc.com/teensy/td_libs_Time.html
  ```
  ```
  pymysql: $ pip install PyMySql
  ```
  
  ### Installing
  ```
  Connect Arduino and RPi 3 via USB (for serial communication)
  ```
  ```
  Load sensors_and_lcd.ino sketch onto Arduino (this sketch must be in a folder with the same name)
  ```
  ```
  Run Main.py on RPi 3 (the main system)
  ```
  ```
  Run Server.py on RPi 2 (the server) w/ MySQL database connected
  ```
  ## Running the tests
  The TestMonitoringNode independent, i.e. do not require hardware, stubbing is used for Arduino.
  ```
  $ python3 TestMonitoringNode.py
  ```
  The TestDistributedSystem requires a connection to a MySQL database
  ```
  $ python3 TestDistributedSystem.py
  ```
  ## Authors
  * **Joseph Laycano**
  * **Utkarsh Anand**
  * **Hussein Mourad**
  * **Osama Rachid** 
