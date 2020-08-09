$('.main_event_container').slick({
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    dots: true,
    prevArrow: false,
    nextArrow: false,
});
$('.hot_store').slick({
    dots: true,
    prevArrow: false,
    nextArrow: false,
});

$('.store1_slide').slick({
    dots: true,
});

const openLogin = document.getElementById("open_login");
const modal = document.querySelector(".modal");
const overlay = modal.querySelector(".modal_overlay");
const closeBtn = modal.querySelector(".btn_exit");
// const closeBtn = modal.getElementsByClassName("btn_exit");

const openModal = () =>{
    modal.classList.remove("hidden");
}
const closeModal = () => {
    modal.classList.add("hidden");
}
overlay.addEventListener("click", closeModal);
closeBtn.addEventListener("click", closeModal);
openLogin.addEventListener("click",openModal);