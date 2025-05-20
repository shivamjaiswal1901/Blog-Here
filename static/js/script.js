setTimeout(function () {
    var start_container = document.getElementById('start_container');
    if (start_container) {
        start_container.classList.add('slide-up');
    }
}, 3000);



function sideopen() {
    document.getElementById('sidebar').style.left = 0;
}
function sideclose() {
    document.getElementById('sidebar').style.left = "-20%";
}

// let i = 0;
// function like(love) {
//     let likee = document.getElementById(love);
//     if (i === 0) {
//         likee.setAttribute("src", "/static/images/heart.png")
//         likee.style.transform = "scale(1.3)";
//         i = 1;
//     }
//     else{
//         likee.setAttribute("src", "/static/images/love.png")
//         likee.style.transform = "scale(1)";
//         i = 0;
//     }
//     console.log(likee)
// }


function like(love) {
    let likee = document.getElementById(love);
    let isLiked = likee.dataset.liked === 'true';

    if (!isLiked) {
        likee.setAttribute("src", "/static/images/heart.png");
        likee.style.transform = "scale(1.3)";
        likee.dataset.liked = 'true'; 
    } 
    else {
        likee.setAttribute("src", "/static/images/love.png");
        likee.style.transform = "scale(1)";
        likee.dataset.liked = 'false'; 
    }

    console.log(likee);
}

let i = 0;
function profile_menu(){
    let btn = document.getElementById('dots_btn')
    if (i == 0){
        btn.style.display = "flex";
        i = 1;
    }

    else{
        btn.style.display = "none";
        i = 0;
    }
    
}
