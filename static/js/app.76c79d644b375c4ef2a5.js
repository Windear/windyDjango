webpackJsonp([1],{"/p5v":function(t,i){},"2pwM":function(t,i){},"3fOF":function(t,i){},K6VE:function(t,i){},NHnr:function(t,i,e){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var a=e("MVMM"),s=(e("o/kp"),{data:function(){return{scrollType:!1}},props:{bodyWidth:{type:Number,default:1440}},computed:{active:function(){return this.$store.getters.getNavBarActive}},wacth:{},mounted:function(){var t=this;this.$store.commit("updateNavBarActive","1"),this.$nextTick(function(){window.addEventListener("scroll",t.onScroll)})},methods:{openHome:function(){this.$store.commit("updateNavBarActive","1"),this.$router.push({path:"/"})},openProject:function(){this.$store.commit("updateNavBarActive","2")},onScroll:function(){var t=document.documentElement.scrollTop||document.body.scrollTop;this.scrollType=t>=80},postWeChatCenterDialogVisibleTrue:function(){this.$store.commit("updateCenterDialogVisible",!0),this.$store.commit("updatemodalStatus","wechat")},qqIM:function(){window.open("http://wpa.qq.com/msgrd?v=3&uin=197299278&site=qq&menu=yes","_blank","height=502, width=644,toolbar=no,scrollbars=no,menubar=no,status=no")},sendEmail:function(){window.open("mailto:197299278@qq.com","_blank","height=502, width=644,toolbar=no,scrollbars=no,menubar=no,status=no")}},components:{}}),n={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"nav",class:{navBarShadow:t.scrollType}},[e("div",{staticClass:"container",class:{containerLitter:t.scrollType}},[e("div",{staticClass:"nav-left-box"},[e("a",{staticClass:"logo"}),t._v(" "),e("ul",{staticClass:"text-link"},[e("a",{attrs:{href:"javascript:;"},on:{click:t.openHome}},[e("li",{style:1==t.active?"color:#fff;":""},[t._v("首页")])]),t._v(" "),e("a",{attrs:{href:"javascript:;"},on:{click:t.openProject}},[e("li",{style:2==t.active?"color:#fff;":""},[t._v("项目")])]),t._v(" "),e("a",{attrs:{href:"javascript:;"}},[e("li",{style:3==t.active?"color:#fff;":""},[t._v("素材")])])])]),t._v(" "),e("div",{staticClass:"nav-right-box"},[e("a",{attrs:{href:"javascript:;"},on:{click:t.postWeChatCenterDialogVisibleTrue}},[e("div",{staticClass:"wechat chat"})]),t._v(" "),e("a",{attrs:{href:"javascript:;"},on:{click:t.qqIM}},[e("div",{staticClass:"qq chat"})]),t._v(" "),e("a",{attrs:{href:"javascript:;"},on:{click:t.sendEmail}},[e("div",{staticClass:"email chat"})])])])])},staticRenderFns:[]};var o=e("Z0/y")(s,n,!1,function(t){e("ghgw")},"data-v-22638c73",null).exports,c={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"footer"},[e("div",{staticClass:"linkBox"},[e("div",{staticClass:"link"},[e("div",{staticClass:"linkTitle"},[t._v("实用网站")]),t._v(" "),e("div",{staticClass:"linkText"},[e("a",{attrs:{href:"http://www.iconfont.cn/",target:"view_window"}},[t._v("Iconfont-阿里巴巴矢量图标")]),t._v(" "),e("a",{attrs:{href:"http://www.huaban.cn/",target:"view_window"}},[t._v("花瓣-设计师灵感来源")]),t._v(" "),e("a",{attrs:{href:"http://www.niudana.com/",target:"view_window"}},[t._v("牛大拿-设计师导航网站")]),t._v(" "),e("a",{attrs:{href:"http://www.chongbuluo.com/",target:"view_window"}},[t._v("虫部落-让搜索更简单")]),t._v(" "),e("a",{attrs:{href:"http://www.ui.cn/",target:"view_window"}},[t._v("UI中国")]),t._v(" "),e("a",{attrs:{href:"http://xclient.info/",target:"view_window"}},[t._v("MAC精品应用免费下载")]),t._v(" "),e("a",{attrs:{href:"http://www.zcool.com.cn/",target:"view_window"}},[t._v("站酷")])])]),t._v(" "),e("div",{staticClass:"link"},[e("div",{staticClass:"linkTitle"},[t._v("友情链接")]),t._v(" "),e("div",{staticClass:"linkText"},[e("a",{attrs:{href:"http://5windy.com/",target:"view_window"}},[t._v("有爱设计")]),t._v(" "),e("a",{attrs:{href:"http://5windy.com:8080/",target:"view_window"}},[t._v("有爱设计微信企业号推送助手")])])]),t._v(" "),e("div",{staticClass:"line"}),t._v(" "),e("div",{staticClass:"copyright"},[e("div",[t._v("Copyright   ©   2018 ~ 2023 有爱设计 鄂ICP备15003372号 By Windy.")]),t._v(" "),e("a",{staticStyle:{color:"#475669"},attrs:{href:"/design/list/1"}},[t._v("后台管理")])])])])}]};var l=e("Z0/y")({data:function(){return{}},props:{},wacth:{},mounted:function(){},methods:{},components:{}},c,!1,function(t){e("yULH")},"data-v-0647a468",null).exports,r={data:function(){return{scrollTop:document.body.scrollTop}},computed:{},mounted:function(){window.addEventListener("scroll",this.handleScroll)},wacth:{},methods:{returnTop:function(){document.documentElement.scrollTop=0},handleScroll:function(){var t=window.pageYOffset||document.documentElement.scrollTop||document.body.scrollTop;this.scrollTop=t},destroyed:function(){window.removeEventListener("scroll",this.handleScroll)},postWeChatCenterDialogVisibleTrue:function(){this.$store.commit("updateCenterDialogVisible",!0),this.$store.commit("updatemodalStatus","wechat")},qqIM:function(){window.open("http://wpa.qq.com/msgrd?v=3&uin=197299278&site=qq&menu=yes","_blank","height=502, width=644,toolbar=no,scrollbars=no,menubar=no,status=no")},sendEmail:function(){window.open("mailto:197299278@qq.com","_blank","height=502, width=644,toolbar=no,scrollbars=no,menubar=no,status=no")}}},d={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"btnBox"},[e("div",{directives:[{name:"show",rawName:"v-show",value:t.scrollTop>=60,expression:"scrollTop >= 60"}],staticClass:"returnTop box",on:{click:t.returnTop}},[e("i",{staticClass:"el-icon-arrow-up"})]),t._v(" "),e("div",{staticClass:"box"}),t._v(" "),e("div",{staticClass:"weChat box",on:{click:t.postWeChatCenterDialogVisibleTrue}},[e("span",{staticClass:"wechat-icon"})]),t._v(" "),e("div",{staticClass:"qq box",on:{click:t.qqIM}},[e("span",{staticClass:"qq-icon"})]),t._v(" "),e("div",{staticClass:"email box",on:{click:t.sendEmail}},[e("i",{staticClass:"el-icon-message"})])])},staticRenderFns:[]};var p=e("Z0/y")(r,d,!1,function(t){e("Z6Nx")},"data-v-e13eb1da",null).exports,u={data:function(){return{}},props:{centerDialogVisible:{type:Boolean,default:!1},modalStatus:{type:String,default:""}},wacth:{},mounted:function(){},methods:{postCenterDialogVisibleFalse:function(){this.$store.commit("updateCenterDialogVisible",!1)},handleClose:function(t){this.$store.commit("updateCenterDialogVisible",!1)}},components:{}},v={render:function(){var t=this,i=t.$createElement,a=t._self._c||i;return a("el-dialog",{attrs:{title:"",visible:t.centerDialogVisible,width:"480px","before-close":t.handleClose,center:""},on:{"update:visible":function(i){t.centerDialogVisible=i}}},[a("div",{directives:[{name:"show",rawName:"v-show",value:"wechat"==t.modalStatus,expression:"modalStatus=='wechat'"}],staticClass:"wechatCode"},[a("img",{attrs:{src:e("b3fX")}}),t._v(" "),a("span",[t._v("扫一扫添加微信")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{directives:[{name:"show",rawName:"v-show",value:"wechat"!=t.modalStatus,expression:"modalStatus!='wechat'"}],on:{click:t.postCenterDialogVisibleFalse}},[t._v("取 消")]),t._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:t.postCenterDialogVisibleFalse}},[t._v("确 定")])],1)])])},staticRenderFns:[]};var h={name:"App",data:function(){return{bodyWidth:document.body.clientWidth}},created:function(){try{document.body.removeChild(document.getElementById("appLoading")),setTimeout(function(){document.getElementById("app").style.display="block"},500)}catch(t){}},wacth:{bodyWidth:function(t){this.bodyWidth=t}},mounted:function(){var t=this;window.onresize=_.debounce(function(){t.bodyWidth=document.body.clientWidth},400)},computed:{centerDialogVisible:function(){return this.$store.getters.getCenterDialogVisible},modalStatus:function(){return this.$store.getters.getModalStatus}},components:{navBar:o,pageFooter:l,returnTop:p,modal:e("Z0/y")(u,v,!1,function(t){e("VzMu")},"data-v-40e6624c",null).exports}},g={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{attrs:{id:"app"}},[e("nav-bar",{attrs:{bodyWidth:t.bodyWidth}}),t._v(" "),e("router-view",{attrs:{bodyWidth:t.bodyWidth}}),t._v(" "),e("page-footer"),t._v(" "),e("return-top"),t._v(" "),e("modal",{attrs:{centerDialogVisible:t.centerDialogVisible,modalStatus:t.modalStatus}})],1)},staticRenderFns:[]};var m=e("Z0/y")(h,g,!1,function(t){e("k3Vi")},null,null).exports,f=e("zO6J"),w={data:function(){return{}},props:{bodyWidth:{type:Number,default:1440}},wacth:{},mounted:function(){},methods:{},components:{}},y={render:function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"banner"},[i("el-carousel",{attrs:{height:"580px"}},this._l(2,function(t){return i("el-carousel-item",{key:t})}))],1)},staticRenderFns:[]};var C=e("Z0/y")(w,y,!1,function(t){e("gHoY")},"data-v-005856d2",null).exports,D={data:function(){return{listTitleId:0,listTitle:[],UIlistData:[],UIlist:[],CGlistData:[],CGlist:[],PMlistData:[],PMlist:[],DDDlistData:[],DDDlist:[],DXlistData:[],DXlist:[],listsDatas:[]}},props:{},wacth:{},created:function(){this.getDesignCate(),this.getDesignList()},mounted:function(){},methods:{getDesignCate:function(){var t=this;this.$store.dispatch("getDesignCate","").then(function(i){var e=i.data;"OK"===i.statusText&&200===i.status?t.listTitle=e:alert("网络错误")}).catch(function(t){console.error(t)})},getDesignList:function(){var t=this;this.$store.dispatch("getDesignList","").then(function(i){var e=i.data;"OK"===i.statusText&&200===i.status?(t.listsDatas=e,t.toList(),t.toListData(0,8)):alert("网络错误")}).catch(function(t){console.error(t)})},toList:function(){for(var t=0;t<this.listsDatas.length;t++)"1"==this.listsDatas[t].cate&&(this.UIlistData=this.listsDatas[t].list),"2"==this.listsDatas[t].cate&&(this.CGlistData=this.listsDatas[t].list),"3"==this.listsDatas[t].cate&&(this.PMlistData=this.listsDatas[t].list),"4"==this.listsDatas[t].cate&&(this.DDDlistData=this.listsDatas[t].list),"5"==this.listsDatas[t].cate&&(this.DXlistData=this.listsDatas[t].list)},clickPage:function(t){this.listTitleId=t,this.toListData(0,8)},toListData:function(t,i){this.UIlist=this.UIlistData.slice(t,i),this.PMlist=this.PMlistData.slice(t,i),this.CGlist=this.CGlistData.slice(t,i),this.DDDlist=this.DDDlistData.slice(t,i),this.DXlist=this.DXlistData.slice(t,i)},handleCurrentChange:function(t){this.toListData(8*(t-1),8*t)},openDetails:function(t){localStorage.setItem("projectId",t),this.$router.push({name:"designDetails"})},newList:function(){var t={};this.listsDatas.forEach(function(i){var e=t[i.cate];e||(e=[],t[i.cate]=e,this.newList.push({cate:i.cate,items:e})),e.push(i)}),console.log(typeItems)}},components:{}},j={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"list"},[e("div",{staticClass:"listHeader"},t._l(t.listTitle,function(i,a){return e("a",{key:i.index,class:{active:t.listTitleId==a},attrs:{href:"javascript:;"},on:{click:function(i){t.clickPage(a)}}},[t._v(t._s(i.text))])})),t._v(" "),t._l(t.listTitle,function(i,a){return t.listTitleId==a?e("div",{staticClass:"listBody"},["UI设计"==i.text?e("div",{staticClass:"bodyitem"},[e("div",t._l(t.UIlist,function(i,a){return e("div",{staticClass:"listBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"listImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.listImg+");"}),t._v(" "),e("div",{staticClass:"listText"},[t._v(t._s(i.listText))]),t._v(" "),e("div",{staticClass:"listDate"},[t._v(t._s(i.listDate))]),t._v(" "),e("div",{staticClass:"listLine"})])})),t._v(" "),e("div",{staticClass:"pagination"},[e("el-pagination",{staticStyle:{"margin-left":"5px","white-space":"normal"},attrs:{"page-size":8,layout:"total,prev, pager, next",total:t.UIlistData.length},on:{"current-change":t.handleCurrentChange}})],1)]):t._e(),t._v(" "),"插画/原画"==i.text?e("div",{staticClass:"bodyitem"},[e("div",t._l(t.CGlist,function(i,a){return e("div",{staticClass:"listBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"listImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.listImg+");"}),t._v(" "),e("div",{staticClass:"listText"},[t._v(t._s(i.listText))]),t._v(" "),e("div",{staticClass:"listDate"},[t._v(t._s(i.listDate))]),t._v(" "),e("div",{staticClass:"listLine"})])})),t._v(" "),e("div",{staticClass:"pagination"},[e("el-pagination",{staticStyle:{"margin-left":"5px","white-space":"normal"},attrs:{"page-size":8,layout:"total,prev, pager, next",total:t.CGlistData.length},on:{"current-change":t.handleCurrentChange}})],1)]):t._e(),t._v(" "),"平面设计"==i.text?e("div",{staticClass:"bodyitem"},[e("div",t._l(t.PMlist,function(i,a){return e("div",{staticClass:"listBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"listImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.listImg+");"}),t._v(" "),e("div",{staticClass:"listText"},[t._v(t._s(i.listText))]),t._v(" "),e("div",{staticClass:"listDate"},[t._v(t._s(i.listDate))]),t._v(" "),e("div",{staticClass:"listLine"})])})),t._v(" "),e("div",{staticClass:"pagination"},[e("el-pagination",{staticStyle:{"margin-left":"5px","white-space":"normal"},attrs:{"page-size":8,layout:"total,prev, pager, next",total:t.PMlistData.length},on:{"current-change":t.handleCurrentChange}})],1)]):t._e(),t._v(" "),"3D设计"==i.text?e("div",{staticClass:"bodyitem"},[e("div",t._l(t.DDDlist,function(i,a){return e("div",{staticClass:"listBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"listImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.listImg+");"}),t._v(" "),e("div",{staticClass:"listText"},[t._v(t._s(i.listText))]),t._v(" "),e("div",{staticClass:"listDate"},[t._v(t._s(i.listDate))]),t._v(" "),e("div",{staticClass:"listLine"})])})),t._v(" "),e("div",{staticClass:"pagination"},[e("el-pagination",{staticStyle:{"margin-left":"5px","white-space":"normal"},attrs:{"page-size":8,layout:"total,prev, pager, next",total:t.DDDlistData.length},on:{"current-change":t.handleCurrentChange}})],1)]):t._e(),t._v(" "),"动效设计"==i.text?e("div",{staticClass:"bodyitem"},[e("div",t._l(t.DXlist,function(i,a){return e("div",{staticClass:"listBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"listImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.listImg+");"}),t._v(" "),e("div",{staticClass:"listText"},[t._v(t._s(i.listText))]),t._v(" "),e("div",{staticClass:"listDate"},[t._v(t._s(i.listDate))]),t._v(" "),e("div",{staticClass:"listLine"})])})),t._v(" "),e("div",{staticClass:"pagination"},[e("el-pagination",{staticStyle:{"margin-left":"5px","white-space":"normal"},attrs:{"page-size":8,layout:"total,prev, pager, next",total:t.DXlistData.length},on:{"current-change":t.handleCurrentChange}})],1)]):t._e()]):t._e()})],2)},staticRenderFns:[]};var b=e("Z0/y")(D,j,!1,function(t){e("2pwM")},"data-v-1f56f8f4",null).exports,x={data:function(){return{projectLists:[],projectListsData:[]}},props:{yearsTitle:{type:String,default:""}},wacth:{},mounted:function(){this.postProjectList()},methods:{openProject:function(){console.log(this.projectList)},postProjectList:function(){var t=this,i={year:this.yearsTitle};this.$store.dispatch("postProjectList",i).then(function(i){var e=i.data;"OK"===i.statusText&&200===i.status?(console.log(e),t.projectListsData=e,t.projectLists=t.projectListsData.slice(0,4)):alert("网络错误")}).catch(function(t){console.error(t)})},openDetails:function(t){localStorage.setItem("projectId",t),this.$router.push({name:"designDetails"})}},components:{}},T={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return 0!=t.projectLists.length?e("div",{staticClass:"listBox"},[e("div",{staticClass:"textBox"},[e("div",{staticClass:"yearsTitle"},[t._v(t._s(t.yearsTitle)+"年")]),t._v(" "),t.projectListsData.length>4?e("div",{staticClass:"more"},[e("a",{attrs:{href:"javascript:;"}},[t._v("更多 >")])]):t._e()]),t._v(" "),e("div",{staticClass:"projectList"},t._l(t.projectLists,function(i,a){return e("div",{staticClass:"projectBox",on:{click:function(e){t.openDetails(i.projectId)}}},[e("div",{staticClass:"listMask"}),t._v(" "),e("div",{staticClass:"projectImg",style:"background-image: url(http://5windy.com/static/uploads/"+i.projectImg+")"}),t._v(" "),e("div",{staticClass:"projectTitle"},[t._v(t._s(i.projectTitle))]),t._v(" "),e("div",{staticClass:"projectText"},[t._v(t._s(i.projectText))])])}))]):t._e()},staticRenderFns:[]};var I=e("Z0/y")(x,T,!1,function(t){e("3fOF")},"data-v-04960e84",null).exports,k={render:function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"downloadBox"},[i("a",{attrs:{href:"http://sketch.im/",target:"_blank"}},[i("div",{staticClass:"downloadLink",style:"background-image: url(static/banner/"+this.linkImg+")"})])])},staticRenderFns:[]};var S=e("Z0/y")({data:function(){return{linkImg:"link.png",downloadPictuer:[{pictuer:"jidong.png"},{pictuer:"jidong.png"},{pictuer:"jidong.png"},{pictuer:"jidong.png"}]}},props:{},wacth:{},mounted:function(){},methods:{},components:{}},k,!1,function(t){e("iRdH")},"data-v-a938ff68",null).exports,P={data:function(){return{}},props:{bodyWidth:{type:Number,default:1600}},wacth:{},mounted:function(){document.documentElement.scrollTop=0},methods:{},components:{navBar:o,banner:C,designList:b,projectList:I,download:S}},L={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"homeBody"},[e("banner"),t._v(" "),e("download"),t._v(" "),t._m(0),t._v(" "),e("design-list"),t._v(" "),t._m(1),t._v(" "),e("project-list",{attrs:{"years-title":"2018"}}),t._v(" "),e("project-list",{attrs:{"years-title":"2017"}}),t._v(" "),e("project-list",{attrs:{"years-title":"2016"}})],1)},staticRenderFns:[function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"text-title"},[i("h2",[this._v("作品欣赏")]),this._v(" "),i("p",[this._v("Windy作品分类，包含练习")])])},function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"text-title"},[i("h2",[this._v("参与项目")]),this._v(" "),i("p",[this._v("从事UI设计工作以来，所参与过的项目")])])}]};var B=e("Z0/y")(P,L,!1,function(t){e("/p5v")},"data-v-43fd7d0b",null).exports,E=(e("L7Pj"),e("yZpe"),{data:function(){return{projectId:localStorage.getItem("projectId"),showPayBox:!1,projectData:"",litterImg:"",baobei201708:{projectTitle:"香港报贝2.0商务移动报销APP",projectPic:"baobei201708.png",projectDate:"2017年4月",projectCopyright:"Windy",projectSynopsis:"这是在2015年通过朋友介绍所获得的一次与香港同胞合作的项目，当时的香港互联网并不发达，移动互联网刚刚兴起，于是一位与时俱进的香港老板来到大陆寻求移动互联网的契机。在这次机会中，我有幸与她合作，完成当时报贝的1.0版本。这是在2年后，这位老朋友再次找到我，让我给当时的报贝1.0设计升级迭代版本。于是有了下面的报贝2.0。",projectImg:"baobei201708.png"},jidong201801:{projectTitle:"广州极动MES工业PAD移动端",projectPic:"jidong201801.png",projectDate:"2018年1月",projectCopyright:"Windy",projectSynopsis:"该项目为任职东风设计院，与广州极动焊接技术有限公司所接的一个生产执行系统的一个外包项目。该项目的需求为将已经成熟软件MES，作为平台技术，通过数据接口调用，二次开发工人的手持移动端。由于移动端上需求只需要对生产报工，质检，设备故障报警，以及工时统计查询等功能，只需要对数据库进行增删改查的调用。所以，在不需要原生系统开发的情况下，我选用的vue.js作为webapp的开发框架。针对工厂需求，从原型到UI设计，再到前端代码实现，最后与平台对接口，到一个完整的APP，其中整个项目都由我一人包办。",projectImg:"jidong201801.png"},xunyi201711:{projectTitle:"寻医问药APP",projectPic:"xunyi201711.png",projectDate:"2017年11月",projectCopyright:"Windy",projectSynopsis:"这是一款为了方便用户，直接就能使用语音输入控制的医院挂号APP。用户仅仅只需要点击按钮录音，APP会根据用户的语音自动匹配响应的医生给用户选择挂号。",projectImg:"xunyi201711.png"},waimai201707:{projectTitle:"报贝外卖",projectPic:"waimai201707.png",projectDate:"2017年07月",projectCopyright:"Windy",projectSynopsis:"由于报贝2.0的业务扩展需求，需要将外卖的业务扩展至报贝的模块之中，特此，设计了这款外卖的APP。该APP分为商户版和用户版。商户登录商户版进行产品的上架管理与收银。用户登录用户版本进行点餐与外卖。红色为商户版，橙色为用户版。",projectImg:"waimai201707.png"},xiaodianlun201705:{projectTitle:"小电轮-共享电动车",projectPic:"xiaodianlun201705.png",projectDate:"2017年05月",projectCopyright:"Windy",projectSynopsis:"该项目为微信小程序共享电动车，从LOGO设计到整个小程序的界面，以及共享电车的车架设计都经过了几次的改版和头脑风暴。该项目暂未上线。",projectImg:"xiaodianlun201705.png"},mss201704:{projectTitle:"东风设计研究院智能管理系统MSS",projectPic:"mss201704.png",projectDate:"2017年04月",projectCopyright:"Windy",projectSynopsis:"该项目目前与东风本田与郑州日产设备管理进行使用中。",projectImg:"mss201704.png"},mesapp201703:{projectTitle:"东风设计研究院生产执行系统APP",projectPic:"mesapp201703.png",projectDate:"2017年03月",projectCopyright:"Windy",projectSynopsis:"该项目目前与东风设计研究院装备研发中心（东风涂装）使用中，从原型到设计到程序代码到平台发布，全部由我主导并完成。",projectImg:"mesapp201703.png"},one2pay201709:{projectTitle:"香港one2payPOS机界面",projectPic:"one2pay201709.png",projectDate:"2017年09月",projectCopyright:"Windy",projectSynopsis:"为香港报贝POS机界面设计。",projectImg:"one2pay201709.png"}}},created:function(){var t=this;this.$nextTick(function(){t.changyan()})},props:{},wacth:{},mounted:function(){this.$store.commit("updateNavBarActive",""),document.documentElement.scrollTop=0,this.getDesignData()},methods:{refish:function(){location.reload()},changyan:function(){window.changyan.api.config({appid:"cyt3crepq",conf:"prod_a13b2e3f57b739f379a9d121e340340d"})},getDesignData:function(){var t=this,i=this.projectId;this.$store.dispatch("getDesignData",i).then(function(i){var e=i.data;"OK"===i.statusText&&200===i.status?(t.projectData=e,t.litterImg="/static/uploads/"+t.projectData.projectPic):alert("网络错误")}).catch(function(t){console.error(t)})},encodeHtml:function(t){var i="";if(""==t)return i;for(var e=0;e<t.length;e++)i+="&#"+t.substring(e,e+1).charCodeAt().toString(10)+";";return i}},components:{}}),$={render:function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("div",{staticClass:"detailsBody"},[e("div",{staticClass:"detailsHeader"},[e("div",{staticClass:"detailsTop"},[e("div",{staticClass:"litterImg",style:"background-image: url(http://5windy.com"+t.litterImg+");"}),t._v(" "),e("div",{staticClass:"detailsTextBox"},[e("div",{staticClass:"textTitle"},[t._v(t._s(t.projectData.projectTitle))]),t._v(" "),e("div",{staticClass:"dateAndCopyright"},[t._v(t._s(t.projectData.projectDate)+" ©"+t._s(t.projectData.projectCopyright))]),t._v(" "),e("div",{staticClass:"textSynopsis"},[t._v(t._s(t.projectData.projectSynopsis))])]),t._v(" "),e("a",{attrs:{href:"javascript:;"}},["windy"!=t.projectData.projectCopyright?e("div",{staticClass:"downloadBtn"},[e("div",{staticClass:"btnIcon"}),t._v(" "),e("div",{staticClass:"btnText"},[t._v("本地下载")])]):t._e()])])]),t._v(" "),e("div",{staticClass:"details"},[e("div",{staticClass:"detailBody",staticStyle:{color:"#000!important"},domProps:{innerHTML:t._s(t.projectData.projectDetail)}}),t._v(" "),e("div",{staticClass:"text"},[t._v("如果您觉得本狗做的不错，或者资源对您有用，欢迎任意金额打赏支持")]),t._v(" "),e("div",{staticStyle:{display:"flex",margin:"auto",width:"180px"}},[e("a",{attrs:{href:"javascript:;"},on:{click:function(i){t.showPayBox=!t.showPayBox}}},[e("div",{staticClass:"payBtn"},[t._v("赏")])]),t._v(" "),e("a",{attrs:{href:"javascript:;"},on:{click:t.refish}},[e("div",{staticClass:"pinlun"},[t._v("评论")])])]),t._v(" "),e("transition",{attrs:{name:"payBox"}},[t.showPayBox?e("div",[e("div",{staticClass:"payBox"}),t._v(" "),e("div",{staticClass:"payText"},[t._v("打赏将支持作者提供更好的服务与更优质的资源")])]):t._e()]),t._v(" "),e("div",{attrs:{id:"SOHUCS",sid:t.projectId}})],1)])},staticRenderFns:[]};var M=e("Z0/y")(E,$,!1,function(t){e("SGkK")},"data-v-e4f42650",null).exports;a.default.use(f.a);var V=new f.a({routes:[{path:"/",name:"home",component:B},{path:"/designDetails",name:"designDetails",component:M}]}),A=e("9rMa"),q=e("2sCs"),W=e.n(q),H={getDesignCate:function(t,i){t.commit,t.state;return W()({url:"api/design_cate",method:"get",params:i})},getDesignList:function(t,i){t.commit,t.state;return W()({url:"api/design_list",method:"get",params:i})},getDesignData:function(t,i){t.commit,t.state;return W()({url:"api/design_detail/"+i,method:"get",params:i})},postProjectList:function(t,i){t.commit,t.state;return W()({url:"api/project_list",method:"post",params:i})}};a.default.use(A.a);var F=new A.a.Store({actions:H,state:{centerDialogVisible:!1,modalStatus:"",navBarActive:"",projectId:""},getters:{getCenterDialogVisible:function(t){return t.centerDialogVisible},getModalStatus:function(t){return t.modalStatus},getNavBarActive:function(t){return t.navBarActive}},mutations:{updateCenterDialogVisible:function(t,i){t.centerDialogVisible=i},updatemodalStatus:function(t,i){t.modalStatus=i},updateNavBarActive:function(t,i){t.navBarActive=i},updateProjectId:function(t,i){t.projectId=i}}}),N=e("lJzc"),U=e.n(N),Z=e("5VXh"),O=e.n(Z);e("K6VE");a.default.use(O.a),a.default.use(U.a,{loading:"/static/loading-svg/loading-bubbles.svg"}),new a.default({el:"#app",router:V,store:F,components:{App:m},template:"<App/>"})},SGkK:function(t,i){},VzMu:function(t,i){},Z6Nx:function(t,i){},b3fX:function(t,i,e){t.exports=e.p+"static/img/wechatCode.c566fe4.jpg"},gHoY:function(t,i){},ghgw:function(t,i){},iRdH:function(t,i){},k3Vi:function(t,i){},yULH:function(t,i){},yZpe:function(t,i){!function(){if(void 0===window.changyan&&void 0===window.cyan){var t,i,e,a,s;void 0===window.changyan&&(window.changyan={},window.changyan.api={},window.changyan.api.config=function(t){window.changyan.api.tmpIsvPageConfig=t},window.changyan.api.ready=function(t){window.changyan.api.tmpHandles=window.changyan.api.tmpHandles||[],window.changyan.api.tmpHandles.push(t)},window.changyan.ready=function(t){window.changyan.rendered?t&&t():(window.changyan.tmpHandles=window.changyan.tmpHandles||[],window.changyan.tmpHandles.push(t))}),window.cyan||(window.cyan={},window.cyan.api={},window.cyan.api.ready=function(t){window.cyan.api.tmpHandles=window.cyan.api.tmpHandles||[],window.cyan.api.tmpHandles.push(t)}),s=+new Date+window.Math.random().toFixed(16),t="https://changyan.itc.cn/upload/version-v3.js?"+s,e=document.getElementsByTagName("head")[0]||document.head||document.documentElement,(a=document.createElement("script")).setAttribute("type","text/javascript"),a.setAttribute("charset","UTF-8"),a.setAttribute("src",t),"function"==typeof i&&(window.attachEvent?a.onreadystatechange=function(){var t=a.readyState;"loaded"!==t&&"complete"!==t||(a.onreadystatechange=null,i())}:a.onload=i),e.appendChild(a)}}()}},["NHnr"]);
//# sourceMappingURL=app.76c79d644b375c4ef2a5.js.map