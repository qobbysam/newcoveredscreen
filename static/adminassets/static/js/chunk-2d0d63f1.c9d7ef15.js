(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0d63f1"],{7277:function(t,a,s){"use strict";s.r(a);var i=s("62ad"),l=s("a523"),e=s("0fd9"),r=function(){var t=this,a=t._self._c;return a("div",{staticClass:"page-dashboard"},[a(l["a"],[a(e["a"],[a(i["a"],{attrs:{cols:12,sm:6,lg:3}},[a("mini-statistic-card",{attrs:{icon:"mdi-facebook",title:"100+","sub-title":"Likes",color:"indigo"}})],1),a(i["a"],{attrs:{cols:12,sm:6,lg:3}},[a("mini-statistic-card",{attrs:{icon:"mdi-google",title:"150+","sub-title":"Connections",color:"red"}})],1),a(i["a"],{attrs:{cols:12,sm:6,lg:3}},[a("mini-statistic-card",{attrs:{icon:"mdi-twitter",title:"200+","sub-title":"Followers",color:"light-blue"}})],1),a(i["a"],{attrs:{cols:12,sm:6,lg:3}},[a("mini-statistic-card",{attrs:{icon:"mdi-instagram",title:"50+","sub-title":"Shots",color:"purple"}})],1)],1)],1)],1)},o=[];const n=(t,a)=>new Array(a-t).fill(t).map((a,s)=>t+s),c=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],u=(c.map(t=>{return{month:t,"Unique Visit":Math.floor(1e3*Math.random())+200,"Page View":Math.floor(1e3*Math.random())+250}}),[220,182,191,234,290,330,310,123,442,321,90,149,210,122,133,334,198,123,125,220]);u.map((t,a)=>{return{label:a+"D",max:500,sales:t}}),n(1,12).map(t=>{return{cate:"Cat"+t,value:5*(Math.sin(t/5)*(t/5-.1)+t/6)}});var d=s("c0a4"),p=s.n(d),m=s("b0af"),b=s("99d9"),g=s("132d"),h=function(){var t=this,a=t._self._c;return a(m["a"],{attrs:{tile:""}},[a(b["b"],{staticClass:"pa-0"},[a(e["a"],{attrs:{"no-gutters":""}},[a(i["a"],{staticClass:"pa-3"},[a("div",{staticClass:"layout justify-center align-center"},[a(g["a"],{attrs:{size:"56px",color:t.color}},[t._v(t._s(t.icon))])],1)]),a(i["a"],{staticClass:"pa-3",class:t.color},[a("div",{staticClass:"white--text"},[t._v(t._s(t.title))]),a("span",{staticClass:"white--text"},[t._v(t._s(t.subTitle))])])],1)],1)],1)},f=[],v={props:{icon:String,title:String,subTitle:String,color:String}},w=v,C=s("2877"),_=Object(C["a"])(w,h,f,!1,null,null,null),M=_.exports,S={name:"PageDashboard",components:{MiniStatisticCard:M},data:()=>({color:p.a,selectedTab:"tab-1"}),computed:{}},x=S,k=Object(C["a"])(x,r,o,!1,null,null,null);a["default"]=k.exports}}]);