var canvas;
var px;
var py;
var sx;
var sy;
var col;

function setup() {
  // put setup code here
  canvas = createCanvas(windowWidth, windowHeight);
  canvas.position(0,0);
  canvas.style('z-index', '-1');
  px = width/2;
  py = height/2;
  col = true;
  //background(0);
}


function draw() {
  // put drawing code here
  noStroke();

  if(col){
    fill(255,random(1.6,0.4));
  } else{
     fill(0,0,255,random(1.6,0.4));
  }

  var r = random(500,1000);
  sx = random(-2,2);
  sy = random(-2,2);

  px = px - (px-mouseX)*0.005;
  py = py - (py-mouseY)*0.005;

  ellipse(px,py,r,r);

  if(frameCount%100==0){
    col =!col;
  }
  
}

function windowResized(){
  resizeCanvas(windowWidth, windowHeight);
}
