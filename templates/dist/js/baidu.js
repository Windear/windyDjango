export default {
  //百度统计代码
  baidu(web) {
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?f98ad40b514bec35bf76a940f1a5e468";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
    console.log("当前页面："+ web)
  }
 
}
