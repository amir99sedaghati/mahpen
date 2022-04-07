//slider
let images = ["product1.png", "product2.png", "product3.png"];
let slideCounter = 0;

const nextSlide = () => {
    slideCounter++;
    if(slideCounter == 3){
        slideCounter = 0;
    }
    document.getElementById('slideImage').src = images[slideCounter];
}
const previousSlide = () => {
    slideCounter--;
    if(slideCounter == -1){
        slideCounter = 2;
    }
    document.getElementById('slideImage').src = images[slideCounter];
}


let whiteCircle = document.getElementById('whiteCircle');
let rectangle = document.getElementById('rectangle');
const shadowEffect = () =>{
    
    whiteCircle.style.backgroundColor = "#88153E";
    rectangle.style.backgroundColor = "#88153E";
    whiteCircle.style.boxShadow = "0px 10px 10px 16px #88153E";
}

const normalEffect = () =>{
    whiteCircle.style.backgroundColor = "white";
    rectangle.style.backgroundColor = "white";
    whiteCircle.style.boxShadow = "none";
}

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