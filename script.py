# Erstelle alle HTML-Seiten für die KMUpower Website V2.0 mit korrekten Preisen und Features

# Definiere die Unternehmensfarbe und andere Variablen
brand_color = "#48e0d1"
secondary_color = "#2c3e50"
text_color = "#333333"

# Gemeinsames CSS mit der korrekten Unternehmensfarbe
css_content = f"""
:root {{
  /* KMUpower Brand Colors */
  --color-brand-primary: {brand_color};
  --color-brand-primary-hover: #3dd3c4;
  --color-brand-secondary: {secondary_color};
  --color-text: {text_color};
  --color-text-light: #666666;
  --color-background: #ffffff;
  --color-surface: #f8f9fa;
  --color-border: #e0e0e0;
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-error: #dc3545;
  
  /* Typography */
  --font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  --font-size-base: 16px;
  --font-size-sm: 14px;
  --font-size-lg: 18px;
  --font-size-xl: 24px;
  --font-size-2xl: 32px;
  --font-size-3xl: 48px;
  
  /* Spacing */
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  --spacing-md: 24px;
  --spacing-lg: 32px;
  --spacing-xl: 48px;
  --spacing-2xl: 64px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  
  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 8px rgba(0,0,0,0.12);
  --shadow-lg: 0 8px 16px rgba(0,0,0,0.15);
}}

/* Reset & Base Styles */
* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  color: var(--color-text);
  line-height: 1.6;
  background-color: var(--color-background);
}}

/* Container */
.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-sm);
}}

/* Navigation */
.navbar {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--color-border);
  z-index: 1000;
  transition: all 0.3s ease;
}}

.navbar.scrolled {{
  background: rgba(255, 255, 255, 0.98);
  box-shadow: var(--shadow-sm);
}}

.navbar .container {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--spacing-sm);
}}

.navbar__brand h2 {{
  color: var(--color-brand-primary);
  font-size: var(--font-size-xl);
  font-weight: 700;
}}

.navbar__menu {{
  display: flex;
  list-style: none;
  gap: var(--spacing-lg);
  margin: 0;
}}

.navbar__link {{
  color: var(--color-text);
  text-decoration: none;
  font-weight: 500;
  padding: var(--spacing-xs) 0;
  position: relative;
  transition: color 0.3s ease;
}}

.navbar__link:hover,
.navbar__link.active {{
  color: var(--color-brand-primary);
}}

.navbar__link::after {{
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--color-brand-primary);
  transition: width 0.3s ease;
}}

.navbar__link:hover::after,
.navbar__link.active::after {{
  width: 100%;
}}

.navbar__toggle {{
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--spacing-xs);
}}

.navbar__toggle span {{
  width: 24px;
  height: 2px;
  background: var(--color-text);
  margin: 2px 0;
  transition: all 0.3s ease;
}}

/* Buttons */
.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: 600;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}}

.btn--primary {{
  background: var(--color-brand-primary);
  color: white;
}}

.btn--primary:hover {{
  background: var(--color-brand-primary-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}}

.btn--outline {{
  background: transparent;
  color: var(--color-brand-primary);
  border: 2px solid var(--color-brand-primary);
}}

.btn--outline:hover {{
  background: var(--color-brand-primary);
  color: white;
}}

.btn--lg {{
  padding: var(--spacing-md) var(--spacing-lg);
  font-size: var(--font-size-lg);
}}

.btn--full {{
  width: 100%;
}}

/* Hero Section */
.hero {{
  padding: 120px 0 var(--spacing-2xl);
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  text-align: center;
  margin-top: 80px;
}}

.hero__title {{
  font-size: clamp(var(--font-size-2xl), 5vw, var(--font-size-3xl));
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: var(--spacing-md);
}}

.hero__subtitle {{
  font-size: var(--font-size-lg);
  color: var(--color-text-light);
  margin-bottom: var(--spacing-xl);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}}

.hero__stats {{
  display: flex;
  justify-content: center;
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-xl);
  flex-wrap: wrap;
}}

.stat {{
  text-align: center;
}}

.stat__number {{
  display: block;
  font-size: var(--font-size-2xl);
  font-weight: 700;
  color: var(--color-brand-primary);
  margin-bottom: var(--spacing-xs);
}}

.stat__label {{
  font-size: var(--font-size-sm);
  color: var(--color-text-light);
  font-weight: 500;
}}

.hero__actions {{
  display: flex;
  gap: var(--spacing-md);
  justify-content: center;
  flex-wrap: wrap;
}}

/* Trusted Companies */
.trusted-companies {{
  padding: var(--spacing-xl) 0;
  background: var(--color-surface);
  text-align: center;
}}

.trusted-companies__title {{
  margin-bottom: var(--spacing-lg);
  color: var(--color-text-light);
  font-size: var(--font-size-lg);
  font-weight: 500;
}}

.trusted-companies__grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: var(--spacing-md);
  max-width: 800px;
  margin: 0 auto;
}}

.trusted-company {{
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-md);
  background: var(--color-background);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  transition: all 0.3s ease;
}}

.trusted-company:hover {{
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}}

/* Cards */
.card {{
  background: var(--color-background);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  padding: var(--spacing-lg);
  transition: all 0.3s ease;
}}

.card:hover {{
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}}

.card__icon {{
  width: 60px;
  height: 60px;
  background: var(--color-brand-primary);
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto var(--spacing-md) auto;
}}

.card__icon svg {{
  color: white;
  width: 32px;
  height: 32px;
}}

.card h3, .card h4 {{
  color: var(--color-text);
  margin-bottom: var(--spacing-sm);
  text-align: center;
}}

.card p {{
  color: var(--color-text-light);
  text-align: center;
  margin-bottom: 0;
}}

/* Grid Layouts */
.grid {{
  display: grid;
  gap: var(--spacing-lg);
}}

.grid--2 {{
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}}

.grid--3 {{
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}}

.grid--4 {{
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}}

/* Sections */
.section {{
  padding: var(--spacing-2xl) 0;
}}

.section--bg {{
  background: var(--color-surface);
}}

.section__header {{
  text-align: center;
  margin-bottom: var(--spacing-xl);
}}

.section__title {{
  font-size: var(--font-size-2xl);
  color: var(--color-text);
  margin-bottom: var(--spacing-md);
  font-weight: 700;
}}

.section__subtitle {{
  font-size: var(--font-size-lg);
  color: var(--color-text-light);
  max-width: 600px;
  margin: 0 auto;
}}

/* Forms */
.form-group {{
  margin-bottom: var(--spacing-md);
}}

.form-label {{
  display: block;
  margin-bottom: var(--spacing-xs);
  font-weight: 500;
  color: var(--color-text);
}}

.form-control {{
  width: 100%;
  padding: var(--spacing-sm);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  color: var(--color-text);
  background: var(--color-background);
  transition: border-color 0.3s ease;
}}

.form-control:focus {{
  outline: none;
  border-color: var(--color-brand-primary);
  box-shadow: 0 0 0 3px rgba(72, 224, 209, 0.1);
}}

textarea.form-control {{
  resize: vertical;
  min-height: 120px;
}}

/* Newsletter Popup */
.newsletter-popup {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}}

.newsletter-popup.show {{
  display: flex;
}}

.newsletter-popup__content {{
  background: var(--color-background);
  padding: var(--spacing-xl);
  border-radius: var(--radius-xl);
  max-width: 400px;
  width: 90%;
  position: relative;
  text-align: center;
}}

.newsletter-popup__close {{
  position: absolute;
  top: var(--spacing-sm);
  right: var(--spacing-sm);
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--color-text-light);
}}

.newsletter-popup__title {{
  color: var(--color-brand-primary);
  margin-bottom: var(--spacing-sm);
}}

.newsletter-popup__text {{
  color: var(--color-text-light);
  margin-bottom: var(--spacing-lg);
}}

/* ROI Calculator */
.roi-calculator {{
  background: var(--color-surface);
  padding: var(--spacing-xl);
  border-radius: var(--radius-xl);
  margin: var(--spacing-xl) 0;
}}

.calculator-inputs {{
  display: grid;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}}

.calculator-results {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--spacing-md);
}}

.result-card {{
  background: var(--color-background);
  padding: var(--spacing-md);
  border-radius: var(--radius-lg);
  text-align: center;
  border: 1px solid var(--color-border);
}}

.result-card__label {{
  font-size: var(--font-size-sm);
  color: var(--color-text-light);
  margin-bottom: var(--spacing-xs);
}}

.result-card__value {{
  font-size: var(--font-size-xl);
  font-weight: 700;
  color: var(--color-brand-primary);
}}

.slider {{
  width: 100%;
  height: 8px;
  border-radius: var(--radius-sm);
  background: var(--color-border);
  outline: none;
  -webkit-appearance: none;
}}

.slider::-webkit-slider-thumb {{
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--color-brand-primary);
  cursor: pointer;
}}

.slider::-moz-range-thumb {{
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--color-brand-primary);
  cursor: pointer;
  border: none;
}}

/* Pricing Cards */
.pricing-card {{
  background: var(--color-background);
  border: 2px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--spacing-xl);
  text-align: center;
  position: relative;
  transition: all 0.3s ease;
}}

.pricing-card:hover {{
  border-color: var(--color-brand-primary);
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}}

.pricing-card--featured {{
  border-color: var(--color-brand-primary);
  background: linear-gradient(135deg, var(--color-brand-primary) 0%, var(--color-brand-primary-hover) 100%);
  color: white;
  transform: scale(1.05);
}}

.pricing-card--featured::before {{
  content: 'Beliebt';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-brand-primary);
  color: white;
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-lg);
  font-size: var(--font-size-sm);
  font-weight: 600;
}}

.pricing-card__title {{
  font-size: var(--font-size-lg);
  font-weight: 600;
  margin-bottom: var(--spacing-md);
}}

.pricing-card__price {{
  font-size: var(--font-size-2xl);
  font-weight: 700;
  color: var(--color-brand-primary);
  margin-bottom: var(--spacing-md);
}}

.pricing-card--featured .pricing-card__price {{
  color: white;
}}

.pricing-card__features {{
  list-style: none;
  margin-bottom: var(--spacing-lg);
}}

.pricing-card__features li {{
  padding: var(--spacing-xs) 0;
  border-bottom: 1px solid var(--color-border);
}}

.pricing-card__features li:last-child {{
  border-bottom: none;
}}

/* Footer */
.footer {{
  background: var(--color-brand-secondary);
  color: white;
  padding: var(--spacing-xl) 0 var(--spacing-lg);
}}

.footer__content {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
}}

.footer__brand h3 {{
  color: var(--color-brand-primary);
  margin-bottom: var(--spacing-sm);
}}

.footer__brand p {{
  color: rgba(255, 255, 255, 0.8);
}}

.footer__column h4 {{
  color: white;
  margin-bottom: var(--spacing-md);
}}

.footer__column ul {{
  list-style: none;
}}

.footer__column li {{
  margin-bottom: var(--spacing-xs);
}}

.footer__column a {{
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: color 0.3s ease;
}}

.footer__column a:hover {{
  color: var(--color-brand-primary);
}}

.footer__bottom {{
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  padding-top: var(--spacing-md);
  text-align: center;
}}

.footer__bottom p {{
  color: rgba(255, 255, 255, 0.6);
  margin: 0;
}}

/* Utilities */
.text-center {{ text-align: center; }}
.text-left {{ text-align: left; }}
.text-right {{ text-align: right; }}

.mb-0 {{ margin-bottom: 0; }}
.mb-1 {{ margin-bottom: var(--spacing-xs); }}
.mb-2 {{ margin-bottom: var(--spacing-sm); }}
.mb-3 {{ margin-bottom: var(--spacing-md); }}
.mb-4 {{ margin-bottom: var(--spacing-lg); }}

.mt-0 {{ margin-top: 0; }}
.mt-1 {{ margin-top: var(--spacing-xs); }}
.mt-2 {{ margin-top: var(--spacing-sm); }}
.mt-3 {{ margin-top: var(--spacing-md); }}
.mt-4 {{ margin-top: var(--spacing-lg); }}

.d-flex {{ display: flex; }}
.align-items-center {{ align-items: center; }}
.justify-content-center {{ justify-content: center; }}
.justify-content-between {{ justify-content: space-between; }}
.gap-1 {{ gap: var(--spacing-xs); }}
.gap-2 {{ gap: var(--spacing-sm); }}
.gap-3 {{ gap: var(--spacing-md); }}

/* Responsive */
@media (max-width: 768px) {{
  .navbar__menu {{
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: var(--spacing-md);
    box-shadow: var(--shadow-md);
    gap: 0;
  }}

  .navbar__menu.active {{
    display: flex;
  }}

  .navbar__toggle {{
    display: flex;
  }}

  .hero {{
    padding: 100px 0 var(--spacing-xl);
  }}

  .hero__stats {{
    gap: var(--spacing-md);
  }}

  .hero__actions {{
    flex-direction: column;
    align-items: center;
  }}

  .grid--2,
  .grid--3,
  .grid--4 {{
    grid-template-columns: 1fr;
  }}

  .calculator-results {{
    grid-template-columns: 1fr;
  }}

  .pricing-card--featured {{
    transform: none;
  }}
}}

/* Animation classes */
.fade-in {{
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.6s ease-out;
}}

.fade-in.visible {{
  opacity: 1;
  transform: translateY(0);
}}

/* Smooth scrolling */
html {{
  scroll-behavior: smooth;
}}
"""

# Speichere das CSS
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS-Datei erstellt mit KMUpower Branding (#48e0d1)")
print("Nächster Schritt: HTML-Seiten erstellen...")