let attendanceBtn;
let leavingBtn;

const dakokuStatus = Object.freeze({
    attend: 'attend',
    leave: 'leave',
    none: 'none'
})

const attendanceDakoku = async () => {
    // ボタン連打防止処理
    attendanceBtn = document.getElementById("attendance_button");
    attendanceBtn.disabled = true;
    // TODO: ローディング処理ほしい
    document.getElementById("dakoku_result").textContent = `Loading...`
    // ログイン処理
    let data = getFormData();
    let res = await pywebview.api.ieyasu_login(data);

    if (res) {
        // ログイン成功時
        document.getElementById("dakoku_result").textContent = `ログイン成功`
        localStorage.setItem('login_url', data["url"]);
        let res = await pywebview.api.ieyasu_attendance();
        localStorage.setItem('last_timestamp', res);
        // 打刻状態判定
        let dakokuStats = await pywebview.api.check_leaving(true);
        if (dakokuStats) {
            saveStorageUserInfo(data);
            document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
            document.getElementById("dakoku_result").textContent = `出勤完了!!`
        } else {
            document.getElementById("dakoku_result").textContent = `[Error]: 出勤打刻に失敗しました。`
        }

    } else {
        document.getElementById("dakoku_result").textContent = `[Error]: ログイン処理に失敗しました。`
    }
}

const leavingDakoku = async () => {
    // ボタン連打防止処理
    leavingBtn = document.getElementById("leaving_button");
    leavingBtn.disabled = true;
    // TODO: ローディング処理ほしい
    document.getElementById("dakoku_result").textContent = `Loading...`

    // ログイン処理
    let data = getFormData();
    let res = await pywebview.api.ieyasu_login(data);

    if (res) {
        // ログイン成功時
        document.getElementById("dakoku_result").textContent = `ログイン成功`
        localStorage.setItem('login_url', data["url"]);
        let res = await pywebview.api.ieyasu_leaving();
        localStorage.setItem('last_timestamp', res);
        // 打刻状態判定
        let dakokuStats = dakokuStatus.none;
        // dakokuStats = await pywebview.api.check_leaving(true);
        if (dakokuStats === dakokuStatus.none) {
            saveStorageUserInfo(data);
            document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
            document.getElementById("dakoku_result").textContent = `お疲れさまでした!!!`
        } else {
            document.getElementById("dakoku_result").textContent = `[Error]: 退勤打刻に失敗しました。`
        }

    } else {
        document.getElementById("dakoku_result").textContent = `[Error]: ログイン処理に失敗しました。`
    }
}

// クライアントのフォーム入力値を取得
const getFormData = () => {
    let user_info = {};
    user_info["url"] = document.getElementById("url").value;
    user_info["username"] = document.getElementById("username").value;
    user_info["password"] = document.getElementById("password").value;
    return user_info;
}

const saveStorageUserInfo = (data) => {
    localStorage.setItem('username', data["username"]);
    localStorage.setItem('password', data["password"]);
}