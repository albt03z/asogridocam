document.addEventListener('DOMContentLoaded', function () {
    function scrollHeader() {
        const header = document.getElementById('navbar'); 
        if (window.scrollY >= 50) {
            header.classList.add('scroll-header');
        } else {
            header.classList.remove('scroll-header');
        }
    }
    window.addEventListener('scroll', scrollHeader);
});

// Inicializar AOS
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar AOS
    AOS.init;
    AOS.init({disable: 'mobile'});
        
    // Actualizar AOS cuando se carguen las imágenes
    window.addEventListener('load', function() {
        if (window.innerWidth >= 1000) {
            AOS.refresh();
        }
    });
});

// Función para manejar el scroll header y menú activo
function handleHeaderAndMenu() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    
    // Función para remover todas las clases active
    const removeAllActive = () => {
        navLinks.forEach(link => link.classList.remove('active'));
    };

    // Función para manejar el scroll
    window.addEventListener('scroll', () => {
        // Manejar el header con scroll
        if (window.scrollY >= 50) {
            navbar.classList.add('scroll-header');
        } else {
            navbar.classList.remove('scroll-header');
        }

        // Manejar el menú activo
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - navbar.offsetHeight - 20;
            const sectionHeight = section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        removeAllActive();
        const activeLink = document.querySelector(`.nav-link[href="#${current}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
    });

    // Manejar el clic en los links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            removeAllActive();
            link.classList.add('active');

            // Si estamos en móvil, cerrar el menú después del clic
            const offcanvas = document.querySelector('.offcanvas');
            if (offcanvas && window.innerWidth < 992) {
                const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvas);
                if (bsOffcanvas) bsOffcanvas.hide();
            }
        });
    });

    // Manejar el estado inicial
    document.addEventListener('DOMContentLoaded', () => {
        const hash = window.location.hash || '#home';
        const activeLink = document.querySelector(`.nav-link[href="${hash}"]`);
        if (activeLink) {
            removeAllActive();
            activeLink.classList.add('active');
        }

    // NICE SELECT PARA SELECT
    $('select').niceSelect();
    });
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', handleHeaderAndMenu);

