/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

// drag profile circle
function rotateAnnotationCropper(offsetSelector, xCoordinate, yCoordinate, cropper){
        //alert(offsetSelector.left);
    
        var x = xCoordinate - offsetSelector.offset().left - offsetSelector.width()/2;
        var y = -1*(yCoordinate - offsetSelector.offset().top - offsetSelector.height()/2);
        var theta = Math.atan2(y,x)*(180/Math.PI);        


        var cssDegs = convertThetaToCssDegs(theta);
        var rotate = 'rotate(' +cssDegs + 'deg)';
        cropper.css({'-moz-transform': rotate, 'transform' : rotate, '-webkit-transform': rotate, '-ms-transform': rotate});
        
        $('body').on('mouseup', function(event){ $('body').unbind('mousemove')}); 
        $('body').on('touchend', function(event){ $('body').unbind('touchmove')}); 

}

function convertThetaToCssDegs(theta){
    var cssDegs = 90 - theta;
    return cssDegs;
}

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
    return sec;
}

function gen_x(i,d){
                    var x;
                    if(i<3){
                        switch (i) {
                            case 0:
                                x = -d;
                                break;
                            case 1:
                                x = 0;
                                break;
                            case 2:
                                x = d;
                                break;
                        }
                    }else if(i<6){
                        switch (i) {
                            case 3:
                                x = -d;
                                break;
                            case 4:
                                x = 0;
                                break;
                            case 5:
                                x = d;
                                break;
                        }
                    }else{
                        switch (i) {
                            case 6:
                                x = -d;
                                break;
                            case 7:
                                x = 0;
                                break;
                            case 8:
                                x = d;
                                break;
                        }
                    }
                    return x;
                }
function gen_y(i,d){
    var x;
    if(i<3){
        x = -d;
    }else if(i<6){
        x = 0;
    }else{
        x = d;
    }
    return x;
}

                