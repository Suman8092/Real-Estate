import json
import os

from sync_footer import shared_footer

with open('data/properties.json', 'r', encoding='utf-8') as f:
    properties = json.load(f)

os.makedirs('properties', exist_ok=True)

# Template for dedicated property detail pages
def generate_property_page(prop, all_props):
    slug = prop['slug']
    name = prop['name']
    city = prop['city']
    developer = prop['developer']
    status = prop['status']
    price = prop['priceDisplay']
    prop_type = prop['propertyType']
    address = prop['address']
    overview = prop['overview']
    description = prop['description']
    rera = prop.get('reraNumber', 'Registration in progress / Documentation available upon request')
    image = prop['image']
    gallery = prop['gallery']
    highlights = prop['highlights']
    specs = prop['specifications']
    amenities = prop['amenities']
    advantages = prop['locationAdvantages']
    payment = prop['paymentPlan']
    bhk = prop['bhkConfig']
    carpet = prop['carpetArea']
    super_area = prop['superArea']
    possession = prop['possessionDate']

    # Find 3 similar projects (same city or same category, different id)
    similar = [p for p in all_props if p['id'] != prop['id'] and (p['city'] == city or p['category'] == prop['category'])][:3]
    if len(similar) < 3:
        similar = [p for p in all_props if p['id'] != prop['id']][:3]

    # HTML content
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} in {city} | {developer} | Premium Property Depot</title>
  <meta name="description" content="{name} by {developer} in {city}. {prop_type}. Price: {price}. Explore verified overview, floor plans, amenities, and location advantages." />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Premium Properties" />
  <meta property="og:title" content="{name} in {city} | {developer}" />
  <meta property="og:description" content="{name} by {developer} in {city}. Explore verified specifications, amenities, and prices." />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" href="../images/peminum_logo_-png.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/utilities.css" />
  <link rel="stylesheet" href="../css/custom.css" />
  <link rel="stylesheet" href="../css/property-detail.css" />
  <link rel="stylesheet" href="../css/shared-footer.css" />
</head>
<body class="prop-detail-body">
  <!-- HEADER -->
  <header class="prop-detail-header">
    <div class="prop-header-inner">
      <a href="../index.html" class="prop-logo-link" aria-label="Premium Property Depot — Home">
        <img src="../images/premium-property-depot-logo.png" alt="Premium Property Depot Logo" width="971" height="257" class="prop-logo-img" />
      </a>
      <nav class="prop-nav" aria-label="Main navigation">
        <a href="../index.html">Home</a>
        <a href="../about.html">About Us</a>
        <a href="../properties.html">All Properties</a>
        <a href="../residential.html">Residential</a>
        <a href="../commercial.html">Commercial</a>
        <a href="../farmhouses.html">Farm Houses</a>
        <a href="../gallery.html">Gallery</a>
        <a href="../contact.html">Contact Us</a>
      </nav>
      <div class="prop-header-actions">
        <a href="tel:+919415378938" class="prop-phone-link">
          <small>Call Expert</small>
          <span>+91 9415378938</span>
        </a>
        <a href="#enquiry-section" class="prop-enquire-btn">Enquire Now</a>
      </div>
    </div>
  </header>

  <!-- BREADCRUMBS -->
  <nav class="prop-breadcrumb-bar" aria-label="Breadcrumb">
    <div class="prop-container">
      <a href="../index.html">Home</a> / <a href="../{prop['category']}.html">{prop['category'].capitalize()}</a> / <span>{name}</span>
    </div>
  </nav>

  <!-- MAIN CONTENT -->
  <main class="prop-main">
    <div class="prop-container">

      <!-- SECTION 1 & 2: HERO & TITLE BANNER -->
      <section class="prop-hero-section">
        <div class="prop-hero-grid">
          <div class="prop-hero-media">
            <img src="../{image}" alt="{name} — Primary project view" width="800" height="600" class="prop-hero-img" />
            <div class="prop-hero-badges">
              <span class="prop-badge prop-badge-status">{status}</span>
              <span class="prop-badge prop-badge-city">{city}</span>
            </div>
          </div>
          <div class="prop-hero-info">
            <span class="prop-dev-label">{developer} Presents</span>
            <h1>{name} — {city}</h1>
            <p class="prop-address-line">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              {address}
            </p>
            <div class="prop-quick-metrics">
              <div class="prop-metric">
                <small>Starting Price</small>
                <strong>{price}</strong>
              </div>
              <div class="prop-metric">
                <small>Configuration</small>
                <strong>{bhk}</strong>
              </div>
              <div class="prop-metric">
                <small>Super Area</small>
                <strong>{super_area}</strong>
              </div>
              <div class="prop-metric">
                <small>Possession</small>
                <strong>{possession}</strong>
              </div>
            </div>
            <div class="prop-rera-block">
              <strong>RERA Registration:</strong> <span>{rera}</span>
            </div>
            <div class="prop-cta-row">
              <a href="#enquiry-section" class="prop-btn-primary">Request Price Sheet &amp; Brochure</a>
              <a href="tel:+919415378938" class="prop-btn-secondary">Call +91 9415378938</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 3: PROJECT OVERVIEW -->
      <section class="prop-section" id="overview">
        <h2>Project Overview</h2>
        <div class="prop-prose">
          <p class="prop-lead">{overview}</p>
          <p>{description}</p>
        </div>
      </section>

      <!-- SECTION 4: IMAGE GALLERY -->
      <section class="prop-section" id="gallery">
        <h2>Project Gallery</h2>
        <div class="prop-gallery-grid">
"""
    for idx, img_path in enumerate(gallery, 1):
        html += f"""          <div class="prop-gallery-item">
            <img src="../{img_path}" alt="{name} photo {idx}" width="516" height="360" class="prop-gallery-img" loading="lazy" />
          </div>\n"""

    html += f"""        </div>
      </section>

      <!-- SECTION 5: PROJECT HIGHLIGHTS -->
      <section class="prop-section" id="highlights">
        <h2>Project Highlights</h2>
        <div class="prop-highlights-grid">
"""
    for item in highlights:
        html += f"""          <div class="prop-highlight-card">
            <div class="prop-highlight-icon">✓</div>
            <p>{item}</p>
          </div>\n"""

    html += f"""        </div>
      </section>

      <!-- SECTION 6 & 8: SPECIFICATIONS & SIZES -->
      <section class="prop-section" id="specifications">
        <h2>Property Specifications &amp; Available Sizes</h2>
        <div class="prop-specs-grid">
          <div class="prop-spec-col">
            <h3>Key Technical Specifications</h3>
            <ul class="prop-spec-list">
"""
    for spec in specs:
        html += f"""              <li>{spec}</li>\n"""

    html += f"""            </ul>
          </div>
          <div class="prop-spec-col">
            <h3>Size &amp; Unit Options</h3>
            <table class="prop-size-table">
              <thead>
                <tr>
                  <th>Configuration</th>
                  <th>Carpet Area</th>
                  <th>Super Area</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{bhk}</td>
                  <td>{carpet}</td>
                  <td>{super_area}</td>
                </tr>
              </tbody>
            </table>
            <div class="prop-note-box">
              <p><strong>Note:</strong> Dimensions, layouts, and specifications are reproduced from the developer's official brochure and remain subject to final verification and authority approvals.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 7: AMENITIES -->
      <section class="prop-section" id="amenities">
        <h2>Amenities &amp; Lifestyle Features</h2>
        <div class="prop-amenities-grid">
"""
    for am in amenities:
        html += f"""          <div class="prop-amenity-pill">
            <span class="prop-amenity-bullet">•</span>
            <span>{am}</span>
          </div>\n"""

    html += f"""        </div>
      </section>

      <!-- SECTION 9 & 10: PRICING & PAYMENT PLAN -->
      <section class="prop-section" id="pricing">
        <h2>Pricing Details &amp; Payment Plan</h2>
        <div class="prop-pricing-card">
          <div class="prop-price-header">
            <div>
              <h3>Indicative Price Guidance</h3>
              <p class="prop-price-big">{price}</p>
            </div>
            <div class="prop-price-tag">Status: {status}</div>
          </div>
          <p class="prop-price-sub">{prop['priceNote']}</p>
          <div class="prop-payment-detail">
            <h3>Standard Payment Structure</h3>
            <p>{payment}</p>
          </div>
        </div>
      </section>

      <!-- SECTION 11 & 12: LOCATION ADVANTAGES & MAP -->
      <section class="prop-section" id="location">
        <h2>Location Advantages &amp; Connectivity</h2>
        <div class="prop-loc-grid">
          <div class="prop-loc-advantages">
            <h3>Key Distances &amp; Landmarks</h3>
            <ul class="prop-loc-list">
"""
    for adv in advantages:
        html += f"""              <li>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                {adv}
              </li>\n"""

    html += f"""            </ul>
          </div>
          <div class="prop-loc-info-card">
            <h3>Address &amp; Landmark Vicinity</h3>
            <p><strong>Full Address:</strong> {address}</p>
            <p><strong>Region:</strong> {city}, {prop['state']}</p>
            <div class="prop-site-visit-prompt">
              <p>Site visits are accompanied by our certified property advisors. Transport assistance and chauffeured inspections are arranged upon request.</p>
              <a href="tel:+919415378938" class="prop-visit-btn">Schedule Site Visit</a>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 13: ENQUIRY / CONSULTATION FORM -->
      <section class="prop-section prop-enquiry-section" id="enquiry-section">
        <div class="prop-enquiry-wrap">
          <div class="prop-enquiry-intro">
            <h2>Arrange a Consultation for {name}</h2>
            <p>Connect directly with our dedicated real estate advisors for verified price sheets, site layouts, booking availability, and loan documentation assistance.</p>
            <div class="prop-direct-contacts">
              <p>Direct Enquiries:</p>
              <a href="tel:+919415378938">+91 9415378938</a>
              <a href="tel:+919305486716">+91 9305486716</a>
              <a href="mailto:info@premiumpropertydepot.com?subject=Enquiry%20for%20{name}">info@premiumpropertydepot.com</a>
            </div>
          </div>
          <div class="prop-enquiry-form-card">
            <h3>Express Enquiry</h3>
            <form action="mailto:info@premiumpropertydepot.com" method="GET" class="prop-form" onsubmit="handlePropSubmit(event, '{name}')">
              <input type="hidden" name="subject" value="Property Enquiry: {name}" />
              <div class="prop-form-group">
                <label for="form-name">Your Full Name</label>
                <input type="text" id="form-name" name="name" required placeholder="Dr. / Mr. / Ms." />
              </div>
              <div class="prop-form-row">
                <div class="prop-form-group">
                  <label for="form-phone">Phone Number</label>
                  <input type="tel" id="form-phone" name="phone" pattern="[0-9]{{10}}" maxlength="10" required placeholder="e.g. 9415378938" />
                </div>
                <div class="prop-form-group">
                  <label for="form-email">Email Address</label>
                  <input type="email" id="form-email" name="email" required placeholder="yourname@gmail.com" />
                </div>
              </div>
              <div class="prop-form-group">
                <label for="form-message">Specific Requirements</label>
                <textarea id="form-message" name="body" rows="3" placeholder="Interested in {name}. Please share latest pricing, floor plan, and site visit availability."></textarea>
              </div>
              <div class="prop-consent-check">
                <label>
                  <input type="checkbox" required checked />
                  <span>I authorize Premium Property Depot to contact me via call or email regarding {name}.</span>
                </label>
              </div>
              <button type="submit" class="prop-submit-btn">Send Enquiry via Email</button>
            </form>
          </div>
        </div>
      </section>

      <!-- SECTION 14: SIMILAR PROJECTS -->
      <section class="prop-section" id="similar">
        <h2>Similar Projects You May Like</h2>
        <div class="prop-similar-grid">
"""
    for sim in similar:
        html += f"""          <article class="prop-similar-card">
            <a href="{sim['slug']}.html" class="prop-similar-img-link">
              <img src="../{sim['image']}" alt="{sim['name']}" width="516" height="360" class="prop-similar-img" loading="lazy" />
            </a>
            <div class="prop-similar-body">
              <span class="prop-similar-city">{sim['city']}</span>
              <h3><a href="{sim['slug']}.html">{sim['name']}</a></h3>
              <p class="prop-similar-dev">{sim['developer']}</p>
              <p class="prop-similar-price">{sim['priceDisplay']}</p>
              <div class="prop-similar-actions">
                <a href="{sim['slug']}.html" class="prop-similar-view-btn">View Details ↗</a>
              </div>
            </div>
          </article>\n"""

    html += f"""        </div>
      </section>

    </div>
  </main>

  <!-- FOOTER -->
  {shared_footer('../')}

  <script>
    function handlePropSubmit(event, projectName) {{
      event.preventDefault();
      var name = document.getElementById('form-name').value;
      var phone = document.getElementById('form-phone').value;
      var email = document.getElementById('form-email').value;
      var msg = document.getElementById('form-message').value;
      var body = 'Property Enquiry for: ' + projectName + '\\r\\n' +
                 'Name: ' + name + '\\r\\n' +
                 'Phone: ' + phone + '\\r\\n' +
                 'Email: ' + email + '\\r\\n' +
                 'Requirements: ' + msg;
      var mailto = 'mailto:info@premiumpropertydepot.com?subject=' + encodeURIComponent('Property Enquiry: ' + projectName) + '&body=' + encodeURIComponent(body);
      window.location.href = mailto;
    }}
  </script>
</body>
</html>
"""
    return html

count = 0
for prop in properties:
    filepath = os.path.join('properties', f"{prop['slug']}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(generate_property_page(prop, properties))
    count += 1

print(f"Generated {count} dedicated property detail pages in properties/")

