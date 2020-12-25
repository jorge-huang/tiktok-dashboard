function createTd(val) {
    const tdEl = document.createElement('td');
    tdEl.innerHTML = val;
    return tdEl;
}

function updateTable(data) {
    const trEl = document.createElement('tr');
    trEl.appendChild(createTd(new Date()))
    trEl.appendChild(createTd(data.followers))
    trEl.appendChild(createTd(data.likes))
    $('#tracker tbody').prepend(trEl);
}

const socket = io();
let prevVals = '';
socket.emit('refresh_data');
socket.on('data', (data) => {
    if (!data) return;

    document.getElementById('followers').innerHTML = data.followers;
    document.getElementById('likes').innerHTML = data.likes;

    const currentVals = data.followers + data.likes;
    if (currentVals === prevVals) return;

    updateTable(data)
    prevVals = currentVals;
});

setInterval(() => {
    socket.emit('refresh_data');
}, 60 * 1000 / 4);


