function typeEffect(element, speed) {
    const text = element.innerHTML;
    element.innerHTML = "";
    let i = 0;
    let timer = setInterval(() => {
        element.innerHTML += text.charAt(i);
        i++;
        if (i > text.length) clearInterval(timer);
    }, speed);
}

window.onload = function() {
    const elems = document.querySelectorAll('.typing');
    elems.forEach(e => typeEffect(e, 50));
};
