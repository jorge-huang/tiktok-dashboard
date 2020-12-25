function createTd(val) {
    const tdEl = document.createElement('td');
    tdEl.innerHTML = val;
    return tdEl;
}

function calcValueDelta(curr, prev) {
    curr = parseInt(curr);
    prev = parseInt(prev);
    let res = curr - prev;

    if (curr > prev) {
        return '+' + res;
    }

    return res;
}

function updateTable(data, prevFollowers, prevLikes) {
    const trEl = document.createElement('tr');
    trEl.appendChild(createTd(new Date().toLocaleString()))
    trEl.appendChild(createTd(data.followers))
    trEl.appendChild(createTd(calcValueDelta(data.followers, prevFollowers)))
    trEl.appendChild(createTd(data.likes))
    trEl.appendChild(createTd(calcValueDelta(data.likes, prevLikes)))
    $('#tracker tbody').prepend(trEl);

    if ($('tr').length > 10) {
        $('tr').last().remove();
    }
}

const socket = io();
let prevVals = [0, 0];
socket.emit('refresh_data');
socket.on('data', (data) => {
    if (!data) return;

    document.getElementById('followers').innerHTML = data.followers;
    document.getElementById('likes').innerHTML = data.likes;

    const currentVals = [data.followers, data.likes];
    const hasChange = currentVals.some((val, i) => {
        return (val - prevVals[i]) !== 0;
    });
    if (!hasChange) return;

    updateTable(data, prevVals[0], prevVals[1])
    prevVals = currentVals;
});

setInterval(() => {
    socket.emit('refresh_data');
}, 60 * 1000 / 4);


