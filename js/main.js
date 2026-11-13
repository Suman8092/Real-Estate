/**
 * Main JavaScript for Premium Infra Developer - Vacant Plots Website
 */

document.addEventListener('DOMContentLoaded', () => {
  // Desktop Properties menu: preserve native category links and support click,
  // hover, keyboard, outside-click and Escape without a shared redirect target.
  const desktopProperties = document.querySelector('#nav-menu .group');
  if (desktopProperties) {
    const trigger = desktopProperties.querySelector('button');
    const panel = trigger?.nextElementSibling;
    if (trigger && panel) {
      let pinned = false;
      panel.id = 'properties-dropdown';
      trigger.setAttribute('aria-controls', panel.id);
      const setOpen = open => {
        trigger.setAttribute('aria-expanded', String(open));
        panel.style.visibility = open ? 'visible' : 'hidden';
        panel.style.opacity = open ? '1' : '0';
        panel.style.pointerEvents = open ? 'auto' : 'none';
      };
      const close = () => { pinned = false; setOpen(false); };
      setOpen(false);
      desktopProperties.addEventListener('mouseenter', () => setOpen(true));
      desktopProperties.addEventListener('mouseleave', () => { if (!pinned) setOpen(false); });
      trigger.addEventListener('click', () => { pinned = !pinned; setOpen(pinned); });
      trigger.addEventListener('keydown', event => {
        if (event.key === 'ArrowDown') {
          event.preventDefault();
          pinned = true;
          setOpen(true);
          panel.querySelector('a')?.focus();
        }
      });
      desktopProperties.addEventListener('keydown', event => {
        if (event.key === 'Escape') { close(); trigger.focus(); }
      });
      desktopProperties.addEventListener('focusout', event => {
        if (!desktopProperties.contains(event.relatedTarget)) close();
      });
      document.addEventListener('click', event => {
        if (!desktopProperties.contains(event.target)) close();
      });
    }
  }

  // Mobile Menu Elements
  const menuToggle = document.getElementById("menu-toggle");
  const menuClose = document.getElementById("menu-close");
  const mobileMenu = document.getElementById("mobile-menu");
  const mobileOverlay = document.getElementById("mobile-overlay");

  // Open Mobile Menu
  const openMenu = () => {
    if (!mobileOverlay || !mobileMenu) return;
    mobileOverlay.classList.remove("hidden");
    setTimeout(() => {
      mobileOverlay.classList.remove("opacity-0");
      mobileMenu.classList.remove("translate-x-full");
    }, 10);
    document.body.style.overflow = 'hidden';
  };

  // Close Mobile Menu
  const closeMenu = () => {
    if (!mobileOverlay || !mobileMenu) return;
    mobileMenu.classList.add("translate-x-full");
    mobileOverlay.classList.add("opacity-0");
    setTimeout(() => {
      mobileOverlay.classList.add("hidden");
    }, 300);
    document.body.style.overflow = '';
  };

  if (menuToggle) menuToggle.addEventListener("click", openMenu);
  if (menuClose) menuClose.addEventListener("click", closeMenu);
  if (mobileOverlay) mobileOverlay.addEventListener("click", closeMenu);

  // Mobile Accordion (Submenu)
  const mobileSubmenuToggles = document.querySelectorAll(".mobile-submenu-toggle");
  mobileSubmenuToggles.forEach(button => {
    button.addEventListener("click", function() {
      const submenu = this.nextElementSibling;
      const icon = this.querySelector("svg");

      if (!submenu) return;
      this.setAttribute('aria-expanded', String(submenu.classList.contains('hidden')));

      if (submenu.classList.contains("hidden")) {
        submenu.classList.remove("hidden");
        submenu.classList.add("flex");
        if (icon) icon.classList.add("rotate-180");
      } else {
        submenu.classList.add("hidden");
        submenu.classList.remove("flex");
        if (icon) icon.classList.remove("rotate-180");
      }
    });
  });

  // Modal Handling for Property Enquiries
  const enquiryModal = document.getElementById("enquiry-modal");
  const modalClose = document.getElementById("modal-close");
  const modalPropertyTitle = document.getElementById("modal-property-title");
  const modalPropertyInput = document.getElementById("modal-property-input");
  const enquiryForm = document.getElementById("property-enquiry-form");
  const toastNotice = document.getElementById("toast-notice");
  const toastMessage = document.getElementById("toast-message");

  const openEnquiryModal = (propertyTitle) => {
    if (!enquiryModal) return;
    if (modalPropertyTitle) modalPropertyTitle.textContent = propertyTitle || "Vacant Plot Property";
    if (modalPropertyInput) modalPropertyInput.value = propertyTitle || "Vacant Plot Property";
    enquiryModal.classList.add("active");
    document.body.style.overflow = 'hidden';
  };

  const closeEnquiryModal = () => {
    if (!enquiryModal) return;
    enquiryModal.classList.remove("active");
    document.body.style.overflow = '';
  };

  if (modalClose) modalClose.addEventListener("click", closeEnquiryModal);
  if (enquiryModal) {
    enquiryModal.addEventListener("click", (e) => {
      if (e.target === enquiryModal) closeEnquiryModal();
    });
  }

  // Attach click handler to property cards
  const propertyCards = document.querySelectorAll(".property-card");
  propertyCards.forEach(card => {
    card.addEventListener("click", (e) => {
      // If user clicked directly on a phone or map link inside card, don't trigger modal
      if (e.target.closest('a')) return;
      const titleElem = card.querySelector(".property-title");
      const title = titleElem ? titleElem.textContent.trim() : "Vacant Plot Inquiry";
      openEnquiryModal(title);
    });
  });

  // Form Submission
  if (enquiryForm) {
    enquiryForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = enquiryForm.querySelector('input[name="name"]')?.value || '';
      const phone = enquiryForm.querySelector('input[name="phone"]')?.value || '';
      const email = enquiryForm.querySelector('input[name="email"]')?.value || '';
      const message = enquiryForm.querySelector('[name="message"]')?.value || '';
      const prop = modalPropertyInput ? modalPropertyInput.value : 'Vacant Plot';

      if (!enquiryForm.reportValidity()) return;
      openEmailDraft(`Property enquiry: ${prop}`, `Name: ${name}\r\nPhone: ${phone}\r\nEmail: ${email}\r\nProject: ${prop}\r\nMessage: ${message}`);
      closeEnquiryModal();
      showToast('Complete your enquiry in your email application, or call +91 9415378938.');
    });
  }

  // This static site has no message-delivery backend. Never claim a message was received.
  function openEmailDraft(subject, body) {
    window.open(`mailto:info@premiumpropertydepot.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`, '_self');
  }
  // Contact-page form submits directly to its configured email endpoint.

  // Toast notification helper
  function showToast(msg) {
    if (!toastNotice) return;
    if (toastMessage) toastMessage.textContent = msg;
    toastNotice.classList.add("show");
    setTimeout(() => {
      toastNotice.classList.remove("show");
    }, 5000);
  }

  // Global Keydown (Escape to close menus and modals)
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeMenu();
      closeEnquiryModal();
    }
  });
});
