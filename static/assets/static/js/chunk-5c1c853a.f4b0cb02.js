(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5c1c853a"],{"1e6c":function(e,t,l){"use strict";var s=l("9d65"),a=l("4e82"),r=l("c3f0"),o=l("80d2"),i=l("58df");const n=Object(i["a"])(s["a"],Object(a["a"])("windowGroup","v-window-item","v-window"));t["a"]=n.extend().extend().extend({name:"v-window-item",directives:{Touch:r["a"]},props:{disabled:Boolean,reverseTransition:{type:[Boolean,String],default:void 0},transition:{type:[Boolean,String],default:void 0},value:{required:!1}},data(){return{isActive:!1,inTransition:!1}},computed:{classes(){return this.groupClasses},computedTransition(){return this.windowGroup.internalReverse?"undefined"!==typeof this.reverseTransition?this.reverseTransition||"":this.windowGroup.computedTransition:"undefined"!==typeof this.transition?this.transition||"":this.windowGroup.computedTransition}},methods:{genDefaultSlot(){return this.$slots.default},genWindowItem(){return this.$createElement("div",{staticClass:"v-window-item",class:this.classes,directives:[{name:"show",value:this.isActive}],on:this.$listeners},this.genDefaultSlot())},onAfterTransition(){this.inTransition&&(this.inTransition=!1,this.windowGroup.transitionCount>0&&(this.windowGroup.transitionCount--,0===this.windowGroup.transitionCount&&(this.windowGroup.transitionHeight=void 0)))},onBeforeTransition(){this.inTransition||(this.inTransition=!0,0===this.windowGroup.transitionCount&&(this.windowGroup.transitionHeight=Object(o["h"])(this.windowGroup.$el.clientHeight)),this.windowGroup.transitionCount++)},onTransitionCancelled(){this.onAfterTransition()},onEnter(e){this.inTransition&&this.$nextTick(()=>{this.computedTransition&&this.inTransition&&(this.windowGroup.transitionHeight=Object(o["h"])(e.clientHeight))})}},render(e){return e("transition",{props:{name:this.computedTransition},on:{beforeEnter:this.onBeforeTransition,afterEnter:this.onAfterTransition,enterCancelled:this.onTransitionCancelled,beforeLeave:this.onBeforeTransition,afterLeave:this.onAfterTransition,leaveCancelled:this.onTransitionCancelled,enter:this.onEnter}},this.showLazyContent(()=>[this.genWindowItem()]))}})},d59c:function(e,t,l){"use strict";l.r(t);var s=l("8336"),a=l("b0af"),r=l("99d9"),o=l("62ad"),i=l("a523"),n=l("0fd9"),d=function(){var e=this,t=e._self._c;return t("section",[t(i["a"],[t(n["a"],[t(o["a"],{attrs:{cols:"12"}},[t(a["a"],{staticClass:"mx-auto"},[t(r["c"],[t("div",[e._v(e._s(e.focused.title))]),t("p",{domProps:{innerHTML:e._s(e.focused.description)}}),t("div",{staticClass:"text--primary"},[e._v(" well meaning and kindly."),t("br"),e._v(' "a benevolent smile" ')])]),t(r["c"],[t("DrugtestForm")],1),t(r["a"],[t(s["a"],{attrs:{color:"deep-purple accent-4"}},[e._v(" Add To Basket ")])],1)],1)],1)],1)],1)],1)},c=[],m=l("2f62"),u=l("ce7e"),h=function(){var e=this,t=e._self._c;return t(i["a"],{attrs:{loading:e.loading,outlined:""}},[t(r["d"],[e._v(e._s(e.formTitle))]),t(u["a"]),t(n["a"],[t("EmployeeFormVue")],1),t(n["a"],[t("DrugtestDetailVue")],1),t(u["a"],{staticClass:"mt-5"})],1)},f=[],p=(l("14d9"),l("2e4b")),b=l("4bd4"),g=l("e449"),v=l("b974"),x=l("8654"),M=function(){var e=this,t=e._self._c;return t(a["a"],{staticClass:"mx-auto"},[t(r["d"],[e._v(e._s(e.formTitle))]),t(u["a"]),t(r["c"],[t(n["a"],[t(o["a"],{attrs:{xl:10,lg:10,md:10,sm:12,xs:12}},[t(v["a"],{attrs:{outlined:"",label:e.form.gender.label,placeholder:e.form.gender.placeholder,rules:e.form.gender.rules,items:e.genders,required:""},model:{value:e.formModel.gender,callback:function(t){e.$set(e.formModel,"gender",t)},expression:"formModel.gender"}})],1)],1)],1),t(r["c"],[t(b["a"],{ref:"form",model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t(n["a"],[t(o["a"],{attrs:{cols:12,md:4,lg:4,xl:4,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.firstname.label,placeholder:e.form.firstname.placeholder,required:"",rules:e.form.firstname.rules},model:{value:e.formModel.firstname,callback:function(t){e.$set(e.formModel,"firstname",t)},expression:"formModel.firstname"}})],1),t(o["a"],{attrs:{cols:12,md:4,lg:4,xl:4,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.middlename.label,placeholder:e.form.middlename.placeholder,required:"",rules:e.form.middlename.rules},model:{value:e.formModel.middlename,callback:function(t){e.$set(e.formModel,"middlename",t)},expression:"formModel.middlename"}})],1),t(o["a"],{attrs:{cols:12,md:4,lg:4,xl:4,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.lastname.label,placeholder:e.form.lastname.placeholder,required:"",rules:e.form.lastname.rules},model:{value:e.formModel.lastname,callback:function(t){e.$set(e.formModel,"lastname",t)},expression:"formModel.lastname"}})],1),t(o["a"],{attrs:{cols:10}},[t("div",[t(g["a"],{ref:"menu",attrs:{"close-on-content-click":!1,transition:"scale-transition","offset-y":"","min-width":"auto"},scopedSlots:e._u([{key:"activator",fn:function({on:l,attrs:s}){return[t(x["a"],e._g(e._b({attrs:{label:"Birthday date","prepend-icon":"mdi-calendar",readonly:""},model:{value:e.formModel.date,callback:function(t){e.$set(e.formModel,"date",t)},expression:"formModel.date"}},"v-text-field",s,!1),l))]}}]),model:{value:e.formModel.menu,callback:function(t){e.$set(e.formModel,"menu",t)},expression:"formModel.menu"}},[t(p["a"],{attrs:{"active-picker":e.formModel.activePicker,max:new Date(Date.now()-6e4*(new Date).getTimezoneOffset()).toISOString().substr(0,10),min:"1950-01-01"},on:{"update:activePicker":function(t){return e.$set(e.formModel,"activePicker",t)},"update:active-picker":function(t){return e.$set(e.formModel,"activePicker",t)},change:e.save},model:{value:e.formModel.date,callback:function(t){e.$set(e.formModel,"date",t)},expression:"formModel.date"}})],1)],1)]),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.email.label,placeholder:e.form.email.placeholder,"append-icon":e.form.email.icon,required:"",rules:e.form.email.rules},model:{value:e.formModel.email,callback:function(t){e.$set(e.formModel,"email",t)},expression:"formModel.email"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.phone.label,placeholder:e.form.phone.placeholder,required:"",rules:e.form.phone.rules,"append-icon":e.form.phone.icon},model:{value:e.formModel.phone,callback:function(t){e.$set(e.formModel,"phone",t)},expression:"formModel.phone"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(v["a"],{attrs:{outlined:"",label:e.form.licensestate.label,placeholder:e.form.licensestate.placeholder,rules:e.form.licensestate.rules,items:e.states,required:""},model:{value:e.formModel.licensestate,callback:function(t){e.$set(e.formModel,"licensestate",t)},expression:"formModel.licensestate"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.form.licensenumber.label,placeholder:e.form.licensenumber.placeholder,required:"",rules:e.form.licensenumber.rules,"append-icon":e.form.licensenumber.icon},model:{value:e.formModel.licensenumber,callback:function(t){e.$set(e.formModel,"licensenumber",t)},expression:"formModel.licensenumber"}})],1)],1)],1)],1)],1)},T=[],w=l("10b8"),q={props:{userId:[Number,String]},data:()=>({genders:["male","female","other"],states:["OH","PA","MI"],valid:!0,loading:!1,cardTypes:[{value:"visa",text:"Visa Express"},{value:"master",text:"Mastard"}],formModel:{username:null,password:null,email:null,phone:null,firstname:null,lastname:null,middlename:null,gender:"male",card_type:null,picker:null,activePicker:null,date:null,menu:!1,licensestate:null,licensenumber:null},form:{username:{label:"Username",placeholder:"Tookit",rules:[e=>!!e||"This field is required"]},card_type:{label:"Card type",placeholder:"Mater",rules:[e=>!!e||"This field is required"]},password:{label:"Password",placeholder:"xxx",rules:[e=>!!e||"This field is required"]},email:{label:"Email",placeholder:"wangqiangshen@gmail.com",icon:"mdi-email",rules:[e=>!!e||"This field is required",e=>w["a"].test(e)||"Invalid email"]},phone:{label:"phone",placeholder:"18682157492",icon:"mdi-phone",rules:[e=>!!e||"This field is required"]},firstname:{label:"Firstname",placeholder:"Firstname",rules:[e=>!!e||"This field is required"]},lastname:{label:"Lastname",placeholder:"Lastname",rules:[e=>!!e||"This field is required"]},middlename:{label:"Middlename",placeholder:"Middlename",rules:[e=>!!e||"This field is required"]},gender:{label:"Employee Selector",placeholder:"gender",rules:[e=>!!e||"This field is required"]},licensestate:{label:"LicenseState",placeholder:"Select State",rules:[e=>!!e||"This field is required"]},licensenumber:{label:"License Number",placeholder:"OH8894443",rules:[e=>!!e||"This field is required"]}},formHasErrors:!1}),computed:{formTitle(){return"Employee form User"}},watch:{userId:{handler(e){e&&this.getItemById(e)},immediate:!0},menu(e){e&&setTimeout(()=>this.activePicker="YEAR")}},methods:{save(e){this.$refs.menu.save(e)},getItemById(e){this.loading=!0,this.$store.dispatch("getUserById",e).then(({data:e})=>{this.formModel=e,this.loading=!1}).catch(()=>{this.loading=!1})},handleCancelForm(){this.$refs.form.reset()},handleSubmitForm(){this.loading=!0,this.$refs.form.validate()&&(this.userId?this.updateUser(this.userId):this.createUser())},updateUser(){this.$store.dispatch("updateUser",{id:this.userId,data:this.formModel}).then(()=>{this.loading=!1}).catch(()=>{this.loading=!1})},createUser(){this.$store.dispatch("createUser",this.formModel).then(({data:e})=>{this.loading=!1,this.$router.push({path:`/acl/user/item/${e.id}`})}).catch(()=>{this.loading=!1})}}},$=q,y=l("2877"),k=Object(y["a"])($,M,T,!1,null,null,null),I=k.exports,_=l("b73d"),C=l("71a3"),S=l("1e6c"),U=S["a"].extend({name:"v-tab-item",props:{id:String},methods:{genWindowItem(){const e=S["a"].options.methods.genWindowItem.call(this);return e.data.domProps=e.data.domProps||{},e.data.domProps.id=this.id||this.value,e}}}),B=l("fe57"),E=l("aac8"),F=function(){var e=this,t=e._self._c;return t(a["a"],{attrs:{loading:e.loading,cols:8,tile:""}},[t(r["d"],[e._v(e._s(e.formTitle))]),t(u["a"]),t(r["c"],[t(b["a"],{ref:"form",model:{value:e.valid,callback:function(t){e.valid=t},expression:"valid"}},[t(n["a"],[t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(v["a"],{attrs:{outlined:"",label:e.form.typeofcollection.label,placeholder:e.form.typeofcollection.placeholder,rules:e.form.typeofcollection.rules,items:e.typeofcollectionitems,"item-text":"label","item-value":"value",required:""},model:{value:e.formModel.typeofcollection,callback:function(t){e.$set(e.formModel,"typeofcollection",t)},expression:"formModel.typeofcollection"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(v["a"],{attrs:{outlined:"",label:e.form.testreason.label,placeholder:e.form.testreason.placeholder,rules:e.form.testreason.rules,items:e.testreasonitems,"item-text":"label","item-value":"value",required:""},model:{value:e.formModel.testreason,callback:function(t){e.$set(e.formModel,"testreason",t)},expression:"formModel.testreason"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(_["a"],{attrs:{label:e.form.observerequested.label},model:{value:e.formModel.observerequested,callback:function(t){e.$set(e.formModel,"observerequested",t)},expression:"formModel.observerequested"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(_["a"],{attrs:{label:e.form.splitrequested.label},model:{value:e.formModel.splitrequested,callback:function(t){e.$set(e.formModel,"splitrequested",t)},expression:"formModel.splitrequested"}})],1),t(o["a"],{attrs:{cols:12}},[t(i["a"],[t(n["a"],[t(o["a"],[t(b["a"],[t(n["a"],[t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(x["a"],{attrs:{disabled:""},model:{value:e.formModel.collectionlocation,callback:function(t){e.$set(e.formModel,"collectionlocation",t)},expression:"formModel.collectionlocation"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(x["a"],{attrs:{outlined:"",label:e.searchform.locationsearch.label,placeholder:e.searchform.locationsearch.placeholder,required:"",rules:e.searchform.locationsearch.rules,"append-icon":e.searchform.locationsearch.icon},model:{value:e.locationSearchModel.searchtext,callback:function(t){e.$set(e.locationSearchModel,"searchtext",t)},expression:"locationSearchModel.searchtext"}})],1),t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(s["a"],[e._v("Search Location")])],1)],1)],1)],1)],1),t(n["a"],[t(o["a"],{attrs:{cols:12,md:9,lg:9,xl:9,sm:12,xs:12}},[t(n["a"],[t(o["a"],{attrs:{cols:12,md:6,lg:6,xl:6,sm:12,xs:12}},[t(B["a"],{attrs:{"slider-color":"yellow"},model:{value:e.locationsearch,callback:function(t){e.locationsearch=t},expression:"locationsearch"}},[t(C["a"],{attrs:{href:"#tab-list"}},[e._v("List Results")]),t(C["a"],{attrs:{href:"#tab-map"}},[e._v("Map Results")])],1)],1)],1),t(E["a"],{model:{value:e.locationsearch,callback:function(t){e.locationsearch=t},expression:"locationsearch"}},[t(U,{attrs:{value:"tab-list"}},[t("p",[e._v("List info")])]),t(U,{attrs:{value:"tab-map"}},[t("p",[e._v("Map info")])])],1)],1)],1)],1)],1)],1)],1)],1),t(u["a"],{staticClass:"mt-5"})],1)},D=[],L={props:{userId:[Number,String]},data:()=>({text:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",genders:["male","female","other"],typeofcollectionitems:[{label:"Urine Test",value:"1xxx"},{label:"Breath Test",value:"2xxx"}],testreasonitems:[{label:"Pre-Employment",value:"1xxx"},{label:"Post Accident",value:"2xxx"}],locationsearch:null,valid:!0,loading:!1,locationSearchModel:{searchtext:null},formModel:{typeofcollection:null,testreason:null,observerequested:null,splitrequested:null,collectionlocation:"null"},searchform:{locationsearch:{label:"Search Location",placeholder:"Enter Zipcode or CityName",rules:[e=>!!e||"This field is required"]}},form:{typeofcollection:{label:"Type Of Collection",placeholder:"Collection type",rules:[e=>!!e||"This field is required"]},testreason:{label:"Test Reason",placeholder:"xxx",rules:[e=>!!e||"This field is required"]},observerequested:{label:"Observe Requested",placeholder:"observe requested",rules:[e=>!!e||"This field is required"]},splitrequested:{label:"Split Specimen Requested",placeholder:"split specimen",rules:[e=>!!e||"This field is required"]},collectionlocation:{label:"Collection Location",placeholder:"Collection Location",rules:[e=>!!e||"This field is required"]}},formHasErrors:!1}),computed:{formTitle(){return"DrugTestDetail"}},watch:{userId:{handler(e){e&&this.getItemById(e)},immediate:!0}},methods:{getItemById(e){this.loading=!0,this.$store.dispatch("getUserById",e).then(({data:e})=>{this.formModel=e,this.loading=!1}).catch(()=>{this.loading=!1})},handleCancelForm(){this.$refs.form.reset()},handleSubmitForm(){this.loading=!0,this.$refs.form.validate()&&(this.userId?this.updateUser(this.userId):this.createUser())},updateUser(){this.$store.dispatch("updateUser",{id:this.userId,data:this.formModel}).then(()=>{this.loading=!1}).catch(()=>{this.loading=!1})},createUser(){this.$store.dispatch("createUser",this.formModel).then(({data:e})=>{this.loading=!1,this.$router.push({path:`/acl/user/item/${e.id}`})}).catch(()=>{this.loading=!1})}}},P=L,O=Object(y["a"])(P,F,D,!1,null,null,null),G=O.exports,H={components:{EmployeeFormVue:I,DrugtestDetailVue:G},props:{userId:[Number,String]},data:()=>({genders:["male","female","other"],valid:!0,loading:!1,formModel:{username:null,password:null,email:null,phone:null,firstname:null,lastname:null,gender:"male"},form:{username:{label:"Username",placeholder:"Tookit",rules:[e=>!!e||"This field is required"]},password:{label:"Password",placeholder:"xxx",rules:[e=>!!e||"This field is required"]},email:{label:"Email",placeholder:"wangqiangshen@gmail.com",rules:[e=>!!e||"This field is required",e=>w["a"].test(e)||"Invalid email"]},phone:{label:"phone",placeholder:"18682157492",rules:[e=>!!e||"This field is required"]},firstname:{label:"Firstname",placeholder:"Firstname",rules:[e=>!!e||"This field is required"]},lastname:{label:"Lastname",placeholder:"Lastname",rules:[e=>!!e||"This field is required"]},gender:{label:"Gender",placeholder:"gender",rules:[e=>!!e||"This field is required"]}},formHasErrors:!1}),computed:{formTitle(){return"DrugTest Form"}},watch:{userId:{handler(e){e&&this.getItemById(e)},immediate:!0}},methods:{getItemById(e){this.loading=!0,this.$store.dispatch("getUserById",e).then(({data:e})=>{this.formModel=e,this.loading=!1}).catch(()=>{this.loading=!1})},handleCancelForm(){this.$refs.form.reset()},handleSubmitForm(){this.loading=!0,this.$refs.form.validate()&&(this.userId?this.updateUser(this.userId):this.createUser())},updateUser(){this.$store.dispatch("updateUser",{id:this.userId,data:this.formModel}).then(()=>{this.loading=!1}).catch(()=>{this.loading=!1})},createUser(){this.$store.dispatch("createUser",this.formModel).then(({data:e})=>{this.loading=!1,this.$router.push({path:`/acl/user/item/${e.id}`})}).catch(()=>{this.loading=!1})}}},A=H,j=Object(y["a"])(A,h,f,!1,null,null,null),R=j.exports,N={props:["upc"],components:{DrugtestForm:R},computed:{...Object(m["c"])(["getFocusDrugTest"])},mounted(){this.focused={...this.getFocusDrugTest(this.upc)}},methods:{focusedProduct(){return this.getFocusDrugTest(this.upc)}},data(){return{focused:{}}}},V=N,W=Object(y["a"])(V,d,c,!1,null,null,null);t["default"]=W.exports}}]);