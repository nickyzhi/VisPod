$(function(){
    var $write = $('#write')
     
    $('#keyboard li').click(function(){
        var $this = $(this),
            character = $this.html(); // If it's a lowercase letter, nothing happens to this variable
        if ($this.hasClass('space')) character = ' ';
        if ($this.hasClass('enter')) character = "\n";
         
        $write.html($write.html() + character);
    });
    $('#wordPrediction li').click(function(){
        var $this = $(this),
            character = $this.html(); // If it's a lowercase letter, nothing happens to this variable
         
        $write.html($write.html() + character);
    });
});