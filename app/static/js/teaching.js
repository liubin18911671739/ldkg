// 创建SVG元素
var svg = d3
  .select("#teaching-graph")
  .append("svg")
  .attr("width", "100%")
  .attr("height", "100%");

// 定义力导向图的参数
var simulation = d3
  .forceSimulation()
  .force(
    "link",
    d3.forceLink().id(function (d) {
      return d.id;
    })
  )
  .force("charge", d3.forceManyBody())
  .force(
    "center",
    d3.forceCenter(
      svg.node().getBoundingClientRect().width / 2,
      svg.node().getBoundingClientRect().height / 2
    )
  );

// 处理数据
var graph = {
  nodes: [],
  links: [],
};

teachingData.forEach(function (data) {
  var course = data.c;
  var instructor = data.i;

  // 添加节点
  if (
    !graph.nodes.some(function (node) {
      return node.id === course.id;
    })
  ) {
    graph.nodes.push({ id: course.id, label: course.name, type: "course" });
  }
  if (
    !graph.nodes.some(function (node) {
      return node.id === instructor.id;
    })
  ) {
    graph.nodes.push({
      id: instructor.id,
      label: instructor.name,
      type: "instructor",
    });
  }

  // 添加边
  graph.links.push({ source: course.id, target: instructor.id });
});

// 更新力导向图
var link = svg
  .append("g")
  .attr("class", "links")
  .selectAll("line")
  .data(graph.links)
  .enter()
  .append("line")
  .attr("stroke", "#999")
  .attr("stroke-width", 1);

var node = svg
  .append("g")
  .attr("class", "nodes")
  .selectAll("circle")
  .data(graph.nodes)
  .enter()
  .append("circle")
  .attr("r", 5)
  .attr("fill", function (d) {
    return d.type === "course" ? "#3498db" : "#e74c3c";
  })
  .call(
    d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended)
  );

var label = svg
  .append("g")
  .attr("class", "labels")
  .selectAll("text")
  .data(graph.nodes)
  .enter()
  .append("text")
  .text(function (d) {
    return d.label;
  })
  .attr("font-size", "12px")
  .attr("dx", 8)
  .attr("dy", 3);

simulation.nodes(graph.nodes).on("tick", ticked);

simulation.force("link").links(graph.links);

function ticked() {
  link
    .attr("x1", function (d) {
      return d.source.x;
    })
    .attr("y1", function (d) {
      return d.source.y;
    })
    .attr("x2", function (d) {
      return d.target.x;
    })
    .attr("y2", function (d) {
      return d.target.y;
    });

  node
    .attr("cx", function (d) {
      return d.x;
    })
    .attr("cy", function (d) {
      return d.y;
    });

  label
    .attr("x", function (d) {
      return d.x;
    })
    .attr("y", function (d) {
      return d.y;
    });
}

function dragstarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragended(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
