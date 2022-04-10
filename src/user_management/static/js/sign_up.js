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



let randomNumber = () => {
    let val = Math.floor(1000+Math.random() * 9000)
    return val;
}
let registerSecurityCode = document.getElementById('registerSecurityCode');
registerSecurityCode.innerText = randomNumber();


var loginSecurityCode = document.getElementById('loginSecurityCode');
loginSecurityCode.innerText = randomNumber();


var changeRegisterCode = () => {
    registerSecurityCode.innerText = randomNumber();
    
}
var changeLoginCode = () => {
    loginSecurityCode.innerText = randomNumber();
    
}
console.log(loginSecurityCode.innerText);


let registerFunction = () => {
    if(document.getElementById('registerPassword').value === document.getElementById('repeatRegisterPassword').value && document.getElementById('registerCode').value === document.getElementById('registerSecurityCode').innerText){
        var names = document.getElementById('registerName').value;
        var lastNames = document.getElementById('registerLastName').value;
        var passwords = document.getElementById('registerPassword').value;
        var emails = document.getElementById('registerEmail').value;
        var numbers = document.getElementById('registerNumber').value;
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