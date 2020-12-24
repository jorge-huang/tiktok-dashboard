const socket = io();
socket.emit('refresh_data');
socket.on('data', (data) => {
    document.getElementById('followers').innerHTML = data.followers;
    document.getElementById('likes').innerHTML = data.likes;
    timestamp = Date.now();
    console.log(timestamp, data);
});

setInterval(() => {
    socket.emit('refresh_data');
}, 30 * 1000);