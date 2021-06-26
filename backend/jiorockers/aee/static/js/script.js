function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

    var Nightly = new Nightly();
    //onstart condition
    const dark_switch = document.getElementById('flexSwitchCheckChecked')
    if (getCookie('dark')=='true'){
        dark_switch.checked = true
    }
    else{
        dark_switch.checked = false
    }
    alert_me()

    function alert_me(){
        const ele = document.getElementById('flexSwitchCheckChecked');
        if (ele.checked){
                Nightly.darkify();
                //console.log('dark mode')
                setCookie('dark',true,10);
            }
        else{
                Nightly.lightify();
               //console.log('light mode')
                setCookie('dark',false,10);
        }
    }

let title_name = document.getElementById('title-name');
title_name['href'] = window.location.origin;

const searchButton = document.getElementById('search-button');
        const searchInput = document.getElementById('search-input');
        searchButton.addEventListener('click', () => {
            const inputValue = searchInput.value;
            window.location.replace('/search?q=' + inputValue);
        });

