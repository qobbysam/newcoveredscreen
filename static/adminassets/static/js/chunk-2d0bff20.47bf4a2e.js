(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0bff20"],{"404b":function(e,t,s){"use strict";s.r(t);var a=s("b0af"),i=s("99d9"),l=s("62ad"),n=s("0fd9"),d=function(){var e=this,t=e._self._c;return t(a["a"],[t(i["b"],[t(n["a"],[t(l["a"],{staticClass:"text-center mx-auto",attrs:{cols:10}},[t("results-table")],1)],1)],1)],1)},o=[],r=s("8336"),c=s("8fea"),u=s("169a"),h=s("ce7e"),m=s("132d"),f=s("2fa4"),x=s("71d9"),b=s("2a7f"),p=function(){var e=this,t=e._self._c;return t(a["a"],[t(i["b"],[t(c["a"],{staticClass:"elevation-1",attrs:{headers:e.headers,items:e.itemsList,"sort-by":"calories"},scopedSlots:e._u([{key:"top",fn:function(){return[t(x["a"],{attrs:{flat:""}},[t(b["b"],[e._v("Drug Tests Results")]),t(h["a"],{staticClass:"mx-4",attrs:{inset:"",vertical:""}}),t(f["a"]),t(u["a"],{attrs:{"max-width":"500px"},model:{value:e.dialogDelete,callback:function(t){e.dialogDelete=t},expression:"dialogDelete"}},[t(a["a"],[t(i["c"],{staticClass:"text-h5"},[e._v("Are you sure you want to delete this employee? ")]),t(i["a"],[t(f["a"]),t(r["a"],{attrs:{color:"blue darken-1",text:""},on:{click:e.closeDelete}},[e._v("Cancel")]),t(r["a"],{attrs:{color:"blue darken-1",text:""},on:{click:e.deleteItemConfirm}},[e._v("OK")]),t(f["a"])],1)],1)],1)],1)]},proxy:!0},{key:"item.actions",fn:function({item:s}){return[t(m["a"],{attrs:{small:""},on:{click:function(t){return e.deleteItem(s)}}},[e._v(" mdi-delete ")])]}},{key:"no-data",fn:function(){return[t(m["a"],[e._v(" mdi-empty ")]),e._v(" No orders Yet ")]},proxy:!0}])})],1)],1)},v=[],g=(s("14d9"),{components:{},data(){return{employees:[],headers:[{text:"",align:"start",sortable:!1,value:"name"},{text:"Products",align:"start",sortable:!1,value:"name"},{text:"Quantity",align:"start",sortable:!1,value:"quantity"},{text:"Amount",align:"start",sortable:!1,value:"price"},{text:"Actions",value:"actions",sortable:!1}]}},computed:{itemsList(){return this.employees}},watch:{dialog(e){e||this.close()},dialogDelete(e){e||this.closeDelete()}},created(){},methods:{deleteItem(e){this.editedIndex=this.desserts.indexOf(e),this.editedItem=Object.assign({},e),this.dialogDelete=!0},deleteItemConfirm(){this.desserts.splice(this.editedIndex,1),this.closeDelete()},close(){this.dialog=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},closeDelete(){this.dialogDelete=!1,this.$nextTick(()=>{this.editedItem=Object.assign({},this.defaultItem),this.editedIndex=-1})},save(){this.editedIndex>-1?Object.assign(this.desserts[this.editedIndex],this.editedItem):this.desserts.push(this.editedItem),this.close()}}}),I=g,k=s("2877"),y=Object(k["a"])(I,p,v,!1,null,null,null),_=y.exports,D={components:{ResultsTable:_}},w=D,O=Object(k["a"])(w,d,o,!1,null,null,null);t["default"]=O.exports}}]);