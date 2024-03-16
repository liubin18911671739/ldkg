$(document).ready(function () {
  // 提交搜索表单时触发
  $("#search-form").submit(function (event) {
    event.preventDefault();
    var query = $("#query").val();

    // 发送AJAX请求到后端进行搜索
    $.ajax({
      url: "/search",
      method: "POST",
      data: { query: query },
      dataType: "json",
      beforeSend: function () {
        // 显示加载中的提示
        $("#search-results").html(
          '<div class="loading">正在搜索,请稍候...</div>'
        );
      },
      success: function (response) {
        if (response.error) {
          // 显示错误消息
          $("#search-results").html(
            '<div class="error">' + response.error + "</div>"
          );
        } else {
          // 显示搜索结果
          var results = response.results;
          var html = "";
          if (results.length > 0) {
            html += "<ul>";
            results.forEach(function (result) {
              html += "<li>";
              html += "<h3>" + result.title + "</h3>";
              html += "<p>" + result.snippet + "</p>";
              html +=
                '<a href="' + result.url + '" target="_blank">查看详情</a>';
              html += "</li>";
            });
            html += "</ul>";
          } else {
            html += '<div class="no-results">没有找到相关结果。</div>';
          }
          $("#search-results").html(html);
        }
      },
      error: function () {
        // 显示错误消息
        $("#search-results").html(
          '<div class="error">搜索时发生错误,请稍后重试。</div>'
        );
      },
    });
  });

  // 点击搜索结果中的链接时触发
  $("#search-results").on("click", "a", function (event) {
    event.preventDefault();
    var url = $(this).attr("href");

    // 发送AJAX请求获取链接的详细内容
    $.ajax({
      url: "/details",
      method: "POST",
      data: { url: url },
      dataType: "json",
      beforeSend: function () {
        // 显示加载中的提示
        $("#search-details").html(
          '<div class="loading">正在加载,请稍候...</div>'
        );
      },
      success: function (response) {
        if (response.error) {
          // 显示错误消息
          $("#search-details").html(
            '<div class="error">' + response.error + "</div>"
          );
        } else {
          // 显示链接的详细内容
          var details = response.details;
          var html = "";
          html += "<h2>" + details.title + "</h2>";
          html += "<p>" + details.content + "</p>";
          $("#search-details").html(html);
        }
      },
      error: function () {
        // 显示错误消息
        $("#search-details").html(
          '<div class="error">加载详细内容时发生错误,请稍后重试。</div>'
        );
      },
    });
  });
});
