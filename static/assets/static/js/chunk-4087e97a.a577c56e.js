(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4087e97a"],{"461b":function(t,e,a){"use strict";a.r(e);var s=a("62ad"),i=a("0fd9"),n=function(){var t=this,e=t._self._c;return e("section",[e(i["a"],{attrs:{"no-gutters":""}},[e(s["a"],{attrs:{cols:"12"}},[e("SectionsHeroAlt",{attrs:{"hero-alt":t.heroAlt}})],1),e(s["a"],{staticClass:"mx-auto",attrs:{cols:"8"}},[t.loading?t._e():[e("AllProductsVue")]],2)],1)],1)},o=[],l=a("5799"),r=a("4000"),c={components:{AllProductsVue:l["a"],SectionsHeroAlt:r["a"]},data(){return{loading:!0,heroAlt:[{src:"pexels-andrea-piacquadio-3884440.jpg",heading:" All Products "}]}},async mounted(){this.loading=!0,this.$store.dispatch("setupAllproducts").finally(()=>this.loading=!1)}},u=c,d=a("2877"),p=Object(d["a"])(u,n,o,!1,null,null,null);e["default"]=p.exports},5799:function(t,e,a){"use strict";var s=a("2fa4"),i=function(){var t=this,e=t._self._c;return e("section",{staticClass:"py-16",class:t.$vuetify.theme.dark?"black":"white"},[e("membership-vue"),e(s["a"]),e("DrugTestVue"),e(s["a"]),e("LocalVue")],1)},n=[],o=a("8336"),l=a("b0af"),r=a("99d9"),c=a("62ad"),u=a("a523"),d=a("ce87"),p=a("132d"),h=a("8860"),m=a("da13"),x=a("5d23"),f=a("34c3"),g=a("0fd9"),_=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],[e(g["a"],[e(c["a"],[e(g["a"],{attrs:{"no-gutters":""}},[e(c["a"],{},[e("h3",{staticClass:"text-h4 text-md-h3 text-capitalize mb-4"},[t._v(" Our Affordable Consortium Prices ")]),e("p",{staticClass:"my-10 title"}),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(u["a"],[e(g["a"],{staticClass:"mx-auto",staticStyle:{"max-width":"1200px"}},t._l(t.plans,(function(a,s){return e(c["a"],{key:`plan-${s}`,attrs:{cols:"12",md:"4"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:s}){return[e(l["a"],{staticClass:"mx-auto transition-swing",class:s?"zoom":"notzoom",attrs:{elevation:s?24:a.elevation,color:a.color,"max-width":"400"}},[e("h3",{staticClass:"text-h4 text-center font-weight-black white--text pt-5",domProps:{textContent:t._s(a.plan)}}),e(r["c"],{staticClass:"text-center subtitle-1 white--text py-2",domProps:{textContent:t._s(a.description)}}),e(r["b"],{staticClass:"text-h5 font-weight-black text-center white--text pt-0"},[t._v(" "+t._s(a.yearly)+" "),e("span",{staticClass:"subtitle-1"},[t._v("per year ")])]),e(h["a"],[t._l(a.features,(function(a,s){return e(m["a"],{key:`feature-${s}`,attrs:{dense:""}},[e(f["a"],[e(p["a"],[t._v(" "+t._s(a.icon)+" ")])],1),e(x["a"],[e(x["c"],{staticClass:"text-capitalize",domProps:{textContent:t._s(a.text)}})],1)],1)})),e(m["a"],[e(o["a"],{staticClass:"mx-auto my-3",attrs:{color:"primary",large:"",block:"",rounded:""},on:{click:function(e){return t.handleBuyMembership(a.prod_id)}}},[t._v(" Buy Now ")])],1)],2)],1)]}}],null,!0)})],1)})),1)],1)],1)},b=[],v=(a("14d9"),a("2f62")),y={data(){return{showbtn:!0,planDuration:"monthly",loading:!0}},computed:{...Object(v["c"])(["getMembershipDisplay"]),plans:{get(){return this.getMembershipDisplay}}},async mounted(){console.log(this.plans),this.loading=!1},methods:{handleBuyMembership(t){this.$router.push(`/open/products/view-membership/${t}`)}}},C=y,w=a("2877"),k=Object(w["a"])(C,_,b,!1,null,null,null),j=k.exports,z=a("8212"),P=a("adda"),A=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],{attrs:{fluid:""}},[e(u["a"],[e(g["a"],[e(c["a"],{attrs:{cols:"12"}},[e(g["a"],{attrs:{"no-gutters":""}},[e(c["a"],{},[e("h5",{staticClass:"text-h4 text-md-h3 text-capitalize mb-4"},[t._v(" "+t._s(t.page_obj.title)+" ")]),e("p",{staticClass:"my-10 title"},[t._v(" "+t._s(t.page_obj.sub)+" ")]),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(g["a"],{staticClass:"mx-auto"},t._l(t.getDrugTest,(function(a,s){return e(c["a"],{key:"P"+s,attrs:{cols:"12"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:s}){return[e(l["a"],{staticClass:"mx-auto transition-swing",class:s?"zoom":"notzoom",attrs:{elevation:s?24:36,color:"primary"}},[e("div",{staticClass:"d-flex flex-no-wrap justify-space-between"},[e("div",[e(r["d"],{staticClass:"text-h5 text-h4 text-md-h3 text-center text-capitalize mb-4 white--text",domProps:{textContent:t._s(a.title)}}),e(r["c"],{staticClass:"title white--text"},[e("p",{domProps:{innerHTML:t._s(a.description)}})]),e(r["a"],[e(o["a"],{staticClass:"ml-2 mt-5 white--text",attrs:{"x-large":"",outlined:"",rounded:""},on:{click:function(e){return t.handleSelected(a.upc)}}},[t._v(" BUY NOW ")])],1)],1),e(z["a"],{staticClass:"ma-3",attrs:{size:t.size,tile:""}},[e(P["a"],{attrs:{src:a.images[0].original}})],1)],1)])]}}],null,!0)})],1)})),1)],1)],1)},O=[],S={data(){return{showbtn:!0,page_obj:{title:"Nationwide DrugTest",sub:""}}},computed:{...Object(v["c"])(["getDrugTest"]),size(){switch(this.$vuetify.breakpoint.name){case"xs":return 100;case"sm":return 100;case"md":return 300;case"lg":return 300;case"xl":return 300}}},mounted(){},methods:{handleSelected(t){this.$router.push(`/open/products/view-drugtest/${t}`)}}},$=S,D=Object(w["a"])($,A,O,!1,null,null,null),T=D.exports,M=a("ce7e"),V=a("8e36"),B=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],{attrs:{fluid:""}},[e(u["a"],[e(g["a"],[e(c["a"],[e(g["a"],{attrs:{"no-gutters":""}},[e(c["a"],{},[e("h5",{staticClass:"text-h4 text-md-h3 text-capitalize mb-4"},[t._v(" "+t._s(t.page_obj.title)+" ")]),e("p",{staticClass:"my-10 title"},[t._v(" "+t._s(t.page_obj.sub)+" ")]),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(g["a"],{staticClass:"mx-auto",staticStyle:{"max-width":"1200px"}},t._l(t.locationproducts,(function(a,s){return e(c["a"],{key:"P"+s,attrs:{cols:"12",sm:"12",xs:"12",md:"4",lg:"4",xl:"4"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:s}){return[e(l["a"],{staticClass:"mx-auto my-12",attrs:{elevation:s?24:36,loading:t.loading,"max-width":"374"}},[e("template",{slot:"progress"},[e(V["a"],{attrs:{color:"deep-purple",height:"10",indeterminate:""}})],1),e(P["a"],{attrs:{height:"150",src:a.images[0].original}}),e(r["d"],[t._v(t._s(a.title))]),e(r["c"],[e("div",{domProps:{innerHTML:t._s(a.description)}})]),e(M["a"],{staticClass:"mx-4 my-3"}),e(r["a"],[e("div",{staticClass:"mx-auto text-center"},[e(o["a"],{attrs:{color:"primary ",large:"","text-center":""},on:{click:t.reserve}},[t._v(" Buy Now ")])],1)])],2)]}}],null,!0)})],1)})),1)],1)],1)},L=[],H={computed:{...Object(v["c"])(["getLocal"]),locationproducts:{get(){return this.getLocal}}},mounted(){},methods:{reserve(){this.loading=!0,setTimeout(()=>this.loading=!1,2e3)},handleBuy(t){}},data(){return{showbtn:!0,loading:!1,selection:1,page_obj:{title:"At our location",sub:""}}}},N=H,J=Object(w["a"])(N,B,L,!1,null,null,null),q=J.exports,U={components:{MembershipVue:j,DrugTestVue:T,LocalVue:q},data(){return{loading:!0}},async mounted(){this.loading=!1}},W=U,Y=(a("afaf"),Object(w["a"])(W,i,n,!1,null,"d3ecdae2",null));e["a"]=Y.exports},"65ff":function(t,e,a){},afaf:function(t,e,a){"use strict";a("65ff")}}]);