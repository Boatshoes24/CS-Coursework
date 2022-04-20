// Name: Wade Moulton
// Date: 09/15/2020
// Class: CS 4720
// Section: W01
// Instructor: Dr. Sarah North

const fixSubmit = document.getElementById('fix-start-submit');
const fixInput = document.getElementById('fix-start-input');
const fixReset = document.getElementById('fix-start-reset');
const fixTextBox = document.getElementById('fix-start-value');

fixSubmit.addEventListener('click', () => {
    try {
        fixTextBox.innerHTML = `Your new string is: <strong>${fixStart(fixInput.value)}`;
    } catch(err) {
        fixTextBox.innerHTML = `Oops something went wrong! Try again!`;
    }
})

fixReset.addEventListener('click', () => {
    fixTextBox.innerHTML = "";
    fixInput.value = "";
})

function fixStart(text){
    const first = text[0];
    const end = text.substring(1).replaceAll(first.toUpperCase(), '*').replaceAll(first.toLowerCase(), '*');
    return `${first}${end}`;
}
