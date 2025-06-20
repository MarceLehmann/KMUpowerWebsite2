# Erstelle das JavaScript mit Newsletter-Pop-up und ROI-Rechner

javascript_content = """// KMUpower Multi-Page Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavigation();
    initNewsletterPopup();
    initForms();
    initScrollAnimations();
    initScrollEffects();
    
    // Page-specific initializations
    const currentPage = getCurrentPage();
    if (currentPage === 'suite') {
        initROICalculator();
    }
});

// Get current page based on URL
function getCurrentPage() {
    const path = window.location.pathname;
    if (path.includes('about.html')) return 'about';
    if (path.includes('suite.html')) return 'suite';
    if (path.includes('pricing.html')) return 'pricing';
    if (path.includes('partners.html')) return 'partners';
    if (path.includes('contact.html')) return 'contact';
    return 'index';
}

// Navigation functionality
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const navbarToggle = document.getElementById('navbar-toggle');
    const navbarMenu = document.getElementById('navbar-menu');
    const navLinks = document.querySelectorAll('.navbar__link');

    if (!navbar || !navbarToggle || !navbarMenu) return;

    // Mobile menu toggle
    navbarToggle.addEventListener('click', function() {
        navbarMenu.classList.toggle('active');
        
        // Animate hamburger menu
        const spans = navbarToggle.querySelectorAll('span');
        if (navbarMenu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    // Close mobile menu when clicking on links
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navbarMenu.classList.remove('active');
            const spans = navbarToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        });
    });
}

// Newsletter popup functionality
function initNewsletterPopup() {
    const popup = document.getElementById('newsletter-popup');
    const closeBtn = document.getElementById('popup-close');
    const popupForm = document.getElementById('popup-newsletter-form');
    
    if (!popup) return;

    let popupShown = false;
    let scrollThreshold = false;

    // Show popup after 30 seconds
    setTimeout(() => {
        if (!popupShown) {
            showNewsletterPopup();
        }
    }, 30000);

    // Show popup when user scrolls to 50%
    window.addEventListener('scroll', () => {
        if (!scrollThreshold && !popupShown) {
            const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            if (scrollPercent > 50) {
                scrollThreshold = true;
                setTimeout(() => {
                    if (!popupShown) {
                        showNewsletterPopup();
                    }
                }, 2000);
            }
        }
    });

    function showNewsletterPopup() {
        if (localStorage.getItem('newsletter-popup-shown')) {
            return; // Don't show if already shown in this session
        }
        
        popup.classList.add('show');
        popupShown = true;
        localStorage.setItem('newsletter-popup-shown', 'true');
    }

    // Close popup
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            popup.classList.remove('show');
        });
    }

    // Close popup when clicking outside
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            popup.classList.remove('show');
        }
    });

    // Handle popup form submission
    if (popupForm) {
        popupForm.addEventListener('submit', handleNewsletterSubmission);
    }
}

// Newsletter form handling
function handleNewsletterSubmission(e) {
    e.preventDefault();
    
    const form = e.target;
    const email = form.querySelector('input[type="email"]').value;
    
    if (!email || !isValidEmail(email)) {
        alert('Bitte geben Sie eine gültige E-Mail-Adresse ein.');
        return;
    }

    // Simulate newsletter signup
    const submitButton = form.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    
    submitButton.textContent = 'Wird angemeldet...';
    submitButton.disabled = true;

    setTimeout(() => {
        alert('Vielen Dank für Ihre Newsletter-Anmeldung! Sie erhalten in Kürze eine Bestätigungs-E-Mail.');
        form.reset();
        submitButton.textContent = originalText;
        submitButton.disabled = false;
        
        // Close popup if it's the popup form
        const popup = document.getElementById('newsletter-popup');
        if (popup && popup.classList.contains('show')) {
            popup.classList.remove('show');
        }
    }, 1500);
}

// ROI Calculator functionality
function initROICalculator() {
    const employeesSlider = document.getElementById('employees');
    const hourlyWageInput = document.getElementById('hourly-wage');
    const manualHoursSlider = document.getElementById('manual-hours');
    const efficiencySlider = document.getElementById('efficiency');

    if (!employeesSlider || !hourlyWageInput || !manualHoursSlider || !efficiencySlider) {
        return; // ROI calculator elements not found
    }

    const employeesValue = document.getElementById('employees-value');
    const manualHoursValue = document.getElementById('manual-hours-value');
    const efficiencyValue = document.getElementById('efficiency-value');

    const currentCostsDisplay = document.getElementById('current-costs');
    const savingsDisplay = document.getElementById('savings');
    const roiMonthsDisplay = document.getElementById('roi-months');
    const recommendedPackageDisplay = document.getElementById('recommended-package');

    // Update slider values
    employeesSlider.addEventListener('input', function() {
        employeesValue.textContent = this.value;
        calculateROI();
    });

    manualHoursSlider.addEventListener('input', function() {
        manualHoursValue.textContent = this.value;
        calculateROI();
    });

    efficiencySlider.addEventListener('input', function() {
        efficiencyValue.textContent = this.value;
        calculateROI();
    });

    hourlyWageInput.addEventListener('input', calculateROI);

    function calculateROI() {
        const employees = parseInt(employeesSlider.value);
        const hourlyWage = parseFloat(hourlyWageInput.value);
        const manualHoursPerWeek = parseInt(manualHoursSlider.value);
        const efficiencyGain = parseInt(efficiencySlider.value) / 100;

        // Calculate current annual costs
        const weeklyManualCosts = manualHoursPerWeek * hourlyWage;
        const annualManualCosts = weeklyManualCosts * 52;
        const currentCosts = annualManualCosts * employees;

        // Calculate potential savings
        const potentialSavings = currentCosts * efficiencyGain;

        // Calculate ROI months based on package recommendation
        let recommendedPackage = '';
        let packageCost = 0;

        if (employees <= 10) {
            recommendedPackage = 'Einzelmodul';
            packageCost = 1000;
        } else if (employees <= 25) {
            recommendedPackage = 'Kernpaket';
            packageCost = 2222;
        } else {
            recommendedPackage = 'Komplett';
            packageCost = 7500;
        }

        const monthlySavings = potentialSavings / 12;
        const roiMonths = Math.ceil(packageCost / monthlySavings);

        // Update displays
        if (currentCostsDisplay) currentCostsDisplay.textContent = `CHF ${Math.round(currentCosts).toLocaleString('de-CH')}`;
        if (savingsDisplay) savingsDisplay.textContent = `CHF ${Math.round(potentialSavings).toLocaleString('de-CH')}`;
        if (roiMonthsDisplay) roiMonthsDisplay.textContent = roiMonths > 24 ? '24+' : roiMonths;
        if (recommendedPackageDisplay) recommendedPackageDisplay.textContent = recommendedPackage;

        // Add visual feedback for good ROI
        if (roiMonthsDisplay) {
            const roiCard = roiMonthsDisplay.closest('.result-card');
            if (roiCard) {
                if (roiMonths <= 6) {
                    roiCard.style.borderColor = '#28a745';
                    roiCard.style.backgroundColor = 'rgba(40, 167, 69, 0.1)';
                } else if (roiMonths <= 12) {
                    roiCard.style.borderColor = '#ffc107';
                    roiCard.style.backgroundColor = 'rgba(255, 193, 7, 0.1)';
                } else {
                    roiCard.style.borderColor = '';
                    roiCard.style.backgroundColor = '';
                }
            }
        }
    }

    // Initial calculation
    calculateROI();
}

// Form handling
function initForms() {
    // Newsletter forms
    const newsletterForms = document.querySelectorAll('.newsletter-form, #popup-newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', handleNewsletterSubmission);
    });

    // Contact form
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactFormSubmission);
    }
}

function handleContactFormSubmission(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    
    // Basic validation
    if (!data.company || !data.name || !data.email) {
        alert('Bitte füllen Sie alle Pflichtfelder (*) aus.');
        return;
    }
    
    if (!isValidEmail(data.email)) {
        alert('Bitte geben Sie eine gültige E-Mail-Adresse ein.');
        return;
    }

    // Simulate form submission
    const submitButton = form.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    
    submitButton.textContent = 'Wird gesendet...';
    submitButton.disabled = true;

    setTimeout(() => {
        alert('Vielen Dank für Ihre Anfrage! Wir melden uns innerhalb von 24 Stunden bei Ihnen.');
        form.reset();
        submitButton.textContent = originalText;
        submitButton.disabled = false;
    }, 1500);
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Add fade-in class to elements that should animate
    const animatedElements = document.querySelectorAll(`
        .hero__content,
        .trusted-companies,
        .card,
        .pricing-card,
        .result-card
    `);

    animatedElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// Scroll effects for navbar
function initScrollEffects() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add scrolled class for styling
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
}

// Utility functions
function isValidEmail(email) {
    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
    return emailRegex.test(email);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Handle window resize events
window.addEventListener('resize', debounce(function() {
    // Close mobile menu on resize to larger screen
    if (window.innerWidth > 768) {
        const navbarMenu = document.getElementById('navbar-menu');
        const navbarToggle = document.getElementById('navbar-toggle');
        
        if (navbarMenu && navbarToggle) {
            navbarMenu.classList.remove('active');
            const spans = navbarToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    }
}, 250));

// Add keyboard navigation support
document.addEventListener('keydown', function(e) {
    // Close mobile menu and popup with Escape key
    if (e.key === 'Escape') {
        const navbarMenu = document.getElementById('navbar-menu');
        const navbarToggle = document.getElementById('navbar-toggle');
        const popup = document.getElementById('newsletter-popup');
        
        if (navbarMenu && navbarMenu.classList.contains('active')) {
            navbarMenu.classList.remove('active');
            const spans = navbarToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
        
        if (popup && popup.classList.contains('show')) {
            popup.classList.remove('show');
        }
    }
});

// Clear newsletter popup flag when page is refreshed
window.addEventListener('beforeunload', function() {
    localStorage.removeItem('newsletter-popup-shown');
});
"""

# Speichere app.js
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(javascript_content)

print("✅ app.js erstellt")
print("Features: Newsletter-Pop-up (30s + 50% Scroll), ROI-Rechner, Mobile Navigation, Formular-Handling")