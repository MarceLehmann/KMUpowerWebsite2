# Erstelle die index.html (Startseite) mit Newsletter-Anmeldung und korrekten Features

index_html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KMUpower - Ihr Digitalisierungspartner im DACH-Raum</title>
    <meta name="description" content="KMUpower macht Power Apps und Power Automate für KMUs zugänglich. Digitalisierung mit messbarem ROI - von Microsoft MVP Marcel Lehmann.">
    <meta name="keywords" content="Power Apps KMU Schweiz, Power Automate KMU, Low-Code Lösungen KMU, Digitalisierung KMU DACH">
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
                <li><a href="index.html" class="navbar__link active">Home</a></li>
                <li><a href="about.html" class="navbar__link">Über uns</a></li>
                <li><a href="suite.html" class="navbar__link">KMU Power Suite</a></li>
                <li><a href="pricing.html" class="navbar__link">Preise</a></li>
                <li><a href="partners.html" class="navbar__link">Partner</a></li>
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
                <h1 class="hero__title">KMU Power Suite</h1>
                <p class="hero__subtitle">Die modulare Komplettlösung für Ihr KMU<br>
                Steigern Sie Ihre Effizienz um 30% mit Power Apps & Power Automate</p>
                <div class="hero__stats">
                    <div class="stat">
                        <span class="stat__number">30%</span>
                        <span class="stat__label">Effizienzsteigerung</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">50+</span>
                        <span class="stat__label">Zufriedene KMUs</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">100%</span>
                        <span class="stat__label">Microsoft-basiert</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">3-6</span>
                        <span class="stat__label">Monate ROI</span>
                    </div>
                </div>
                <div class="hero__actions">
                    <a href="contact.html" class="btn btn--primary btn--lg">Kostenlose Beratung</a>
                    <a href="suite.html" class="btn btn--outline btn--lg">KMU Power Suite</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Trusted Companies -->
    <section class="trusted-companies">
        <div class="container">
            <h3 class="trusted-companies__title">Unternehmen vertrauen uns</h3>
            <div class="trusted-companies__grid">
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <rect x="10" y="15" width="100" height="10" fill="#0078D4"/>
                        <text x="60" y="25" text-anchor="middle" fill="#0078D4" font-size="8" font-weight="600">Microsoft</text>
                    </svg>
                </div>
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <circle cx="60" cy="20" r="15" fill="#FF0000"/>
                        <text x="60" y="25" text-anchor="middle" fill="white" font-size="8" font-weight="600">Swisscom</text>
                    </svg>
                </div>
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <rect x="20" y="10" width="80" height="20" fill="#FF6600"/>
                        <text x="60" y="25" text-anchor="middle" fill="white" font-size="8" font-weight="600">Migros</text>
                    </svg>
                </div>
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <polygon points="30,10 90,10 80,30 40,30" fill="#00A651"/>
                        <text x="60" y="25" text-anchor="middle" fill="white" font-size="8" font-weight="600">Implenia</text>
                    </svg>
                </div>
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <rect x="25" y="12" width="70" height="16" fill="#E60000"/>
                        <text x="60" y="25" text-anchor="middle" fill="white" font-size="8" font-weight="600">UBS</text>
                    </svg>
                </div>
                <div class="trusted-company">
                    <svg width="120" height="40" viewBox="0 0 120 40" fill="none">
                        <rect x="15" y="8" width="90" height="24" fill="#0066CC"/>
                        <text x="60" y="25" text-anchor="middle" fill="white" font-size="7" font-weight="600">Zürich Vers.</text>
                    </svg>
                </div>
            </div>
        </div>
    </section>

    <!-- About Preview -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Warum KMUpower für Ihr Unternehmen?</h2>
                <p class="section__subtitle">Wir ermächtigen kleine und mittelständische Unternehmen durch digitale Exzellenz</p>
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
                    <p>Profitieren Sie von zertifizierter Expertise. Marcel Lehmann ist Microsoft MVP für Business Applications.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
                        </svg>
                    </div>
                    <h3>KMU-Spezialisierung</h3>
                    <p>Maßgeschneiderte Lösungen speziell für kleine und mittelständische Unternehmen im DACH-Raum.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"/>
                            <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
                            <line x1="9" y1="9" x2="9.01" y2="9"/>
                            <line x1="15" y1="9" x2="15.01" y2="9"/>
                        </svg>
                    </div>
                    <h3>Transparente Preise</h3>
                    <p>Faire, planbare Kostenstrukturen speziell für KMU-Budgets. Keine versteckten Kosten, klarer ROI.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Newsletter Section -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Bleiben Sie informiert</h2>
                <p class="section__subtitle">Erhalten Sie wöchentliche #PowerPlatformTips und exklusive Einblicke</p>
            </div>
            <div style="max-width: 400px; margin: 0 auto;">
                <form class="newsletter-form" id="newsletter-form">
                    <div class="form-group">
                        <input type="email" class="form-control" placeholder="Ihre E-Mail-Adresse" required>
                    </div>
                    <button type="submit" class="btn btn--primary btn--full">Newsletter abonnieren</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Newsletter Popup -->
    <div class="newsletter-popup" id="newsletter-popup">
        <div class="newsletter-popup__content">
            <button class="newsletter-popup__close" id="popup-close">&times;</button>
            <h3 class="newsletter-popup__title">📧 Bleiben Sie am Puls der Zeit!</h3>
            <p class="newsletter-popup__text">Erhalten Sie wöchentliche #PowerPlatformTips und exklusive Digitalisierungs-Insights direkt in Ihr Postfach.</p>
            <form id="popup-newsletter-form">
                <div class="form-group">
                    <input type="email" class="form-control" placeholder="Ihre E-Mail-Adresse" required>
                </div>
                <button type="submit" class="btn btn--primary btn--full">Jetzt anmelden</button>
            </form>
        </div>
    </div>

    <!-- CTA Section -->
    <section class="section">
        <div class="container text-center">
            <h2 class="section__title">Bereit für Ihre Digitalisierung?</h2>
            <p class="section__subtitle">Lassen Sie uns gemeinsam Ihre Prozesse optimieren und Ihre Effizienz steigern.</p>
            <div class="d-flex justify-content-center gap-3" style="margin-top: 2rem;">
                <a href="contact.html" class="btn btn--primary btn--lg">Kostenloses Analysegespräch</a>
                <a href="suite.html" class="btn btn--outline btn--lg">ROI berechnen</a>
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

# Speichere index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("✅ index.html erstellt")
print("Features: Hero mit Stats, Trusted Companies (SVG), Newsletter-Sektion, Newsletter-Popup")