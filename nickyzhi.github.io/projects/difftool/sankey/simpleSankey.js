// <!--
// A simple sankey diagram for linking same text from two datasets

// Qiyu
// --> 

function simpleSankey(dataset1,dataset2){
    

    var len1 = dataset1.length,
        len2 = dataset2.length;
    var dataset = dataset1.concat(dataset2);
    var margin = {top: 20, right:10, bottom:20,left:10},
        width = 560,
        height = 2000,
        recW = 60,
        recH = 80,
        recD = width/2;
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

    for (var i=0;i<len1;i++){
        for (var j=len2;j<len;j++){
            if (dataset[i] == dataset[j]){
                if(dataX[j]>(dataX[i]+recD/2)){
                    svg.append("line")
                    .attr("class","link")
                    .style("stroke-width", 3)
                    .attr("x1", (dataX[i]+recW))
                    .attr("y1", (dataY[i]+recH/2))
                    .attr("x2", (dataX[j]))
                    .attr("y2", (dataY[j]+recH/2));
                }
            }
        }
    };
}

