(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-14beeeea"],{"461b":function(t,e,s){"use strict";s.r(e);var a=s("62ad"),r=s("0fd9"),o=function(){var t=this,e=t._self._c;return e("section",[e(r["a"],{attrs:{"no-gutters":""}},[e(a["a"],{attrs:{cols:"12"}},[e("SectionsHeroAlt",{attrs:{"hero-alt":t.heroAlt}})],1),e(a["a"],{staticClass:"mx-auto",attrs:{cols:"8"}},[t.loading?t._e():[e("AllProductsVue")]],2)],1)],1)},i=[],n=s("5799"),c=s("4000"),l={components:{AllProductsVue:n["a"],SectionsHeroAlt:c["a"]},data(){return{loading:!0,heroAlt:[{src:"pexels-andrea-piacquadio-3884440.jpg",heading:" All Products "}]}},async created(){this.loading=!0,this.$store.dispatch("setupAllproducts").finally(()=>this.loading=!1)}},u=l,d=s("2877"),p=Object(d["a"])(u,o,i,!1,null,null,null);e["default"]=p.exports},5231:function(t,e,s){"use strict";var a=function(){var t=this,e=t._self._c;return e("span",[t._v(t._s(this.focusPrice))])},r=[],o=s("7adc"),i={props:{priceurl:{required:!0}},data(){return{price:0}},computed:{focusPrice(){return this.price}},async created(){await this.getPrice()},methods:{async getPrice(){Object(o["e"])(this.priceurl).then(t=>{console.log(t),this.price=t.incl_tax}).catch(t=>{console.log(t)})}}},n=i,c=s("2877"),l=Object(c["a"])(n,a,r,!1,null,null,null);e["a"]=l.exports},5799:function(t,e,s){"use strict";var a=s("2fa4"),r=function(){var t=this,e=t._self._c;return e("section",{staticClass:"py-16",class:t.$vuetify.theme.dark?"black":"white"},[t.show_membership?[e("membership-vue")]:t._e(),e(a["a"]),e("DrugTestVue"),e(a["a"]),e("LocalVue")],2)},o=[],i=s("8336"),n=s("b0af"),c=s("99d9"),l=s("62ad"),u=s("a523"),d=s("ce87"),p=s("132d"),h=s("8860"),m=s("da13"),g=s("5d23"),x=s("34c3"),f=s("0fd9"),_=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],[t.computedready?e(f["a"],[e(l["a"],[e(f["a"],{attrs:{"no-gutters":""}},[e(l["a"],{},[e("h4",{staticClass:"text-h4 text-md-h4 text-capitalize mb-4"},[t._v("Affordable Consortium")]),e("p",{staticClass:"my-10 title"}),e("div",{staticClass:"text-center"})])],1)],1)],1):t._e()],1),e(u["a"],[e(f["a"],{staticClass:"mx-auto",staticStyle:{"max-width":"1200px"}},t._l(t.plans,(function(s,a){return e(l["a"],{key:`plan-${a}`,attrs:{cols:"12",md:"4"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:a}){return[e(n["a"],{staticClass:"mx-auto",class:a?"zoom":"notzoom",attrs:{elevation:a?24:s.elevation,color:s.color,"max-width":"400",transition:"fade-transition"}},[e("h3",{staticClass:"text-h4 text-center font-weight-black white--text pt-5",domProps:{textContent:t._s(s.plan)}}),e(c["c"],{staticClass:"text-center subtitle-1 white--text py-2",domProps:{textContent:t._s(s.description)}}),e(c["b"],{staticClass:"text-h5 font-weight-black text-center white--text pt-0"},[t._v(" "+t._s(s.yearly)+" "),e("span",{staticClass:"subtitle-1"},[t._v("per year ")])]),e(h["a"],[t._l(s.features,(function(s,a){return e(m["a"],{key:`feature-${a}`,attrs:{dense:""}},[e(x["a"],[e(p["a"],{attrs:{color:"green"}},[t._v(" "+t._s(s.icon)+" ")])],1),e(g["a"],[e(g["c"],{staticClass:"text-capitalize",domProps:{textContent:t._s(s.text)}})],1)],1)})),e(m["a"],[e(i["a"],{staticClass:"mx-auto my-3",attrs:{color:"primary",large:"",block:"",rounded:""},on:{click:function(e){return t.handleBuyMembership(s)}}},[t._v(" Buy Now ")])],1)],2)],1)]}}],null,!0)})],1)})),1)],1)],1)},b=[],y=(s("14d9"),s("2f62")),v={data(){return{showbtn:!0,planDuration:"monthly",loading:!0}},computed:{...Object(y["c"])(["getMembershipDisplay"]),plans:{get(){return this.getMembershipDisplay}},computedready:{get(){return this.getMembershipDisplay.length>0}}},async mounted(){console.log(this.plans),this.loading=!1},methods:{handleBuyMembership(t){console.log(t);let e=`/open/products/view-membership/${t.prod_id}/${t.plan}/`;console.log(e),this.$router.push(e)}}},C=v,w=s("2877"),k=Object(w["a"])(C,_,b,!1,null,null,null),j=k.exports,P=s("8212"),$=s("adda"),z=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],{attrs:{fluid:""}},[e(u["a"],[t.computedready?e(f["a"],[e(l["a"],{attrs:{cols:"12"}},[e(f["a"],{attrs:{"no-gutters":""}},[e(l["a"],{},[e("h4",{staticClass:"text-h4 text-md-h4 text-capitalize mb-4"},[t._v(" "+t._s(t.page_obj.title)+" ")]),e("p",{staticClass:"my-10 title"},[t._v(" "+t._s(t.page_obj.sub)+" ")]),e("div",{staticClass:"text-center"})])],1)],1)],1):t._e()],1),e(f["a"],{staticClass:"mx-auto"},t._l(t.getDrugTest,(function(s,a){return e(l["a"],{key:"P"+a,attrs:{cols:"12"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:a}){return[e(n["a"],{staticClass:"mx-auto transition-swing",class:a?"zoom":"notzoom",attrs:{elevation:a?24:36,color:"",transition:"fade-transition"}},[e("div",{staticClass:"d-flex flex-no-wrap justify-space-between"},[e("div",[e(c["d"],{staticClass:"text-h4 text-md-h4 text-center text-capitalize mb-4",domProps:{textContent:t._s(s.title)}}),e(c["c"],{staticClass:"description"},[e("p",{domProps:{innerHTML:t._s(s.description)}})]),e(c["c"],{staticClass:"text-h5 font-weight-black green--text pt-0"},[t._v(" $ "),e("price",{attrs:{priceurl:s.price}})],1),e(c["a"],[e(i["a"],{staticClass:"mx-auto ml-2 mt-5 primary white--text",attrs:{"x-large":"",block:"",rounded:""},on:{click:function(e){return t.handleSelected(s.upc)}}},[t._v(" BUY NOW ")])],1)],1),e(P["a"],{staticClass:"ma-3",attrs:{size:t.size,tile:""}},[e($["a"],{attrs:{src:s.images[0].original}})],1)],1)])]}}],null,!0)})],1)})),1)],1)],1)},O=[],A=s("5231"),D={components:{price:A["a"]},data(){return{showbtn:!0,page_obj:{title:"Nationwide DrugTest",sub:""}}},computed:{...Object(y["c"])(["getDrugTest"]),size(){switch(this.$vuetify.breakpoint.name){case"xs":return 100;case"sm":return 100;case"md":return 300;case"lg":return 300;case"xl":return 300}},computedready:{get(){return this.getDrugTest.length>0}}},mounted(){},methods:{handleSelected(t){this.$router.push(`/open/products/view-drugtest/${t}`)}}},T=D,M=Object(w["a"])(T,z,O,!1,null,null,null),S=M.exports,B=s("ce7e"),L=s("8e36"),V=function(){var t=this,e=t._self._c;return e("section",[e(u["a"],{attrs:{fluid:""}},[e(u["a"],[t.computedready?e(f["a"],[e(l["a"],{attrs:{cols:"12"}},[e(f["a"],{attrs:{"no-gutters":""}},[e(l["a"],{},[e("h4",{staticClass:"text-h4 text-md-h4 text-capitalize mb-4"},[t._v(" "+t._s(t.page_obj.title)+" ")]),e("div",{staticClass:"text-center"})])],1)],1)],1):t._e()],1),e(f["a"],{staticClass:"mx-auto"},t._l(t.locationproducts,(function(s,a){return e(l["a"],{key:"P"+a,attrs:{cols:"12",sm:"12",xs:"12",md:"5",lg:"5",xl:"5"}},[e(d["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:a}){return[e(n["a"],{staticClass:"mx-auto my-12",attrs:{elevation:a?24:36,loading:t.loading,"max-width":"374",transition:"fade-transition"}},[e("template",{slot:"progress"},[e(L["a"],{attrs:{color:"deep-purple",height:"10",indeterminate:""}})],1),e($["a"],{attrs:{height:"150",src:s.images[0].original}}),e(c["d"],[t._v(t._s(s.title))]),e(c["c"],{attrs:{"min-height":"50px"}},[e("div",{domProps:{innerHTML:t._s(s.description)}})]),e(c["c"],{staticClass:"text-h5 font-weight-black pt-0 green--text"},[t._v(" $ "),e("price",{attrs:{priceurl:s.price}})],1),e(B["a"],{staticClass:"mx-4 my-3"}),e(c["a"],[e("div",{staticClass:"mx-auto text-center"},[e(i["a"],{staticClass:"mx-auto my-3",attrs:{color:"primary",large:"",block:"",rounded:""},on:{click:function(e){return t.handleBuy(s.upc)}}},[t._v(" Buy Now ")])],1)])],2)]}}],null,!0)})],1)})),1)],1)],1)},H=[],N={components:{price:A["a"]},computed:{...Object(y["c"])(["getLocal"]),locationproducts:{get(){return this.getLocal}},computedready:{get(){return this.getLocal.length>0}}},mounted(){},methods:{reserve(){this.loading=!0,setTimeout(()=>this.loading=!1,2e3)},handleBuy(t){this.$router.push(`/open/products/view-local/${t}`)}},data(){return{showbtn:!0,loading:!1,selection:1,page_obj:{title:"At our location",sub:""}}}},U=N,q=Object(w["a"])(U,V,H,!1,null,null,null),J=q.exports,W={components:{MembershipVue:j,DrugTestVue:S,LocalVue:J},data(){return{loading:!0}},computed:{...Object(y["c"])(["getUserProfile"]),show_membership:{get(){return!this.getUserProfile.company||!this.getUserProfile.company.consortium_purchased}}},async mounted(){this.loading=!1}},Y=W,E=(s("b9d2"),Object(w["a"])(Y,r,o,!1,null,"48f9bff2",null));e["a"]=E.exports},"6ec5":function(t,e,s){},b9d2:function(t,e,s){"use strict";s("6ec5")}}]);