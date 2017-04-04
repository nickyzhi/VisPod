function update(index,speakers) {

  // DATA JOIN
  // Join new data with old elements, if any.
  var data = speakers[index];
  var picture = g.selectAll("profilecircle")
    .data(data);

  // UPDATE
  // Update old elements as needed.
  text.attr("class", "update");

  // ENTER
  // Create new elements as needed.
  //
  // ENTER + UPDATE
  // After merging the entered elements with the update selection,
  // apply operations to both.
  picture.enter().append("text")
      .attr("class", "enter")
      .attr("x", function(d, i) { return i * 32; })
      .attr("dy", ".35em")
    .merge(text)
      .text(function(d) { return d; });

  // EXIT
  // Remove old elements as needed.
  text.exit().remove();
}