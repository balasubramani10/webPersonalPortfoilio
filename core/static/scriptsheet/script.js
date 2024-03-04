//Navigation Bar
let menuBtn = document.querySelector("#navToggleBtn");
let showOptions = document.querySelector(".navLinks");
menuBtn.addEventListener("click",()=>{
    
    showOptions.classList.toggle("showToggleOptions")
});
