HTMLTextAreaElement.prototype.getCaretPosition = function() { //return the caret position of the textarea
    return this.selectionStart;
};
HTMLTextAreaElement.prototype.setCaretPosition = function(position) { //change the caret position of the textarea
    this.selectionStart = position;
    this.selectionEnd = position;
    this.focus();
};

var textarea = document.getElementsByTagName('textarea')[0];


textarea.onkeydown = function(event) {
    
    //support tab on textarea
    if (event.keyCode == 9) { //tab was pressed
        var newCaretPosition;
        newCaretPosition = textarea.getCaretPosition() + "    ".length;
        textarea.value = textarea.value.substring(0, textarea.getCaretPosition()) + "    " + textarea.value.substring(textarea.getCaretPosition(), textarea.value.length);
        textarea.setCaretPosition(newCaretPosition);
        return false;
    }
    if (event.keyCode == 8) { //backspace
        if (textarea.value.substring(textarea.getCaretPosition() - 4, textarea.getCaretPosition()) == "    ") { //it's a tab space
            var newCaretPosition;
            newCaretPosition = textarea.getCaretPosition() - 3;
            textarea.value = textarea.value.substring(0, textarea.getCaretPosition() - 3) + textarea.value.substring(textarea.getCaretPosition(), textarea.value.length);
            textarea.setCaretPosition(newCaretPosition);
        }
    }
    if (event.keyCode == 37) { //left arrow
        var newCaretPosition;
        if (textarea.value.substring(textarea.getCaretPosition() - 4, textarea.getCaretPosition()) == "    ") { //it's a tab space
            newCaretPosition = textarea.getCaretPosition() - 3;
            textarea.setCaretPosition(newCaretPosition);
        }
    }
    if (event.keyCode == 39) { //right arrow
        var newCaretPosition;
        if (textarea.value.substring(textarea.getCaretPosition() + 4, textarea.getCaretPosition()) == "    ") { //it's a tab space
            newCaretPosition = textarea.getCaretPosition() + 3;
            textarea.setCaretPosition(newCaretPosition);
        }
    }
}