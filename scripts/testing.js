var t;
var col;

function setup() {
    createCanvas(windowWidth,windowHeight);


    // put setup code here
    canvas = createCanvas(windowWidth, windowHeight);
    canvas.position(0,0);
    canvas.style('z-index', '-1');
    px = width/2;
    py = height/2;
    col = true;



    stroke(255,random(1,20));
    t = 1
}

function draw() {    




    noFill();
    var x1 = 0
    var x2 = 30
    var x3 = width * noise(t );
    var x4 = width * noise(t )
    var y1 = noise(t) * height
    var y2 = width * noise(t +20 )
    var y3 = 0
    var y4 = 0

    bezier(x1, y1, x2, y2, x3, y3, x4, y4);
    // bezier(80, 100, 100, frameCount, 90, 90, frameCount, 80);

    t += 0.005;

    // if(frameCount%100==0){
    // col =!col;
    // }

  if (frameCount % 1000 == 0) {
	background(0);
  }
}