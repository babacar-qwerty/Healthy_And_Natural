const hamburger = document.querySelector('#hamburger');

const links_container = document.querySelector('.links-container');

hamburger.addEventListener('click', function(){
    links_container.classList.toggle('open');
    hamburger.classList.toggle('open');

})