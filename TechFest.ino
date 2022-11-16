
int relay1 = 1;int relay2 = 2;int relay3 = 3;int relay4 = 4;int incomingByte;int e1=9;
int llm1=5;int llm2=6;int rrm1=7;int rrm2=8;int mer=10;int mel=11; int ir=12;

void setup() {
    pinMode(relay1, OUTPUT);pinMode(relay2, OUTPUT);pinMode(e1, OUTPUT);pinMode(relay3, OUTPUT);pinMode(relay4, OUTPUT); 
    
    pinMode(llm2,OUTPUT); pinMode(llm1,OUTPUT);  pinMode(rrm1,OUTPUT); pinMode(rrm2,OUTPUT);  pinMode(mer,OUTPUT);
    pinMode(mel,OUTPUT);pinMode(ir,INPUT);
    Serial.begin(9600);
}

void stop_arduino()
{
 digitalWrite(relay1,HIGH);digitalWrite(relay2,HIGH);digitalWrite(relay3,HIGH);digitalWrite(relay4,HIGH); 
}
void glass(){
  digitalWrite(llm1,HIGH);digitalWrite(llm2,LOW);
  digitalWrite(rrm1,HIGH);digitalWrite(rrm2,LOW);
  analogWrite(mer,200);
  analogWrite(mel,200);  
  delay(1300); //go forward 2 seconds 
  digitalWrite(llm1,LOW);digitalWrite(llm2,LOW);
  digitalWrite(rrm1,LOW);digitalWrite(rrm2,LOW);
  delay(5000);//time to pivk up glass
  bool a=true;
  while (a)
  {
    
    if(digitalRead(ir)==0)
    {
      a=false;
      delay(2500);    
      digitalWrite(llm1,LOW);digitalWrite(llm2,HIGH);
      digitalWrite(rrm1,LOW);digitalWrite(rrm2,HIGH);
      analogWrite(mer,200);
      analogWrite(mel,200);
      delay(1300);
      digitalWrite(llm1,LOW);digitalWrite(llm2,LOW);
      digitalWrite(rrm1,LOW);digitalWrite(rrm2,LOW);
    }
  }
}
void start_arduino()
{
  // Rotate in CW direction
  digitalWrite(relay1,HIGH);digitalWrite(relay2,LOW);
  digitalWrite(relay3,LOW);digitalWrite(relay4,HIGH);
  analogWrite(e1,255);
  delay(7000);
  glass();
  delay(30000);  
  digitalWrite(relay1,HIGH);digitalWrite(relay2,HIGH);
  digitalWrite(relay3,HIGH);digitalWrite(relay4,HIGH);
  //delay(500);
}
void loop() {
//  start_arduino();
//  stop_arduino();
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      start_arduino();
      
    }
    if (incomingByte == 'L') {
      stop_arduino();
    }
  }
  }
