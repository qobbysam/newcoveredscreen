(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21af16"],{be52:function(t,e,s){"use strict";s.r(e);var a=s("8336"),o=s("b0af"),n=s("99d9"),r=s("62ad"),c=s("a523"),i=s("0fd9"),p=function(){var t=this,e=t._self._c;return e("section",[e(i["a"],{attrs:{"no-gutters":""}},[e(r["a"],{attrs:{cols:"12"}},[e("SectionsHeroAlt",{attrs:{"hero-alt":t.page_obj.alt_info}}),e(c["a"],[e(i["a"],{staticClass:"py-16",attrs:{justify:"space-around"}},[e(r["a"],{attrs:{cols:"12",md:"7",lg:"7"}},[e("p",{domProps:{innerHTML:t._s(t.page_obj.body.body)}}),e("p")]),e(r["a"],{attrs:{cols:"12",md:"5",lg:"5"}},[e(o["a"],{staticClass:"mx-auto"},[e(n["d"],[t._v(" Price: $"+t._s(t.page_obj.product.price)+" ")]),e(n["a"],[e(a["a"],{staticClass:"primary",attrs:{large:"",rounded:""},on:{click:function(e){return t.handleBuynow(t.page_obj.product.product_link)}}},[t._v(" Buy Now")])],1)],1)],1)],1)],1),e("StepsSection",{attrs:{steps:t.page_obj.steps}})],1)],1)],1)},u=[],l=(s("14d9"),function(){var t=this,e=t._self._c;return e(c["a"],[e(i["a"],t._l(t.steps,(function(s,a){return e(r["a"],{key:a},[e(o["a"],{attrs:{outline:""}},[e(n["d"],{domProps:{textContent:t._s(s.step_info_one)}}),e(n["c"],{attrs:{height:"100px"},domProps:{textContent:t._s(s.description)}})],1)],1)})),1)],1)}),d=[],g={name:"StepsSection",props:["steps"]},_=g,h=s("2877"),b=Object(h["a"])(_,l,d,!1,null,null,null),f=b.exports,m=s("4000"),j=s("2f62"),w={name:"OneService",components:{StepsSection:f,SectionsHeroAlt:m["a"]},props:{pageid:String},computed:{...Object(j["c"])(["getLocalPageObj"]),page_obj:{get(){return this.getLocalPageObj(this.pageid)}}},async mounted(){await this.$store.dispatch("checkPages"),await this.$store.dispatch("setupOneService",this.pageid)},methods:{handleBuynow(t){const e="#";this.$router.push(e)}}},S=w,y=Object(h["a"])(S,p,u,!1,null,null,null);e["default"]=y.exports}}]);