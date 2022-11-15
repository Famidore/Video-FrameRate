let dropzone;
let vid;

function setup() {
  noCanvas()
  dropzone = select('#dropzone');
  dropzone.dragOver(highlight);
  dropzone.dragLeave(unhighlight)
  dropzone.drop(readFile, unhighlight)
  
}

function draw() {
  background(51);
  // createP(getFrameRate())
}



function highlight(){
  dropzone.style('background-color', '#ccc')
}

function unhighlight(){
  dropzone.style('background-color', '#fff')
}

function readFile(file){
  vid = createVideo(file.data)
  vid.size(1200,640)
  vid.volume(0)
  vid.play()
}