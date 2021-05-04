#include <AccelStepper.h>

#define motorPin1  8     // IN1 on the ULN2003 driver 1
#define motorPin2  9     // IN2 on the ULN2003 driver 1
#define motorPin3  10     // IN3 on the ULN2003 driver 1
#define motorPin4  11     // IN4 on the ULN2003 driver 1


#define s21 2
#define s22 3
#define s23 5
#define s24 4
int notePins[] = {22, 24, 26, 28, 30, 32, 34, 36};
int note0Reading = LOW;
int note1Reading = LOW;
int note2Reading = LOW;
int note3Reading = LOW;
int note4Reading = LOW;
int note5Reading = LOW;
int note6Reading = LOW;
int note7Reading = LOW;


//Create stepper object
AccelStepper stepper(4, motorPin1, motorPin2, motorPin3, motorPin4);
AccelStepper stepper2(4, s21, s22, s23, s24);

void setup()
{

  stepper.setMaxSpeed(1000);
  stepper.setCurrentPosition(0);
  stepper2.setMaxSpeed(1000);
  stepper2.setCurrentPosition(0);

}
void loop()
{
  // check if there is a "rising edge" with the button
  note0Reading = digitalRead(notePins[0]);
  note1Reading = digitalRead(notePins[1]);
  note2Reading = digitalRead(notePins[2]);
  note3Reading = digitalRead(notePins[3]);
  note4Reading = digitalRead(notePins[4]);
  note5Reading = digitalRead(notePins[5]);
  note6Reading = digitalRead(notePins[6]);
  note7Reading = digitalRead(notePins[7]);


  if (note0Reading == HIGH) {
    while (note0Reading == HIGH) {
      stepper.setSpeed(395);
      stepper.runSpeed();
      

      note0Reading = digitalRead(notePins[0]);
    }
  } else if (note1Reading == HIGH) {
    while (note1Reading == HIGH) {
      stepper.setSpeed(444);
      stepper.runSpeed();

      note1Reading = digitalRead(notePins[1]);
    }
  } else if (note2Reading == HIGH) {
    while (note2Reading == HIGH) {
      stepper.setSpeed(498);
      stepper.runSpeed();

      note2Reading = digitalRead(notePins[2]);
    }
  } else if (note3Reading == HIGH) {
    while (note3Reading == HIGH) {
      stepper.setSpeed(529);
      stepper.runSpeed();

      note3Reading = digitalRead(notePins[3]);
    }
  } else if (note4Reading == HIGH) {
    while (note4Reading == HIGH) {
      stepper.setSpeed(595);
      stepper.runSpeed();

      note4Reading = digitalRead(notePins[4]);
    }
  } else if (note5Reading == HIGH) {
    while (note5Reading == HIGH) {
      stepper.setSpeed(665);
      stepper.runSpeed();

      note5Reading = digitalRead(notePins[5]);
    }
  } else if (note6Reading == HIGH) {
    while (note6Reading == HIGH) {
      stepper.setSpeed(748);
      stepper.runSpeed();

      note6Reading = digitalRead(notePins[6]);
    }
  } else if (note7Reading == HIGH) {
    while (note7Reading == HIGH) {
      stepper.setSpeed(794);
      stepper.runSpeed();

      note7Reading = digitalRead(notePins[7]);
    }
  }
  
  
}
