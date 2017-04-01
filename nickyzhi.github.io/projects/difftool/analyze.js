$(document).ready(function() {
        $('.menu').dropit();
    });

//draw pie chart
function piechart(dataset){
        var width = 560,
            height = 280,
            margin = 17,
            radius = Math.min(width, height-margin) / 2;
        var arc = d3.svg.arc()
                    .outerRadius(radius - 10)
                     .innerRadius(0);
        var labelArc = d3.svg.arc()
                        .outerRadius(radius - 60)
                        .innerRadius(radius - 60);
        var pie = d3.layout.pie()
                    .sort(null)
                    .value(function(d) { return d.percentage; });
        var color = d3.scale.category10();
        var svg = d3.select("#pie").append("svg")
                    .attr("width", width)
                    .attr("height", height)
                  .append("g")
                    .attr("transform", "translate(" + width/2 + "," + (height / 2-margin) + ")");
        

        var g = svg.selectAll('.arc')
                      .data(pie(dataset))
                      .enter()
                      .append('g')
                      .attr("class", "arc");

            g.append('path')
                      .attr('d', arc)
                      .attr('fill', function(d, i) { 
                        return color(d.data.label);
                      });

            g.append("text")
                .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
                .attr("dy", ".35em")
                .text(function(d) { return d.data.label; });

            g.append("text")
                .attr("transform", "translate(" + 0 + "," + (height/2+margin/2) + ")")
                .style("text-anchor", "middle")
                .text("Machine output and gold result difference");
}

String.prototype.width = function(font) {
  var f = font || '12px arial',
      o = $('<div>' + this + '</div>')
            .css({'position': 'absolute', 'float': 'left', 'white-space': 'nowrap', 'visibility': 'hidden', 'font': f})
            .appendTo($('body')),
      w = o.width();

  o.remove();

  return w;
}

Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};
// <!--
// A simple sankey diagram for linking same text from two datasets

// Qiyu
// --> 

function simpleSankey(dataset1,dataset2){
    

    var len1 = dataset1.length,
        len2 = dataset2.length;
    var maxlen = 0;
    if (len1>len2) maxlen = len1;
    else maxlen = len2;
    var dataset = dataset1.concat(dataset2);
    var lgth = 0;
    var longest;

    for(var i=0; i < dataset.length; i++){
        if(dataset[i].length > lgth){
            var lgth = dataset[i].length;
            longest = dataset[i];
        }      
    }
    console.log(longest.width());
    if(longest.width()<60){
        recW = 60;
    }
    else recW = longest.width()+1;

    var margin = {top: 20, right:10, bottom:20,left:10},
        width = 560,
        recH = 80,
        recD = width/2;

    var height = (recH+10)*maxlen+100;
    var color = d3.scale.category20();

    var svg = d3.select("#sankey").append("svg")
            .attr("width", width)
            .attr("height", height)
        .append("g")
            .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");

    var len = dataset.length;
    var dataX = new Array();
    var dataY = new Array();

    for (var i=0; i < len;i++){
        if (i<len1){
            dataY[i] = 90*i+margin.top;
            dataX[i] = width/4-recW/2;
        }
        else{
            dataY[i] = 90*(i-len1)+margin.top;
            dataX[i] = 3*width/4-recW/2;
        }
    };
    
    

    var node = svg.append("g").selectAll(".node")
                .data(dataset)
                .enter()
                .append("g")
                .attr("class", "node")
                .attr("transform", function(d,i){ 
                    return "translate(" + dataX[i] + "," + dataY[i] + ")"
                });

        node.append("rect")
                .attr("height", recH)
                .attr("width", recW)
                .attr("class", "node")
                .style("fill", function(d) { 
                    return d.color = color(d); })
                .style("stroke", function(d) { 
                    return d3.rgb(d.color).darker(2); });
    
    var label = svg.selectAll("text")
               .data(dataset)
               .enter()
               .append("text")
               .text(function(d) {
                    return d;
               })
               .attr("text-anchor", "middle")
               .attr("x", function(d, i) {
                    return (dataX[i]+recW/2);
               })
               .attr("y", function(d,i) {
                    return (dataY[i]+recH/2);
               });
    var lineIndex = new Array(2);
    for (i=0; i <2; i++) lineIndex[i]=new Array;          
    for (var i=0;i<len1;i++){
        lineIndex[0].push(i);
    }
    for (var i=0;i<len2;i++){
        lineIndex[1].push(i);
    }
    console.log(lineIndex);
    for (var i=0;i<len1;i++){
        for (var j=len1;j<len;j++){
            if (dataset[i] == dataset[j]){
                console.log(lineIndex[1]);
                console.log(j);
                if (lineIndex[0].indexOf(i)!=-1 && lineIndex[1].indexOf(j-len1)!=-1){
                    if(dataX[j]>(dataX[i]+recD/2)){
                        svg.append("line")
                        .attr("class","link")
                        .style("stroke-width", 3)
                        .attr("x1", (dataX[i]+recW))
                        .attr("y1", (dataY[i]+recH/2))
                        .attr("x2", (dataX[j]))
                        .attr("y2", (dataY[j]+recH/2));
                    }
                    lineIndex[0].remove(i);
                    lineIndex[1].remove(j-len1);
                    console.log(lineIndex);
                }
            }
        }
    };
}



function findMaxSubStr(s1,s2){ 
    var str= "",
        L1=s1.length,
        L2=s2.length; 
    
    if (L1>L2){ 
        var s3=s1;
        s1=s2;
        s2=s3;
        s3 = null;
        L1=s2.length;
        L2=s1.length;
    }
    
    
    for (var i=L1; i > 0; i--) {
        for (var j= 0; j <= L2 - i && j < L1; j++){ 
            str = s1.substr(j, i);
            if (s2.indexOf(str) >= 0) {
                return str; 
            }
        } 
    }
    
    return ""; 
}

function diff (s1,s2){
    var a = s1.split(" ");
    var b = s2.split(" ");
    var aLen = a.length ;
    var bLen = b.length ;
    PlusResult = [];
    MinusResult = [];
    for (var i = 0 ; i < bLen ; i ++){
        if (a.indexOf (b[i ]) == -1 ){
            MinusResult .push (b[i ]);
         }
    }
    for (var i = 0 ; i < aLen ; i ++){
        if (b.indexOf (a[i ]) == -1 ){
            PlusResult .push (a[i ]);
         }
    }
    return [PlusResult,MinusResult];
}

function levenshtein(s1, s2) {
    // init
    var d = [],
        m = s1.length,
        n = s2.length,
        i, j,cost;
    for (i = 0; i <= m; i++) {
        d[i] = [];
        d[i][0] = i;
    }
    for (j = 0; j <= n; j++) {
        d[0][j] = j;
    }
    
    for (j = 1; j <= n; j++) {
        for (i = 1; i <= m; i++) {
            if (s1[i] === s2[j]) {
                cost = 0;
            } 
            else {
                cost =1;
            }
            d[i][j] = Math.min(
                    d[i - 1][j] + 1, // a deletion
                    d[i][j - 1] + 1, // an insertion
                    d[i - 1][j - 1] + cost // a substitution
                )
        }
    }
    
    return d[m][n];
}

function similarity(a, b) {
    var s1 = a.split(" ");
    var s2 = b.split(" ");
    return 1 - levenshtein(s1, s2) / Math.max(s1.length, s2.length);
};