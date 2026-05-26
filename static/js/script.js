const hamburger = document.querySelector('#hamburger');

const links_container = document.querySelector('.links-container');

hamburger.addEventListener('click', function(){
    links_container.classList.toggle('open');
    hamburger.classList.toggle('open');

})

const nav = document.querySelector('nav')

// Effet de scroll sur la navbar
window.addEventListener("scroll", ()=>{
    if (window.scrollY >= 150){
        nav.style.top = "-200px";//quand on swipe ça cache
        if (links_container.classList.contains("open") && hamburger.classList.contains("open")){
            //si le menu ham était ouvert, au scroll il se ferme
            links_container.classList.remove('open');
             hamburger.classList.remove('open');           
        }
    }else{
        nav.style.top = 0;
    }
})