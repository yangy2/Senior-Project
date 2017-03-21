#include <SoftwareSerial.h>// import the serial library

SoftwareSerial Nao(10, 11); // TX, RX

int BluetoothData; // the data given from Computer

void setup() 
{
  Nao.begin(9600);
  Nao.println("Bluetooth On, Awaiting Instruction");
  
  Serial.begin(9600);
}

void loop() 
{
   if (Nao.available())
   {
      BluetoothData=Nao.read();

      if (BluetoothData=='2')
      {
         Nao.println("Backward");
         Serial.println("b");
      }
      
      if (BluetoothData=='4')
      {
         Nao.println("Left");
         Serial.println("l");
      }

      if (BluetoothData=='5')
      {
         Nao.println("Stop");
         Serial.println("s");
      }
      
      if (BluetoothData=='6')
      {
         Nao.println("Right");
         Serial.println("r");
      }

      if (BluetoothData=='7')
      {
         Nao.println("C-Clkwise");
         Serial.println("k");
      }
      
      if (BluetoothData=='8')
      {
         Nao.println("Forward");
         Serial.println("f");
      }
      
      if (BluetoothData=='9')
      {
         Nao.println("Clkwise");
         Serial.println("c");
      }
   }
   delay(100);// prepare for next data ...
}
