const allImages = document.getElementsByTagName('img');

function styleImage(image, width, height) {
  image.style.width = width + 'px';
  image.style.height = height + 'px';
  image.style.margin = '0 auto'; 
}

for (let i = 0; i < allImages.length; i++) {
  styleImage(allImages[i], 500, 500); 
}
(function sayy(){
  alert('Thanks for coming');

}

)()