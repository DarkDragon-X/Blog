window.onload=function(){
    
    const menu_button = document.querySelector('.open-nav');
    const mobile_menu = document.querySelector('.mobile-nav');

    menu_button.addEventListener('click', function(){
        mobile_menu.classList.toggle('opened');
    });
}
