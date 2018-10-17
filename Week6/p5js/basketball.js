var serial; // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbserial-DN05134U';  // fill in your serial port name here
var a;
var b;
var c;
var radian;
var resistence;
var rectheight;
var flex;
var touch;
var Status=0;
var vo;
var x;
var y;
var z;
var t=0;
var ball;
var basket;
var congrats;
var lose;

function preload(){
  ball = loadImage("basketball.png");
  basket = loadImage("basketball-basket.jpg");
  congrats = loadFont('04b.ttf');
  lose = loadFont('04b.ttf');
}

function setup() {
 //String[] fontList = PFont.list();
 createCanvas(1000,500);
 strokeWeight(2);
 fill(0);

 serial = new p5.SerialPort(); // make a new instance of the serialport library
 //serial.on('list', printList); // set a callback function for the serialport list event
 serial.on('data', serialEvent);     // callback for when new data arrives
 var options = { baudrate: 9600}; // change the data rate to whatever you wish
 serial.open(portName, options);
 
}

function serialEvent() {
  // read a string from the serial port
  // until you get carriage return and newline:
  var inString = serial.readStringUntil('\r\n'); //check to see that there's actually a string there:
  
  if (inString.length > 0) {
    var sensors = split(inString, ','); // split the string on the commas
      if (sensors.length >= 3) { // if there are three elements
        flex = Number(sensors[0]); // element 0 is the flex
        resistence = Number(sensors[1]); // element 1 is the resistence
        touch = Number(sensors[2]); // element 2 is the touch
      }
    serial.write('x'); // send a byte requesting more serial data 
  }
}

function draw(){//————————————————————————————————
  if(Status==0)
    {print("Status: ");
     print(Status);
     print("\n");
     print("Flex: ");
     print(flex);
     print("\n");
     print("Resistence: ");
     print(resistence);
     print("\n");
     print("Touch: ");
     print(touch);
     print("\n");
     radian = map(resistence,400,1024,0,90)*TWO_PI/360;
     background(255);
     imageMode(CORNER);
     image(basket,0,200,93.5,87);
     line(1000-22.5,400-22.5,1000-22.5-cos(radian)*100,400-22.5-sin(radian)*100);
     image(ball,1000-45,400-45,45,45);
     rect(1000-90,200,45,-rectheight);
    }
    else if (Status==1)
    {
     print("Status: ");
     print(Status);
     print("\n");
     print("Flex: ");
     print(flex);
     print("\n");
     print("Resistence: ");
     print(resistence);
     print("\n");
     print("Touch: ");
     print(touch);
     print("\n");
     rectheight = map(flex,0,1000,0,90);
     background(255);
     imageMode(CORNER);
     image(basket,0,200,93.5,87);
     line(1000-22.5,400-22.5,1000-22.5-cos(radian)*100,400-22.5-sin(radian)*100);
     image(ball,1000-45,400-45,45,45);
     rect(1000-90,200,45,-rectheight);
    }
    else if (Status==2)
    {
     print("Status: ");
     print(Status);
     print("\n");
     print("Rectheight: ");
     print(rectheight);
     print("\n");
     print("Radian: ");
     print(radian);
     print("\n");
     print("X: ");
     print(x);
     print("\n");
     print("Y: ");
     print(y);
     print("\n");
     print("T: ");
     print(t);
     print("\n");
     x=x+cos(radian)*vo;
     y=y+sin(radian)*vo;
     t=t+1;
     z=z+t;
     background(255);
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
       textSize(32);
       text("Good Job!", 500, 250); 
       fill('#62c18d');
   		
     }
     else if (b==1)
     {
       textFont(lose);
       textAlign(CENTER, CENTER);
       textSize(32);
       text("You Lose, Tap to Continue", 500, 250); 
       fill('#62c18d');
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