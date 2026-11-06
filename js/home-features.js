import catalogue from './home-catalogue.js';
const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const currency = value => new Intl.NumberFormat('en-IN', { style:'currency', currency:'INR', maximumFractionDigits:0 }).format(value);
export function initHomeFeatures(root) {
  const dialog = root.getElementById('pp-local-dialog');
  const content = root.getElementById('pp-dialog-content');
  const heading = root.getElementById('pp-dialog-title');
  const notice = root.querySelector('.pp-local-notice');
  const known = new Map(catalogue.map(p => [p.slug,p]));
  const read = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } };
  const saved = new Set((Array.isArray(read('premium-saved-projects',[])) ? read('premium-saved-projects',[]) : []).filter(id => known.has(id)));
  const initialProfile = read('premium-local-profile', {});
  if (typeof initialProfile?.name === 'string') root.getElementById('name').value = initialProfile.name;
  if (typeof initialProfile?.email === 'string') root.getElementById('email').value = initialProfile.email;
  const compare = new Set();
  let noticeTimer;
  function announce(message) {
    notice.textContent = message; notice.hidden = false;
    clearTimeout(noticeTimer); noticeTimer = setTimeout(() => { notice.hidden = true; },4500);
  }
  function open(title, html) {
    heading.textContent = title; content.innerHTML = html;
    if (!dialog.open) dialog.showModal();
  }
  dialog.addEventListener('click', event => { if(event.target === dialog) dialog.close(); });
  function paintSaved() {
    root.querySelectorAll('[data-save]').forEach(button => {
      const selected = saved.has(button.dataset.save);
      button.setAttribute('aria-pressed',String(selected));
      button.innerHTML = `<svg width="23" height="23" viewBox="0 0 24 24" fill="${selected?'currentColor':'none'}" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/></svg>`;
      button.setAttribute('aria-label',`${selected ? 'Unsave' : 'Save'} ${known.get(button.dataset.save).name}`);
    });
    document.querySelectorAll('.pp-saved-count').forEach(el => { el.hidden = saved.size===0; el.textContent=saved.size; });
    try {localStorage.setItem('premium-saved-projects',JSON.stringify([...saved]));} catch {announce('Saving is unavailable in this browser.');}
  }
  root.querySelectorAll('[data-save]').forEach(button => button.addEventListener('click',()=>{
    const id=button.dataset.save;saved.has(id)?saved.delete(id):saved.add(id);paintSaved();announce(saved.has(id)?'Property saved on this browser.':'Property removed from saved list.');
  }));
  function savedList() {
    open('Saved Properties', '<p class="pp-dialog-note">Stored on this browser. No online account or cross-device sync.</p>'+([...saved].map(id=>{
      const p=known.get(id);return `<article class="pp-saved-item"><div><a href="${p.href}"><h3>${escape(p.name)}</h3></a><p>${escape(p.location)}</p></div><button type="button" data-remove-saved="${id}" aria-label="Remove ${escape(p.name)}">×</button></article>`;
    }).join('') || '<p>No saved properties yet. Use the heart on a project card to save it.</p>'));
    content.querySelectorAll('[data-remove-saved]').forEach(button=>button.addEventListener('click',()=>{saved.delete(button.dataset.removeSaved);paintSaved();savedList();}));
  }
  document.querySelectorAll('[data-open-saved]').forEach(button=>button.addEventListener('click',savedList));
  paintSaved();
  const dock = root.querySelector('.pp-compare-dock');
  function paintCompare(){
    root.querySelectorAll('[data-compare]').forEach(input=>{input.checked=compare.has(input.dataset.compare);});
    root.getElementById('pp-compare-count').textContent=compare.size;dock.hidden=compare.size===0;
  }
  root.querySelectorAll('[data-compare]').forEach(input=>input.addEventListener('change',()=>{
    const id=input.dataset.compare;
    if(input.checked&&compare.size===3){input.checked=false;announce('You can compare up to three properties at a time.');return;}
    input.checked?compare.add(id):compare.delete(id);paintCompare();
  }));
  root.querySelector('[data-clear-compare]').addEventListener('click',()=>{compare.clear();paintCompare();});
  root.querySelector('[data-open-compare]').addEventListener('click',()=>{
    if(compare.size<2){announce('Select at least two properties to compare.');return;}
    const list=[...compare].map(id=>known.get(id));
    const rows=[['Location','location'],['Category','category'],['Project information','description']];
    open('Compare Properties',`<div class="pp-comparison-scroll"><table class="pp-comparison"><thead><tr><th>Property</th>${list.map(p=>`<th><a href="${p.href}">${escape(p.name)}</a></th>`).join('')}</tr></thead><tbody>${rows.map(([label,key])=>`<tr><th>${label}</th>${list.map(p=>`<td>${escape(p[key])}</td>`).join('')}</tr>`).join('')}<tr><th>Project details</th>${list.map(p=>`<td><a href="${p.href}">View project ↗</a></td>`).join('')}</tr></tbody></table></div><p class="pp-dialog-note">Only published project details are shown; no prices or availability have been assumed.</p>`);
  });
  root.querySelectorAll('[data-share]').forEach(button=>button.addEventListener('click',async()=>{
    const p=known.get(button.dataset.share);const url=new URL(p.href,location.href).href;
    try{
      if(navigator.share){await navigator.share({title:p.name,text:p.location,url});}
      else if(navigator.clipboard){await navigator.clipboard.writeText(url);announce('Project link copied.');}
      else throw new Error('Clipboard unavailable');
    }catch(error){if(error.name==='AbortError')return;open('Share Project',`<p>${escape(p.name)}</p><label class="pp-tool-label">Copy this project link<input readonly value="${escape(url)}"/></label>`);content.querySelector('input').select();}
  }));
  document.querySelectorAll('[data-open-profile]').forEach(button=>button.addEventListener('click',()=>{
    const profile=read('premium-local-profile',{});
    open('Your Local Profile',`<p class="pp-dialog-note">A convenience profile stored only in this browser. This is not an online login.</p><form id="pp-profile-form"><label class="pp-tool-label">Name<input name="name" autocomplete="name" value="${escape(profile.name||'')}" required/></label><label class="pp-tool-label">Email<input name="email" type="email" autocomplete="email" value="${escape(profile.email||'')}" required/></label><button class="pp-button">Save Profile</button><button class="pp-text-button" type="button" data-clear-profile>Clear profile</button><p role="status" class="pp-profile-status"></p></form>`);
    content.querySelector('form').addEventListener('submit',event=>{event.preventDefault();const f=new FormData(event.target);try{localStorage.setItem('premium-local-profile',JSON.stringify({name:f.get('name').trim(),email:f.get('email').trim()}));root.getElementById('name').value=f.get('name');root.getElementById('email').value=f.get('email');content.querySelector('.pp-profile-status').textContent='Profile saved on this browser.';}catch{content.querySelector('.pp-profile-status').textContent='Browser storage is unavailable.';}});
    content.querySelector('[data-clear-profile]').addEventListener('click',()=>{try{localStorage.removeItem('premium-local-profile');}catch{}content.querySelector('form').reset();content.querySelectorAll('input').forEach(i=>i.value='');content.querySelector('.pp-profile-status').textContent='Local profile cleared.';});
  }));
  // Search is an actual local catalogue search, not a simulated AI/API service.
  const search=document.querySelector('.pp-header-search');
  if(search){
    const searchInput=search.querySelector('input');
    const results=search.querySelector('.pp-search-results');
    const normalize=value=>value.toLowerCase().normalize('NFKD').replace(/[^a-z0-9\s]/g,' ').replace(/\s+/g,' ').trim();
    function findProjects(query){const tokens=normalize(query).split(' ').filter(Boolean);return catalogue.filter(p=>tokens.every(t=>normalize([p.name,p.location,p.category,p.description].join(' ')).includes(t)));}
    function showResults(){
      const query=searchInput.value.trim();if(!query){results.hidden=true;return;}
      const matches=findProjects(query);results.replaceChildren();results.hidden=false;
      const count=document.createElement('p');count.textContent=`${matches.length} matching ${matches.length===1?'project':'projects'}`;results.append(count);
      for(const p of matches){const a=document.createElement('a');a.href=p.href;const title=document.createElement('strong');title.textContent=p.name;const subtitle=document.createElement('span');subtitle.textContent=p.location;a.append(title,subtitle);results.append(a);}
      if(!matches.length){const text=document.createElement('p');text.textContent='Try a project name, location or property category.';results.append(text);}
    }
    searchInput.addEventListener('input',showResults);searchInput.addEventListener('focus',()=>{if(searchInput.value)showResults();});
    search.addEventListener('submit',event=>{event.preventDefault();showResults();results.querySelector('a')?.focus();});
    searchInput.addEventListener('keydown',event=>{if(event.key==='Escape'){results.hidden=true;}if(event.key==='ArrowDown'){event.preventDefault();results.querySelector('a')?.focus();}});
    document.addEventListener('click',event=>{if(!search.contains(event.target))results.hidden=true;});
  }
  // Gallery controls use only project-matched images from the source catalogue.
  const galleryStates=[];
  let timer=null;
  function startAutoAdvance(){
    if(timer)clearInterval(timer);
    if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
    timer=setInterval(()=>{
      if(document.hidden||dialog?.open)return;
      const activeGallery=galleryStates.find(state=>!state.gallery.closest('[hidden]'));
      if(activeGallery)activeGallery.advance();
      else root.querySelector('[data-project-step="1"]')?.click();
    },6000);
  }

  root.querySelectorAll('.pp-gallery').forEach(gallery=>{
    const imgs=[...gallery.querySelectorAll('img')];const dots=[...gallery.querySelectorAll('[data-photo]')];let index=0,paused=false;
    const pause=gallery.querySelector('.pp-gallery-pause');
    function show(next){
      index=(next+imgs.length)%imgs.length;
      imgs.forEach((img,i)=>img.hidden=i!==index);
      dots.forEach((dot,i)=>{
        dot.removeAttribute('data-completed');
        dot.setAttribute('aria-pressed','false');
      });
      void gallery.offsetWidth;
      dots.forEach((dot,i)=>{
        dot.setAttribute('aria-pressed',String(i===index));
        if(i<index)dot.setAttribute('data-completed','true');
      });
      if(!paused && !gallery.closest('[hidden]')) startAutoAdvance();
    }
    dots.forEach((dot,i)=>dot.addEventListener('click',()=>show(i)));
    gallery.querySelector('.pp-gallery-prev')?.addEventListener('click',()=>{
      if(imgs.length>1)show(index-1);
      else root.querySelector('[data-project-step="-1"]')?.click();
    });
    gallery.querySelector('.pp-gallery-next')?.addEventListener('click',()=>{
      if(imgs.length>1)show(index+1);
      else root.querySelector('[data-project-step="1"]')?.click();
    });
    pause?.addEventListener('click',()=>{
      paused=!paused;
      gallery.classList.toggle('is-paused',paused);
      pause.textContent=paused?'▶':'Ⅱ';
      pause.setAttribute('aria-pressed',String(paused));
      pause.setAttribute('aria-label',paused?'Play project timer':'Pause project timer');
      if(paused){if(timer)clearInterval(timer);}
      else startAutoAdvance();
    });
    let start=0;gallery.addEventListener('touchstart',event=>{start=event.changedTouches[0].clientX;},{passive:true});gallery.addEventListener('touchend',event=>{const delta=event.changedTouches[0].clientX-start;if(Math.abs(delta)>45){
      if(imgs.length>1)show(index+(delta<0?1:-1));
      else root.querySelector(`[data-project-step="${delta<0?1:-1}"]`)?.click();
    }},{passive:true});
    galleryStates.push({gallery,advance:()=>{
      if(paused||gallery.closest('[hidden]'))return;
      if(index===imgs.length-1){show(0);root.querySelector('[data-project-step="1"]').click();}
      else show(index+1);
    }});
  });
  if(galleryStates.length>0)startAutoAdvance();
  window.addEventListener('pagehide',()=>{if(timer)clearInterval(timer);},{once:true});
  // Tools calculate from user-supplied values. No property prices or statutory rates are fabricated.
  const field=(label,name,extra='')=>`<label class="pp-tool-label">${label}<input name="${name}" ${extra} required/></label>`;
  const numeric='type="number" min="0" step="any"';
  const configurations={
    stamp:{title:'Stamp Duty Calculator',fields:field('Property value (₹)','value',numeric)+field('Applicable stamp duty rate (%)','rate','type="number" min="0" max="100" step="any"'),note:'Enter the applicable rate yourself. This arithmetic estimate excludes registration fees, exemptions and other charges.',calculate:f=>`Estimated duty: ${currency(Number(f.get('value'))*Number(f.get('rate'))/100)}`},
    emi:{title:'EMI Calculator',fields:field('Loan amount (₹)','principal',numeric)+field('Annual interest rate (%)','rate','type="number" min="0" max="100" step="any"')+field('Loan tenure (years)','years','type="number" min="0.083333" max="100" step="any"'),note:'Illustrative calculation based on your inputs, using monthly compounding. Lender fees and insurance are excluded.',calculate:f=>{const principal=Number(f.get('principal')),rate=Number(f.get('rate'))/1200,n=Math.max(1,Math.round(Number(f.get('years'))*12)),emi=rate?principal*rate/(1-Math.pow(1+rate,-n)):principal/n;return `Monthly EMI: ${currency(emi)} · Total repayment: ${currency(emi*n)} · Interest: ${currency(emi*n-principal)}`;}},
    investment:{title:'Investment Calculator',fields:field('Initial amount (₹)','principal',numeric)+field('Assumed annual growth (%)','rate','type="number" min="-99" max="1000" step="any"')+field('Time horizon (years)','years','type="number" min="0" max="100" step="any"'),note:'A mathematical projection using your growth assumption; no returns are promised.',calculate:f=>`Projected amount: ${currency(Number(f.get('principal'))*Math.pow(1+Number(f.get('rate'))/100,Number(f.get('years'))))}`},
    units:{title:'Unit Converter',fields:field('Area','area',numeric)+'<label class="pp-tool-label">From<select name="from"><option value="1">Square feet</option><option value="10.7639104167">Square metres</option><option value="9">Square yards</option><option value="43560">Acres</option><option value="107639.104167">Hectares</option></select></label><label class="pp-tool-label">To<select name="to"><option value="10.7639104167">Square metres</option><option value="1">Square feet</option><option value="9">Square yards</option><option value="43560">Acres</option><option value="107639.104167">Hectares</option></select></label>',note:'Standard area conversion; figures are rounded to four decimal places.',calculate:f=>`${new Intl.NumberFormat('en-IN',{maximumFractionDigits:4}).format(Number(f.get('area'))*Number(f.get('from'))/Number(f.get('to')))} ${content.querySelector('[name="to"] option:checked').textContent.toLowerCase()}`}
  };
  root.querySelectorAll('[data-tool]').forEach(button=>button.addEventListener('click',()=>{
    const key=button.dataset.tool;if(key==='advisory'){root.getElementById('connect').scrollIntoView({behavior:'smooth'});root.getElementById('name').focus({preventScroll:true});return;}
    if(key==='receipt'){
      open('Get Rent Receipts','<p class="pp-dialog-note">Create a printable receipt using your own details. Nothing is submitted or saved online.</p><form class="pp-tool-form">'+field('Tenant name','tenant')+field('Landlord name','landlord')+field('Property address','address')+field('Rent amount (₹)','rent',numeric)+field('Rental period','period')+field('Payment date','date','type="date"')+'<button class="pp-button">Preview Receipt</button></form><div class="pp-receipt-preview"></div>');
      content.querySelector('form').addEventListener('submit',event=>{event.preventDefault();const f=new FormData(event.target);const receipt=`<h2>Rent Receipt</h2><p>Received from <strong>${escape(f.get('tenant'))}</strong> the amount of <strong>${currency(Number(f.get('rent')))}</strong> for rent of ${escape(f.get('address'))}.</p><p>Period: ${escape(f.get('period'))}</p><p>Payment date: ${escape(f.get('date'))}</p><p>Landlord: ${escape(f.get('landlord'))}</p><p>Signature: ____________________</p>`;const preview=content.querySelector('.pp-receipt-preview');preview.innerHTML=receipt+'<button type="button" class="pp-button" data-print-receipt>Print Receipt</button>';preview.querySelector('button').addEventListener('click',()=>{const print=window.open('','_blank','width=800,height=700');if(!print){announce('Allow popups to print the receipt.');return;}print.document.write('<!doctype html><html><head><title>Rent Receipt</title><style>body{font:16px/1.8 Arial;padding:40px}h2{margin-bottom:30px}</style></head><body>'+receipt+'</body></html>');print.document.close();print.focus();print.print();});});return;
    }
    const config=configurations[key];open(config.title,`<p class="pp-dialog-note">${config.note}</p><form class="pp-tool-form">${config.fields}<button class="pp-button">Calculate</button><output class="pp-tool-result" aria-live="polite"></output></form>`);content.querySelector('form').addEventListener('submit',event=>{event.preventDefault();content.querySelector('output').textContent=config.calculate(new FormData(event.target));});
  }));
}
