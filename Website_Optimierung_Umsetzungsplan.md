# KMUpower Website – Konkreter Umsetzungsplan

## 🚨 1. Kritische Sofortmassnahmen (Woche 1)

### 1.1 Preismodell-Korrekturen (Stability Retainer) ✅ erledigt
- **Datei:** `pricing.html`
- **Aktion:** Ersetze die aktuellen Pakete durch die korrekten Pakete und Preise:
  - 1h-Paket: CHF 220/h → CHF 880/Monat (4h)
  - 2h-Paket: CHF 210/h → CHF 1.680/Monat (8h)
  - 4h-Paket: CHF 200/h → CHF 3.200/Monat (16h)
  - 8h-Paket: CHF 190/h → CHF 6.080/Monat (32h)
  - 16h-Paket: CHF 180/h → CHF 11.520/Monat (64h)
- **Hinweis:** Immer Stundenpreis UND Monatswert (x4) angeben. Feature-Listen und Stundenzahlen anpassen.

### 1.2 Stundensatz-Konsistenz ✅ erledigt
- **Dateien:** `pricing.html`, `index.html`
- **Aktion:** Stelle sicher, dass der Stundensatz (CHF 200/h als Basis) überall korrekt und einheitlich kommuniziert wird. Hinweis: Es gibt gestaffelte Preise für Retainer und FlexScale, daher wird auf der Startseite auf die transparente Preisstaffelung und die Preisseite verwiesen.

### 1.3 Analytics & Tracking ✅ erledigt
- **Datei:** `index.html` (und alle Hauptseiten)
- **Aktion:** Google Analytics 4 Code (und optional Microsoft Clarity) im `<head>`-Bereich eingefügt. GA4-Mess-ID muss noch eingetragen werden.

### 1.4 Schema.org Markup ✅ erledigt
- **Datei:** `index.html` (und alle Hauptseiten)
- **Aktion:** LocalBusiness/ProfessionalService Schema.org Markup im <head>-Bereich eingefügt.

---

## ⚡ 2. Kurzfristige Optimierungen (2-4 Wochen)

### 2.1 Testimonials & Social Proof ✅ erledigt
- **Datei:** `index.html` (neue Section nach trusted-companies)
- **Aktion:** Authentische Testimonials-Sektion mit 3 passenden Platzhalter-Kundenstimmen eingefügt.

### 2.2 Case Studies ✅ erledigt
- **Datei:** Neue Seite `case-studies.html`
- **Aktion:** 3 authentische, passende Beispiel-Erfolgsgeschichten als Case Studies angelegt.

### 2.3 SEO-Keywords Integration ✅ erledigt
- **Dateien:** `index.html`, `about.html`, `suite.html`, `pricing.html`
- **Aktion:** Optimiere Title, Description, Überschriften und Fliesstext für die wichtigsten Keywords aus der SEO-Strategie.

### 2.4 Performance-Optimierung ✅ erledigt
- **Dateien:** `style.css`, `app.js`, Bilder
- **Aktion:** Minifiziere CSS/JS, optimiere Bilder (WebP), aktiviere Browser-Caching.

---

## 📈 3. Mittelfristig (1-3 Monate)

### 3.1 Blog-Sektion ✅ erledigt
- **Datei:** Neue Struktur `/blog/`
- **Aktion:** Erstelle Blog-Übersicht und erste Beiträge (KMU Digitalisierung). -> wichtig: mittels jekyll und markdowns

### 3.2 Lead Magnets & Newsletter (übersprungen)
- **Datei:** `index.html`, `newsletter-form`
- **Aktion:** Biete Download (z.B. ROI-Rechner als Excel) gegen E-Mail an, verbessere Newsletter-Opt-In.
- **Conversion-Kette:** Verknüpfe den Lead Magnet (z.B. ROI-Rechner) im Content gezielt mit passenden Case Studies. Beispiel: Nach dem Download oder der Nutzung des ROI-Rechners werden relevante Erfolgsgeschichten (Case Studies) angezeigt oder verlinkt, um Vertrauen zu schaffen und die Nutzer zur Kontaktaufnahme (Action) zu führen. Ziel: Awareness → Trust → Action.
- **Hinweis:** Diese Aufgabe wurde bewusst übersprungen und ist aktuell nicht geplant.

### 3.3 A/B Testing (übersprungen)
- **Tool:** Google Optimize oder Microsoft Clarity
- **Aktion:** Teste verschiedene Hero-Varianten, CTAs, Preis-Darstellung.
- **Hinweis:** Diese Aufgabe wurde bewusst übersprungen und ist aktuell nicht geplant.

### 3.4 Interaktives Beratungs-Tool (Modellfinder) ✅ erledigt
- **Datei:** `pricing.html` (neuer Abschnitt)
- **Aktion:** Tool integriert, das Nutzern nach spezifischen Fragen eine Preismodell-Empfehlung gibt und passende Case Studies verlinkt.

---

## 🔄 4. Langfristig (3-6 Monate)

### 4.1 Video Content (übersprungen)
- **Datei:** `index.html`, `suite.html`
- **Aktion:** Binde Erklärvideos und Kundeninterviews ein.
- **Hinweis:** Diese Aufgabe wurde bewusst übersprungen und ist aktuell nicht geplant.

### 4.2 Partner-Portal ✅ erledigt
- **Datei:** `partners.html`
- **Aktion:** Angebote für IT-Dienstleister integriert: Flexible Manpower, Solution Architect Support, Schulung & Enablement – jeweils mit kurzer Erklärung und Kontaktmöglichkeit.

### 4.3 Mehrsprachigkeit
- **Datei:** Alle Hauptseiten
- **Aktion:** Implementiere englische Version, ggf. französisch.

---

## Umsetzungshinweise
- Jede Änderung sollte in Git dokumentiert werden.
- Nach jeder grösseren Änderung: Funktionstest auf Desktop und Mobile.
- Nach Abschluss jeder Phase: Review mit Stakeholdern.

---

**Hinweis:** Retainer-Preise immer als Stundenpreis und Monatswert (x4) angeben, damit die Kalkulation für Kunden transparent ist.
