export default {
    changyan() {
        (function () {
            var appid = 'cyt3crepq';
            var conf = 'prod_a13b2e3f57b739f379a9d121e340340d';
            var width = window.innerWidth || document.documentElement.clientWidth;
            if (width < 960) {
                var loadJs = function (d, a) { var c = document.getElementsByTagName("head")[0] || document.head || document.documentElement; var b = document.createElement("script"); b.setAttribute("type", "text/javascript"); b.setAttribute("charset", "UTF-8"); b.setAttribute("src", d); if (typeof a === "function") { if (window.attachEvent) { b.onreadystatechange = function () { var e = b.readyState; if (e === "loaded" || e === "complete") { b.onreadystatechange = null; a() } } } else { b.onload = a } } c.appendChild(b) }; loadJs("https://www.cgtblog.com/skin/default/js/changyan/changyan.js", function () { window.changyan.api.config({ appid: appid, conf: conf }) });
            } else {
                var loadJs = function (d, a) { var c = document.getElementsByTagName("head")[0] || document.head || document.documentElement; var b = document.createElement("script"); b.setAttribute("type", "text/javascript"); b.setAttribute("charset", "UTF-8"); b.setAttribute("src", d); if (typeof a === "function") { if (window.attachEvent) { b.onreadystatechange = function () { var e = b.readyState; if (e === "loaded" || e === "complete") { b.onreadystatechange = null; a() } } } else { b.onload = a } } c.appendChild(b) }; loadJs("https://www.cgtblog.com/skin/default/js/changyan/changyan.js", function () { window.changyan.api.config({ appid: appid, conf: conf }) });
            }
        })();
    }
}

// https://changyan.sohu.com/upload/changyan.js