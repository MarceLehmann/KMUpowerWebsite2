// KMUpower Multi-Page Website JavaScript

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

    // Set active navigation link based on current page
    updateActiveNavigation();
}

// Update active navigation link
function updateActiveNavigation() {
    const navLinks = document.querySelectorAll('.navbar__link');
    const currentPage = getCurrentPage();
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href');
        
        if ((currentPage === 'index' && href === 'index.html') ||
            (currentPage === 'about' && href === 'about.html') ||
            (currentPage === 'suite' && href === 'suite.html') ||
            (currentPage === 'pricing' && href === 'pricing.html') ||
            (currentPage === 'partners' && href === 'partners.html') ||
            (currentPage === 'contact' && href === 'contact.html')) {
            link.classList.add('active');
        }
    });
}

// Newsletter popup functionality
function initNewsletterPopup() {
    const popup = document.getElementById('newsletter-popup');
    const closeButton = document.getElementById('newsletter-popup-close');
    const form = document.getElementById('newsletter-popup-form');
    
    if (!popup) return;

    let popupShown = false;
    let scrollTriggered = false;
    let timeTriggered = false;

    // Show popup after 30 seconds
    setTimeout(() => {
        if (!popupShown) {
            timeTriggered = true;
            showNewsletterPopup();
        }
    }, 30000);

    // Show popup when scrolled 50%
    window.addEventListener('scroll', debounce(() => {
        if (!popupShown && !scrollTriggered) {
            const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
            if (scrollPercent >= 50) {
                scrollTriggered = true;
                showNewsletterPopup();
            }
        }
    }, 100));

    function showNewsletterPopup() {
        if (popupShown) return;
        popupShown = true;
        popup.classList.add('active');
    }

    // Close popup
    if (closeButton) {
        closeButton.addEventListener('click', closeNewsletterPopup);
    }

    // Close popup when clicking outside
    popup.addEventListener('click', function(e) {
        if (e.target === popup) {
            closeNewsletterPopup();
        }
    });

    function closeNewsletterPopup() {
        popup.classList.remove('active');
    }

    // Handle newsletter popup form submission
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = form.querySelector('input[type="email"]').value;
            
            if (validateEmail(email)) {
                // Simulate newsletter signup
                showNotification('Vielen Dank! Sie haben sich erfolgreich für unseren Newsletter angemeldet.', 'success');
                form.reset();
                closeNewsletterPopup();
            } else {
                showNotification('Bitte geben Sie eine gültige E-Mail-Adresse ein.', 'error');
            }
        });
    }

    // Close popup with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && popup.classList.contains('active')) {
            closeNewsletterPopup();
        }
    });
}

// Form handling
function initForms() {
    // Newsletter form (in footer/section) - fix for both forms
    const newsletterForms = document.querySelectorAll('#newsletter-form, .newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const submitButton = this.querySelector('button[type="submit"]');
            const email = emailInput.value;
            
            if (validateEmail(email)) {
                // Show loading state
                const originalText = submitButton.textContent;
                submitButton.textContent = 'Wird angemeldet...';
                submitButton.disabled = true;
                
                // Simulate API call
                setTimeout(() => {
                    showNotification('Vielen Dank für Ihre Newsletter-Anmeldung! Sie erhalten in Kürze eine Bestätigungs-E-Mail.', 'success');
                    this.reset();
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;
                }, 1000);
            } else {
                showNotification('Bitte geben Sie eine gültige E-Mail-Adresse ein.', 'error');
            }
        });
    });

    // Contact form
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (validateContactForm(this)) {
                const submitButton = this.querySelector('button[type="submit"]');
                const originalText = submitButton.textContent;
                
                submitButton.textContent = 'Wird gesendet...';
                submitButton.disabled = true;

                // Simulate form submission
                setTimeout(() => {
                    showNotification('Nachricht erfolgreich gesendet! Wir melden uns innerhalb von 24 Stunden bei Ihnen.', 'success');
                    this.reset();
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;
                }, 1500);
            }
        });
    }
}

// Contact form validation
function validateContactForm(form) {
    const name = form.querySelector('#name');
    const email = form.querySelector('#email');
    const message = form.querySelector('#message');
    let isValid = true;

    // Clear previous errors
    clearFormErrors(form);

    // Validate name
    if (!name.value.trim()) {
        showFieldError(name, 'Name ist erforderlich');
        isValid = false;
    }

    // Validate email
    if (!email.value.trim()) {
        showFieldError(email, 'E-Mail ist erforderlich');
        isValid = false;
    } else if (!validateEmail(email.value)) {
        showFieldError(email, 'Bitte geben Sie eine gültige E-Mail-Adresse ein');
        isValid = false;
    }

    // Validate message
    if (!message.value.trim()) {
        showFieldError(message, 'Nachricht ist erforderlich');
        isValid = false;
    } else if (message.value.trim().length < 10) {
        showFieldError(message, 'Nachricht muss mindestens 10 Zeichen lang sein');
        isValid = false;
    }

    return isValid;
}

function clearFormErrors(form) {
    const inputs = form.querySelectorAll('.form-control');
    inputs.forEach(input => {
        input.classList.remove('error');
        const errorMsg = input.parentNode.querySelector('.error-message');
        if (errorMsg) errorMsg.remove();
    });
}

function showFieldError(field, message) {
    field.classList.add('error');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

// ROI Calculator functionality (for suite.html)
function initROICalculator() {
    const employeesSlider = document.getElementById('employees');
    const hourlyWageInput = document.getElementById('hourly-wage');
    const manualHoursSlider = document.getElementById('manual-hours');
    const efficiencySlider = document.getElementById('efficiency');

    if (!employeesSlider || !hourlyWageInput || !manualHoursSlider || !efficiencySlider) return;

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
        if (currentCostsDisplay) currentCostsDisplay.textContent = `CHF ${currentCosts.toLocaleString('de-CH')}`;
        if (savingsDisplay) savingsDisplay.textContent = `CHF ${Math.round(potentialSavings).toLocaleString('de-CH')}`;
        if (roiMonthsDisplay) roiMonthsDisplay.textContent = roiMonths > 24 ? '24+' : roiMonths;
        if (recommendedPackageDisplay) recommendedPackageDisplay.textContent = recommendedPackage;

        // Add visual feedback for good ROI
        if (roiMonthsDisplay) {
            const roiCard = roiMonthsDisplay.closest('.result-card');
            if (roiCard) {
                if (roiMonths <= 6) {
                    roiCard.style.borderColor = '#48e0d1';
                    roiCard.style.backgroundColor = 'rgba(72, 224, 209, 0.1)';
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

// Scroll animations using Intersection Observer
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
        .about__features .feature,
        .module-card,
        .roi-calculator__content,
        .pricing-card,
        .testimonial-card,
        .contact__content,
        .partner-benefit,
        .newsletter-signup__content
    `);

    animatedElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });

    // Stagger animation for grids
    const gridContainers = document.querySelectorAll('.modules-grid, .pricing-grid, .testimonials-grid, .partner-benefits-grid');
    gridContainers.forEach(container => {
        const items = container.children;
        Array.from(items).forEach((item, index) => {
            item.style.transitionDelay = `${index * 0.1}s`;
        });
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

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.innerHTML = `
        <div class="notification__content">
            <span class="notification__message">${message}</span>
            <button class="notification__close" onclick="this.parentElement.parentElement.remove()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                </svg>
            </button>
        </div>
    `;

    // Add styles if not already present
    if (!document.querySelector('#notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            .notification {
                position: fixed;
                top: 90px;
                right: 20px;
                z-index: 3000;
                max-width: 400px;
                border-radius: var(--radius-base, 8px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
                animation: slideInRight 0.3s ease-out;
            }
            
            .notification--success {
                background: rgba(72, 224, 209, 0.1);
                border: 1px solid #48e0d1;
                color: #48e0d1;
            }
            
            .notification--error {
                background: rgba(192, 21, 47, 0.1);
                border: 1px solid #c0152f;
                color: #c0152f;
            }
            
            .notification--info {
                background: rgba(98, 108, 113, 0.1);
                border: 1px solid #626c71;
                color: #626c71;
            }
            
            .notification__content {
                display: flex;
                align-items: flex-start;
                justify-content: space-between;
                padding: 16px;
                gap: 12px;
            }
            
            .notification__message {
                flex: 1;
                font-size: 14px;
                font-weight: 500;
                line-height: 1.4;
            }
            
            .notification__close {
                background: none;
                border: none;
                cursor: pointer;
                color: inherit;
                opacity: 0.7;
                transition: opacity 0.15s;
                flex-shrink: 0;
                padding: 2px;
                margin-top: -2px;
            }
            
            .notification__close:hover {
                opacity: 1;
            }
            
            @keyframes slideInRight {
                from {
                    opacity: 0;
                    transform: translateX(100%);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            
            @keyframes slideOutRight {
                from {
                    opacity: 1;
                    transform: translateX(0);
                }
                to {
                    opacity: 0;
                    transform: translateX(100%);
                }
            }
            
            @media (max-width: 480px) {
                .notification {
                    right: 10px;
                    left: 10px;
                    max-width: none;
                }
            }
        `;
        document.head.appendChild(style);
    }

    // Add to page
    document.body.appendChild(notification);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        }
    }, 5000);
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
    // Close mobile menu with Escape key
    if (e.key === 'Escape') {
        const navbarMenu = document.getElementById('navbar-menu');
        const navbarToggle = document.getElementById('navbar-toggle');
        
        if (navbarMenu && navbarToggle && navbarMenu.classList.contains('active')) {
            navbarMenu.classList.remove('active');
            const spans = navbarToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    }
});

// Initialize smooth scrolling for anchor links
document.querySelectorAll('a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Only handle internal anchor links (not external pages with anchors)
        if (href.includes('.html#')) {
            return; // Let the browser handle navigation to other pages
        }
        
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetId = href.substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Performance optimization: Preload critical pages
function preloadPages() {
    const criticalPages = ['about.html', 'suite.html', 'pricing.html', 'contact.html'];
    
    criticalPages.forEach(page => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = page;
        document.head.appendChild(link);
    });
}

// Initialize page preloading after initial load
window.addEventListener('load', () => {
    setTimeout(preloadPages, 2000);
});

// Add smooth scroll behavior
document.documentElement.style.scrollBehavior = 'smooth';