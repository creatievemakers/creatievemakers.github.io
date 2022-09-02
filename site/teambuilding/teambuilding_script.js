

var bCheckEnabled = true;
var bFinishCheck = false;

var img;
var imgArray = new Array();
var i = 0;

var myInterval = setInterval(loadImage, 1);

function loadImage() {


        img = new Image();
        img.onload = fExists;
        img.onerror = fDoesntExist;
        img.src = './images/a_' + i + '.jpg';

    

}

function fExists() {
    imgArray.push(img);
    i++;
    bCheckEnabled = true;
}

function fDoesntExist() {
    bFinishCheck = true;
}