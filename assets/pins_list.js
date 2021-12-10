/* >> GLOBAL FUNCTIONS << */
var main_content_area_overlay = document.querySelector('.main-content-area-overlay');
const openOverlay = () =>{
    /* return main_content_area_overlay.classList.add('content-area-overlay'); */
    return main_content_area_overlay.style.display = 'block';
}
const closeOverlay = () =>{
    /* return main_content_area_overlay.classList.remove('content-area-overlay'); */
    return main_content_area_overlay.style.display = 'none';
}


/* >> COMMENTS SECTION << */
var reveal_comments = Array.from(document.querySelectorAll('.reveal-comments'));
var comments_section = Array.from(document.querySelectorAll('.comments-section'));
var comments_section_close = Array.from(document.querySelectorAll('.comments-close-fa-times'));

window.onload = function() {
    associateIdsAndClickHandler();
    closeAssociateIdsAndClickHandler();
  }
function associateIdsAndClickHandler() {
    for (var i = 0; i < comments_section.length; ++i) {
      reveal_comments[i].id = i;
      reveal_comments[i].addEventListener('click',DisplayComments);
    }
}
function closeAssociateIdsAndClickHandler() {
    for (var i = 0; i < comments_section_close.length; ++i) {
        comments_section_close[i].id = i;
        comments_section_close[i].addEventListener('click',CloseComments);
    }
}

function DisplayComments(event){
    comments_section[this.id].classList.add('open-comments-section');
    openOverlay();
}
function CloseComments(event){
    comments_section[this.id].classList.remove('open-comments-section');
    closeOverlay();
}
 for(var x = 0; x < reveal_comments.length;x++){
     console.log(reveal_comments[x]);
     reveal_comments[x].addEventListener('click',DisplayComments);
 }
 for(var x = 0; x < comments_section_close.length;x++){
     comments_section_close[x].addEventListener('click',CloseComments);
 }

/* >> ACCOUNT DROPDOWN <<*/
/*
var account_link_dropdown = document.querySelector('.account-link-dropdown');
var nav_account_link_img = document.querySelector('.nav-account-link-img');
const open_AccountDropDown = () =>{
    if(account_link_dropdown.style.display === 'none'){
        account_link_dropdown.style.display = 'inline';
    }else{
        account_link_dropdown.style.display = 'none';
    }
}
nav_account_link_img.addEventListener('click',open_AccountDropDown);
*/


/* >> MAKE A POST SECTION << */
var nav_fas_fa_plus = document.querySelector('.nav-fas-fa-plus');
var make_a_post = document.querySelector('.make-a-post');
var make_a_post_close_fa_times = document.querySelector('.make-a-post-close-fa-times');

const openMakeAPost = () =>{
    make_a_post.style.display = 'block';
    openOverlay();
}
nav_fas_fa_plus.addEventListener('click',openMakeAPost);

const closeMakeAPost = () =>{
    make_a_post.style.display = 'none';
    closeOverlay();
}
make_a_post_close_fa_times.addEventListener('click',closeMakeAPost);




/** <<-- LIKE AND DISLIKE BUTTON COLOR -->> */
like_btn = Array.from(document.querySelectorAll('.like-color-btn'));
dislike_btn = Array.from(document.querySelectorAll('.dislike-color-btn'));
has_liked = Array.from(document.querySelectorAll('.has_liked'));
has_disliked = Array.from(document.querySelectorAll('.has_disliked'));

const btn_color = () =>{
  for(var x = 0; x < like_btn.length;x++){
    if(Number(has_liked[x].innerHTML) > 0){
      like_btn[x].style.color = 'red'; 
    }
    if(Number(has_disliked[x].innerHTML) > 0){
      dislike_btn[x].style.color = 'red';
    }
}}
window.addEventListener("load", btn_color);
