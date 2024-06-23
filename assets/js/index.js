document.querySelector('.search-btn').onclick = function() {
    var query = document.querySelector('.search-box').value;
    window.open('https://www.bing.com/search?q=' + encodeURIComponent(query));
};

document.querySelector('.scroll-container').addEventListener('wheel', function(e) {
    if (e.deltaY > 0) this.scrollLeft += 100;
    else this.scrollLeft -= 100;
  });


  var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  slides[slideIndex-1].style.display = "block";  
}

// Auto-advance every 3 seconds (adjust as needed)
setInterval(function() {
  plusSlides(1);
}, 3000); // Change the duration (in milliseconds) as desired

window.addEventListener('scroll', function() {
  var scrollPosition = window.scrollY;
  var whitePoint = 600; // Set the scroll position you want for the color change
  if (scrollPosition > whitePoint) {
    document.body.style.backgroundColor = 'white';
  } else {
    document.body.style.backgroundColor = ''; // Or set it back to any other color
  }
});

// Autoplay video
document.addEventListener('DOMContentLoaded', function() {
  var videos = document.querySelectorAll('video');
  videos.forEach(function(video) {
    video.play();
  });
});