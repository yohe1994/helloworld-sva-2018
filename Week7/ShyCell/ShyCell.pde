import gab.opencv.*;
import processing.video.*;
import java.awt.*;
 
// audio bits
import ddf.minim.*;
import ddf.minim.ugens.*;
AudioOutput out;

// video bits
Capture video;
OpenCV opencv;
 
boolean playOnce=false;  
static final int NUM_LINES = 20;

//define the movement of the bubble
float x1(float t) {  return sin (-t / 10) * 100 + sin (t / 5) * 20;}
float y1(float t) {  return cos (-t / 10) * 100 + sin (t/5) * 50;}
float x2(float t) {  return sin (t / 10) * 200 + sin (t) * 2 + cos (t) * 10;}
float y2(float t) {  return -cos (t / 20) * 200 + cos (t / 12) * 20;}

float t;
float s;//the parameter control the extent of bubble transformation
int x=0;//the index of the array, which is to save faces length everytime when it changes
int a=0;//the parameter to control the transition time
float b=0.05;//the parameter to control the speed of bubble's moving
float c=186;//the parameter to control the color
float []leng;

void setup() {
  size (1500, 800);
  colorMode(HSB,360,100,100);
  video = new Capture(this, 640/2, 480/2);
  opencv = new OpenCV(this, 640/2, 480/2);
  leng = new float[1000];
  leng[0] = 1;
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);  
  video.start();
  Minim minim = new Minim(this);
  out = minim.getLineOut();
}
 
void draw() {
  //analyze the face
  opencv.loadImage(video);
  Rectangle[] faces = opencv.detect();
  print("faces.length: ");
  println(faces.length);

  //print the size of face
  for (int i = 0; i < faces.length; i++) {
    print("faces.size: ");
    println(faces[i].x + "," + faces[i].y);
    if(playOnce==false){
      out.playNote(0, 1, (faces[i].width*2));
      playOnce=true;
    }
    //if detect change of face numbers, store the number as leng[x], 
    if(leng[x]!=faces.length){
      x++;//turn to next index of array
      a=60;//the time of transition (by default, the frame rate is 60 frame per second, so draw function runs 60 times per second)
      leng[x]=faces.length;//store the length of faces 
      if(faces.length>leng[x-1]){
        b=b+0.4;//everytime when the number of faces increases, b (control speed)is added by 0.4
      }
      else{
        b=b-0.4;//everytime when the number of faces decreases, b (control speed)is substracted by 0.4
      }
      s=0;//everytime when the number of faces changes, reset the value of s
    }
  }
  
  
  
  //draw bubble
  background(70);// the color of background
  stroke (c,100,100);// the color of picture
  strokeWeight (300);// make the shape of creature
  translate (width/2, height/2);//move the shape to the center
    
  if(a>0){
    if(faces.length>leng[x-1]){
      //to calculate the value of s, only runs when s<abs((1.5/leng[x-1])-(1.5/faces.length), i.e. only runs 60 times
      if(s<abs((1.5/leng[x-1])-(1.5/faces.length))){
        s=s+abs((1.5/leng[x-1])-(1.5/faces.length))/60;//every frame, s was added by 1/60 of difference between last scale and this scale, so in 1 second(60 frames), s was added by the difference between last scale and this scale 
        if(faces.length<=7){
          c=c+0.5;//every frame, c was added by 0.5, so in 1 second(60 frames), c was added by 30, making color warmer
        }
        else{
          c=360;//if the number of faces are more than 7, keep c=360(the most reddish)
        }
      }
      scale(1.5/leng[x-1]-s);
      stroke (c,100,100);
    }
    else if(faces.length<leng[x-1]){
      if(s<abs((1.5/leng[x-1])-(1.5/faces.length))){
        s=s+abs((1.5/leng[x-1])-(1.5/faces.length))/60;
        if(faces.length<=7){
          c=c-0.5;//every frame, c was substracted by 0.5, so in 1 second(60 frames), c was substracted by 30, making color warmer
        }
        else{
          c=360;//if the number of faces are more than 7, keep c=360(the most reddish) 
        }
      }
      scale(1.5/leng[x-1]+s);
      stroke (c,100,100);
    }
    a=a-1;//every frame subtracted by 1, so it takes 60 times to make a from 60 to 0, which means 1 second
  }
  else{
      scale(1.5/faces.length);
  }
    
  for (int i = 0; i < NUM_LINES; i++) {
    line (x1(t + i), y1(t + i), x2(t + i), y2(t + i));
  }//multiple lines
  t += b;//the speed of move
}
 
void captureEvent(Capture c) {
  c.read();
}
