// JavaScript document to store all form functions and poll functions
function getDataFromWorkshop() {
    let isValid = true; //LAR: The convention is to use a question that can be answered yes/no (t/f)
                         //LAR: for boolean flags.
    let resetSession2 = false;
    let resetSession3 = false;
    let session1 = null,
        session2 = null,
        session3 = null;
    let i;
    let message = "";

    let workshopSesh1 = document.getElementsByName('session1');
    let workshopSesh2 = document.getElementsByName('session2');
    let workshopSesh3 = document.getElementsByName('session3');

    for (i = 0; i < workshopSesh1.length; i++) {
        if (workshopSesh1[i].checked) {
            session1 = workshopSesh1[i].value;
        }
    }
    for (i = 0; i < workshopSesh2.length; i++) {
        if (workshopSesh2[i].checked) {
            session2 = workshopSesh2[i].value;
        }
    }

    for (i = 0; i < workshopSesh3.length; i++) {
        if (workshopSesh3[i].checked) {
            session3 = workshopSesh3[i].value;
        }
    }

    //LAR: Check for the F and H combo
    if ((session3 === "workshop8" && session2 !== "workshop6") ||
        (session3 !== "workshop8" && session2 === "workshop6")) {
        isValid = false;
        message += "Can only select Advertisement/Promotion of videos if doing Video Enhancing.<br><br>";
        resetSession3 = true;
    }

    //LAR: Check for B and session 2 options
    if (session1 === "workshop2" && session2 !== null) {
        isValid = false;
        message += "Cannot select a second session if doing Thumbnail Design.<br><br>";
        resetSession2 = true;
    }
    if (!isValid) {
        openWin(message);
        if (resetSession2) {
            for (i = 0; i < workshopSesh2.length; i++) {
                if (workshopSesh2[i].checked) {
                    workshopSesh2[i].checked = false;
                }
            }
        }
        if (resetSession3) {
            for (i = 0; i < workshopSesh3.length; i++) {
                if (workshopSesh3[i].checked) {
                    workshopSesh3[i].checked = false;
                }
            }
        }
    }
    return isValid;
}

function openWin(message) {

    let desiredWidth = 500;
    let desiredHeight = 400;
    let left = window.screenX;
    let top = window.screenY;
    let width = window.outerWidth;
    let height = window.outerHeight;
    let positionLeft = left + (width / 2 - desiredWidth / 2);
    let positionTop = top + (height / 2 - desiredHeight / 2);

    let myWindow = window.open("", "MsgWindow", 'resizable=yes, width=' + desiredWidth + ', height=' + desiredHeight + ', top=' + positionTop + ', left=' + positionLeft);

    myWindow.document.write(message);
    myWindow.document.body.style.backgroundColor = "lightpink";
}
function validateData() {
    if (getDataFromWorkshop()) {
        let i;
        let workshopSesh1 = document.getElementsByName('session1');
        let workshopSesh2 = document.getElementsByName('session2');
        let workshopSesh3 = document.getElementsByName('session3');
        let currCookie = makeCookieString("title", document.getElementById('selecttitle').value);

        currCookie += makeCookieString("firstname", document.getElementById('firstname').value);
        currCookie += makeCookieString("lastname", document.getElementById('lastname').value);
        currCookie += makeCookieString("address1", document.getElementById('address1').value);
        currCookie += makeCookieString("address2", document.getElementById('address2').value);
        currCookie += makeCookieString("city", document.getElementById('city').value);
        currCookie += makeCookieString("state", document.getElementById('selectstate').value);
        currCookie += makeCookieString("zip", document.getElementById('zip').value);
        currCookie += makeCookieString("phonenumber", document.getElementById('phone').value);
        currCookie += makeCookieString("email", document.getElementById('email').value);
        currCookie += makeCookieString("position", document.getElementById('position').value);
        currCookie += makeCookieString("company", document.getElementById('company').value);

        for (i = 0; i < workshopSesh1.length; i++) {
            if (workshopSesh1[i].checked) {
                currCookie += makeCookieString("session1", workshopSesh1[i].value);
            }
        }
        for (i = 0; i < workshopSesh2.length; i++) {
            if (workshopSesh2[i].checked) {
                currCookie += makeCookieString("session2", workshopSesh2[i].value);
            }
        }
        for (i = 0; i < workshopSesh3.length; i++) {
            if (workshopSesh3[i].checked) {
                currCookie += makeCookieString("session3", workshopSesh3[i].value);
            }
        }

        makeCookie(document.getElementById('conferenceid').value, currCookie);
        return true;
    } else {
        openWin("Error creating cookie <br><br>");
        return false;
    }
}

function makeCookie(key, value) {
    document.cookie += key + "=" + value + ";";
}

function makeCookieString(key, value) {
    return key + "~" + value + "|";
}

function parseCookie (cookieString, key) {
    let cookiesArray = cookieString.split(";");

    let val = null;

    for (let i = 0; i < cookiesArray.length; i++) {
        let keyValuePairArray = cookiesArray[i].split("=");

        if (keyValuePairArray[0].trim() === key) {
            val = keyValuePairArray[1];
        }
    }
    return val;
}

function populateForm() {
    let key = document.getElementById('conferenceid');
    // key = 123456

    if (key.length === 6) {
        let allCookies = document.cookie;
        // allCookies = 123456=firstname~Laura|lastname~Churchill;

        let valueString = parseCookie(allCookies, key);
        // firstname~Laura|lastname~Churchill

        if (valueString !== null) {
            let kvps = valueString.split("|");
            // yields array
            // 0: firstname~Laura
            // 1: lastname~Rey

            for (let i = 0; i < kvps.length; i++) {
                let kv = kvps[i].split("~");

                document.getElementById(kv[0]).value = kv[1];
            }
        }
    }


}


let idElem = document.getElementById('conferenceid');

// Set up listener for event and connect to the element.
idElem.addEventListener('blur', populateForm, false);


