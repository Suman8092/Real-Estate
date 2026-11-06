import catalogue from './home-catalogue.js';
import { homeMedia } from './home-media.js';
const safe=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let enquiryOpener;
const icon=(name,size=20)=>{
  const paths={chat:'<path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8z"/>',phone:'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.7 2z"/>',mail:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',share:'<path d="M15 8h4v12H4V5h7M14 3h7v7M10 14 21 3"/>',zoom:'<path d="M8 3H3v5M16 3h5v5M3 16v5h5M21 16v5h-5"/>',arrow:'<path d="m6 15 6-6 6 6"/>',location:'<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="2.5"/>'};
  return `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]||paths.chat}</svg>`;
};
export function openHomeEnquiry(name,root){
  const modal=document.getElementById('enquiry-modal');
  if(!modal){root.getElementById('connect').scrollIntoView({behavior:'smooth'});return;}
  enquiryOpener=root.activeElement||document.activeElement;
  document.getElementById('modal-property-title').textContent=name||'Property Enquiry';
  document.getElementById('modal-property-input').value=name||'Property Enquiry';
  modal.classList.add('active');document.body.style.overflow='hidden';
  modal.querySelector('input[name="name"]')?.focus({preventScroll:true});
}
export function initHomeWidgets(root){
  const dialog=root.getElementById('pp-local-dialog'),content=root.getElementById('pp-dialog-content'),title=root.getElementById('pp-dialog-title');
  function open(heading,html){title.textContent=heading;content.innerHTML=html;if(!dialog.open)dialog.showModal();}
  function closeMenus(){document.querySelectorAll('#pp-home-header details[open]').forEach(d=>d.open=false);}
  const parse=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
  const names=[...new Set(catalogue.map(p=>p.city))];
  const enquiryModal=document.getElementById('enquiry-modal');
  if(enquiryModal){
    let wasOpen=false;
    new MutationObserver(()=>{
      const active=enquiryModal.classList.contains('active');
      if(wasOpen&&!active&&enquiryOpener?.getClientRects().length)enquiryOpener.focus();
      wasOpen=active;
    }).observe(enquiryModal,{attributes:true,attributeFilter:['class']});
    enquiryModal.addEventListener('keydown',event=>{
      if(event.key!=='Tab'||!enquiryModal.classList.contains('active'))return;
      const items=[...enquiryModal.querySelectorAll('button,input:not([type=hidden]),textarea,a[href]')].filter(e=>!e.disabled);
      const first=items[0],last=items.at(-1);
      if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}
      if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
    });
  }
  const categoryOf=p=>p.name==='BNX Group'?['commercial','residential']:p.name==='Vantara Heritage'?['farmhouse','residential']:['Lifestyle Central','EON Fairfox'].includes(p.name)?['commercial']:['Anantara','Casa Corbett'].includes(p.name)?['farmhouse']:['residential'];
  // The header services are real entry points to the existing local tools.
  document.querySelectorAll('[data-header-tool]').forEach(button=>button.addEventListener('click',()=>{closeMenus();root.querySelector(`[data-tool="${button.dataset.headerTool}"]`).click();}));
  const menus=[...document.querySelectorAll('#pp-home-header .pp-desktop-nav>details')];
  menus.forEach(menu=>{
    let pinned=false,closeTimer;
    menu.addEventListener('pointerenter',()=>{clearTimeout(closeTimer);if(matchMedia('(hover:hover)').matches){menus.forEach(other=>{if(other!==menu)other.open=false;});menu.open=true;}});
    menu.addEventListener('pointerleave',()=>{closeTimer=setTimeout(()=>{if(!pinned&&!menu.contains(document.activeElement))menu.open=false;},180);});
    menu.querySelector('summary').addEventListener('click',event=>{event.preventDefault();pinned=!pinned;menu.open=pinned;});
    menu.addEventListener('toggle',()=>{if(menu.open)menus.forEach(other=>{if(other!==menu)other.open=false;});else pinned=false;});
  });
  // An actual filter form, with only source-backed locations and categories.
  document.querySelector('[data-open-filters]')?.addEventListener('click',()=>{
    open('Find Properties',`<form class="pp-advanced-filter"><label class="pp-tool-label">Project or locality<input name="query" type="search" value="${safe(document.querySelector('.pp-header-search input')?.value || '')}"/></label><div class="pp-field-pair"><label class="pp-tool-label">Location<select name="city"><option value="all">All locations</option>${names.map(n=>`<option>${safe(n)}</option>`).join('')}</select></label><label class="pp-tool-label">Property category<select name="category"><option value="all">All properties</option><option value="residential">Residential</option><option value="commercial">Commercial</option><option value="farmhouse">Farmhouse</option></select></label></div><button class="pp-button">Apply Filters</button></form><div class="pp-filter-results" aria-live="polite"></div>`);
    content.querySelector('form').addEventListener('submit',event=>{
      event.preventDefault();const f=new FormData(event.target),city=f.get('city'),category=f.get('category');
      const tokens=String(f.get('query')).toLowerCase().trim().split(/\s+/).filter(Boolean);
      const matches=catalogue.filter(p=>(city==='all'||p.city===city)&&(category==='all'||categoryOf(p).includes(category))&&tokens.every(t=>[p.name,p.location,p.category,p.description].join(' ').toLowerCase().includes(t)));
      content.querySelector('.pp-filter-results').innerHTML=`<p class="pp-filter-count">${matches.length} matching ${matches.length===1?'listing':'listings'}</p>`+matches.map(p=>`<a href="${p.href}" class="pp-filter-result"><strong>${safe(p.name)}</strong><span>${safe(p.location)}</span><small>${safe(p.category)}</small></a>`).join('');
      const categoryButton=root.querySelector(`[data-category="${category}"]`);categoryButton?.click();
      root.querySelector(`.pp-tabs button[data-city="${city}"]`)?.click();
    });
  });
  // The source's Submit Property control stores a private draft locally, never a fake public listing.
  function propertyDraft(){
    closeMenus();const drafts=parse('premium-property-drafts',[]);const draft=Array.isArray(drafts)?drafts.at(-1)||{}:{};
    open('Submit Property',`<p class="pp-dialog-note">Save a property draft on this browser. It is not published or sent to a server.</p><form class="pp-property-draft"><div class="pp-field-pair"><label class="pp-tool-label">Your name<input name="owner" autocomplete="name" maxlength="100" value="${safe(draft.owner||'')}" required/></label><label class="pp-tool-label">Email<input name="email" type="email" autocomplete="email" value="${safe(draft.email||'')}" required/></label></div><label class="pp-tool-label">Property / project name<input name="property" maxlength="160" value="${safe(draft.property||'')}" required/></label><div class="pp-field-pair"><label class="pp-tool-label">Category<select name="category"><option>Residential</option><option>Commercial</option><option>Farm Houses</option><option>Vacant Plots</option><option>Industrial</option></select></label><label class="pp-tool-label">Phone<input name="phone" type="tel" inputmode="numeric" pattern="[0-9]{10}" maxlength="10" value="${safe(draft.phone||'')}" required/></label></div><label class="pp-tool-label">Location / address<input name="location" value="${safe(draft.location||'')}" maxlength="300" required/></label><label class="pp-tool-label">Property details<textarea name="description" rows="4" maxlength="3000" required>${safe(draft.description||'')}</textarea></label><div class="pp-draft-actions"><button class="pp-button">Save Draft</button><button type="button" class="pp-text-button" data-download-draft>Download Draft</button></div><p role="status" class="pp-draft-status"></p></form>`);
    const form=content.querySelector('form');if(draft.category)form.elements.category.value=draft.category;
    const getDraft=()=>Object.fromEntries(new FormData(form));
    form.addEventListener('submit',event=>{event.preventDefault();try{const all=parse('premium-property-drafts',[]);const entries=Array.isArray(all)?all:[];entries.push({...getDraft(),savedAt:new Date().toISOString()});localStorage.setItem('premium-property-drafts',JSON.stringify(entries.slice(-20)));content.querySelector('.pp-draft-status').textContent='Draft saved on this browser. It has not been published.';}catch{content.querySelector('.pp-draft-status').textContent='Browser storage is unavailable. Use Download Draft to keep a copy.';}});
    form.querySelector('[data-download-draft]').addEventListener('click',()=>{if(!form.reportValidity())return;const blob=new Blob([JSON.stringify(getDraft(),null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='property-draft.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
  }
  document.querySelectorAll('[data-submit-property]').forEach(button=>button.addEventListener('click',propertyDraft));
  // Project photos get the reference's full-size gallery widget as well as inline story controls.
  root.querySelectorAll('.pp-gallery').forEach(gallery=>{
    const project=catalogue[Number(gallery.closest('[data-panel]').dataset.panel)];
    if(!project?.gallery.length)return;
    const button=document.createElement('button');button.type='button';button.className='pp-open-gallery';button.setAttribute('aria-label',`View all ${project.name} photos`);button.innerHTML=icon('zoom',17)+'<span>View Photos</span>';gallery.append(button);
    button.addEventListener('click',()=>{
      let index=0;open(project.name+' — Photos','<div class="pp-photo-viewer"><button type="button" class="pp-viewer-prev" aria-label="Previous photo">‹</button><img alt=""/><button type="button" class="pp-viewer-next" aria-label="Next photo">›</button></div><div class="pp-viewer-thumbs"></div><p class="pp-viewer-count" role="status"></p>');
      const img=content.querySelector('.pp-photo-viewer img'),rail=content.querySelector('.pp-viewer-thumbs');
      const render=()=>{img.src=homeMedia(project.gallery[index]);img.alt=project.name+' — photo '+(index+1);rail.querySelectorAll('button').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===index)));content.querySelector('.pp-viewer-count').textContent=`${index+1} / ${project.gallery.length}`;};
      project.gallery.forEach((path,i)=>{const thumb=document.createElement('button');thumb.type='button';thumb.setAttribute('aria-label','View photo '+(i+1));thumb.innerHTML=`<img src="${homeMedia(path)}" alt="${safe(project.name)}"/>`;thumb.addEventListener('click',()=>{index=i;render();});rail.append(thumb);});
      content.querySelector('.pp-viewer-prev').addEventListener('click',()=>{index=(index-1+project.gallery.length)%project.gallery.length;render();});content.querySelector('.pp-viewer-next').addEventListener('click',()=>{index=(index+1)%project.gallery.length;render();});render();
    });
  });
  // Expand the reference-style comparison dock to show each selected listing.
  const dock=root.querySelector('.pp-compare-dock');const chips=document.createElement('div');chips.className='pp-compare-chips';dock.prepend(chips);
  const updateChips=()=>{chips.replaceChildren();root.querySelectorAll('[data-compare]:checked').forEach(input=>{const p=catalogue.find(p=>p.slug===input.dataset.compare);const chip=document.createElement('div');chip.className='pp-compare-chip';chip.innerHTML=(p.image?`<img src="${homeMedia(p.image)}" alt="${safe(p.name)}"/>`:'')+`<span>${safe(p.name)}</span><button type="button" aria-label="Remove ${safe(p.name)} from comparison">×</button>`;chip.querySelector('button').addEventListener('click',()=>{input.checked=false;input.dispatchEvent(new Event('change',{bubbles:true}));updateChips();});chips.append(chip);});};
  root.querySelectorAll('[data-compare]').forEach(input=>input.addEventListener('change',updateChips));root.querySelector('[data-clear-compare]').addEventListener('click',updateChips);
  // Footer's location widget operates the same actual catalogue as the city tabs.
  document.querySelectorAll('[data-home-city]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();root.querySelector(`.pp-tabs button[data-city="${link.dataset.homeCity}"]`)?.click();root.getElementById('projects').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});}));
  // Floating help widget uses verified phone/email destinations, not an assumed WhatsApp number.
  const helper=document.createElement('div');helper.className='pp-help-widget';helper.innerHTML=`<div class="pp-help-tip"><p>Speak with our team to arrange a site visit.</p><button type="button" aria-label="Dismiss contact message">×</button></div><button class="pp-help-toggle" type="button" aria-label="Open contact help" aria-expanded="false">${icon('chat',27)}</button><aside class="pp-help-panel" aria-label="Contact Us" hidden><header><img src="${homeMedia('images/premium-property-depot-logo.png')}" alt="Premium Property Depot LLP"/><button type="button" class="pp-help-close" aria-label="Close contact help">×</button></header><div class="pp-help-body"><h2>Contact Us</h2><p>Speak with our team to arrange a site visit and discuss next steps.</p><div class="pp-help-contact"><a href="tel:+919415378938">${icon('phone',17)} +91 9415378938</a><a href="tel:+919305486716">${icon('phone',17)} +91 9305486716</a><a href="mailto:info@premiumpropertydepot.com">${icon('mail',17)} Email Us</a><button type="button" data-help-enquire>Enquire Now</button></div><details class="pp-help-search"><summary>Explore Projects</summary><p>Search the published project information.</p><form><input type="search" aria-label="Search projects in contact help" placeholder="Project or location" required/><button aria-label="Search project information">→</button></form><div aria-live="polite" class="pp-help-results"></div></details></div></aside>`;root.querySelector('.hp-home').append(helper);
  const helpPanel=helper.querySelector('aside'),helpToggle=helper.querySelector('.pp-help-toggle');
  const showHelp=open=>{helpPanel.hidden=!open;helpToggle.setAttribute('aria-expanded',String(open));if(open){helper.querySelector('.pp-help-tip').hidden=true;helper.querySelector('.pp-help-close').focus();}};
  helpToggle.addEventListener('click',()=>showHelp(helpPanel.hidden));helper.querySelector('.pp-help-close').addEventListener('click',()=>{showHelp(false);helpToggle.focus();});helper.querySelector('.pp-help-tip>button').addEventListener('click',()=>helper.querySelector('.pp-help-tip').hidden=true);helper.addEventListener('keydown',event=>{if(event.key==='Escape'){showHelp(false);helpToggle.focus();}});
  helper.querySelector('[data-help-enquire]').addEventListener('click',()=>{showHelp(false);const panel=root.querySelector('.pp-project-panel:not([hidden])');openHomeEnquiry(catalogue[Number(panel.dataset.panel)]?.name,root);});
  helper.querySelector('.pp-help-search form').addEventListener('submit',event=>{event.preventDefault();const query=event.target.querySelector('input').value.toLowerCase().trim();const words=query.split(/\s+/).filter(w=>!['in','near','a','the','find','me','for'].includes(w));const matches=catalogue.filter(p=>words.every(w=>[p.name,p.location,p.category,p.description].join(' ').toLowerCase().includes(w)));helper.querySelector('.pp-help-results').innerHTML=matches.length?matches.map(p=>`<a href="${p.href}"><strong>${safe(p.name)}</strong><span>${safe(p.location)}</span></a>`).join(''):'<p>No matching projects. Try a project name or location.</p>';});
  const back=document.createElement('button');back.className='pp-floating-top';back.type='button';back.innerHTML=icon('arrow');back.setAttribute('aria-label','Back to Top Projects');back.hidden=true;back.addEventListener('click',()=>root.getElementById('projects').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'}));root.querySelector('.hp-home').append(back);const paintBack=()=>back.hidden=scrollY<500;addEventListener('scroll',paintBack,{passive:true});paintBack();
  // Crisp SVG controls replace font-dependent placeholder glyphs.
  root.querySelectorAll('[data-share]').forEach(button=>button.innerHTML=icon('share',14)+'<span>Share Details</span>');
  root.querySelectorAll('.pp-card-actions .pp-button').forEach(button=>button.innerHTML=icon('phone',14)+'<span>Contact Now</span>');

  function openCityProjects(cityName){
    const cleanCity=(cityName||'').split(',')[0].trim();
    const tab=root.querySelector(`.pp-tabs button[data-city="${cleanCity}"]`)||root.querySelector(`.pp-tabs button[data-city="${cityName}"]`);
    if(tab&&!tab.classList.contains('active')){
      tab.click();
    }
    const target=cleanCity.toLowerCase();
    const matches=catalogue.filter(p=>{
      const pCity=(p.city||'').toLowerCase();
      return pCity.includes(target)||target.includes(pCity);
    });
    if(!matches.length){
      open(`Projects in ${cleanCity}`,`<p class="pp-dialog-note">No other projects found currently listed for ${safe(cleanCity)}.</p>`);
      return;
    }
    const countText=`${matches.length} ${matches.length===1?'Project':'Projects'}`;
    const heading=`All Projects in ${cleanCity} (${countText})`;
    const html=`<p class="pp-dialog-note">Explore all verified residential and commercial developments located in <strong>${safe(cleanCity)}</strong>.</p><div class="pp-city-projects-grid">${matches.map(p=>`<article class="pp-city-card"><div class="pp-city-card-media"><img src="${homeMedia(p.image)}" alt="${safe(p.name)}" loading="lazy" /><span class="pp-city-card-badge">${safe(p.status||'Active')}</span></div><div class="pp-city-card-body"><span class="pp-city-card-dev">${safe(p.developer)}</span><h3>${safe(p.name)}</h3><p class="pp-city-card-loc">${icon('location',14)} <span>${safe(p.location)}</span></p><div class="pp-city-card-meta"><span>${safe(p.bhk||p.categoryName||'Luxury Residences')}</span></div><div class="pp-city-card-price"><small>Pricing</small><strong>${safe(p.price)}</strong></div><div class="pp-city-card-actions"><a href="${p.href}" class="pp-btn-view-details">Explore Project</a><button type="button" class="pp-btn-enquire" data-city-enquire="${safe(p.name)}">Contact Us</button></div></div></article>`).join('')}</div>`;
    open(heading,html);
    content.querySelectorAll('[data-city-enquire]').forEach(btn=>{
      btn.addEventListener('click',()=>{
        dialog.close();
        openHomeEnquiry(btn.dataset.cityEnquire,root);
      });
    });
  }

  root.querySelectorAll('.pp-view-projects-link').forEach(button=>{
    button.addEventListener('click',event=>{
      event.preventDefault();
      const city=button.dataset.viewCity||button.closest('[data-city]')?.dataset.city||'Noida';
      openCityProjects(city);
    });
  });
}
