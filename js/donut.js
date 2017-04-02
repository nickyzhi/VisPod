function donutChart() {

    // All options that should be accessible to caller
    var width = 500;
    var height = 300;
    var radius = Math.min(width, height) / 2;

    var updateWidth;
    var updateHeight;
    //var updateFillColor;
    var updateData;
    function chart(selection){

        selection.each(function () {
          var color = d3.scale.category20();

          var pie = d3.layout.pie()
            .value(function(d) { return d.apples; })
            .sort(null);

          var arc = d3.svg.arc()
            .innerRadius(radius - 100)
            .outerRadius(radius - 20);

          var svg = d3.select("body").append("svg")
              .attr("width", width)
              .attr("height", height)
              .append("g")
              .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

        
            // update functions
            updateWidth = function() {
                widthScale = width / maxValue;
                bars.transition().duration(1000).attr('width', function(d) { return d * widthScale; });
                svg.transition().duration(1000).attr('width', width);
            };

            updateHeight = function() {
                barSpacing = height / data.length;
                barHeight = barSpacing - barPadding;
                bars.transition().duration(1000).attr('y', function(d, i) { return i * barSpacing; })
                    .attr('height', barHeight);
                svg.transition().duration(1000).attr('height', height);

            };

            updateFillColor = function() {
                svg.transition().duration(1000).style('fill', fillColor);
            };

            updateData = function() {
            }

        });
    }

    chart.width = function(value) {
        if (!arguments.length) return width;
        width = value;
        if (typeof updateWidth === 'function') updateWidth();
        return chart;
    };

    chart.height = function(value) {
        if (!arguments.length) return height;
        height = value;
        if (typeof updateHeight === 'function') updateHeight();
        return chart;
    };

    chart.data = function(value) {
        if (!arguments.length) return data;
        data = value;
        if (typeof updateData === 'function') updateData();
        return chart;
    };

    return chart;
}
