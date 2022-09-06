"use strict";(self.webpackChunkraumdeuter_info=self.webpackChunkraumdeuter_info||[]).push([[671],{3905:(e,n,t)=>{t.d(n,{Zo:()=>c,kt:()=>d});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function l(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var s=r.createContext({}),u=function(e){var n=r.useContext(s),t=n;return e&&(t="function"==typeof e?e(n):i(i({},n),e)),t},c=function(e){var n=u(e.components);return r.createElement(s.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},m=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=u(t),d=a,f=m["".concat(s,".").concat(d)]||m[d]||p[d]||o;return t?r.createElement(f,i(i({ref:n},c),{},{components:t})):r.createElement(f,i({ref:n},c))}));function d(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var o=t.length,i=new Array(o);i[0]=m;var l={};for(var s in n)hasOwnProperty.call(n,s)&&(l[s]=n[s]);l.originalType=e,l.mdxType="string"==typeof e?e:a,i[1]=l;for(var u=2;u<o;u++)i[u]=t[u];return r.createElement.apply(null,i)}return r.createElement.apply(null,t)}m.displayName="MDXCreateElement"},9881:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>s,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>l,toc:()=>u});var r=t(7462),a=(t(7294),t(3905));const o={sidebar_position:1},i="intro",l={unversionedId:"intro",id:"intro",title:"intro",description:"prerequisites",source:"@site/docs/intro.md",sourceDirName:".",slug:"/intro",permalink:"/docs/intro",draft:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",next:{title:"examples",permalink:"/docs/category/examples"}},s={},u=[{value:"prerequisites",id:"prerequisites",level:3},{value:"install",id:"install",level:3},{value:"configure",id:"configure",level:3},{value:"create a sequence",id:"create-a-sequence",level:3},{value:"download the sequnce",id:"download-the-sequnce",level:3},{value:"run the sequence",id:"run-the-sequence",level:3}],c={toc:u};function p(e){let{components:n,...t}=e;return(0,a.kt)("wrapper",(0,r.Z)({},c,t,{components:n,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"intro"},"intro"),(0,a.kt)("h3",{id:"prerequisites"},"prerequisites"),(0,a.kt)("p",null,"raumd is a python script, so the prerequisite for using raumd is python, the programming language for running, and pip the package installer for installation. (version>=3) "),(0,a.kt)("p",null,"as far as module goes these are the current requirements:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"argcomplete==2.0.0\ncolorama==0.4.4\ncommonmark==0.9.1\npsutil==5.9.0\nPygments==2.11.2\nrich==11.0.0\npython-json-logger==2.0.2\n\n")),(0,a.kt)("h3",{id:"install"},"install"),(0,a.kt)("p",null,"install the pre-built version from the official python artifactory, using pip:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"pip install raumd\n")),(0,a.kt)("p",null,"install via ",(0,a.kt)("strong",{parentName:"p"},"setup.py")," from source code: "),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"git clone https://github.com/romanbotnari/raumd.git\ncd raumd\npython3 setup.py install  \n")),(0,a.kt)("h3",{id:"configure"},"configure"),(0,a.kt)("p",null,"there is a default configuration that one can change at any time (",(0,a.kt)("em",{parentName:"p"},"using administrative rights"),")."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"raumd configure -show    \n\nurl      : https://airlocks.xyz\npath     : sequence.json\ntimeout  : \nlocalssl : No\nfailearly: Yes\n")),(0,a.kt)("h3",{id:"create-a-sequence"},"create a sequence"),(0,a.kt)("p",null,"visit ",(0,a.kt)("a",{parentName:"p",href:"https://airlocks.xyz"},"https://airlocks.xyz")," to create a sequence of commands.\nthere's also ",(0,a.kt)("strong",{parentName:"p"},"samplesequence")," for linux based OSs you can try out."),(0,a.kt)("h3",{id:"download-the-sequnce"},"download the sequnce"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"raumd download samplesequence             \n")),(0,a.kt)("h3",{id:"run-the-sequence"},"run the sequence"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-sh"},"raumd run samplesequence\n")),(0,a.kt)("p",null,"A sequence of commands looks like this:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-json"},"{\n    'id': 'samplesequence',\n    'title': 'samplesequence',\n    'parent_id': None,\n    'seq': [\n        {\n            'name': 'Print something ',\n            'command': 'echo \"Lorem Ipsum is ..\"'\n        },\n        {'name': 'Sleep a little bit', 'command': 'sleep 10'},\n        {'name': 'Print a json file ', 'command': 'echo \n        \"{\\n  \"squadName\": \"Super hero squad\",\\n  \n        \"homeTown\": \"Metro City\",\\n  \n        \"formed\": 2016,\\n  \n        \"secretBase\": \"Super tower\",\\n  \n        \"active\": true\\n}\"'},\n        {\n            'id': '9hl8k',\n            'title': 'sublist',\n            'parent_id': None,\n            'seq': [\n                {'name': 'sub_command_a', 'command': 'ping -t 10 www.google.com'},\n                {'name': 'whereas', 'command': 'pwd'},\n                {'name': 'whatishere', 'command': 'ls -l'},\n                {'name': 'disk usage', 'command': 'du -s'}\n            ],\n            'lastAutoSave': '03/04/2022, 17:03:39',\n            'lock': None\n        }\n    ],\n    'lastAutoSave': '03/04/2022, 16:54:07',\n    'lock': None\n}\n\n")))}p.isMDXComponent=!0}}]);