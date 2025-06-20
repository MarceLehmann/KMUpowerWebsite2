# Erstelle partners.html für IT-Dienstleister

partners_html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Partner & IT-Dienstleister - Gemeinsam stark | KMUpower</title>
    <meta name="description" content="Werden Sie KMUpower Partner. Spezielle Konditionen für IT-Dienstleister, White-Label-Lösungen und Referral-Programm für Power Platform Services.">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="container">
            <div class="navbar__brand">
                <h2>KMUpower</h2>
            </div>
            <ul class="navbar__menu" id="navbar-menu">
                <li><a href="index.html" class="navbar__link">Home</a></li>
                <li><a href="about.html" class="navbar__link">Über uns</a></li>
                <li><a href="suite.html" class="navbar__link">KMU Power Suite</a></li>
                <li><a href="pricing.html" class="navbar__link">Preise</a></li>
                <li><a href="partners.html" class="navbar__link active">Partner</a></li>
                <li><a href="contact.html" class="navbar__link">Kontakt</a></li>
            </ul>
            <button class="navbar__toggle" id="navbar-toggle">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero__content">
                <h1 class="hero__title">Partner & IT-Dienstleister</h1>
                <p class="hero__subtitle">Erweitern Sie Ihr Portfolio mit Microsoft Power Platform Expertise<br>
                Profitieren Sie von unserem Microsoft MVP Know-how</p>
                <div class="hero__stats">
                    <div class="stat">
                        <span class="stat__number">15%</span>
                        <span class="stat__label">Referral-Provision</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">MVP</span>
                        <span class="stat__label">Microsoft Expertise</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">24h</span>
                        <span class="stat__label">SLA Support</span>
                    </div>
                </div>
                <div class="hero__actions">
                    <a href="contact.html" class="btn btn--primary btn--lg">Partner werden</a>
                    <a href="#partner-benefits" class="btn btn--outline btn--lg">Vorteile entdecken</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Partner Benefits -->
    <section class="section" id="partner-benefits">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Warum mit KMUpower partnern?</h2>
                <p class="section__subtitle">Maximieren Sie Ihre Geschäftsmöglichkeiten mit unserem Partnerprogramm</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 11 5.16-1.26 9-5.45 9-11V7l-10-5z"/>
                            <path d="M9 12l2 2 4-4"/>
                        </svg>
                    </div>
                    <h3>Microsoft MVP Expertise</h3>
                    <p>Profitieren Sie von zertifizierter Microsoft MVP Expertise ohne eigene Spezialisierung aufbauen zu müssen.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="1" x2="12" y2="23"/>
                            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                        </svg>
                    </div>
                    <h3>Neue Umsatzquellen</h3>
                    <p>Erschließen Sie lukrative Power Platform Projekte und erweitern Sie Ihr Service-Portfolio profitabel.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <h3>White-Label Services</h3>
                    <p>Bieten Sie Power Platform Services unter Ihrer Marke an - Ihre Kunden, unser Know-how.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                        </svg>
                    </div>
                    <h3>Schnelle Implementierung</h3>
                    <p>Keine langen Einarbeitungszeiten - starten Sie sofort mit Power Platform Projekten für Ihre Kunden.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9c2.03 0 4.43.82 6.3 2.5"/>
                            <path d="M12 16v-4l3-3"/>
                        </svg>
                    </div>
                    <h3>Garantierte SLAs</h3>
                    <p>Verlässliche 4h Reaktionszeit und professioneller Support für Ihre Kundenprojekte.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <h3>Schulungen & Enablement</h3>
                    <p>Kostenlose Schulungen für Ihr Team und kontinuierliche Weiterbildung in Power Platform Technologien.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Partner Programs -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Unsere Partnerprogramme</h2>
                <p class="section__subtitle">Wählen Sie das Programm, das am besten zu Ihrem Geschäftsmodell passt</p>
            </div>
            <div class="grid grid--3">
                <div class="pricing-card">
                    <div class="pricing-card__title">Referral Partner</div>
                    <div class="pricing-card__price">15%<span style="font-size: 1rem; color: #666;"> Provision</span></div>
                    <ul class="pricing-card__features">
                        <li>Keine Mindestanforderungen</li>
                        <li>15% Provision auf vermittelte Projekte</li>
                        <li>Marketing-Materialien</li>
                        <li>Einfache Registrierung</li>
                        <li>Monatliche Auszahlung</li>
                        <li>Transparentes Tracking</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Kostenlos registrieren</a>
                </div>
                <div class="pricing-card pricing-card--featured">
                    <div class="pricing-card__title">Solution Partner</div>
                    <div class="pricing-card__price">CHF 1.400<span style="font-size: 1rem; color: white;">/Monat</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>8h monatlicher Retainer</strong></li>
                        <li>White-Label Services</li>
                        <li>Ihre Marke, unser Know-how</li>
                        <li>4h SLA Reaktionszeit</li>
                        <li>Kostenlose Team-Schulungen</li>
                        <li>Premium-Support</li>
                        <li>Co-Marketing Möglichkeiten</li>
                    </ul>
                    <a href="contact.html" class="btn btn--primary btn--full">Partner werden</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Strategic Partner</div>
                    <div class="pricing-card__price">Individual</div>
                    <ul class="pricing-card__features">
                        <li>Maßgeschneidertes Programm</li>
                        <li>Exklusive Gebietsrechte</li>
                        <li>Dedizierter Account Manager</li>
                        <li>Gemeinsame Marktbearbeitung</li>
                        <li>Produkt-Mitentwicklung</li>
                        <li>Strategische Roadmap-Planung</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Gespräch vereinbaren</a>
                </div>
            </div>
        </div>
    </section>

    <!-- IT Service Provider Benefits -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Speziell für IT-Dienstleister</h2>
                <p class="section__subtitle">Maximieren Sie Ihren Kundennutzen mit Power Platform Expertise</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <h3>Erweitern Sie Ihr Portfolio</h3>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>Power Apps Entwicklung</li>
                        <li>Power Automate Workflows</li>
                        <li>SharePoint-Integration</li>
                        <li>Microsoft 365 Optimierung</li>
                        <li>Business Intelligence</li>
                        <li>Prozessautomatisierung</li>
                    </ul>
                    <p>Ohne eigene Entwicklerressourcen aufbauen zu müssen.</p>
                </div>
                <div class="card">
                    <h3>Ihre Vorteile auf einen Blick</h3>
                    <ul style="text-align: left; margin: 1rem 0;">
                        <li>✅ Sofort verfügbare Expertise</li>
                        <li>✅ Keine Investition in Ausbildung</li>
                        <li>✅ Garantierte Qualität durch MVP</li>
                        <li>✅ Planbare Kosten</li>
                        <li>✅ Skalierbare Kapazitäten</li>
                        <li>✅ White-Label möglich</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Success Stories -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Partner-Erfolgsgeschichten</h2>
                <p class="section__subtitle">Wie unsere Partner von der Zusammenarbeit profitieren</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <h4>IT-Systemhaus Bayern</h4>
                    <p style="font-style: italic; margin: 1rem 0;">"Dank der Partnerschaft mit KMUpower konnten wir unser Service-Portfolio um Power Platform erweitern, ohne eigene Spezialisten aufzubauen. In 6 Monaten haben wir zusätzlich CHF 85.000 Umsatz generiert."</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        Geschäftsführer IT-Systemhaus
                    </div>
                </div>
                <div class="card">
                    <h4>Managed Service Provider</h4>
                    <p style="font-style: italic; margin: 1rem 0;">"Die White-Label-Lösung ermöglicht es uns, Power Platform Services unter unserer Marke anzubieten. Unsere Kunden schätzen die professionelle Umsetzung und wir die planbaren Kosten."</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        CEO Managed Services AG
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Partner Onboarding -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Ihr Weg zur Partnerschaft</h2>
                <p class="section__subtitle">In 4 einfachen Schritten zum erfolgreichen Partner</p>
            </div>
            <div class="grid grid--4">
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14,2 14,8 20,8"/>
                        </svg>
                    </div>
                    <h4>1. Anmeldung</h4>
                    <p>Registrieren Sie sich als Partner über unser Kontaktformular</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9c2.03 0 4.43.82 6.3 2.5"/>
                            <path d="M12 16v-4l3-3"/>
                        </svg>
                    </div>
                    <h4>2. Gespräch</h4>
                    <p>Persönliches Kennenlernen und Abstimmung der Zusammenarbeit</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <h4>3. Onboarding</h4>
                    <p>Einführung in unsere Prozesse und Schulung Ihres Teams</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                        </svg>
                    </div>
                    <h4>4. Start</h4>
                    <p>Beginnen Sie mit Power Platform Projekten für Ihre Kunden</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="section section--bg">
        <div class="container text-center">
            <h2 class="section__title">Bereit für eine erfolgreiche Partnerschaft?</h2>
            <p class="section__subtitle">Lassen Sie uns gemeinsam Ihre Geschäftsmöglichkeiten erweitern.</p>
            <div class="d-flex justify-content-center gap-3" style="margin-top: 2rem;">
                <a href="contact.html" class="btn btn--primary btn--lg">Partner werden</a>
                <a href="mailto:marcel@kmupower.ch" class="btn btn--outline btn--lg">Direkt kontaktieren</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer__content">
                <div class="footer__brand">
                    <h3>KMUpower</h3>
                    <p>Ihr Digitalisierungspartner im DACH-Raum. Wir ermächtigen KMUs durch Microsoft Power Platform Expertise.</p>
                </div>
                <div class="footer__column">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="suite.html">KMU Power Suite</a></li>
                        <li><a href="pricing.html">Preismodelle</a></li>
                        <li><a href="partners.html">Partner werden</a></li>
                        <li><a href="contact.html">Beratung</a></li>
                    </ul>
                </div>
                <div class="footer__column">
                    <h4>Unternehmen</h4>
                    <ul>
                        <li><a href="about.html">Über uns</a></li>
                        <li><a href="contact.html">Kontakt</a></li>
                        <li>Datenschutz</li>
                        <li>Impressum</li>
                    </ul>
                </div>
                <div class="footer__column">
                    <h4>Kontakt</h4>
                    <ul>
                        <li>marcel@kmupower.ch</li>
                        <li>Zug, Schweiz</li>
                        <li>DACH-Region Service</li>
                    </ul>
                </div>
            </div>
            <div class="footer__bottom">
                <p>&copy; 2025 KMUpower. Alle Rechte vorbehalten. Microsoft MVP für Business Applications.</p>
            </div>
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>"""

# Speichere partners.html
with open('partners.html', 'w', encoding='utf-8') as f:
    f.write(partners_html)

print("✅ partners.html erstellt")
print("Features: Partnerprogramme, IT-Dienstleister Vorteile, Referral-Programm, White-Label Services")