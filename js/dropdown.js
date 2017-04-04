/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function Search(array, key) {
    var i,y;
    for (i = 0; i < array.length; i++){
        if (key >= array[i]) y = i;
    }
    return y;
}
function ParseTime(time){
    var str = time.split(':');
    var sec = (+str[0])*3600 + (+str[1])*60 + (+str[2]);
    return sec
}