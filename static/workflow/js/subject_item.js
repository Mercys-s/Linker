
// Функционал для формы
const editWorkButton = document.querySelector ('#subject-item-edit')
const addWorkForm = document.querySelector ('.add-task-form');
const addWorkClose = document.querySelector ('#form-close');

editWorkButton.addEventListener('click', function () {
    addWorkForm.classList.remove('display-none');
    setTimeout (function () {
        addWorkForm.classList.remove('element-hidden');
    } , 1)
});

addWorkClose.addEventListener('click', function () {
    addWorkForm.classList.add('element-hidden');
    setTimeout (function () {
        addWorkForm.classList.add('display-none');
    } , 400)
});


// Подгон файла под размеры страницы и формы
const workFile = document.querySelector('.subject-item-file-embed')
editWorkButton.addEventListener('click', function () {
    workFile.classList.remove('file-resolution-long');
    workFile.classList.add('file-resolution-short');
});

addWorkClose.addEventListener('click', function () {
    workFile.classList.remove('file-resolution-short');
    workFile.classList.add('file-resolution-long');
});


// Сообщение об ошибке
closeFormError = document.querySelector('.form-error');
closeFormErrorButton = document.querySelector('.close-button3');

if (closeFormErrorButton !== null) {
    closeFormErrorButton.addEventListener('click' , function () {
        closeFormError.classList.add('display-none');
    });
}

// Адаптация под телефон - регулировка верхнего отступа 

const burgerIcon2 = document.querySelector ('#burger-icon')
const cardInfo = document.querySelector ('.card-info');
const burgerIconClosed = document.querySelector ('#burger-icon-close');

burgerIcon2.addEventListener ('click', function() {
    cardInfo.classList.add('margin-top-4per')
});

burgerIconClosed.addEventListener ('click', function() {
    cardInfo.classList.remove('margin-top-4per')
});


const editFormButton = document.querySelector('#image-button-edit')
const blackOut = document.querySelector('.background-blackout')
const anotherOneCloseForm = document.querySelector('#form-close')

editFormButton.addEventListener('click' , function() {
    blackOut.classList.remove('none')
    setTimeout (function () {
        blackOut.classList.remove('opacity-none');
    } , 1)
});

anotherOneCloseForm.addEventListener('click' , function() {
    blackOut.classList.add('opacity-none');
    setTimeout (function () {
        blackOut.classList.add('none')
    } , 1)
});