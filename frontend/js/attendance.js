// 勤怠ボタンクリック時処理
async function onClickAttendance() {
    let data = {};
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
    await pywebview.api.pyprint(data);
    // 打刻成功時にログイン情報を保持
    if (data["username"]) {
        localStorage.setItem('username', data["username"]);
        localStorage.setItem('password', data["password"]);
    }
}

async function onClickLeaving() {
    let data = {};
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
    await pywebview.api.pyprint(data);
}