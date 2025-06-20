# Erstelle contact.html

contact_html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kontakt - Kostenloses Analysegespräch | KMUpower</title>
    <meta name="description" content="Kontaktieren Sie Marcel Lehmann für ein kostenloses Analysegespräch. Microsoft MVP für Business Applications im DACH-Raum. 24h Reaktionszeit garantiert.">
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
                <li><a href="partners.html" class="navbar__link">Partner</a></li>
                <li><a href="contact.html" class="navbar__link active">Kontakt</a></li>
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
                <h1 class="hero__title">Jetzt kostenlose Beratung anfragen</h1>
                <p class="hero__subtitle">Lassen Sie uns gemeinsam Ihre Digitalisierung vorantreiben<br>
                Kostenloser Digitaler Reifegradscheck und ROI-Berechnung</p>
                <div class="hero__stats">
                    <div class="stat">
                        <span class="stat__number">24h</span>
                        <span class="stat__label">Reaktionszeit</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">100%</span>
                        <span class="stat__label">Kostenfrei</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">MVP</span>
                        <span class="stat__label">Expertise</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Form Section -->
    <section class="section">
        <div class="container">
            <div class="grid grid--2">
                <!-- Contact Information -->
                <div class="card">
                    <h3>Marcel Lehmann</h3>
                    <p style="color: #48e0d1; font-weight: 600; margin-bottom: 1rem;">Microsoft MVP für Business Applications</p>
                    <div style="margin-bottom: 2rem;">
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#48e0d1" stroke-width="2">
                                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                                <circle cx="12" cy="10" r="3"/>
                            </svg>
                            <span>Zug, Schweiz</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#48e0d1" stroke-width="2">
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                <polyline points="22,6 12,13 2,6"/>
                            </svg>
                            <span>marcel@kmupower.ch</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#48e0d1" stroke-width="2">
                                <circle cx="12" cy="12" r="10"/>
                                <polyline points="12,6 12,12 16,14"/>
                            </svg>
                            <span>Mo-Fr: 8-18 Uhr</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#48e0d1" stroke-width="2">
                                <path d="M9 11H1v3h8v3l7-7-7-7v3z"/>
                            </svg>
                            <span>24h Reaktionszeit</span>
                        </div>
                    </div>

                    <h4>Serviceregionen</h4>
                    <ul style="list-style: none; padding: 0; margin: 1rem 0;">
                        <li style="margin-bottom: 0.5rem;">🇨🇭 <strong>Schweiz:</strong> Direkter Service in Zürich, Bern, Basel</li>
                        <li style="margin-bottom: 0.5rem;">🇩🇪 <strong>Deutschland:</strong> Partnernetzwerk in Süddeutschland</li>
                        <li style="margin-bottom: 0.5rem;">🇦🇹 <strong>Österreich:</strong> Remote-Service mit Fokus auf Wien</li>
                    </ul>
                </div>

                <!-- Contact Form -->
                <div class="card">
                    <h3>Kontaktformular</h3>
                    <form id="contact-form">
                        <div class="form-group">
                            <label class="form-label">Firma *</label>
                            <input type="text" class="form-control" name="company" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Name *</label>
                            <input type="text" class="form-control" name="name" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">E-Mail *</label>
                            <input type="email" class="form-control" name="email" required>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Telefon</label>
                            <input type="tel" class="form-control" name="phone">
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Anzahl Mitarbeiter</label>
                            <select class="form-control" name="employees">
                                <option value="">Bitte wählen</option>
                                <option value="1-9">1-9 Mitarbeiter</option>
                                <option value="10-24">10-24 Mitarbeiter</option>
                                <option value="25-49">25-49 Mitarbeiter</option>
                                <option value="50-99">50-99 Mitarbeiter</option>
                                <option value="100-249">100-249 Mitarbeiter</option>
                                <option value="250+">250+ Mitarbeiter</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Interesse an</label>
                            <select class="form-control" name="interest">
                                <option value="">Bitte wählen</option>
                                <option value="beratung">Digitalisierungsberatung</option>
                                <option value="suite">KMU Power Suite</option>
                                <option value="custom">Individuelle Lösung</option>
                                <option value="support">Support & Managed Services</option>
                                <option value="partner">Partner werden</option>
                                <option value="schulung">Schulungen</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Ihre Nachricht</label>
                            <textarea class="form-control" name="message" placeholder="Beschreiben Sie kurz Ihre Anforderungen oder Herausforderungen..."></textarea>
                        </div>
                        
                        <div class="form-group">
                            <button type="submit" class="btn btn--primary btn--full">
                                Kostenlose Beratung anfragen
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- What to Expect -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Das können Sie erwarten</h2>
                <p class="section__subtitle">Ihr Weg zur erfolgreichen Digitalisierung in 4 Schritten</p>
            </div>
            <div class="grid grid--4">
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="10,8 16,12 10,16"/>
                        </svg>
                    </div>
                    <h4>1. Kostenlose Analyse</h4>
                    <p>Digitaler Reifegradscheck Ihres Unternehmens und Identifikation von Optimierungspotenzialen.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                            <polyline points="14,2 14,8 20,8"/>
                        </svg>
                    </div>
                    <h4>2. Maßgeschneiderte Lösung</h4>
                    <p>Passende Empfehlungen für Ihre spezifischen Anforderungen und Unternehmensgröße.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="12" y1="1" x2="12" y2="23"/>
                            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                        </svg>
                    </div>
                    <h4>3. Transparente Kostenschätzung</h4>
                    <p>Klare ROI-Berechnung und realistische Amortisationszeiträume für alle Investitionen.</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <h4>4. Unverbindlicher Austausch</h4>
                    <p>Keine Verpflichtungen, nur wertvolle Erkenntnisse für Ihre Digitalisierungsstrategie.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Success Stories -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Kundenstimmen</h2>
                <p class="section__subtitle">Was unsere Kunden über die Zusammenarbeit sagen</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <p style="font-style: italic; margin-bottom: 1rem;">"Dank KMUpower konnten wir unsere Zeiterfassung um 40% effizienter gestalten und sparen monatlich CHF 2.000. Die Investition hat sich bereits nach 3 Monaten amortisiert."</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        Geschäftsführer, Produktionsunternehmen (50 MA)
                    </div>
                </div>
                <div class="card">
                    <p style="font-style: italic; margin-bottom: 1rem;">"Als Microsoft MVP bringt Marcel die perfekte Mischung aus technischer Expertise und praktischem KMU-Verständnis. Absolute Empfehlung!"</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        IT-Leiter, Dienstleistungsunternehmen
                    </div>
                </div>
                <div class="card">
                    <p style="font-style: italic; margin-bottom: 1rem;">"Die KMU Power Suite hat unsere Geschäftsprozesse revolutioniert. ROI bereits nach 4 Monaten erreicht und die Mitarbeiter sind begeistert."</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        CEO, Handelsunternehmen (25 MA)
                    </div>
                </div>
                <div class="card">
                    <p style="font-style: italic; margin-bottom: 1rem;">"Professionelle Beratung, schnelle Umsetzung und transparente Preise. Genau das, was wir als KMU gebraucht haben."</p>
                    <div style="font-weight: 600; color: #48e0d1;">
                        Geschäftsführer, IT-Dienstleister
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Häufige Fragen</h2>
                <p class="section__subtitle">Antworten auf die wichtigsten Fragen zur Zusammenarbeit</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <h4>Ist das Beratungsgespräch wirklich kostenlos?</h4>
                    <p>Ja, das Erstgespräch ist zu 100% kostenfrei und unverbindlich. Sie erhalten wertvolle Einblicke in Ihre Digitalisierungsmöglichkeiten ohne jede Verpflichtung.</p>
                </div>
                <div class="card">
                    <h4>Wie lange dauert die Implementierung?</h4>
                    <p>Die Implementierung der KMU Power Suite dauert typischerweise 4 Wochen für das Kernpaket. Einzelmodule können bereits in 1-2 Wochen produktiv sein.</p>
                </div>
                <div class="card">
                    <h4>Welche Microsoft-Lizenzen benötige ich?</h4>
                    <p>Microsoft 365 Business Standard (oder höher) pro User reicht aus. Keine Premium Power Apps Lizenz nötig. Wir beraten Sie gerne zur optimalen Lizenzierung.</p>
                </div>
                <div class="card">
                    <h4>Bieten Sie auch Schulungen an?</h4>
                    <p>Ja, wir bieten umfassende Schulungen für Ihre Mitarbeiter und IT-Teams an. Von Anwenderschulungen bis hin zu Citizen Developer Programmen.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Alternative Contact Methods -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Alternative Kontaktmöglichkeiten</h2>
            </div>
            <div class="grid grid--3">
                <div class="card text-center">
                    <h4>📧 Direkte E-Mail</h4>
                    <p>Schreiben Sie uns direkt an:</p>
                    <a href="mailto:marcel@kmupower.ch" class="btn btn--outline">marcel@kmupower.ch</a>
                </div>
                <div class="card text-center">
                    <h4>💼 LinkedIn</h4>
                    <p>Vernetzen Sie sich mit Marcel:</p>
                    <a href="https://linkedin.com/in/marcel-lehmann-powerplatform" target="_blank" class="btn btn--outline">LinkedIn Profil</a>
                </div>
                <div class="card text-center">
                    <h4>📅 Termin buchen</h4>
                    <p>Buchen Sie direkt einen Termin:</p>
                    <a href="#" class="btn btn--outline">Kalender öffnen</a>
                </div>
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

# Speichere contact.html
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("✅ contact.html erstellt")
print("Features: Kontaktformular, Marcel Lehmann Infos, Kundenstimmen, FAQ, alternative Kontaktmöglichkeiten")