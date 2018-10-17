var serial; // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbserial-DN05134U';  // fill in your serial port name here
var inData;
var x=1;
var y=1;
var i;
var c;
var f;

function setup() {
 createCanvas(500, 500);
 strokeWeight(2);
 stroke(255);
 noFill();
 colorMode(HSB);

 serial = new p5.SerialPort(); // make a new instance of the serialport library
 serial.on('data', serialEvent);     // callback for when new data arrives
 var options = { baudrate: 9600}; // change the data rate to whatever you wish
 serial.open(portName, options);
 
}

function serialEvent() {
  // retreive value from serial port
  inData = Number(serial.read());
  
}

function draw() {

	c=map(inData, 129, 255, 0, 255);
	stroke(c,100,100);
  for(var i=map(inData, 129, 255, 1, 15); i<10+map(inData, 129, 255, 1, 15);i+=1){
	background(0);
    for (var x=1; x<5;x++){
     for (var y=1; y<5; y++){
       ellipse(100*x,100*y,50+(random(i,i+4)*10),50+(random(i,i+4)*10));  
       
     }
  }
  }  
}