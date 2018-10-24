import processing.serial.*;

Serial myPort;
float a;
float b;
float c;
float radian;
float resistence;
float rectheight;
float flex;
float touch;
float Status=0;
float vo;
float x;
float y;
float z;
float t=0;
PImage ball;
PImage basket;
PFont congrats;
PFont lose;

void setup()
  {size(1000,500);
   strokeWeight(2);
   fill(0);
   printArray(Serial.list());
   myPort =new Serial(this,"/dev/cu.usbserial-DN05134U",9600);
   myPort.bufferUntil('\n');
   ball = loadImage("basketball.png");
   basket = loadImage("basketball-basket.jpg");
   String[] fontList = PFont.list();
   congrats = createFont("04b",32);
   lose = createFont("04b",32);
}

void serialEvent(Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    inString = trim(inString);
    float[] inputs = float(split(inString, ","));
    if (inputs.length >=3) {
      flex = inputs[0];
      resistence = inputs[1];
      touch = inputs[2];
    }
  }
}

void draw(){//————————————————————————————————
  if (myPort.available()>0)
  { 
    if(Status==0)
    {print("Status: ");
     println(Status);
     print("Flex: ");
     println(flex);
     print("Resistence: ");
     println(resistence);
     print("Touch: ");
     println(touch);
     radian = map(resistence,400,1024,0,90)*TWO_PI/360;
     background(255);
     //ball = loadImage("basketball.png");
     //basket = loadImage("basketball-basket.jpg");
     imageMode(CORNER);
     image(basket,0,200,93.5,87);
     line(1000-22.5,400-22.5,1000-22.5-cos(radian)*100,400-22.5-sin(radian)*100);
     image(ball,1000-45,400-45,45,45);
     rect(1000-90,200,45,-rectheight);
    }
    else if (Status==1)
    {
     print("Status: ");
     println(Status);
     print("Flex: ");
     println(flex);
     print("Resistence: ");
     println(resistence);
     print("Touch: ");
     println(touch);
     //rectheight = map(flex,30,180,0,90);
     rectheight = map(flex,0,1000,0,90);
     background(255);
     //ball = loadImage("basketball.png");
     //basket = loadImage("basketball-basket.jpg");
     imageMode(CORNER);
     image(basket,0,200,93.5,87);
     line(1000-22.5,400-22.5,1000-22.5-cos(radian)*100,400-22.5-sin(radian)*100);
     image(ball,1000-45,400-45,45,45);
     rect(1000-90,200,45,-rectheight);
    }
    else if (Status==2)
    {
     print("Status: ");
     println(Status);
     print("Rectheight: ");
     println(rectheight);
     print("Radian: ");
     println(radian);
     print("X: ");
     println(x);
     print("Y: ");
     println(y);
     print("T: ");
     println(t);
     x=x+cos(radian)*vo;
     y=y+sin(radian)*vo;
     t=t+1;
     z=z+t;
     background(255);
     //ball = loadImage("basketball.png");
     //basket = loadImage("basketball-basket.jpg");
     imageMode(CORNER);
     image(basket,0,200,93.5,87);
     image(ball,955-x,355-y+z,45,45);
     if(x<977.5 && x>906.5 && y-z<155.5 && y-z>127.5)
     {
       c=1;
     }
     else if ((y-z<-145) && (c!=1))
     {
       b=1;
     }
     if(c==1)
     {
       textFont(congrats);
       textAlign(CENTER, CENTER);
       text("Good Job!", 500, 250); 
       fill(98, 193, 141);
     }
     else if (b==1)
     {
       textFont(lose);
       textAlign(CENTER, CENTER);
       text("You Lose, Tap to Continue", 500, 250); 
       fill(98, 193, 141);
     }
    }
      
    if(touch==1)
    {
      a=1;//use a to check the touch action
    }
    else if(touch==0)
    {
      if(a==1)//use a to check the touch action
      {
        Status=Status+1;
        if(Status==2)
        {
         vo=rectheight;
        }
        if(Status==3)
        {
         Status=0;
         rectheight=0;
         x=y=z=t=0;
         b=0;
         c=0;
         fill(0);
        }
        a=0;
      }
    }
  }  
}
