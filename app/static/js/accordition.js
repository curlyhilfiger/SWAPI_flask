
var accorditions = document.getElementsByClassName("accordition");
console.log(accorditions);
    for (var i = 0; i < accorditions.length; i++) {
        accorditions[i].onclick = function () {
            var content = this.nextElementSibling;
            console.log(content);

            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    }
