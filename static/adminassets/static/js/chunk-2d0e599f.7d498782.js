(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0e599f"],{"94d2":function(e,t,s){"use strict";s.r(t);var a=s("b0af"),i=s("99d9"),l=s("62ad"),r=s("0fd9"),o=function(){var e=this,t=e._self._c;return t(a["a"],[e.loading?e._e():t(i["b"],[t(r["a"],[t(l["a"],{staticClass:"text-center mx-auto",attrs:{cols:8}},[t("orders-table")],1)],1)],1)],1)},d=[],n=s("8336"),c=s("8fea"),u=s("169a"),h=s("ce7e"),m=s("132d"),f=s("2fa4"),g=s("71d9"),w=s("2a7f"),x=function(){var e=this,t=e._self._c;return t(a["a"],[t(i["b"],[t(c["a"],{staticClass:"elevation-1",attrs:{headers:e.headers,items:e.itemsList,"sort-by":"calories"},scopedSlots:e._u([{key:"top",fn:function(){return[t(g["a"],{attrs:{flat:""}},[t(w["b"],[e._v("Past Orders")]),t(h["a"],{staticClass:"mx-4",attrs:{inset:"",vertical:""}}),t(f["a"]),t(u["a"],{model:{value:e.dialogView,callback:function(t){e.dialogView=t},expression:"dialogView"}},[e.showReorder?e._e():t(a["a"],[t(i["c"],{staticClass:"text-h5"},[e._v("Order Details "+e._s(e.focusView.number)+" ")]),t(i["a"],[t(f["a"]),t(n["a"],{attrs:{color:"blue darken-1",text:""},on:{click:e.closeViewDialog}},[e._v("Cancel")]),t(f["a"])],1)],1),t(a["a"],{directives:[{name:"show",rawName:"v-show",value:e.showReorder,expression:"showReorder"}]},[t(i["a"],[t(f["a"]),t(n["a"],{attrs:{color:"blue darken-1",text:""},on:{click:e.closeViewDialog}},[e._v("Cancel")]),t(f["a"])],1)],1)],1)],1)]},proxy:!0},{key:"item.date_placed",fn:function({item:t}){return[e._v(" "+e._s(e.transformDate(t.date_placed))+" ")]}},{key:"item.actions",fn:function({item:s}){return[t(n["a"],{staticClass:"mx-1",attrs:{small:""},on:{click:function(t){return e.handleView(s)}}},[e._v("View")]),t(n["a"],{staticClass:"mx-1",attrs:{small:""},on:{click:function(t){return e.handleReorder(s)}}},[e._v("ReOrder")])]}},{key:"no-data",fn:function(){return[t(m["a"],[e._v(" mdi-empty ")]),e._v(" No orders Yet ")]},proxy:!0}])})],1)],1)},b=[],v=(s("14d9"),s("2f62")),p={components:{},data(){return{orders:[],dialogDelete:null,dialogView:null,focusView:{},showReorder:!1,headers:[{text:"Date",align:"start",sortable:!0,value:"date_placed"},{text:"Products",align:"start",sortable:!1,value:"number"},{text:"Amount",align:"start",sortable:!1,value:"total_incl_tax"},{text:"Actions",value:"actions",sortable:!1}]}},watch:{dialog(e){e||this.close()},dialogDelete(e){e||this.closeDelete()}},created(){},computed:{...Object(v["c"])(["getAllOrders"]),itemsList:{get(){return this.getAllOrders}}},mounted(){console.log(this.itemsList)},methods:{transformDate(e){var t=new Date(e);return t.toISOString().substring(0,10)},handleView(e){this.focusView={...e},this.dialogView=!0},handleReorder(e){},closeViewDialog(){this.dialogView=!1},deleteItem(e){this.editedIndex=this.desserts.indexOf(e),this.editedItem=Object.assign({},e),this.dialogDelete=!0},deleteItemConfirm(){this.desserts.splice(this.editedIndex,1),this.closeDelete()},close(){this.dialog=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},closeDelete(){this.dialogDelete=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},save(){this.editedIndex>-1?Object.assign(this.desserts[this.editedIndex],this.editedItem):this.desserts.push(this.editedItem),this.close()}}},_=p,k=s("2877"),I=Object(k["a"])(_,x,b,!1,null,null,null),O=I.exports,D={components:{OrdersTable:O},data(){return{loading:!0}},async mounted(){await this.$store.dispatch("LoadOrders").finally(()=>{this.loading=!1})}},V=D,y=Object(k["a"])(V,o,d,!1,null,null,null);t["default"]=y.exports}}]);