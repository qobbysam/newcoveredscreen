(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1ecea079"],{"461b":function(t,e,a){"use strict";a.r(e);var s=a("62ad"),i=a("0fd9"),n=function(){var t=this,e=t._self._c;return e("section",[e(i["a"],{attrs:{"no-gutters":""}},[e(s["a"],{attrs:{cols:"12"}},[e("SectionsHeroAlt",{attrs:{"hero-alt":t.heroAlt}}),e("AllProductsVue")],1)],1)],1)},r=[],o=a("5799"),l=a("4000"),c={components:{AllProductsVue:o["a"],SectionsHeroAlt:l["a"]},data(){return{heroAlt:[{src:"pexels-andrea-piacquadio-3884440.jpg",heading:" All Products "}]}},mounted(){this.$store.dispatch("fetchProducts")},head(){return{title:"Pricing and Plans",meta:[{hid:"description",name:"description",content:"Infographic hypotheses influencer user experience Long madel ture gen-z paradigm shift client partner network product seilans solve management influencer analytics leverage virality. incubator seed round massmarket. buyer agile development growth hacking business-to-consumer ecosystem"}]}}},d=c,u=a("2877"),m=Object(u["a"])(d,n,r,!1,null,null,null);e["default"]=m.exports},"48f1":function(t,e,a){},5799:function(t,e,a){"use strict";var s=a("2fa4"),i=function(){var t=this,e=t._self._c;return e("section",{staticClass:"py-16",class:t.$vuetify.theme.dark?"black":"white"},[e("membership-vue"),e(s["a"]),e("DrugTestVue"),e(s["a"]),e("LocalVue")],1)},n=[],r=a("62ad"),o=a("a523"),l=a("0fd9"),c=function(){var t=this,e=t._self._c;return e("section",[e(o["a"],[e(l["a"],[e(r["a"],[e(l["a"],{attrs:{"no-gutters":""}},[e(r["a"],{staticClass:"text-center"},[e("h2",{staticClass:"text-h4 text-md-h3 text-center font-weight-black text-capitalize mb-4"},[t._v(" Our Affordable Consortium Prices ")]),e("p",{staticClass:"my-10 title"},[t._v(" Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. ")]),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(o["a"])],1)},d=[],u=(a("14d9"),a("2f62")),m={computed:{...Object(u["c"])(["getMembership"])},mounted(){console.log(this.getMembership)},methods:{handleBuyMembership(t){this.$router.push(`/open/products/view-membership/${t}`)}},data(){return{showbtn:!0,planDuration:"monthly",plan:{plan:"Basic",elevation:0,color:"primary darken-1",description:"Best Plan for Small Businesses",yearly:"$100",features:[{icon:"mdi-dns",text:"premium DNS"}]},plans:[{plan:"Basic",elevation:0,color:"primary darken-1",description:"Best Plan for Small Businesses",yearly:"$100",features:[{icon:"mdi-dns",text:"premium DNS"}]},{plan:"Silver",elevation:16,color:"green darken-2",description:"Best Plan for Professional Users",monthly:"$40",yearly:"$400",features:[{icon:"mdi-dns",text:"premium DNS"}]},{plan:"Gold",elevation:0,color:"orange darken-3",description:"Best Plan for Power Users",monthly:"$100",yearly:"$1000",features:[{icon:"mdi-dns",text:"premium DNS"}]}]}}},p=m,h=a("2877"),f=Object(h["a"])(p,c,d,!1,null,null,null),g=f.exports,x=a("8212"),v=a("8336"),y=a("b0af"),b=a("99d9"),w=a("ce87"),C=a("adda"),_=function(){var t=this,e=t._self._c;return e("section",[e(o["a"],{attrs:{fluid:""}},[e(o["a"],[e(l["a"],[e(r["a"],[e(l["a"],{attrs:{"no-gutters":""}},[e(r["a"],{staticClass:"text-center"},[e("h5",{staticClass:"text-h4 text-md-h3 text-center text-capitalize mb-4"},[t._v(" Our Affordable Consortium Prices ")]),e("p",{staticClass:"my-10 title"},[t._v(" Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. ")]),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(l["a"],{staticClass:"mx-auto",staticStyle:{"max-width":"1200px"}},t._l(t.getDrugTest,(function(a,s){return e(r["a"],{key:"P"+s,attrs:{cols:"12"}},[e(w["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:s}){return[e(y["a"],{staticClass:"mx-auto transition-swing",class:s?"zoom":"notzoom",attrs:{elevation:s?24:t.plan.elevation,color:t.plan.color,"max-width":"1200"}},[e("div",{staticClass:"d-flex flex-no-wrap justify-space-between"},[e("div",[e(b["d"],{staticClass:"text-h5",domProps:{textContent:t._s(a.title)}}),e(b["b"],[e("p",{domProps:{innerHTML:t._s(a.description)}})]),e(b["a"],[e(v["a"],{staticClass:"ml-2 mt-5",attrs:{"x-large":"",outlined:"",rounded:""},on:{click:function(e){return t.handleSelected(a.upc)}}},[t._v(" BUY NOW ")])],1)],1),e(x["a"],{staticClass:"ma-3",attrs:{size:"300",tile:""}},[e(C["a"],{attrs:{src:a.images[0].original}})],1)],1)])]}}],null,!0)})],1)})),1)],1)],1)},k=[],P={computed:{...Object(u["c"])(["getMembership","getDrugTest"])},mounted(){console.log(this.getMembership)},methods:{handleSelected(t){this.$router.push(`/open/products/view-drugtest/${t}`)}},data(){return{showbtn:!0,planDuration:"monthly",items:[{color:"#1F7087",src:"https://cdn.vuetifyjs.com/images/cards/foster.jpg",title:"Supermodel",artist:"Foster the People"}],plan:{plan:"Basic",elevation:0,color:"primary darken-1",description:"Best Plan for Small Businesses",yearly:"$100",features:[{icon:"mdi-web",text:"Up to 20 drivers"},{icon:"mdi-harddisk",text:"10 GB storage"},{icon:"mdi-signal",text:"500 GB bandwidth"},{icon:"mdi-account",text:"10 email addreses"},{icon:"mdi-domain",text:"free domain with annual plan"},{icon:"mdi-server",text:"4X pricessing power"},{icon:"mdi-dns",text:"premium DNS"}]}}}},S=P,B=Object(h["a"])(S,_,k,!1,null,null,null),j=B.exports,$=a("ce7e"),D=a("8e36"),O=function(){var t=this,e=t._self._c;return e("section",[e(o["a"],{attrs:{fluid:""}},[e(o["a"],[e(l["a"],[e(r["a"],[e(l["a"],{attrs:{"no-gutters":""}},[e(r["a"],{staticClass:"text-center"},[e("h5",{staticClass:"text-h4 text-md-h3 text-center text-capitalize mb-4"},[t._v(" Our Affordable Consortium Prices ")]),e("p",{staticClass:"my-10 title"},[t._v(" Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. ")]),e("div",{staticClass:"text-center"})])],1)],1)],1)],1),e(l["a"],{staticClass:"mx-auto d-flex justify-center",staticStyle:{"max-width":"1200px"}},t._l(t.items,(function(a,s){return e(r["a"],{key:"P"+s,attrs:{cols:"4"}},[e(w["a"],{scopedSlots:t._u([{key:"default",fn:function({hover:a}){return[e(y["a"],{staticClass:"mx-auto my-12",attrs:{elevation:a?24:t.plan.elevation,loading:t.loading,"max-width":"374"}},[e("template",{slot:"progress"},[e(D["a"],{attrs:{color:"deep-purple",height:"10",indeterminate:""}})],1),e(C["a"],{attrs:{height:"250",src:"https://cdn.vuetifyjs.com/images/cards/cooking.png"}}),e(b["d"],[t._v("Cafe Badilico")]),e(b["c"],[e("div",[t._v("Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.")])]),e($["a"],{staticClass:"mx-4 my-3"}),e(b["a"],[e("div",{staticClass:"mx-auto text-center"},[e(v["a"],{attrs:{color:"deep-purple lighten-2",large:"","text-center":""},on:{click:t.reserve}},[t._v(" Reserve ")])],1)])],2)]}}],null,!0)})],1)})),1)],1)],1)},A=[],M={computed:{...Object(u["c"])(["getMembership"])},mounted(){console.log(this.getMembership)},methods:{reserve(){this.loading=!0,setTimeout(()=>this.loading=!1,2e3)}},data(){return{showbtn:!0,loading:!1,selection:1,planDuration:"monthly",items:[{color:"#1F7087",src:"https://cdn.vuetifyjs.com/images/cards/foster.jpg",title:"Supermodel",artist:"Foster the People"},{color:"#1F7087",src:"https://cdn.vuetifyjs.com/images/cards/foster.jpg",title:"Supermodel",artist:"Foster the People"}],plan:{plan:"Basic",elevation:0,color:"primary darken-1",description:"Best Plan for Small Businesses",yearly:"$100",features:[{icon:"mdi-web",text:"Up to 20 drivers"},{icon:"mdi-harddisk",text:"10 GB storage"},{icon:"mdi-signal",text:"500 GB bandwidth"},{icon:"mdi-account",text:"10 email addreses"},{icon:"mdi-domain",text:"free domain with annual plan"},{icon:"mdi-server",text:"4X pricessing power"},{icon:"mdi-dns",text:"premium DNS"}]}}}},z=M,L=Object(h["a"])(z,O,A,!1,null,null,null),N=L.exports,V={components:{MembershipVue:g,DrugTestVue:j,LocalVue:N},data(){return{}}},F=V,T=(a("96ec"),Object(h["a"])(F,i,n,!1,null,"7b051d82",null));e["a"]=T.exports},"96ec":function(t,e,a){"use strict";a("48f1")}}]);