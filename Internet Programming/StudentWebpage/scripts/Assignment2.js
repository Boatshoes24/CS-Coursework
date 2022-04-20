// Name: Wade Moulton
// Date: 09/15/2020
// Class: CS 4720
// Section: W01
// Instructor: Dr. Sarah North

const addCellBtn = document.getElementById('add-cell-btn');
const removeCellBtn = document.getElementById('remove-cell-btn');
const sortCellBtn = document.getElementById('sort-cell-btn');
const cellContainer = document.getElementById('input-table');

const firstInputBox = document.getElementById('td-first-input');
const firstTDNum = document.getElementById('td-first-num');
const firstTDCount = document.getElementById('td-first-count');

let count = 2;

firstTDNum.innerText = 1;
firstTDCount.innerText = 0;

firstInputBox.addEventListener('input', () => {
    firstTDCount.innerText = firstInputBox.value.length;
})

addCellBtn.addEventListener('click', () => {
    let newRow = cellContainer.insertRow(-1);
    let td_1 = newRow.insertCell(0);
    let td_2 = newRow.insertCell(1);
    let td_3 = newRow.insertCell(2);
    td_1.innerText = count;
    count += 1;
    const inputBox = document.createElement('input');
    td_2.appendChild(inputBox);
    td_3.innerText = 0;
    inputBox.addEventListener('input', () => {
        td_3.innerText = inputBox.value.length;
    })
})

removeCellBtn.addEventListener('click', () => {
    if (cellContainer.rows.length > 2) {
        cellContainer.deleteRow(cellContainer.rows.length - 1);
        count -= 1;
    }
    else {
        alert('Cannot delete first table entry.');
    }

})

sortCellBtn.addEventListener('click', () => {
    let i, x, y, Switch;
    let switching = true;
    let rows = cellContainer.rows;

    while(switching) {
        switching = false;

        for (i = 1; i < (rows.length - 1); i++) {
            Switch = false;

            x = rows[i].getElementsByTagName('TD')[2];
            y = rows[i + 1].getElementsByTagName('TD')[2];
            
            if (parseInt(x.innerText) < parseInt(y.innerText)) {
                Switch = true;
                break;
            }
        }
        if (Switch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
    count = 1;
    for (i = 1; i < (rows.length); i++) {
        x = rows[i].getElementsByTagName('TD')[0];
        x.innerText = count;
        count += 1;
    }
})