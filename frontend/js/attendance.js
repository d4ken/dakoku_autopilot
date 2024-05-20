let attendanceBtn;
let leavingBtn;

// 勤怠ボタンクリック時処理
const onClickAttendance = async (element) => {
    // ボタン連打防止処理
    attendanceBtn = document.getElementById("attendance-button");
    leavingBtn = document.getElementById("leaving-button");
    attendanceBtn.disabled = true;

    let data = {};
    data["url"] = document.getElementById("url").value;
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
    last_timestamp = await pywebview.api.ieyasu_login(data);
    await pywebview.api.ieyasu_attendance();
    // 打刻成功時にログイン情報を保持
    if (data["username"]) {
        localStorage.setItem('username', data["username"]);
        localStorage.setItem('password', data["password"]);
        localStorage.setItem('last_timestamp', last_timestamp);
        document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
        document.getElementById("dakokuResult").textContent = `出勤完了!!`
        leavingBtn.disabled = false;

    }
}

const onClickLeaving = async (element) => {
    // ボタン連打防止処理
    attendanceBtn = document.getElementById("attendance-button");
    leavingBtn = document.getElementById("leaving-button");
    leavingBtn.disabled = true;
    let data = {};
    data["url"] = document.getElementById("url").value;
    data["username"] = document.getElementById("username").value;
    data["password"] = document.getElementById("password").value;
    document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
    document.getElementById("dakokuResult").textContent = `お疲れさまでした!!!`
    attendanceBtn.disabled = false;
}
