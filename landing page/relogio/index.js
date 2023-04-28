const time = document.getElementById('time');
const nav = document.getElementById('nav');

const clock = () => {
    var date = new Date();
    let h = date.getHours();
    let m = date.getMinutes();
    let s = date.getSeconds();    
    let session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    time.innerHTML = `${h}:${m}:${s} ${session}`

    setTimeout(clock, 1000);
}

const dropdown = () => {
    nav.classList.toggle('drop')
}

clock();
