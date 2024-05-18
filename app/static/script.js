document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.menu li');
    const panels = document.querySelectorAll('.tables .panel');

    panels.forEach(panel => {
        panel.style.display = 'none';
        document.querySelector('.tables .main').style.display = 'block';
    });

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const iconId = button.querySelector('i').getAttribute('class');
            let panelToShow = '';

            // Determine which panel to show based on the clicked button
            switch (iconId) {
                case 'fa-solid fa-user-group':
                    panelToShow = 'student';
                    break;
                case 'fa-solid fa-chalkboard-user':
                    panelToShow = 'instructor';
                    break;
                case 'fa-solid fa-clipboard-user':
                    panelToShow = 'coordinator';
                    break;
                case 'fa-solid fa-laptop':
                    panelToShow = 'program';
                    break;
                case 'fa-solid fa-school':
                    panelToShow = 'aiu';
                    break;
                case 'fa-solid fa-graduation-cap':
                    panelToShow = 'coursera';
                    break;
                case 'fa-solid fa-ticket':
                    panelToShow = 'licence';
                    break;
                default:
                    return;
            }

            // Hide all panels and then display the selected one
            panels.forEach(panel => {
                panel.style.display = 'none';
            });

            document.querySelector(`.tables .${panelToShow}`).style.display = 'block' ;
        });
    });
});




function animateNumber(element, target, duration) {
    let start = 0;
    const increment = target / duration;
    const interval = setInterval(() => {
        start += increment;
        element.textContent = Math.round(start);
        if (start >= target) {
            clearInterval(interval);
            element.textContent = target;
        }
    }, 3); 

}    
function initializeCountup() {
    const numbers = document.querySelectorAll('.countup');
    numbers.forEach(number => {
        const target = parseInt(number.textContent);
        animateNumber(number, target, 600); 
    });
}

window.addEventListener('load', initializeCountup);





