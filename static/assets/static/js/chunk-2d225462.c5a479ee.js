(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d225462"],{e463:function(t,c,s){"use strict";s.r(c);var o=s("8336"),a=s("b0af"),i=s("99d9"),e=s("62ad"),r=s("a523"),d=s("adda"),n=s("0fd9"),u=function(){var t=this,c=t._self._c;return c("section",[t.loading?t._e():c(r["a"],[c(n["a"],[c(e["a"],{staticClass:"mx-auto",attrs:{cols:"12",md:"8",lg:"8",xl:"8"}},[c(a["a"],{attrs:{height:"100vh"}},[c(i["c"],[c(n["a"],{staticClass:"mx-auto pt-10 mt-10"},[c(e["a"],[c(d["a"],{attrs:{"max-height":"150","max-width":"250",src:t.focusProduct.images[0].original}})],1),c(e["a"],[c("h1",[t._v(t._s(t.focusProduct.title))]),c("p",{staticClass:"price"},[t._v(" $ "+t._s(t.focusPrice))]),c("div",{staticClass:"description",domProps:{innerHTML:t._s(t.focusProduct.description)}}),c("div",{},[c(o["a"],{attrs:{color:"primary"},on:{click:t.handleAddBasket}},[t._v(" Add To Basket ")])],1)])],1)],1)],1)],1)],1)],1)],1)},l=[],p=s("7adc"),h={components:{},data(){return{product:{},price:null,loading:!0}},props:{productid:String},computed:{focusProduct(){return this.product},focusPrice(){return this.price}},async created(){await this.setLocalProduct(),await this.getPrice(),this.loading=!1},mounted(){},methods:{async setLocalProduct(){await Object(p["d"])(this.productid).then(t=>{this.product={...t},console.log(t)}).catch(t=>{this.product={},console.log(t)})},async getPrice(){console.log(this.focusProduct.price),Object(p["e"])(this.focusProduct.price).then(t=>{console.log(t),this.price=t.incl_tax}).catch(t=>{console.log(t)})},handleAddBasket(){let t={},c=this.product;const s={options:t,product:c,price:this.focusPrice};this.$store.dispatch("addMembershipToCart",s)}}},g=h,f=s("2877"),m=Object(f["a"])(g,u,l,!1,null,null,null);c["default"]=m.exports}}]);