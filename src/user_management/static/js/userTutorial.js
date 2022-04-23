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







let counter = [0, 0]
let showEpisodes = (x, y) => {
    if(counter[y] == 0){
        document.querySelector('.' + x).style.height = "100%";
        document.querySelector('.' + x).style.opacity = "1";
        counter[y]++;
        return;
    }
    if(counter[y] == 1){
        document.querySelector('.' + x).style.height = "0";
        document.querySelector('.' + x).style.opacity = "0";
        counter[y]--;
        return;
    }
    
    
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