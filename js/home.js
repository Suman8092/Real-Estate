import homeIdentityCss from '../css/home-identity.css?inline';
import { initHomeWidgets, openHomeEnquiry } from './home-widgets.js';
const host = document.getElementById('homepage-content');
let root = host?.shadowRoot;
if (!root && host) {
  const template = host.querySelector('template[shadowrootmode]');
  if (template) {
    root = host.attachShadow({ mode: 'open' });
    root.append(template.content.cloneNode(true));
    template.remove();
  }
}
if (root) {
  const style = document.createElement('style');
  style.textContent = homeIdentityCss;
  root.append(style);
  const headerElement = document.getElementById('pp-home-header');
  if (headerElement) {
    const updateHeaderOffset = () => host.style.setProperty('--home-header-offset', `${headerElement.getBoundingClientRect().height + 16}px`);
    updateHeaderOffset();
    new ResizeObserver(updateHeaderOffset).observe(headerElement);
  }
  const reducedMotion = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scrollToSection = id => root.getElementById(id)?.scrollIntoView({ behavior: reducedMotion() ? 'instant' : 'smooth', block: 'start' });
  const panels = [...root.querySelectorAll('[data-panel]')];
  const thumbs = [...root.querySelectorAll('[data-project-index]')];
  let active = 0;
  let available = thumbs.map((_, index) => index);
  function selectProject(index, reveal = false) {
    active = index;
    panels.forEach((panel, i) => { panel.hidden = i !== index; });
    thumbs.forEach((thumb, i) => {
      thumb.classList.toggle('active', i === index);
      thumb.setAttribute('aria-pressed', String(i === index));
    });
    if (reveal) {
      const rail = root.querySelector('.pp-project-thumbs');
      const thumb = thumbs[index];
      rail.scrollTo({ top: thumb.offsetTop - rail.offsetTop, left: thumb.offsetLeft - rail.offsetLeft, behavior: reducedMotion() ? 'instant' : 'smooth' });
    }
    const activeGallery = panels[index]?.querySelector('.pp-gallery');
    if (activeGallery) {
      const firstDot = activeGallery.querySelector('.pp-gallery-progress [data-photo="0"]');
      firstDot?.click();
    }
  }
  thumbs.forEach((thumb, index) => thumb.addEventListener('click', () => selectProject(index)));
  root.querySelectorAll('[data-project-step]').forEach(button => button.addEventListener('click', () => {
    const current = available.indexOf(active);
    selectProject(available[(current + Number(button.dataset.projectStep) + available.length) % available.length], true);
  }));
  const cities = panels.map(panel => panel.dataset.city);
  const cityButtons = [...root.querySelectorAll('.pp-tabs button[data-city]')];
  cityButtons.forEach(button => button.addEventListener('click', () => {
    cityButtons.forEach(other => {
      other.classList.toggle('active', other === button);
      other.setAttribute('aria-pressed', String(other === button));
    });
    available = thumbs.map((_, i) => i).filter(i => button.dataset.city === 'all' || cities[i] === button.dataset.city);
    thumbs.forEach((thumb, i) => { thumb.hidden = !available.includes(i); });
    selectProject(available[0]);
  }));
  root.querySelectorAll('[data-scroll]').forEach(button => button.addEventListener('click', () => {
    const rail = root.getElementById(button.dataset.scroll);
    rail.scrollBy({ left: rail.clientWidth * Number(button.dataset.direction) * .8, behavior: reducedMotion() ? 'instant' : 'smooth' });
  }));
  const categories = [...root.querySelectorAll('[data-category]')];
  const cards = [...root.querySelectorAll('[data-category-card]')];
  categories.forEach(button => button.addEventListener('click', () => {
    categories.forEach(other => {
      other.classList.toggle('active', other === button);
      other.setAttribute('aria-pressed', String(other === button));
    });
    cards.forEach(card => { card.hidden = button.dataset.category !== 'all' && !card.dataset.categoryCard.split(' ').includes(button.dataset.category); });
    root.querySelectorAll('.pp-developer-card').forEach(group => {
      const visible = [...group.querySelectorAll('[data-category-card]')].filter(card => !card.hidden);
      group.hidden = visible.length === 0;
      group.querySelector('.pp-group-count').textContent = visible.length;
      group.querySelector('.pp-mini-rail').scrollLeft = 0;
    });
    root.getElementById('showcase-rail').scrollLeft = 0;
  }));
  let reviewIndex = 0;
  const reviews = [...root.querySelectorAll('.pp-review')];
  root.querySelectorAll('[data-review-step]').forEach(button => button.addEventListener('click', () => {
    reviewIndex = (reviewIndex + Number(button.dataset.reviewStep) + reviews.length) % reviews.length;
    reviews.forEach((review, i) => { review.hidden = i !== reviewIndex; });
  }));
  root.querySelectorAll('a[href^="#"]').forEach(link => link.addEventListener('click', event => {
    const id = link.getAttribute('href').slice(1);
    if (!root.getElementById(id)) return;
    event.preventDefault();
    scrollToSection(id);
  }));
  document.querySelectorAll('[data-home-anchor]').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    scrollToSection(link.dataset.homeAnchor);
  }));
  if (location.hash) requestAnimationFrame(() => scrollToSection(location.hash.slice(1)));
  root.querySelectorAll('[data-enquire]').forEach(button => button.addEventListener('click', () => {
    root.getElementById('project').value = button.dataset.enquire;
    openHomeEnquiry(button.dataset.enquire, root);
  }));
  // Preserve the existing validated email-draft enquiry action; no server delivery is claimed.
  const form = root.getElementById('contactForm');
  const name = root.getElementById('name');
  const phone = root.getElementById('mobile');
  const email = root.getElementById('email');
  const project = root.getElementById('project');
  const consent = root.querySelector('.mpa-consent-box');
  const status = root.getElementById('successMessage');
  phone.addEventListener('input', () => { phone.value = phone.value.replace(/[^0-9]/g, '').slice(0, 10); });
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const subject = `Property enquiry: ${project.value}`;
    const body = [`Name: ${name.value.trim()}`, `Phone: ${phone.value.trim()}`, `Email: ${email.value.trim()}`, `Project: ${project.value}`].join('\r\n');
    try {
      window.open(`mailto:info@premiumpropertydepot.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`, '_self');
      status.textContent = 'Your email app will open with your enquiry. You can also call +91 9415378938 or +91 9305486716.';
    } catch {
      status.textContent = 'Please email info@premiumpropertydepot.com or call +91 9415378938 to send your enquiry.';
    }
    status.hidden = false;
  });
}
// Homepage-only native navigation: Escape closes open menus and returns focus.
const homeHeader = document.getElementById('pp-home-header');
homeHeader?.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  const open = [...homeHeader.querySelectorAll('details[open]')].reverse();
  open.forEach(details => { details.open = false; });
  open.at(-1)?.querySelector('summary')?.focus();
});
document.addEventListener('click', event => {
  homeHeader?.querySelectorAll('details[open]').forEach(details => {
    if (!details.contains(event.target)) details.open = false;
  });
});

import { initHomeFeatures } from './home-features.js';
if (root) initHomeFeatures(root);
if (root) initHomeWidgets(root);

// City browsing supports pointer, keyboard and touch using the same source links.
if (root) root.querySelectorAll('.pp-location-card').forEach(card => {
  card.setAttribute('aria-expanded', 'false');
  const toggle = () => {
    const open = !card.classList.contains('is-open');
    root.querySelectorAll('.pp-location-card.is-open').forEach(other => {
      other.classList.remove('is-open'); other.setAttribute('aria-expanded', 'false');
    });
    card.classList.toggle('is-open', open); card.setAttribute('aria-expanded', String(open));
  };
  card.addEventListener('click', event => { if (!event.target.closest('a')) toggle(); });
  card.addEventListener('keydown', event => {
    if (event.target !== card) return;
    if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); toggle(); }
    if (event.key === 'Escape') { card.classList.remove('is-open'); card.setAttribute('aria-expanded', 'false'); card.blur(); }
  });
});
