(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d21d464"],{d134:function(t,e,s){"use strict";s.r(e);var a=s("8212"),c=s("62ad"),r=s("a523"),i=s("0fd9"),o=function(){var t=this,e=t._self._c;return e("section",[e(i["a"],{attrs:{"no-gutters":""}},[e(c["a"],{attrs:{cols:"12"}},[e("SectionsHeroAlt",{attrs:{"hero-alt":t.locservice.alt_info}}),e(r["a"],{staticClass:"py-16"},[e("h2",{staticClass:"text-h4 text-md-h3 text-center font-weight-black text-capitalize"},[t._v(" What we do ")]),e("p",{staticClass:"text-h6 text-uppercase font-weight-light text-center my-16"},[t._v(" "+t._s(t.locservice.intro)+" ")]),e(i["a"],t._l(t.locservice.services,(function(s,r){return e(c["a"],{key:r,staticClass:"text-center",attrs:{cols:"12",sm:"6",md:"4",xl:"2"}},[e(a["a"],{staticClass:"mb-5",attrs:{size:"80",color:"primary"}},[e("img",{attrs:{src:s.img}})]),e("div",{staticClass:"title text-uppercase mt-1 mb-4 white--text"},[e("router-link",{staticClass:"text--white",attrs:{to:`/open/services/detail/${s.path}`}},[e("h3",{domProps:{innerHTML:t._s(s.title)}})])],1),e("p",{domProps:{textContent:t._s(s.body)}}),e(i["a"],{attrs:{"no-gutters":""}},[e(c["a"],{attrs:{cols:"12"}})],1)],1)})),1)],1)],1)],1)],1)},n=[],l=s("4000"),p=s("2f62");const h="services";var u={components:{SectionsHeroAlt:l["a"]},computed:{...Object(p["c"])(["getLocalPageObj"]),locservice:{get(){return this.getLocalPageObj(h)}}},async mounted(){await this.$store.dispatch("checkPages"),await this.$store.dispatch("setupServices")},data(){return{}}},d=u,m=s("2877"),v=Object(m["a"])(d,o,n,!1,null,null,null);e["default"]=v.exports}}]);