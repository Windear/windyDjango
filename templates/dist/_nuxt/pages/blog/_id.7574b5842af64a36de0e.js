webpackJsonp([19],{"5X1i":function(t,i,a){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var e=a("88pg"),o=a("RU9Z"),n=!1;var s=function(t){n||a("ExY/")},r=a("C7Lr")(e.a,o.a,!1,s,null,null);r.options.__file="pages/blog/_id.vue",i.default=r.exports},"7BAL":function(t,i,a){"use strict";i.a={baidu:function(t){!function(){var t=document.createElement("script");t.src="https://hm.baidu.com/hm.js?f98ad40b514bec35bf76a940f1a5e468";var i=document.getElementsByTagName("script")[0];i.parentNode.insertBefore(t,i)}(),console.log("当前页面："+t)}}},"88pg":function(t,i,a){"use strict";var e=a("7BAL"),o=a("NYSn");i.a={data:function(){return{ip:this.$store.state.ip,projectId:this.$route.query.projectId,showPayBox:!1,blogData:"",articleTag:[],articlePicture:"",articleCate:"",articleTitle:"文章详情",articleOriginal:"",dialogVisible:!1,payMe:!1,scrollType:!1}},head:function(){return{title:this.articleTitle,meta:[{hid:"有爱设计",name:"keywords",content:"有爱设计,武汉UI设计,武汉程序开发,APP开发,UI设计,UI素材,Sketch素材,PSD素材,XD素材,设计师学程序开发"},{hid:"有爱设计",name:"description",content:this.blogData.articleIntroduction},{hid:"有爱设计",name:"description",content:"欢迎来到windy的设计小站，这里有各种各样的素材，这里接各种各样的APP、网站设计外包。这里可以找到从初学者到设计师的心得体会教程，欢迎来我的家里寻找吧。"}]}},created:function(){},props:{},computed:{bodyWidth:function(){return this.$store.getters.getBodyWidth}},mounted:function(){var t=this;o.a.changyan(),this.$store.commit("updateNavBarActive","4"),document.documentElement.scrollTop=0,this.getBlogDetails(),this.getBlogLooked(),this.$store.commit("updateFooterWidth",0),e.a.baidu("工具详情"),this.$nextTick(function(){window.addEventListener("scroll",t.onScroll)})},methods:{onScroll:function(){var t=document.documentElement.scrollTop||document.body.scrollTop;this.scrollType=t>=80},changyan:function(){window.changyan.api.config({appid:"cyt3crepq",conf:"prod_a13b2e3f57b739f379a9d121e340340d"})},getBlogDetails:function(){var t=this;if(void 0===this.projectId){var i=String(window.location.href.split("/").pop());this.projectId=i}var a=this.projectId;this.$store.dispatch("getBlogDetails",a).then(function(i){var a=i.data;"err"!=a.state&&200===i.status?(t.blogData=a,t.articleTitle=a.articleTitle,t.articleTag=a.articleTag.split(","),t.articleCate=a.articleCate[1],t.articlePicture=t.ip+"/media/"+a.articlePicture,t.articleOriginal=a.articleOriginal[1]):alert("网络错误")}).catch(function(t){console.error(t)})},getBlogLooked:function(){if(void 0===this.projectId){var t=String(window.location.href.split("/").pop());this.projectId=t}var i=this.projectId;this.$store.dispatch("getBlogLooked",i).then(function(t){t.data}).catch(function(t){console.error(t)})},handleClose:function(t){this.$confirm("确认关闭？").then(function(i){t()}).catch(function(t){})},onCopy:function(t){this.clipboardVal=t},onError:function(t){this.clipboardVal="err"},searchTag:function(t){this.$store.commit("updateSearchVal",t),this.$router.push({path:"/search?q="+t})}},components:{}}},"ExY/":function(t,i,a){var e=a("jZVG");"string"==typeof e&&(e=[[t.i,e,""]]),e.locals&&(t.exports=e.locals);a("FIqI")("549dce9e",e,!1,{sourceMap:!1})},NYSn:function(t,i,a){"use strict";i.a={changyan:function(){!function(){var t="prod_a13b2e3f57b739f379a9d121e340340d";(window.innerWidth||document.documentElement.clientWidth)<960?function(t,i){var a=document.getElementsByTagName("head")[0]||document.head||document.documentElement,e=document.createElement("script");e.setAttribute("type","text/javascript"),e.setAttribute("charset","UTF-8"),e.setAttribute("src",t),"function"==typeof i&&(window.attachEvent?e.onreadystatechange=function(){var t=e.readyState;"loaded"!==t&&"complete"!==t||(e.onreadystatechange=null,i())}:e.onload=i),a.appendChild(e)}("https://www.cgtblog.com/skin/default/js/changyan/changyan.js",function(){window.changyan.api.config({appid:"cyt3crepq",conf:t})}):function(t,i){var a=document.getElementsByTagName("head")[0]||document.head||document.documentElement,e=document.createElement("script");e.setAttribute("type","text/javascript"),e.setAttribute("charset","UTF-8"),e.setAttribute("src",t),"function"==typeof i&&(window.attachEvent?e.onreadystatechange=function(){var t=e.readyState;"loaded"!==t&&"complete"!==t||(e.onreadystatechange=null,i())}:e.onload=i),a.appendChild(e)}("https://www.cgtblog.com/skin/default/js/changyan/changyan.js",function(){window.changyan.api.config({appid:"cyt3crepq",conf:t})})}()}}},RU9Z:function(t,i,a){"use strict";var e=function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"homeBody"},[e("div",{staticClass:"container"},[e("div",{staticClass:"left"},[e("div",{staticClass:"image-box-left"},[e("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.articlePicture,expression:"articlePicture"}],attrs:{alt:t.articleTitle}})]),e("div",{staticClass:"content"},[e("div",{staticClass:"title-box"},[e("h3",[t._v(t._s(t.articleTitle))])]),e("div",{staticClass:"introduction"},[t._v(t._s(t.blogData.articleIntroduction))]),e("div",{staticClass:"details",domProps:{innerHTML:t._s(t.blogData.articleContent)}})]),e("div",{staticClass:"comment"},[e("div",{attrs:{id:"SOHUCS",sid:t.blogData.sid}})])]),e("div",{staticClass:"right"},[e("div",{staticClass:"image-box",style:t.scrollType?"position: fixed;top:80px;":""},[e("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.articlePicture,expression:"articlePicture"}],attrs:{alt:t.articleTitle}})]),e("div",{staticClass:"download-box",style:t.scrollType?"position: fixed;top:340px;":""},[e("a",{staticClass:"pay-btn download-box-btn",attrs:{href:"javascript:;"},on:{click:function(i){t.payMe=!0}}},[t._v("打赏站长")])]),e("div",{staticClass:"essential",style:t.scrollType?"position: fixed;top:444px;":""},[e("p",{staticClass:"box-title"},[t._v("基本信息")]),e("div",{staticClass:"box-content"},[e("span",{staticClass:"span-left"},[t._v("作者")]),e("span",{staticClass:"span-right"},[t._v(t._s(t.blogData.articleAuthor))])]),e("div",{staticClass:"box-content"},[e("span",{staticClass:"span-left"},[t._v("类别")]),e("span",{staticClass:"span-right"},[t._v(t._s(t.articleCate))])]),e("div",{staticClass:"box-content"},[e("span",{staticClass:"span-left"},[t._v("发布时间")]),e("span",{staticClass:"span-right"},[t._v(t._s(t.blogData.createTime))])]),e("div",{staticClass:"box-content"},[e("span",{staticClass:"span-left"},[t._v("是否原创")]),e("span",{staticClass:"span-right"},[t._v(t._s(t.articleOriginal))])])]),e("div",{staticClass:"tag",style:t.scrollType?"position: fixed;top:649px;":""},[e("p",{staticClass:"box-title"},[t._v("标签")]),t._l(t.articleTag,function(i){return e("a",{key:i.id,staticClass:"tag-list",attrs:{href:"javascript:;"},on:{click:function(a){return t.searchTag(i)}}},[t._v(t._s(i))])})],2)])]),e("el-dialog",{attrs:{title:"打赏站长","custom-class":"pay-dialog",visible:t.payMe,width:"75%",center:""},on:{"update:visible":function(i){t.payMe=i}}},[e("div",{staticStyle:{"text-align":"center"}},[e("img",{staticStyle:{"max-width":"400px",width:"100%"},attrs:{src:a("SCK0"),alt:""}}),e("br"),e("br"),e("br"),e("span",[t._v("打赏将减轻 5windy.com 服务器与加速流量负担，更好的提供优秀资源")])])])],1)};e._withStripped=!0;var o={render:e,staticRenderFns:[]};i.a=o},SCK0:function(t,i,a){t.exports=a.p+"img/payMoney.07a0c02.png"},jZVG:function(t,i,a){var e=a("L4zZ");(t.exports=a("UTlt")(!1)).push([t.i,"#feedAv{margin-top:-250px!important;-webkit-transform:scale(0);transform:scale(0)}#MZAD_POP_PLACEHOLDER,#pop_ad{display:none!important}.homeBody{background:#f3f4f5;padding-top:20px;padding-bottom:20px}.container{width:1200px;overflow:hidden;margin:0 auto}.left{width:900px;float:left}.image-box-left{display:none}.image-box-left img{width:100%}.content{background:#fff;padding:20px;border-radius:4px}.title-box{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.title-box img{width:80px;height:80px}.title-box h3{font-size:24px;width:760px;font-weight:400}.introduction{background:#eff2f7;padding:20px;color:#5e6d82;font-size:14px;line-height:24px;margin-top:20px}.details{margin-top:40px}.details p{max-width:840px}.details img{max-width:720px}.details a:active,.details a:hover,.details a:link,.details a:visited{color:#0089ff!important}.problem{background:#fff;padding:20px;border-radius:4px;margin-top:20px}.problem-title{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.problem-line{width:4px;height:20px;border-radius:2px;background:#0089ff;display:inline-block;margin-right:10px}.problem-content ol{color:#475669;-webkit-padding-start:20px;padding-inline-start:20px;font-size:14px;margin-top:20px}.problem-content li{margin-bottom:10px}.problem-content code{color:#ff7676}.problem-content a{color:#007ce7}.tag-img{width:16px;height:16px;min-width:16px;display:inline-block;margin-left:5px}.mac{background-image:url("+e(a("qcqO"))+")}.microsoft{background-image:url("+e(a("m5Vw"))+")}.comment{padding:20px;background:#fff;margin-top:20px}.right{width:280px;float:right}.image-box{background:#fff;width:280px;padding:20px 20px 10px;border-radius:4px;margin-bottom:20px}.image-box img{width:100%;border-radius:4px}.download-box{background:#fff;width:280px;padding:20px 20px 10px;border-radius:4px;margin-bottom:20px}.download-box-btn{display:inline-block;width:240px;height:44px;color:#fff!important;font-size:16px;font-weight:400;border-radius:4px;margin-bottom:10px;text-align:center;line-height:44px}.download-btn{background:#0089ff}.download-btn,.download-btn:hover{-webkit-transition:all .3s ease-out 0s;transition:all .3s ease-out 0s}.download-btn:hover{background:#007ce7}.pay-btn{background:#ff7676}.pay-btn,.pay-btn:hover{-webkit-transition:all .3s ease-out 0s;transition:all .3s ease-out 0s}.pay-btn:hover{background:#f84f4f}.essential{background:#fff;width:280px;padding:20px 20px 10px;border-radius:4px;margin-bottom:20px}.box-title{font-size:18px;color:#1f2d3d;margin-bottom:10px}.box-content{margin:10px 0;font-size:14px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.span-left{color:#8492a6}.span-right{color:#475669}.tag{background:#fff;width:280px;padding:20px 20px 10px;margin-bottom:20px}.tag,.tag-list{border-radius:4px}.tag-list{display:inline-block;height:32px;background:#f6f9fa;color:#95a5a6!important;padding:0 12px;margin:5px 10px 5px 0;font-size:14px;line-height:32px}.pay-dialog{max-width:500px}@media screen and (max-width:760px){.container{width:100%}.content{border-radius:0}.image-box-left{background:#fff;width:100%;padding:20px 20px 10px;display:inline-block}.left{border-radius:0}.left,.right{width:100%}.image-box{width:100%;display:none}.download-box{width:100%;position:static!important}.download-box-btn{width:100%}.title-box img{min-width:80px;width:80px;height:80px}.essential,.tag{background:#fff;width:100%;border-radius:0;position:static!important}.details,.details p{width:100%}.details img,.details ol,.details ul{max-width:100%}}",""])},m5Vw:function(t,i,a){t.exports=a.p+"img/wr_icon.763e8a8.svg"},qcqO:function(t,i,a){t.exports=a.p+"img/mac_icon2.d8a718e.svg"}});