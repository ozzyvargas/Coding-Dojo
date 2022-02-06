var requestMinus = document.querySelector('#conrequest')

function changeName(element) {
    document.querySelector(element).innerText="Vargas Ozzy";
}


function hide(element) {
    document.querySelector(element).remove();
    minus1();
}

function minus1(element) {
    requestMinus.innerText--;
}

