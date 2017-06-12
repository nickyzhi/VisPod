'use strict'
var bgm=document.getElementById("bgm");
function bgmPlay(){bgm.play();}
function bgmPause(){bgm.pause();} 
$(".playpause").click(function () {
    if (bgm.paused){
        bgmPlay();
        this.src = "../static/pictures/pause.ico";
        var audio_duration = document.getElementById("bgm").duration;
        d3.timer(function() {
            var currentTime = Math.floor(document.getElementById("bgm").currentTime);
            //360 degree corresponding to the total duration time of audio
            svg.selectAll(".profilecircle").attr("transform", function(d) {
              return "rotate(" +  currentTime*360/audio_duration + ")";
            });
        });
        
    }
    //click to pause
    else{
        bgmPause();
        this.src = "../static/pictures/play.ico";

    }
});

data[data.length - 1].topicDuration = audio_duration - ParseTime(data[data.length - 1].startTime)
var sentenceTime = [],
    sentenceContent = [],
    sentenceSpeaker = [],
    topicDuration = [0],
    topicTime = [],
    topicName = [];
data.forEach(function(d,i) {
    d.topicDuration = +d.topicDuration;
    topicDuration.push(d.topicDuration);
    topicName.push(d.topicName);
    d.sentences.forEach(function(t){
        sentenceTime.push(ParseTime(t.sentenceTime));
        sentenceContent.push(t.sentenceContent);
        sentenceSpeaker.push(t.sentenceSpeaker);
    });
});
//topicTime is accumulate topic duration time
//an example of topicTime = [0, 280, 472, 570, 638, 808, 895]
topicDuration.reduce(function(a,b,i) { return topicTime[i] = a+b; },0);
console.log(topicDuration)
var width = $("#content").width(),
    height = $("#content").height(),
    radius = (Math.min(width, height) / 2),
    out_padding = radius/6,
    inner_padding = radius/2.5;

var color = d3.scale.category20();

var arc = d3.svg.arc()
    .outerRadius(radius - out_padding)
    .innerRadius(radius - inner_padding);
var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.topicDuration; });

// Define the div for the tooltip
var profile_tooltip = d3.select("body").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0)

var svg = d3.select("#content")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
        .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");


var circlesData = [{ r: -10+(inner_padding-out_padding)/2}];

var circleEnter = svg.selectAll(".profilecircle")
    .data(circlesData)
    .enter()
    .append("g")

var circle = circleEnter.append("circle")
    .attr("r", function(d){return d.r})
    .attr("cx",0)
    .attr("cy", function(d){return out_padding-radius-d.r} )
    .attr("class", "profilecircle"); 

var images = circleEnter.append("image")
    .attr("xlink:href",  JadePicturePath)
    .attr("x", function(d){return -d.r})
    .attr("y", function(d){return out_padding-radius-2*d.r})
    .attr("height",function(d){return 2*d.r} )
    .attr("width", function(d){return 2*d.r} )
    .attr("class", "profilecircle")
    .style("cursor","pointer")
    .on("mouseover", function(d){
        profile_tooltip
            .transition()
            .duration(200)      
            .style("opacity", .6);      
        profile_tooltip
            .html(images.attr('id') + "</a>")  
            .style("left", (d3.event.pageX + 50) + "px")     
            .style("top", (d3.event.pageY - 30) + "px") 
    })
    .on("mousemove", function(d){
        profile_tooltip
            .transition()
            .duration(200)      
            .style("opacity", .6);      
        profile_tooltip
            .html(images.attr('id') + "</a>")  
            .style("left", (d3.event.pageX + 50) + "px")     
            .style("top", (d3.event.pageY - 30) + "px") 
    })                     
    .on("mouseout", function(d) {       
        profile_tooltip
            .transition()        
            .duration(500)      
            .style("opacity", 0);   

    })
//Speaker Info
var speakers = svg.selectAll(".speakers")
    .data([{"sname":"Jade", "fullname":"Jade Harrell", "link":""},
        { "sname":"shawn", "fullname":"Shawn Stevenson", "link":""}
      ])
    .enter()
    .append("g")
    .attr("class", "speakers");
var speaker_box = speakers.append("image")
    .attr("xlink:href", function(d) { return "../static/pictures/" + d['sname'] + ".png"})
    .attr("x", function(d,i) { return radius+70; })
    .attr("y", function(d,i) { return i * 50-230; })
    .attr("width", "30px")
    .attr("height", "30px")
    .attr("id", function(d) { return d['sname']+"_image"; })
    .attr("class", "speaker_box");

var speaker_text = speakers.append("text")
    .text(function(d) { return d['fullname']; })
    .attr("x", function(d,i) { return radius+180; })
    .attr("y", function(d,i) { return i * 50-210; })
    .attr("text-anchor", "middle")
    .attr("font-size", "16px")
    .attr("id", function(d) { return d['sname']+"_text"; })
    .attr("class", "speaker_text");

        // mobile devices add play at middle
        if (typeof window.orientation !== 'undefined'){
            d3.selectAll("#playbutton").style("height","100px")
            d3.selectAll("#playbutton").style("margin-right","-20px")
            d3.selectAll("#playbutton").style("width","850px")
            d3.selectAll(".sentenceContent").style("font-size","35px")
            var centerPlayImage = svg.append("image")
            .attr("xlink:href",  "../static/pictures/play.ico")
            .attr("x", -radius/2)
            .attr("y", -radius/2)
            .attr("height", radius)
            .attr("width", radius)
            .attr("opacity", "0.1")
            .attr("class", "centerPlayPause");

            centerPlayImage.on("click",function(){
                if (bgm.paused){
                        bgmPlay();
                        $(this).attr("href","../static/pictures/pause.ico");
                        var audio_duration = document.getElementById("bgm").duration;
                        d3.timer(function() {
                            var currentTime = Math.floor(document.getElementById("bgm").currentTime);
                            //360 degree corresponding to the total duration time of audio
                            svg.selectAll(".profilecircle").attr("transform", function(d) {
                              return "rotate(" +  currentTime*360/audio_duration + ")";
                            });
                        });
                        
                    }
                    //click to pause
                    else{
                        bgmPause();
                        $(this).attr("href", "../static/pictures/play.ico");
                    }
            })
        }


//draw donut
var g = svg.selectAll(".arc")
    .data(pie(data))
    .enter().append("g")
    .attr("class", "arc");

g.append("path")
    .attr("d", arc)
    .style("cursor","pointer")
    .style("fill", function(d) { return color(d.data.topicName); });


//draw topic and drag
var group = svg.selectAll("draggroup").data(data).enter()
    .append("g")
    .attr("class", "topic_rects")

// var draggroup = group.call(drag);

g.on("click", function(d) {
        topicClickFunction(d.data)
    })

            //mobile
            if (typeof window.orientation !== 'undefined') {
                    var rect = group.append("rect")
                        .attr("x", function(d,i) { return i*140-radius+70; })
                        .attr("y", -radius - 1.5 * circlesData[0].r )
                        .attr("width", 150)
                        .attr("height", 50)
                        .attr("fill", function(d) { return color(d.topicName); })
                        .attr("class", "rect")
                        .attr("id", function(d) { return d.topicName.split(" ")[0]+'rect'; })
                        .attr("class", "draggroup")
                        .style("margin-left","20px")
                        .on("click", function(d){
                            topicClickFunction(d);
                        });
                    var rectText = group.append("text")
                        .text(function(d) { return d.topicName; })
                        .attr("text-anchor", "middle")
                        .attr("x", function(d,i) { return i*140-radius+140; })
                        .attr("y", -radius - 1.5 * circlesData[0].r + 30)
                        .attr("font-size", "15px")
                        .attr("fill", "black")
                        .style("margin-left","20px")
                        .attr("class", "text")
                        .attr("id", function(d) { return d.topicName.split(" ")[0]+'text'; })
                        .attr("class", "draggroup")
                        .on("click", function(d){
                            topicClickFunction(d);
                        });

                }
                //Web
                else{
                    var rect = group.append("rect")
                        .attr("x",  -radius-inner_padding-100)
                        .attr("y", function(d,i) { return i*60-radius+70; })
                        .attr("width", 180)
                        .attr("height", 50)
                        .attr("fill", function(d) { return color(d.topicName); })
                        .attr("class", "rect")
                        .attr("id", function(d) { return d.topicName.split(" ")[0]+'rect'; })
                        .attr("class", "draggroup")
                        .style("cursor","pointer")
                        .on("click", function(d){
                            topicClickFunction(d);
                        });
                    var rectText = group.append("text")
                        .text(function(d) { return d.topicName; })
                        .attr("text-anchor", "middle")
                        .attr("x", -radius-inner_padding-10)
                        .attr("y", function(d,i) { return i*60-radius+100; })
                        .attr("font-size", "15px")
                        .style("cursor","pointer")
                        .attr("fill", "black")
                        .style("margin-left","50px")
                        .attr("class", "text")
                        .attr("id", function(d) { return d.topicName.split(" ")[0]+'text'; })
                        .attr("class", "draggroup")
                        .on("click", function(d){
                            topicClickFunction(d);
                        });

                }
console.log(data)
            //draw inner circle
            var topicClickFunction = function(d){
                d3.selectAll("rect").attr("opacity","1");
                d3.selectAll("text").style("font-Weight","")
                svg.selectAll(".innercircle").remove();
                var time = ParseTime(d.startTime);
                document.getElementById("bgm").currentTime = time;
                console.log(audio_duration, time)
                svg.selectAll(".profilecircle").attr("transform", function(d) {
                  return "rotate(" +  time*360/audio_duration + ")";
                });

                //record all attributes
                var topicname_rect = d.topicName.split(" ")[0]+'rect';
                var topicname_text = d.topicName.split(" ")[0]+'text';
                var old_x_rect = d3.selectAll("#"+topicname_rect).attr("x")
                var old_y_rect = d3.selectAll("#"+topicname_rect).attr("y")
                var old_color_rect = d3.selectAll("#"+topicname_rect).attr("fill")
                var old_x_text = d3.selectAll("#"+topicname_text).attr("x")
                var old_y_text = d3.selectAll("#"+topicname_text).attr("y")
                var old_color_text = d3.selectAll("#"+topicname_rect).attr("fill")
                //.attr("display","none")

                d3.selectAll("#"+topicname_rect).transition().attr("x","0").attr("y","0").transition().delay(0).attr("x",old_x_rect).attr("y",old_y_rect).attr("opacity","0.2");
                
                d3.selectAll("#"+topicname_text).transition().attr("x","0").attr("y","0").transition().attr("x",old_x_text).attr("y",old_y_text).style("font-Weight","900");
                var keywordsContent = d.keywords
                var fill = d3.scale.category20();
                var keywordSizeScale = d3.scale.linear()
                    .domain([0, 0.3])
                    .range([1, 20]);
                var layout = d3.layout.cloud()
                    .size([500, 500])
                    .words(keywordsContent)
                    .padding(1)
                    .text(function(d) { return d.keyword; })
                    .rotate(0)
                    .fontSize(function(d) { return keywordSizeScale(d.keywordScore)*3; })
                    .on("end", draw)
                    .start();


                function draw(words) {
                  svg.selectAll("innercircle")
                      .data(keywordsContent)
                    .enter().append("text")
                      .style("font-size", function(d) { return keywordSizeScale(d.keywordScore)*3 + "px"; })
                      .style("font-family", "Impact")
                      .style("fill", function(d, i) { return fill(i); })
                      .attr("class", "innercircle")
                      .attr("text-anchor", "middle")
                      .attr("transform", function(d) {
                        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                      })
                      .text(function(d) { return d.keyword; });
                }
                // var innerCircleEnter = svg.selectAll("innercircle").data(keywordsContent)
                //     .enter()
                //     .append("g")
                //     .attr("class", "innercircles");

                // var circle_r = radius/3;
                // var innerCircle = innerCircleEnter.append("circle")
                //     .attr("r", radius/6)
                //     .attr("cx",function(d,i){return gen_x(i,circle_r)})
                //     .attr("cy", function(d,i){return gen_y(i,circle_r)})
                //     .attr("class", "innercircle")
                //     .attr("fill", old_color_rect)
                //     .attr("opacity",0)
                //     .transition()
                //     .duration(1300)
                //     .attr("opacity",0.8);

                // var innerText = innerCircleEnter.append("text")
                //     .text(function(d) { return d.keyword})
                //     .attr("text-anchor", "middle")
                //     .attr("x", function(d,i){return gen_x(i,circle_r)})
                //     .attr("y", function(d,i){return gen_y(i,circle_r)})
                //     .attr("class", "innercircle")
                //     .attr("fill", "black")
                //     .attr("opacity",0)
                //     .transition()
                //     .duration(1300)
                //     .attr("opacity",0.8);
                // if (typeof window.orientation !== 'undefined'){
                //     innerText.attr("font-size", "25px")
                // }else{
                //     innerText.attr("font-size", "14px")
                // }
            }
            //drag profile circle
            var time_percentage = 0
            $('.profilecircle').on('mousedown', function(){
                $('body')
                    .on('mousemove', function(event){
                            time_percentage = rotateAnnotationCropper($('#content'), event.pageX,event.pageY, $('.profilecircle'));
                    })
                    .on('mouseup', function(event){
                            var audio_duration = document.getElementById("bgm").duration;
                            document.getElementById("bgm").currentTime = time_percentage * audio_duration;
                            $('.profilecircle').css("transform","");
                    });

            });
            //touchscreen touch
            $('.profilecircle').bind('touchstart', function(){
                var time_percentage = 0;
                $('body')
                    .bind('touchmove', function(e){
                        time_percentage = rotateAnnotationCropper($('#content'), e.originalEvent.touches[0].pageX,e.originalEvent.touches[0].pageY, $('.profilecircle'));
                    })
                    .bind('touchend', function(e){
                        var audio_duration = document.getElementById("bgm").duration;
                        document.getElementById("bgm").currentTime = time_percentage * audio_duration;
                        svg.selectAll(".profilecircle").attr("transform", function(d) {
                            return "rotate(" +  time_percentage*360 + ")";
                        });
                        $('.profilecircle').css("transform","");
                    });                
            });
            //console.log(d3.selectAll(".topic_rects").eq(1))
            //Update by d3 timer control
            d3.timer(function() {
                var currentTime = Math.floor(document.getElementById("bgm").currentTime);
                var sentence_index = Search(sentenceTime,currentTime);
                var currentSpeaker = sentenceSpeaker[sentence_index];
                //update profile picture
                if (currentSpeaker != undefined){
                    images.attr("xlink:href",  "../static/pictures/"+currentSpeaker+".png")
                          .attr("id", currentSpeaker);
                    //update transcript
                    $(".sentenceContent").text(sentenceContent[sentence_index]);
                    
                    //update side speaker profiles
                    $(".speaker_box")
                        .attr("width", "30px")
                        .attr("height", "30px");
                    $(".speaker_text")
                        .css("font-weight", "")

                    $("#"+currentSpeaker + "_image")
                        .attr("width", "50px")
                        .attr("height", "50px");
                    $("#"+currentSpeaker + "_text")
                        .css("font-weight", "bold")
                    }
                
                
            });
//});

// d3.json("/data", callback);