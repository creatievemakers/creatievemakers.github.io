var image = document.getElementById("image");




const length = 8 //amount of images in folder

const textTimeouts = [];

function sleep(ms, cb=()=> {}) {
    return new Promise(resolve => {
      const time = setTimeout(() => {
        resolve();
      }, ms);
      cb(time);
    });
  }


 function loadImage() {

    console.log('asdasd')
    image.innerHTML +=    "test" 

//   for (let i = 0; i <= length; i++) {
//     sleep(Math.random()*200 * i, (time) => textTimeouts.push(time)).then(res => {
//       image.innerHTML +=    "test" 

      
//     });
    
//   };
};
