// Javascript file for polls
function getDataFromRadioButtons() {
    let names = document.getElementsByName('poll');
    let usersChoice = null;
    for (let i = 0; i < names.length; i++) {
        if (names[i].checked) {
            window.alert("Thank you for voting for: " + names[i].value);
            usersChoice = names[i].value;
        }
    }
    let votes = parseInt(localStorage.getItem(usersChoice));
    votes = votes + 1;
    localStorage.setItem(usersChoice, votes.toString());
}

function initVotes() {
    let names = document.getElementsByName('poll');
    for (let i = 0; i < names.length; i++) {
        if (localStorage.getItem("Beast") === null ) {
            localStorage.setItem("Beast", "0");
        }
        if (localStorage.getItem("Charlie") === null ) {
            localStorage.setItem("Charlie", "0");
        }
        if (localStorage.getItem("Billy") === null ) {
            localStorage.setItem("Billy", "0");
        }
    }
    document.getElementById("numVotes1").textContent = localStorage.getItem("Beast");
    document.getElementById("numVotes2").textContent = localStorage.getItem("Charlie");
    document.getElementById("numVotes3").textContent = localStorage.getItem("Billy");
}