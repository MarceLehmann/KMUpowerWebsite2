# Erstelle pricing.html mit korrekten Preisen

pricing_html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Preismodelle - Transparente Preise für KMU | KMUpower</title>
    <meta name="description" content="Transparente Preismodelle für KMU: Stability Retainer, FlexScale-Pakete, WinShare-Modell und KMU Power Suite. Faire Konditionen für den DACH-Raum.">
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
                <li><a href="pricing.html" class="navbar__link active">Preise</a></li>
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
                <h1 class="hero__title">Transparente Preismodelle</h1>
                <p class="hero__subtitle">Faire, planbare Preise speziell für KMU-Budgets entwickelt<br>
                Keine versteckten Kosten, klarer ROI</p>
                <div class="hero__stats">
                    <div class="stat">
                        <span class="stat__number">4</span>
                        <span class="stat__label">Preismodelle</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">CHF 200</span>
                        <span class="stat__label">Stundensatz</span>
                    </div>
                    <div class="stat">
                        <span class="stat__number">0%</span>
                        <span class="stat__label">Setup-Gebühren</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Stability Retainer -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Stability Retainer</h2>
                <p class="section__subtitle">Kontinuierliche Unterstützung für Ihre digitale Reise<br>
                <strong>Preise basieren auf wöchentlichen Stunden bei CHF 200/Stunde</strong></p>
            </div>
            <div class="grid grid--3">
                <div class="pricing-card">
                    <div class="pricing-card__title">1h-Paket</div>
                    <div class="pricing-card__price">CHF 800<span style="font-size: 1rem; color: #666;">/Monat</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>1h/Woche = 4h/Monat</strong></li>
                        <li>CHF 200/Stunde</li>
                        <li>Basis-Support & Bugfixes</li>
                        <li>Monitoring</li>
                        <li>Ad-hoc Beratung</li>
                        <li>E-Mail Support</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Anfragen</a>
                </div>
                <div class="pricing-card pricing-card--featured">
                    <div class="pricing-card__title">2h-Paket</div>
                    <div class="pricing-card__price">CHF 1.600<span style="font-size: 1rem; color: white;">/Monat</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>2h/Woche = 8h/Monat</strong></li>
                        <li>CHF 200/Stunde</li>
                        <li>Umfassender Support</li>
                        <li>Monitoring & Bugfixes</li>
                        <li>Kleinere Optimierungen</li>
                        <li>Monatliche Statusberichte</li>
                        <li>8h Reaktionszeit</li>
                    </ul>
                    <a href="contact.html" class="btn btn--primary btn--full">Beliebt</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">4h-Paket</div>
                    <div class="pricing-card__price">CHF 3.200<span style="font-size: 1rem; color: #666;">/Monat</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>4h/Woche = 16h/Monat</strong></li>
                        <li>CHF 200/Stunde</li>
                        <li>Intensive Betreuung</li>
                        <li>Wöchentliche Check-Ins</li>
                        <li>Proaktive Optimierung</li>
                        <li>4h Reaktionszeit</li>
                        <li>Mo-Fr, 8-18 Uhr Support</li>
                        <li>Strategische Beratung</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Anfragen</a>
                </div>
            </div>
            <div class="text-center" style="margin-top: 2rem;">
                <p style="color: #666; font-style: italic;">Nicht genutzte Stunden können zu 25% in den Folgemonat übertragen werden</p>
            </div>
        </div>
    </section>

    <!-- FlexScale -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">FlexScale-Pakete</h2>
                <p class="section__subtitle">Flexible Stundenpakete für projektbezogene Einsätze<br>
                12 Monate gültig, Best-Effort-Service</p>
            </div>
            <div class="grid grid--3" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div class="pricing-card">
                    <div class="pricing-card__title">Flex 5</div>
                    <div class="pricing-card__price">CHF 1.100</div>
                    <ul class="pricing-card__features">
                        <li>5 Stunden Guthaben</li>
                        <li>CHF 220/Stunde</li>
                        <li>12 Monate gültig</li>
                        <li>Best-Effort Support</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Buchen</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Flex 10</div>
                    <div class="pricing-card__price">CHF 2.100</div>
                    <ul class="pricing-card__features">
                        <li>10 Stunden Guthaben</li>
                        <li>CHF 210/Stunde</li>
                        <li>12 Monate gültig</li>
                        <li>Flexible Nutzung</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Buchen</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Flex 20</div>
                    <div class="pricing-card__price">CHF 4.000</div>
                    <ul class="pricing-card__features">
                        <li>20 Stunden Guthaben</li>
                        <li>CHF 200/Stunde</li>
                        <li>12 Monate gültig</li>
                        <li>Projektbezogene Nutzung</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Buchen</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Flex 30</div>
                    <div class="pricing-card__price">CHF 5.700</div>
                    <ul class="pricing-card__features">
                        <li>30 Stunden Guthaben</li>
                        <li>CHF 190/Stunde</li>
                        <li>12 Monate gültig</li>
                        <li>Mengenrabatt</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Buchen</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Flex 50</div>
                    <div class="pricing-card__price">CHF 8.500</div>
                    <ul class="pricing-card__features">
                        <li>50 Stunden Guthaben</li>
                        <li>CHF 170/Stunde</li>
                        <li>Bester Stundensatz</li>
                        <li>Umfangreiche Projekte</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Buchen</a>
                </div>
            </div>
        </div>
    </section>

    <!-- WinShare -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">WinShare-Modell</h2>
                <p class="section__subtitle">Erfolgsbasiertes Modell - Sie zahlen nur, wenn Sie sparen!</p>
            </div>
            <div style="max-width: 500px; margin: 0 auto;">
                <div class="pricing-card" style="background: linear-gradient(135deg, #48e0d1 0%, #3dd3c4 100%); color: white; border: none;">
                    <div class="pricing-card__title">Erfolgsbasierte Vergütung</div>
                    <div class="pricing-card__price">CHF 300 + 11%<span style="font-size: 1rem; color: white;"> der Einsparungen</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>Laufzeit: 6 Monate</strong></li>
                        <li>Monatlicher Fixbetrag: CHF 300</li>
                        <li>Erfolgsbeteiligung: 11% der realen Einsparungen</li>
                        <li>Nach 6 Monaten gehört die Lösung Ihnen</li>
                        <li>Win-Win-Situation für beide Seiten</li>
                    </ul>
                    <a href="contact.html" class="btn" style="background: white; color: #48e0d1; width: 100%;">Jetzt starten</a>
                </div>
            </div>
            <div class="text-center" style="margin-top: 2rem;">
                <h4>Beispielrechnung:</h4>
                <p>Bei einer Einsparung von CHF 1.000/Monat zahlen Sie:<br>
                <strong>CHF 300 + (1.000 × 0,11) = CHF 410/Monat</strong><br>
                Über 6 Monate: CHF 2.460 Gesamtkosten</p>
            </div>
        </div>
    </section>

    <!-- KMU Power Suite -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">KMU Power Suite Pakete</h2>
                <p class="section__subtitle">Einmalige Implementierungskosten für modulare Business-Lösung</p>
            </div>
            <div class="grid grid--3">
                <div class="pricing-card">
                    <div class="pricing-card__title">Einzelmodul</div>
                    <div class="pricing-card__price">CHF 1.000</div>
                    <ul class="pricing-card__features">
                        <li>1 Modul nach Wahl</li>
                        <li>Grundeinrichtung</li>
                        <li>4 Wochen Implementierung</li>
                        <li>Basis-Schulung</li>
                        <li>30 Tage Support</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Anfragen</a>
                </div>
                <div class="pricing-card pricing-card--featured">
                    <div class="pricing-card__title">Kernpaket</div>
                    <div class="pricing-card__price">CHF 2.222</div>
                    <ul class="pricing-card__features">
                        <li><strong>3 Kernmodule</strong></li>
                        <li>CRM + Mailing + Mitarbeiterverwaltung</li>
                        <li>Vollständige Integration</li>
                        <li>Umfassende Schulung</li>
                        <li>60 Tage Support</li>
                    </ul>
                    <a href="contact.html" class="btn btn--primary btn--full">Beliebt</a>
                </div>
                <div class="pricing-card">
                    <div class="pricing-card__title">Komplett</div>
                    <div class="pricing-card__price">CHF 7.500</div>
                    <ul class="pricing-card__features">
                        <li><strong>7 Module inkludiert</strong></li>
                        <li>Alle Kern- und Add-on Module</li>
                        <li>20h Support inkludiert</li>
                        <li>Premium-Schulung</li>
                        <li>90 Tage Support</li>
                        <li>Strategische Beratung</li>
                    </ul>
                    <a href="contact.html" class="btn btn--outline btn--full">Anfragen</a>
                </div>
            </div>
            <div class="text-center" style="margin-top: 2rem;">
                <p><strong>Nachkauf-Staffel:</strong> 2. Modul CHF 900, 3. Modul CHF 800, 4. Modul CHF 700, 5. Modul CHF 600, ab 6. Modul CHF 500</p>
            </div>
        </div>
    </section>

    <!-- Special IT Companies Offer -->
    <section class="section">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Spezielles IT-Firmen-Angebot</h2>
                <p class="section__subtitle">Retainer-Modell für IT-Dienstleister und Partner</p>
            </div>
            <div style="max-width: 500px; margin: 0 auto;">
                <div class="pricing-card" style="border-color: #48e0d1;">
                    <div class="pricing-card__title">IT-Partner Retainer</div>
                    <div class="pricing-card__price">CHF 1.400<span style="font-size: 1rem; color: #666;">/Monat</span></div>
                    <ul class="pricing-card__features">
                        <li><strong>8 Stunden Support pro Monat</strong></li>
                        <li>Regulär CHF 1.600 (Sie sparen CHF 200)</li>
                        <li>Garantierte SLA: 4h Reaktionszeit</li>
                        <li>Werktags 8-18 Uhr Service</li>
                        <li>Integrierbar in IT-Serviceprozesse</li>
                        <li>White-Label-Option möglich</li>
                        <li><strong>Bonus:</strong> Bei 12-Monats-Vertrag gratis 4h Schulung</li>
                    </ul>
                    <a href="partners.html" class="btn btn--primary btn--full">Partner werden</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Pricing Overview -->
    <section class="section section--bg">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Alle Preise beinhalten</h2>
            </div>
            <div class="grid grid--4">
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M9 12l2 2 4-4M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z"/>
                        </svg>
                    </div>
                    <h4>Keine Setup-Gebühren</h4>
                    <p>0% Einrichtungskosten bei allen Modellen</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14 9V5a3 3 0 0 0-6 0v4a3 3 0 0 0 6 0z"/>
                            <path d="M5 9a3 3 0 0 1 6 0v5a3 3 0 0 1-6 0z"/>
                        </svg>
                    </div>
                    <h4>Transparente Kosten</h4>
                    <p>Klare Kostenstrukturen ohne Überraschungen</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="7" height="7"/>
                            <rect x="14" y="3" width="7" height="7"/>
                            <rect x="14" y="14" width="7" height="7"/>
                            <rect x="3" y="14" width="7" height="7"/>
                        </svg>
                    </div>
                    <h4>Microsoft-Lizenzberatung</h4>
                    <p>Optimierung Ihrer Microsoft 365 Lizenzierung</p>
                </div>
                <div class="card">
                    <div class="card__icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                        </svg>
                    </div>
                    <h4>Regelmäßige Updates</h4>
                    <p>Kostenlose Updates und Optimierungen</p>
                </div>
            </div>
            <div class="text-center" style="margin-top: 2rem;">
                <p style="color: #666;"><small>Alle Preise exkl. MwSt. für den DACH-Raum. Zahlungsbedingungen: 30 Tage netto.</small></p>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="section">
        <div class="container text-center">
            <h2 class="section__title">Bereit für Ihre Digitalisierung?</h2>
            <p class="section__subtitle">Wählen Sie das passende Preismodell oder lassen Sie sich kostenlos beraten.</p>
            <div class="d-flex justify-content-center gap-3" style="margin-top: 2rem;">
                <a href="contact.html" class="btn btn--primary btn--lg">Kostenloses Beratungsgespräch</a>
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

# Speichere pricing.html
with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(pricing_html)

print("✅ pricing.html erstellt")
print("Features: Korrekte Stability Retainer Preise (wöchentlich), FlexScale, WinShare, Suite-Pakete, IT-Firmen-Angebot")