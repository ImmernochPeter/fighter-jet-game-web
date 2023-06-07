function wertDesSlidersInElementSchreiben(elementId, sliderId) {
    const element = document.getElementById(elementId);
    const slider = document.getElementById(sliderId);

    if (element && slider) {
        slider.addEventListener('input', function () {
            element.textContent = slider.value;
        });
    } else {
        console.error('Element nicht gefunden');
    }
}