let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")


menu.addEventListener("click", function(){
    if (header.style.height == "110px" || header.offsetHeight == 110){
        header.style.height = 110 + nav.offsetHeight + "px"
    } else {
        header.style.height = "110px"
    }
})

window.addEventListener("resize", function(){
    let anchoVentana = document.documentElement.clientWidth

    if(anchoVentana > 480){
        header.style = "none"
    }})