var profile_page_overlay = document.querySelector('.profile-page-overlay');
var update_profile_details_container_fa_times_close = document.querySelector('.update-profile-details-container-fa-times-close');
var update_profile_details_resetbutton = document.querySelector('.update-profile-details-resetbutton');
var change_profile_details = document.querySelector('.change-profile-details');
var update_profile_details_container = document.querySelector('.update-profile-details-container');

var open_update_profileDetails_form = () =>{
    profile_page_overlay.classList.add('open-profile-page-overlay'); 
    update_profile_details_container.classList.add('open-update-profile-details-container')
}
var close_update_profileDetails_form = () =>{
    profile_page_overlay.classList.remove('open-profile-page-overlay');
    update_profile_details_container.classList.remove('open-update-profile-details-container');
}
change_profile_details.addEventListener('click',open_update_profileDetails_form);
update_profile_details_container_fa_times_close.addEventListener('click',close_update_profileDetails_form);
update_profile_details_resetbutton.addEventListener('click',close_update_profileDetails_form);

/* >> ACCOUNT DROPDOWN <<*/
var profile_account_link_dropdown = document.querySelector('.profile-account-link-dropdown');
var profile_nav_account_link_img = document.querySelector('.profile-nav-account-link-img');
const open_ProfileAccountDropDown = () =>{
    if(profile_account_link_dropdown.style.transform == 'scaleY(0)'){
        /* profile_account_link_dropdown.style.display = 'inline'; */
        profile_account_link_dropdown.style.transform = 'scaleY(1)';
    }else{
        /* profile_account_link_dropdown.style.display = 'none'; */
        profile_account_link_dropdown.style.transform = 'scaleY(0)';
    }
}
profile_nav_account_link_img.addEventListener('click',open_ProfileAccountDropDown);