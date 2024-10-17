var profile = document.querySelector('.profile');
var profile_box = document.querySelector('.profile-box');
var account_switch = document.querySelector('#switch');
var main_wrapper = document.querySelector('.main-wrpper');
var cart_number = document.querySelector('.cart_numbers');


profile.addEventListener('click', () => {
    // Check the current display state and toggle it
    if (profile_box.style.display === 'none' || profile_box.style.display === '') {
        profile_box.style.display = 'flex';
    } else {
        profile_box.style.display = 'none';
    }
});


// document.body.addEventListener('wheel', () => {
//     // Set the margin of the main_wrapper element
//     main_wrapper.style.margin = 'auto 20px';
//     profile_box.style.display = 'none';

// });

if (localStorage.getItem('cart') == null) {
    var cart = {};
    // var cart_num = 
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

var num = 1;
$( document ).ready(function() {
$('.cart').click(function () {

            var tostr = this.id.toString();
            console.log(tostr);

            if (cart[tostr] !== undefined) {
                cart[tostr] = cart[tostr]  +  1;
            } else {
                cart[tostr] = 1;
            }

            console.log(cart);
            var cart_local_num = Object.values(cart).reduce((a, b) => a+b,0);

            localStorage.setItem('cart', JSON.stringify(cart));
            localStorage.setItem('cart_num', cart_local_num);

            if(!cart_number.innerHTML == 1) {
                cart_number.innerHTML =  1;
                cart_number.style.display = 'block';
            }else{
                cart_number.innerHTML=  parseInt(cart_number.innerHTML) + 1;
            }
            
            
        });


        // $('.toast-main').click( ()=>{
        //     $('#liveToast').show();
        // });

        const toastTrigger = document.querySelector('.toast-main')
        const toastLiveExample = document.getElementById('liveToast')

        if (toastTrigger) {
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
        toastTrigger.addEventListener('click', () => {
            toastBootstrap.show()
        })
        }

});

$( window ).on( "load", function() {
    if((localStorage.getItem('cart_num') !== null)) {
        cart_number.innerHTML =  localStorage.getItem('cart_num');
        cart_number.style.display = 'block';
    }

    var value = "new_value";
    document.cookie="new_key="+value;
});








