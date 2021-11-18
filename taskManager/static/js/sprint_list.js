
console.log("sprint_list........")
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
coll[i].addEventListener("click", function() {
    this.classList.toggle("active-header");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
        console.log("none....")
        content.style.display = "none";
    } else {
        console.log("block....")
    content.style.display = "block";
    }
});
}

