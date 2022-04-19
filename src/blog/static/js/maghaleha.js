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












let groupingCounter = 0
const showGroupingDropDown = () => {
    if(groupingCounter == 0){
        document.getElementById('dropDown').style.visibility = "visible";
        document.getElementById('grouping').style.borderRadius = "20px 20px 0 0";
        document.getElementById('groupingAngle').style.transform = "rotate(180deg)";
        groupingCounter++;
        return;
    }
    if(groupingCounter == 1){
        document.getElementById('dropDown').style.visibility = "hidden";
        document.getElementById('grouping').style.borderRadius = "20px";
        document.getElementById('groupingAngle').style.transform = "rotate(0deg)";
        groupingCounter--;
        return;
    }
}

let sortingCounter = 0
const showsortingDropDown = () => {
    if(sortingCounter == 0){
        document.getElementById('sortingDropDown').style.visibility = "visible";
        document.getElementById('sorting').style.borderRadius = "20px 20px 0 0";
        document.getElementById('sortingAngle').style.transform = "rotate(180deg)";
        sortingCounter++;
        return;
    }
    if(sortingCounter == 1){
        document.getElementById('sortingDropDown').style.visibility = "hidden";
        document.getElementById('sorting').style.borderRadius = "20px";
        document.getElementById('sortingAngle').style.transform = "rotate(0deg)";
        sortingCounter--;
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
