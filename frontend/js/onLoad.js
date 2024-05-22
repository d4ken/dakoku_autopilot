// 画面読み込み時に入力情報を読み込み
window.addEventListener("load",async function() {
    if (localStorage.getItem('login_url')) {
        document.getElementById("url").value = localStorage.getItem('login_url')
    }
    if (localStorage.getItem('username')) {
        document.getElementById("username").value = localStorage.getItem('username')
    }
    if (localStorage.getItem('password')) {
        document.getElementById("password").value = localStorage.getItem('password')
        // document.getElementById('attendance_button').disabled = true;
    }
    if (localStorage.getItem('last_timestamp')) {
        document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
    }

})