var bgm=document.getElementById("bgm");
function bgmPlay(){
    bgm.play();
    console.log(bgm.currentTime);
  }
function bgmPause(){
    bgm.pause();
  } 
$(".playpause").click(function () {
    bgm[bgm.paused ? "play" : "pause"]();
    this.src = "pictures/" + (bgm.paused ? "play" : "pause") + ".ico";
});