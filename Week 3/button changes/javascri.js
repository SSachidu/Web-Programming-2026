function changeName() {

   
    document.querySelector("h2").innerHTML = "FlwTrim";
}

function changeBackground() {
    document.body.style.backgroundColor = "lightblue";
}

function showMessage(){
alert("Welcome to my personal profile");

}

function showSkills(){


    alert("my skills are html css and python");
}

function changePhoto() {

    let image = document.querySelector("#profilePhoto");

    if (image.src.includes("images.jpg")) {
        image.src = "image.jpg";
    } else {
        image.src = "id.jpg";
    }
}