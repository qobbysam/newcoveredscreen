(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-01e8717a"],{"4b1e":function(t,e,a){"use strict";a.r(e);var s=a("62ad"),i=a("a523"),r=a("0fd9"),o=function(){var t=this,e=t._self._c;return e("div",[e("hero"),e(i["a"],{staticClass:"page-homepage",attrs:{"fill-height":"",fluid:""}},[e(r["a"],[e(s["a"],[e("hero")],1)],1),e(r["a"],[e(s["a"],{attrs:{cols:12}})],1)],1)],1)},n=[],l=(a("14d9"),a("8336")),c=a("b0af"),d=a("99d9"),h=a("0e8f"),u=a("132d"),m=a("a722"),f=(a("94aa"),a("a026")),p=f["a"].extend({name:"translatable",props:{height:Number},data:()=>({elOffsetTop:0,parallax:0,parallaxDist:0,percentScrolled:0,scrollTop:0,windowHeight:0,windowBottom:0}),computed:{imgHeight(){return this.objHeight()}},beforeDestroy(){window.removeEventListener("scroll",this.translate,!1),window.removeEventListener("resize",this.translate,!1)},methods:{calcDimensions(){const t=this.$el.getBoundingClientRect();this.scrollTop=window.pageYOffset,this.parallaxDist=this.imgHeight-this.height,this.elOffsetTop=t.top+this.scrollTop,this.windowHeight=window.innerHeight,this.windowBottom=this.scrollTop+this.windowHeight},listeners(){window.addEventListener("scroll",this.translate,!1),window.addEventListener("resize",this.translate,!1)},objHeight(){throw new Error("Not implemented !")},translate(){this.calcDimensions(),this.percentScrolled=(this.windowBottom-this.elOffsetTop)/(parseInt(this.height)+this.windowHeight),this.parallax=Math.round(this.parallaxDist*this.percentScrolled)}}}),g=a("58df");const b=Object(g["a"])(p);var w=b.extend().extend({name:"v-parallax",props:{alt:{type:String,default:""},height:{type:[String,Number],default:500},src:String,srcset:String},data:()=>({isBooted:!1}),computed:{styles(){return{display:"block",opacity:this.isBooted?1:0,transform:`translate(-50%, ${this.parallax}px)`}}},mounted(){this.init()},methods:{init(){const t=this.$refs.img;t&&(t.complete?(this.translate(),this.listeners()):t.addEventListener("load",()=>{this.translate(),this.listeners()},!1),this.isBooted=!0)},objHeight(){return this.$refs.img.naturalHeight}},render(t){const e={staticClass:"v-parallax__image",style:this.styles,attrs:{src:this.src,srcset:this.srcset,alt:this.alt},ref:"img"},a=t("div",{staticClass:"v-parallax__image-container"},[t("img",e)]),s=t("div",{staticClass:"v-parallax__content"},this.$slots.default);return t("div",{staticClass:"v-parallax",style:{height:`${this.height}px`},on:this.$listeners},[a,s])}}),x=a("8654"),v=function(){var t=this,e=t._self._c;return e("div",[e("section",[e(w,{attrs:{src:t.imageLink.sub_main,height:"600"}},[e(m["a"],{staticClass:"white--text",attrs:{column:"","align-center":"","justify-center":""}},[e("h1",{staticClass:"white--text mb-2 display-1 text-xs-center",staticStyle:{"font-weight":"900","text-shadow":"3px 2px #000000"}},[t._v(" The social network for epic content ")]),e("div",{staticClass:"white--text subheading mb-3 text-xs-center",staticStyle:{"font-weight":"900","text-shadow":"2px 2px #000000"}},[t._v(" Unlesh your creativity without limitations ")]),e(l["a"],{staticClass:"blue lighten-2 mt-5",attrs:{dark:"",large:"",href:"/pre-made-themes"}},[t._v(" Get Started ")])],1)],1)],1),e("section",[e(m["a"],{staticClass:"my-5",attrs:{column:"",wrap:"","align-center":""}},[e(h["a"],{staticClass:"my-3",attrs:{xs12:"",sm4:""}},[e("div",{staticClass:"text-xs-center"},[e("h2",{staticClass:"headline"},[t._v("The best way to share your amazing stuff")]),e("span",{staticClass:"subheading"},[t._v(" No more restrictions, no more limits ")])])]),e(h["a"],{attrs:{xs12:""}},[e(i["a"],{attrs:{"grid-list-xl":""}},[e(m["a"],{attrs:{row:"",wrap:"","align-center":""}},[e(h["a"],{attrs:{xs12:"",md4:""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["c"],{staticClass:"text-xs-center"},[e(u["a"],{staticClass:"blue--text text--lighten-2",attrs:{"x-large":""}},[t._v("public")])],1),e(d["d"],{staticClass:"layout justify-center",attrs:{"primary-title":""}},[e("div",{staticClass:"headline text-xs-center"},[t._v("Reach the world")])]),e(d["c"],[t._v(" Show your stuff to the whole community of Endorfine not only to your mum or your friends. We love making good content viral. In this moment Endorfine is used by artists who are not famous but that want to share their works to the world. Unfortunately with other social networks this is hard, slow and sometime expensive. ")])],1)],1),e(h["a"],{attrs:{xs12:"",md4:""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["c"],{staticClass:"text-xs-center"},[e(u["a"],{staticClass:"blue--text text--lighten-2",attrs:{"x-large":""}},[t._v("flash_on")])],1),e(d["d"],{staticClass:"layout justify-center",attrs:{"primary-title":""}},[e("div",{staticClass:"headline"},[t._v("Fast feedback")])]),e(d["c"],[t._v(" Time is important, we don't want you to waste it. Here you can get a massive feedback from real users in minutes. And if your stuff is appreciated you won't only get positive feedback but also lovely and sincere fans ")])],1)],1),e(h["a"],{attrs:{xs12:"",md4:""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["c"],{staticClass:"text-xs-center"},[e(u["a"],{staticClass:"blue--text text--lighten-2",attrs:{"x-large":""}},[t._v("share")])],1),e(d["d"],{staticClass:"layout justify-center",attrs:{"primary-title":""}},[e("div",{staticClass:"headline text-xs-center"},[t._v("Create new connections")])]),e(d["c"],[t._v(" Imagine if you can directly speak with the world's population. Don't you think it would be easier to find nice people to interact with? Endorfine is both local and global and help you to connect without limitations with people from your city, your state and your universe! ")])],1)],1)],1)],1)],1)],1)],1),e("section",[e(w,{attrs:{src:t.imageLink.main,height:"380"}},[e(m["a"],{attrs:{column:"","align-center":"","justify-center":""}},[e("div",{staticClass:"headline white--text mb-3 text-xs-center"},[t._v(" Endorfine is a social network that allows everyone to reach a huge audience with a tap ")]),e("em",[t._v("With the power of Endorfine you don't need to be famous or post pics of cute cats in order to get visibility")]),e(l["a"],{staticClass:"blue lighten-2 mt-5",attrs:{dark:"",large:"",href:"/pre-made-themes"}},[t._v(" Get more info ")])],1)],1)],1),e("section",[e(i["a"],{attrs:{"grid-list-md":""}},[e(m["a"],{attrs:{row:"",wrap:""}},[e(h["a"],{staticClass:"mt-5",attrs:{xs12:"","text-xs-center":""}},[e("div",{staticClass:"headline"},[t._v("Are you amazed? Stay tuned!")]),e("br"),e("div",[t._v(" We are lunching the beta in a few time. If you want to be one of the first Endorfine users we will email you as soon as we're ready. In the beginning only few people will test before the launch. Let us know how Endorfine will help you! ")])]),e(h["a"],{attrs:{xs8:"","offset-xs2":""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["c"],[t.subscribed?t._e():e(h["a"],{attrs:{xs12:""}},[e(x["a"],{attrs:{filled:"",label:"Email address",rules:t.emailRules,hint:"Enter your email!","persistent-hint":""},model:{value:t.email,callback:function(e){t.email=e},expression:"email"}})],1),t.subscribed?t._e():e(h["a"],{attrs:{xs12:""}},[e(x["a"],{attrs:{filled:"","multi-line":"",label:"Bio and curiosities"}})],1),t.subscribed?t._e():e(h["a"],{staticClass:"text-xs-center",attrs:{xs12:""}},[e(l["a"],{staticClass:"blue lighten-2 mb-5",attrs:{dark:"",large:""},on:{click:t.subscribe}},[t._v("Get in touch")])],1),t.subscribed?e(h["a"],{staticClass:"text-xs-center",attrs:{xs12:""}},[e(l["a"],{staticClass:"green lighten-2 mb-5",attrs:{dark:"",large:""}},[t._v("Welcome on board!")])],1):t._e()],1)],1)],1)],1)],1)],1),e("section",[e(w,{attrs:{src:t.imageLink.social_cover,height:"380"}},[e(m["a"],{attrs:{column:"","align-center":"","justify-center":""}},[e("div",{staticClass:"headline white--text mb-3 text-xs-center"},[t._v(" We are dropping cool news and opportunities on socials ")])]),e(m["a"],{attrs:{"justify-space-around":"","justify-center":""}},[e(u["a"],{attrs:{"x-large":"",dark:""}},[t._v("fab fa-facebook-f")]),e(u["a"],{attrs:{"x-large":"",dark:""}},[t._v("fab fa-twitter")]),e(u["a"],{attrs:{"x-large":"",dark:""}},[t._v("fab fa-reddit-alien")]),e(u["a"],{attrs:{"x-large":"",dark:""}},[t._v("fab fa-instagram")]),e(u["a"],{attrs:{"x-large":"",dark:""}},[t._v("fab fa-discord")])],1)],1)],1),e("section",[e(i["a"],{attrs:{"grid-list-xl":""}},[e(m["a"],{staticClass:"my-5",attrs:{row:"",wrap:"","justify-center":""}},[e(h["a"],{attrs:{xs12:"",sm4:""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["d"],{staticClass:"layout justify-center",attrs:{"primary-title":""}},[e("div",{staticClass:"headline"},[t._v("Company info")])]),e(d["c"],[t._v(" We are not a company. We hate companies. Just imagine us like the guys from the Silicon Valley series. ")])],1)],1),e(h["a"],{attrs:{xs12:"",sm4:"","offset-sm1":""}},[e(c["a"],{staticClass:"elevation-0 transparent"},[e(d["d"],{staticClass:"layout justify-center",attrs:{"primary-title":""}},[e("div",{staticClass:"headline"},[t._v("We are hiring")])]),e(d["c"],[t._v(" Are you a creative person? Do you like techy stuff? Complete the email form by writing your skills and interests ")])],1)],1)],1)],1)],1),e("section",[e(i["a"],[e(m["a"],[e(h["a"],{staticClass:"text-xs-center",attrs:{xs12:""}},[e("img",{attrs:{height:"200px",src:t.imageLink.logo}})])],1)],1)],1)])},y=[],_={name:"Hero",data:function(){return{title:"Endorfine",imageLink:{main:"https://firebasestorage.googleapis.com/v0/b/endorfinevue.appspot.com/o/assets%2Fb13f0434-b228-11e6-8e5d-5252025056ab_web_scale_0.4666667_0.4666667__.jpg?alt=media&token=660df23e-599e-434b-9313-ba69c973eeea",sub_main:"https://firebasestorage.googleapis.com/v0/b/endorfinevue.appspot.com/o/assets%2FNight-Club-Clubbing-Jobs-Abroad2.jpg?alt=media&token=82bbda7d-5df4-430b-9217-adaf1c8485c5",logo:"https://firebasestorage.googleapis.com/v0/b/endorfinevue.appspot.com/o/assets%2Fandroid-chrome-512x512.png?alt=media&token=8a0a66f6-4741-4ff6-8f28-eb9ec74374df",social_cover:"https://firebasestorage.googleapis.com/v0/b/endorfinevue.appspot.com/o/assets%2Fo-NIGHTCLUB-facebook.jpg?alt=media&token=cefc5c4c-9714-41da-9c22-f63caf5e89a4"},email:"",emailRules:[t=>{return!!t||"E-mail is required"},t=>/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(t)||"E-mail must be valid"],subscribed:!1}},computed:{imgHeight:function(){var t=320;return console.log("new image height is "+(this.pageHeight-t)),this.pageHeight-t}},mounted:function(){},methods:{subscribe:function(){this.subscribed=!this.subscribed}}},C=_,k=(a("af98"),a("2877")),j=Object(k["a"])(C,v,y,!1,null,"05b1573d",null),H=j.exports;const E="page-homepage";var S={name:E,components:{Hero:H},data(){return{loading:!1,formValid:!1,formModel:{username:"admin",password:"admin"},formRule:{username:[t=>!!t||this.$t("rule.required",["username"])],password:[t=>!!t||this.$t("rule.required",["password"])]},socialIcons:[{text:"Google",icon:"mdi-google"},{text:"Facebook",icon:"mdi-facebook"},{text:"Twitter",icon:"mdi-twitter"}]}},computed:{},methods:{handleLogin(){this.$refs.form.validate()&&(this.loading=!0,this.$store.dispatch("demoLogin",this.formModel).then(()=>{const t=this.$route.query.redirect,e=t?{path:t}:{path:"/"};this.$router.push(e),this.loading=!1}).catch(()=>{window._VMA.$emit("SHOW_SNACKBAR",{show:!0,text:"Auth Failed",color:"error"}),this.loading=!1}))},handleRegister(){console.log(this)},handleSocialLogin(){}}},L=S,$=Object(k["a"])(L,o,n,!1,null,"65ff61fa",null);e["default"]=$.exports},"6d05":function(t,e,a){},"94aa":function(t,e,a){},af98:function(t,e,a){"use strict";a("6d05")}}]);