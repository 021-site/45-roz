
const BALE_TOKEN = "973886928:FISShsMogHPRYz2HHomnhqXqfwE2Xxzj2rE";
const BALE_CHAT_ID = 1245087906;
var logs=["در حال روشن شدن هسته‌ی AETHER...","موتور کهکشان آماده شد...","۲۲۰ ستاره روشن شد...","هسته‌ی فیزیک وصل شد...","صداهای نئونی کوک شد...","کانال پیام به بله وصل شد...","تمام شد؛ ۴۵ روز در یک فایل جمع شد..."];
var li=0,lg=document.getElementById('llog'),fl=document.getElementById('lfill');
var iv=setInterval(function(){if(li<logs.length){var d=document.createElement('div');d.textContent="> "+logs[li];lg.appendChild(d);li++;}fl.style.width=Math.round(li/logs.length*100)+"%";if(li>=logs.length){clearInterval(iv);setTimeout(function(){document.getElementById('loader').classList.add('hide');startCounters();},600);}},380);
addEventListener('scroll',function(){var h=document.documentElement;var p=h.scrollTop/(h.scrollHeight-h.clientHeight)*100;document.getElementById('prog').style.width=p+"%";});
var bg=document.getElementById('uni'),bx=bg.getContext('2d'),stars=[];
function rs(){bg.width=innerWidth;bg.height=innerHeight;}rs();addEventListener('resize',rs);
for(var i=0;i<220;i++)stars.push({x:Math.random()*innerWidth,y:Math.random()*innerHeight,r:Math.random()*1.7+.4,s:Math.random()*.5+.12,tw:Math.random()*6.28});
var mx=innerWidth/2,my=innerHeight/2;
addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;});
(function loop(){bx.clearRect(0,0,bg.width,bg.height);var g=bx.createRadialGradient(bg.width*.5,bg.height*.15,0,bg.width*.5,bg.height*.15,bg.height);g.addColorStop(0,'rgba(139,92,255,.12)');g.addColorStop(1,'rgba(0,0,0,0)');bx.fillStyle=g;bx.fillRect(0,0,bg.width,bg.height);for(var k=0;k<stars.length;k++){var s=stars[k];s.y+=s.s;s.tw+=.03;if(s.y>bg.height){s.y=0;s.x=Math.random()*bg.width;}var dx=(mx-bg.width/2)/70*s.r,dy=(my-bg.height/2)/70*s.r;bx.globalAlpha=.3+Math.abs(Math.sin(s.tw))*.7;bx.fillStyle='#cfe4ff';bx.beginPath();bx.arc(s.x+dx,s.y+dy,s.r,0,7);bx.fill();}bx.globalAlpha=1;requestAnimationFrame(loop);})();
var txts=['۴۵ شب، بدون میان‌بُر...','هر ستاره‌اش یک ساعت فکر است...','لمسش کن، صداش را دربیاور...','این تازه یکی از خفن‌ترین‌هاست...'],ti=0,ci=0,del=false;
setInterval(function(){var c=txts[ti];if(!del){ci++;if(ci>=c.length+10)del=true;}else{ci--;if(ci<=0){del=false;ti=(ti+1)%txts.length;}}document.getElementById('typing').textContent=c.slice(0,Math.min(ci,c.length));},95);
setInterval(function(){document.getElementById('clock').textContent=new Date().toLocaleTimeString('en-GB');},1000);
function animateNum(el){if(el.dataset.done)return;el.dataset.done="1";var target=parseFloat(el.dataset.c);var cur=0;var step=Math.max(1,Math.round(target/50));var c=setInterval(function(){cur+=step;if(cur>=target){cur=target;clearInterval(c);}el.textContent=cur;},28);}
function startCounters(){document.querySelectorAll('[data-c]').forEach(function(el){animateNum(el);});}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');e.target.querySelectorAll('.bar div').forEach(function(b){b.style.width=b.style.getPropertyValue('--w');});e.target.querySelectorAll('[data-c]').forEach(function(el){animateNum(el);});}});},{threshold:.15});
document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
var cio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){animateNum(e.target);cio.unobserve(e.target);}});},{threshold:.3});
document.querySelectorAll('[data-c]').forEach(function(el){cio.observe(el);});
document.querySelectorAll('.mod,.tcard').forEach(function(cd){cd.addEventListener('mousemove',function(e){var r=cd.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;cd.style.transform='perspective(700px) rotateY('+(x*10)+'deg) rotateX('+(-y*10)+'deg) translateY(-4px)';});cd.addEventListener('mouseleave',function(){cd.style.transform='';});});
var lab=document.getElementById('labCv'),lc=lab.getContext('2d'),ps=[];
function sz(){lab.width=lab.clientWidth;lab.height=340;}sz();addEventListener('resize',sz);
function boom(x,y,n){var cl=['#8b5cff','#00e5ff','#ff3df0','#ffd166','#7dffb2'];for(var i=0;i<(n||70);i++){var a=Math.random()*6.283,v=Math.random()*5+1;ps.push({x:x,y:y,vx:Math.cos(a)*v,vy:Math.sin(a)*v,life:1,c:cl[Math.floor(Math.random()*cl.length)],r:Math.random()*3+1});}}
var down=false;
lab.addEventListener('pointerdown',function(e){down=true;var r=lab.getBoundingClientRect();boom(e.clientX-r.left,e.clientY-r.top,90);blip(440);});
lab.addEventListener('pointermove',function(e){if(down){var r=lab.getBoundingClientRect();boom(e.clientX-r.left,e.clientY-r.top,6);}});
addEventListener('pointerup',function(){down=false;});
document.getElementById('bBoom').onclick=function(){boom(lab.width/2,lab.height/2,240);blip(220);};
document.getElementById('bVortex').onclick=function(){for(var k=0;k<5;k++)boom(Math.random()*lab.width,Math.random()*lab.height,70);};
document.getElementById('bClear').onclick=function(){ps=[];};
var lt=performance.now(),fr=0;
(function lp(t){lc.fillStyle='rgba(2,4,9,.28)';lc.fillRect(0,0,lab.width,lab.height);ps=ps.filter(function(p){return p.life>0;});for(var i=0;i<ps.length;i++){var p=ps[i];p.x+=p.vx;p.y+=p.vy;p.vy+=.05;p.vx*=.99;p.life-=.011;lc.globalAlpha=Math.max(p.life,0);lc.fillStyle=p.c;lc.beginPath();lc.arc(p.x,p.y,p.r,0,7);lc.fill();}lc.globalAlpha=1;fr++;if(t-lt>500){var f=Math.round(fr*1000/(t-lt));fr=0;lt=t;document.getElementById('fps').textContent=f+' fps • '+ps.length;}requestAnimationFrame(lp);})(performance.now());
setInterval(function(){if(!down&&Math.random()>.75&&ps.length<350)boom(Math.random()*lab.width,Math.random()*lab.height*.7,4);},700);
var AC=null;
function blip(f){try{if(!AC)AC=new (window.AudioContext||window.webkitAudioContext)();var o=AC.createOscillator(),g=AC.createGain();o.type='sine';o.frequency.value=f;g.gain.setValueAtTime(.18,AC.currentTime);g.gain.exponentialRampToValueAtTime(.001,AC.currentTime+.5);o.connect(g);g.connect(AC.destination);o.start();o.stop(AC.currentTime+.5);}catch(e){}}
document.querySelectorAll('.pad button').forEach(function(b){b.onclick=function(){blip(+b.dataset.f);boom(lab.width/2,lab.height/2,40);};});
addEventListener('keydown',function(e){if(e.key.toLowerCase()==='m'){for(var k=0;k<8;k++)setTimeout(function(){boom(Math.random()*lab.width,Math.random()*100,60);},k*150);lab.scrollIntoView({behavior:'smooth',block:'center'});print('<span class="p">➜ aether</span> <span class="pk">شهاب‌باران شروع شد، نگاه کن...</span>');}});
var out=document.getElementById('tout'),inp=document.getElementById('tin');
function print(h){var d=document.createElement('div');d.innerHTML=h;out.appendChild(d);out.scrollTop=out.scrollHeight;}
function run(r){print('<span class="p">➜ aether ~</span> <span style="font-family:monospace">'+r+'</span>');var c=r.trim().toLowerCase();if(!c)return;
if(c==='help')print('<span class="c">دستورات من: story (داستان ۴۵ روز) | stats (آمار) | secret (راز) | matrix (حالت ماتریکس) | date (تاریخ امروز) | clear (پاک کردن)</span>');
else if(c==='story')print('<span class="c">روز اول فقط یه صفحه‌ی سیاه بود. روز ۴۵ این جهان جلوی توئه. ۴۵ شب، بدون قالب آماده، فقط کد خالص.</span>');
else if(c==='stats')print('<span class="w">۴۵ روز تلاش • بیش از ۱۸۰ ساعت • ۲۱۴۰ خط کد • صفر وابستگی</span>');
else if(c==='secret')print('<span class="pk">آفرین پیداش کردی. حالا دکمه‌ی M رو بزن، پشیمون نمی‌شی.</span>');
else if(c==='date')print('<span class="c">امروز: '+new Date().toLocaleDateString('fa-IR',{year:'numeric',month:'long',day:'numeric'})+'</span>');
else if(c==='matrix'){print('<span class="pk">حالت ماتریکس برای ۵ ثانیه...</span>');var m=setInterval(function(){bx.fillStyle='rgba(0,0,0,.18)';bx.fillRect(0,0,bg.width,bg.height);bx.fillStyle='#0f6';bx.font='13px monospace';for(var i=0;i<50;i++)bx.fillText(Math.random()>.5?'1':'0',Math.random()*bg.width,Math.random()*bg.height);},90);setTimeout(function(){clearInterval(m);},5000);}
else if(c==='clear')out.innerHTML='';
else print('<span class="w">این دستور رو نفهمیدم: '+c+' — بنویس help</span>');}
inp.addEventListener('keydown',function(e){if(e.key==='Enter'){run(inp.value);inp.value='';}});
document.getElementById('term').addEventListener('click',function(){inp.focus();});
document.getElementById('fbSend').onclick=async function(){
var btn=this;
var name=document.getElementById('fbName').value.trim();
var opinion=document.getElementById('fbText').value.trim();
var st=document.getElementById('fbStatus');
if(!name||!opinion){st.className="err";st.textContent="اول اسمت و نظرت را بنویس، بعد ارسال را بزن.";return;}
var now=new Date();
var dateFa=now.toLocaleDateString('fa-IR',{year:'numeric',month:'long',day:'numeric'});
var timeFa=now.toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit'});
var text="سلام من "+name+" هستم\nخواستم بهت بگم که "+opinion+" ✨\nتاریخ : "+dateFa+" 🌃\nساعت : "+timeFa+" ⏳️";
st.className="";st.textContent="در حال ارسال...";btn.disabled=true;
try{
var url="https://tapi.bale.ai/bot"+BALE_TOKEN+"/sendMessage";
var body="chat_id="+encodeURIComponent(BALE_CHAT_ID)+"&text="+encodeURIComponent(text);
await fetch(url,{method:"POST",mode:"no-cors",cache:"no-store",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:body});
st.className="ok";st.textContent="فرستاده شد ✔ ممنون که نظر دادی.";document.getElementById('fbName').value="";document.getElementById('fbText').value="";
}catch(e){st.className="err";st.textContent="ارسال نشد. فیلترشکن را خاموش کن و دوباره بزن.";}
btn.disabled=false;
};
