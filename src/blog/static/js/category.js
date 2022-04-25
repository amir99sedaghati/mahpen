//header

let verticalSubMenu = document.querySelectorAll('.verticalSubMenu');
let subCounter = 0;
const openSubMenu = () =>{
    if(subCounter % 2 == 0){
        for(var i = 0; i < verticalSubMenu.length; i++){
            verticalSubMenu[i].style.display = "block"
        }
        subCounter++;
        return;
    }
    if(subCounter % 2 == 1){
        for(var i = 0; i < verticalSubMenu.length; i++){
            verticalSubMenu[i].style.display = "none"
        }
        subCounter--;
        return;
    }
    
}

const closeHamburger = () => {
    document.querySelector('.hamberMenu').style.display = 'none';
    document.querySelector('.hamburgerBtn').style.display = 'flex';
    
}

const openHamburger = () => {
    document.querySelector('.hamberMenu').style.display = 'block';
    document.querySelector('.hamburgerBtn').style.display = 'none';
}

const showSubMenu = () =>{
    document.querySelector('.horizentalSubMenu').style.display = 'block';
}
const hideSubMenu = () =>{
    document.querySelector('.horizentalSubMenu').style.display = 'none';
}






const next = document.querySelector(".carousel__btn--next"),
  back = document.querySelector(".carousel__btn--back"),
  carousel = document.querySelector(".carousel__cards");
let angle = 0;

next.addEventListener("click", () => {
  angle -= 45;
  carousel.style.transform = `translateZ(-25rem) rotateY(${angle}deg)`;
});

back.addEventListener("click", () => {
  angle += 45;
  carousel.style.transform = `translateZ(-25rem) rotateY(${angle}deg)`;
});









const next2 = document.querySelector(".carousel__btn--next2");
const back2 = document.querySelector(".carousel__btn--back2");
const carousel2 = document.querySelector(".carousel__cards2");
let angle2 = 0;

next2.addEventListener("click", () => {
  angle2 -= 45;
  carousel2.style.transform = `translateZ(-25rem) rotateY(${angle2}deg)`;
});

back2.addEventListener("click", () => {
  angle2 += 45;
  carousel2.style.transform = `translateZ(-25rem) rotateY(${angle2}deg)`;
});





let showAllSocialMedias = () => {
    document.getElementById('socialBtn').style.height = "auto";
    
    document.getElementById('instagram').style.display = "block";
    document.getElementById('telegram').style.display = "block";
}
let hideSocialMedias = () => {
    document.getElementById('socialBtn').style.height = "65px";
    
    document.getElementById('instagram').style.display = "none";
    document.getElementById('telegram').style.display = "none";
}