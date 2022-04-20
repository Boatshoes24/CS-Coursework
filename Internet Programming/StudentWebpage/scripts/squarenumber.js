// Name: Wade Moulton
// Date: 09/15/2020
// Class: CS 4720
// Section: W01
// Instructor: Dr. Sarah North

const squareSubmit = document.getElementById('square-number-submit-btn');
const squareReset = document.getElementById('square-number-reset-btn');
const squareInput = document.getElementById('square-number-input');
const squareTextBox = document.getElementById('square-number-value');

squareSubmit.addEventListener('click', () => {
    try {
        const flag = Number.isInteger(parseInt(squareInput.value));
        if (flag) {
            squareTextBox.innerHTML = `The result of squaring <strong>${squareInput.value}</strong> is ${squareNumber(squareInput.value)}!`;
        }
        else{ 
            throw new Error();
        }    
    } catch(err) {
        squareTextBox.innerHTML = `Could not square <span class="error">${squareInput.value}</span>. Please make sure to input a number and try again.`
    }
})

squareReset.addEventListener('click', () => {
    squareTextBox.innerHTML = "";
    squareInput.value = "";
})

function squareNumber(num) {
    return Math.pow(num, 2);
}