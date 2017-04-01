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
                        .outerRadius(radius - 80)
                        .innerRadius(radius - 80);
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
