document.querySelector('.search-btn').onclick = function() {
    var query = document.querySelector('.search-box').value;
    window.open('https://www.bing.com/search?q=' + encodeURIComponent(query));
};

// Accordion functionality
var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}