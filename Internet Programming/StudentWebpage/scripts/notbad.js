// Name: Wade Moulton
// Date: 09/15/2020
// Class: CS 4720
// Section: W01
// Instructor: Dr. Sarah North

const notBadInput = document.getElementById('not-bad-input');
const notBadSubmit = document.getElementById('not-bad-submit');
const notBadReset = document.getElementById('not-bad-reset');
const notBadTextBox = document.getElementById('not-bad-value');

notBadSubmit.addEventListener('click', () => {
    try {
        notBadTextBox.innerHTML = notBad(notBadInput.value);
    } catch (err) {
        notBadTextBox.innerHTML = `Looks like something went wrong! Try again!`;
    }
})

notBadReset.addEventListener('click', () => {
    notBadInput.value = "";
    notBadTextBox.innerHTML = "";
})

function notBad(text) {
    const notIndex = text.search('not');
    const badIndex = text.search('bad');
    if (-1 < notIndex && notIndex < badIndex) {
        return `${text.substring(0, notIndex)}good${text.substring(badIndex + 3)}`;
    }
    else {
        return text;
    }
}