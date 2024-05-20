// 勤怠ボタンクリック時処理
async function onClickAttendance() {
    let data = {};
    data["url"] = document.getElementById("url").value;
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
    last_timestamp = await pywebview.api.ieyasu_login(data);
    console.log(last_timestamp)

    await pywebview.api.ieyasu_attendance();
    // 打刻成功時にログイン情報を保持
    if (data["username"]) {
        localStorage.setItem('username', data["username"]);
        localStorage.setItem('password', data["password"]);
        localStorage.setItem('last_timestamp', last_timestamp);
        document.getElementById("last_timestamp").textContent = localStorage.getItem('last_timestamp')
    }
}

async function onClickLeaving() {
    let data = {};
    data["url"] = document.getElementById("url").value;
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
}