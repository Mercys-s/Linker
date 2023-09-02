// Меню для адаптива под телефон

const burgerIcon = document.querySelector('#burger-icon');
const burgerIconClose = document.querySelector('#burger-icon-close');
const ulNav = document.querySelector('#ul-nav');
const blackout = document.querySelector('.background-blackout')
const navBarEl = document.querySelector('.nav-bar-el')
const addWorkButton = document.querySelector('#add-work-button')

const selectMenu = document.querySelector('.main-menu')


burgerIcon.addEventListener ('click' ,  function () {
    ulNav.classList.add('responsive');
    selectMenu.classList.remove('opacity-none-phone');
    burgerIconClose.classList.remove('element-hidden');

    burgerIcon.classList.add('element-hidden');

    addWorkButton.classList.remove('none');
    blackout.classList.remove('none');
    blackout.classList.remove('opacity-none');
});

burgerIconClose.addEventListener ('click', function() {
    ulNav.classList.remove('responsive');
    selectMenu.classList.add('opacity-none-phone');

    burgerIconClose.classList.add('element-hidden');
    burgerIcon.classList.remove('element-hidden');

    addWorkButton.classList.add('none');
    blackout.classList.add('none');
    blackout.classList.add('opacity-none');
});


burgerIcon.addEventListener ('click' ,  function () {
    blackout.classList.remove('none');
    blackout.classList.remove('opacity-none');
});
burgerIconClose.addEventListener ('click', function() {
    blackout.classList.add('none');
    blackout.classList.add('opacity-none');
});


// --- Работа с формой на телефоне ---

const addWorkText2 = document.querySelector('#add-work-button');
const addWorkForm2 = document.querySelector('.add-task-form');
const addWorkClose2 = document.querySelector('#form-close');
const errorWorkClose = document.querySelector('.close-button3');
const formError = document.querySelector('.form-error')

const header = document.querySelector('.header')


addWorkText2.addEventListener('click' , function () {
    addWorkForm2.classList.remove('element-hidden')
    setTimeout (function () {
        addWorkForm2.classList.remove('opacity-none-phone');
    } , 1)

    header.classList.remove('z-index-2')
    header.classList.add('z-index-1')

    addWorkForm2.classList.add('z-index-2')
});

addWorkClose2.addEventListener('click', function () {
    addWorkForm2.classList.add('opacity-none-phone')
    setTimeout (function () {
        addWorkForm2.classList.add('element-hidden');
    } , 400)
    

    header.classList.add('z-index-2')
    addWorkForm2.classList.remove('z-index-2')
});

errorWorkClose.addEventListener('click', function () {
    formError.classList.add('none');
});


