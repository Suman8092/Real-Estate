import homeIdentityCss from '../css/home-identity.css?inline';
// Homepage-only presentation and interactions; shared navigation and forms stay independent.
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
  const identity = document.createElement('style');
  identity.dataset.siteIdentity = 'premium';
  identity.textContent = homeIdentityCss;
  root.append(identity);

  // Real filters over the actual published catalogue, with no search or invented rental inventory.
  const filters = [...root.querySelectorAll('.hp-filter')];
  const projects = [...root.querySelectorAll('.hp-project')];
  filters.forEach(button => button.addEventListener('click', () => {
    filters.forEach(other => {
      other.classList.toggle('active', other === button);
      other.setAttribute('aria-pressed', String(other === button));
    });
    projects.forEach(project => {
      project.hidden = button.dataset.filter !== 'all' && !project.dataset.categories.split(' ').includes(button.dataset.filter);
    });
  }));

  root.querySelectorAll('a[href^="#"]').forEach(link => link.addEventListener('click', event => {
    const destination = root.getElementById(link.getAttribute('href').slice(1));
    if (!destination) return;
    event.preventDefault();
    destination.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start' });
  }));

  // Preserve the existing required fields, contact consent and native email-draft action.
  const form = root.getElementById('contactForm');
  const name = root.getElementById('name');
  const phone = root.getElementById('mobile');
  const email = root.getElementById('email');
  const project = root.getElementById('project');
  const consent = root.querySelector('.mpa-consent-box');
  const consentBox = root.querySelector('.mpa-consent');
  const status = root.getElementById('successMessage');
  phone.addEventListener('input', () => { phone.value = phone.value.replace(/[^0-9]/g, '').slice(0, 10); });
  consent.addEventListener('change', () => consentBox.classList.toggle('is-on', consent.checked));
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const subject = `Property enquiry: ${project.value}`;
    const body = [`Name: ${name.value.trim()}`, `Phone: ${phone.value.trim()}`, `Email: ${email.value.trim()}`, `Project: ${project.value}`].join('\r\n');
    window.open(`mailto:info@premiumpropertydepot.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`, '_self');
    status.textContent = 'info@premiumpropertydepot.com · +91 9415378938 · +91 9305486716';
    status.hidden = false;
  });
}
