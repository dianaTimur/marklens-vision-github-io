/**
 * Marklens Vision - Main JavaScript File
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functions
    initSmoothScroll();
    initMobileMenu();
    initAnimations();
    initPackageHover();
    initPortfolioItems();
});

/**
 * Smooth scrolling for navigation links
 */
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                const mobileMenu = document.querySelector('.mobile-menu');
                if (mobileMenu && mobileMenu.classList.contains('active')) {
                    mobileMenu.classList.remove('active');
                }
            }
        });
    });
}

/**
 * Mobile menu toggle functionality
 */
function initMobileMenu() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileMenu = document.querySelector('nav ul');
    
    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
    }
    
    // Add mobile menu toggle button if it doesn't exist
    if (!mobileMenuToggle) {
        const header = document.querySelector('header .container');
        if (header) {
            const toggle = document.createElement('div');
            toggle.className = 'mobile-menu-toggle';
            toggle.innerHTML = '<i class="fas fa-bars"></i>';
            header.appendChild(toggle);
            
            // Re-initialize after adding the toggle button
            initMobileMenu();
        }
    }
    
    // Add responsive styles for mobile menu if not already in CSS
    if (!document.getElementById('mobile-menu-styles')) {
        const style = document.createElement('style');
        style.id = 'mobile-menu-styles';
        style.textContent = `
            @media (max-width: 768px) {
                .mobile-menu-toggle {
                    display: block;
                    position: absolute;
                    top: 20px;
                    left: 20px;
                    z-index: 1001;
                }
                
                nav ul {
                    display: none;
                    flex-direction: column;
                    position: fixed;
                    top: 0;
                    right: 0;
                    width: 70%;
                    height: 100vh;
                    background: var(--light-color);
                    box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
                    padding: 80px 20px 20px;
                    z-index: 1000;
                    transform: translateX(100%);
                    transition: transform 0.3s ease;
                }
                
                nav ul.active {
                    display: flex;
                    transform: translateX(0);
                }
                
                nav ul li {
                    margin: 10px 0;
                }
                
                .mobile-menu-toggle.active i:before {
                    content: "\\f00d";
                }
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Scroll animations for elements
 */
function initAnimations() {
    // Add animation class to elements when they come into view
    const animateElements = document.querySelectorAll('.service-card, .package-card, .testimonial-card, .portfolio-item');
    
    // Create observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fadeIn');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.2
    });
    
    // Observe elements
    animateElements.forEach(element => {
        observer.observe(element);
    });
    
    // Add animation delay to stagger animations
    animateElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 0.1}s`;
        element.style.opacity = '0';
    });
}

/**
 * Package card hover effects
 */
function initPackageHover() {
    const packageCards = document.querySelectorAll('.package-card');
    
    packageCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            packageCards.forEach(c => c.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Add hover styles if not already in CSS
    if (!document.getElementById('package-hover-styles')) {
        const style = document.createElement('style');
        style.id = 'package-hover-styles';
        style.textContent = `
            .package-card.active {
                transform: translateY(-15px) scale(1.03);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
                z-index: 1;
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Portfolio item interactions
 */
function initPortfolioItems() {
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    
    portfolioItems.forEach(item => {
        item.addEventListener('click', function() {
            // Create lightbox effect for portfolio items
            const img = this.querySelector('img');
            if (img) {
                const lightbox = document.createElement('div');
                lightbox.className = 'lightbox';
                lightbox.innerHTML = `
                    <div class="lightbox-content">
                        <span class="close">&times;</span>
                        <img src="${img.src}" alt="${img.alt}">
                    </div>
                `;
                document.body.appendChild(lightbox);
                
                // Prevent scrolling when lightbox is open
                document.body.style.overflow = 'hidden';
                
                // Close lightbox on click
                lightbox.addEventListener('click', function(e) {
                    if (e.target === lightbox || e.target.className === 'close') {
                        document.body.removeChild(lightbox);
                        document.body.style.overflow = '';
                    }
                });
            }
        });
    });
    
    // Add lightbox styles if not already in CSS
    if (!document.getElementById('lightbox-styles')) {
        const style = document.createElement('style');
        style.id = 'lightbox-styles';
        style.textContent = `
            .lightbox {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.9);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 2000;
            }
            
            .lightbox-content {
                position: relative;
                max-width: 90%;
                max-height: 90%;
            }
            
            .lightbox img {
                max-width: 100%;
                max-height: 90vh;
                object-fit: contain;
            }
            
            .lightbox .close {
                position: absolute;
                top: -40px;
                right: 0;
                color: white;
                font-size: 30px;
                cursor: pointer;
            }
        `;
        document.head.appendChild(style);
    }
}

/**
 * Scroll to top button
 */
function addScrollToTopButton() {
    // Create button element
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.className = 'scroll-top-btn';
    scrollTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(scrollTopBtn);
    
    // Add button styles
    const style = document.createElement('style');
    style.textContent = `
        .scroll-top-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--primary-gradient);
            color: white;
            border: none;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 999;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        
        .scroll-top-btn.visible {
            opacity: 1;
            visibility: visible;
        }
        
        .scroll-top-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }
    `;
    document.head.appendChild(style);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });
    
    // Scroll to top on click
    scrollTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Add scroll to top button
addScrollToTopButton();