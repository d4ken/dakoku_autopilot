let dakokuBtn;
const dakokuStatus = Object.freeze({
    attend: 'attend',
    leave: 'leave',
    none: 'none'
})

// 打刻ボタンクリック時処理
const onClickDakoku = async () => {
    // ボタン連打防止処理
    dakokuBtn = document.getElementById('dakoku_button');
    dakokuBtn.disabled = true;
    // TODO: ローディング処理ほしい
    document.getElementById("dakoku_result").textContent = `Loading...`

    // ログイン処理
    let data = getFormData();
    let res = await pywebview.api.ieyasu_login(data);
    if (res) {
        // ログイン成功時
        document.getElementById("dakoku_result").textContent = `ログイン成功`
        localStorage.setItem('login_url', data["url"]);
        // 打刻状態判定
        let dakokuStatsBefore = dakokuStatus.none;
        dakokuStatsBefore = await pywebview.api.check_dakoku();
        // 退勤済みなら出勤処理
        if (dakokuStatsBefore === dakokuStatus.leave) {
            let res = await pywebview.api.ieyasu_attendance();
            localStorage.setItem('last_timestamp', res);

            await attendanceDakoku(data);
            // 出勤済みなら退勤処理
        } else if (dakokuStatsBefore === dakokuStatus.attend) {
            let res = await pywebview.api.ieyasu_leaving();
            localStorage.setItem('last_timestamp', res);
            await leavingDakoku(data);
            // 打刻状態の取得失敗時
        } else if (dakokuStatsBefore === dakokuStatus.none) {
            document.getElementById("dakoku_result").textContent = `[Error]: 打刻状態の取得に失敗しました。`
        }
    } else {
        document.getElementById("dakoku_result").textContent = `[Error]: ログイン処理に失敗しました。`
    }
}

const attendanceDakoku = async (data) => {
    // 打刻状態判定
    let dakokuStats = await pywebview.api.check_dakoku(true);
    if (dakokuStats === dakokuStatus.attend) {
        saveStorageUserInfo(data);
        document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
        document.getElementById("dakoku_result").textContent = `出勤完了!!`
    } else {
        document.getElementById("dakoku_result").textContent = `[Error]: 出勤打刻に失敗しました。`
    }
}

const leavingDakoku = async (data) => {
    // 打刻状態判定
    let dakokuStats = dakokuStatus.none;
    dakokuStats = await pywebview.api.check_dakoku(true);
    if (dakokuStats === dakokuStatus.none) {
        saveStorageUserInfo(data);
        document.getElementById("last_timestamp").textContent = `最終打刻日時: ${localStorage.getItem('last_timestamp')}`
        document.getElementById("dakoku_result").textContent = `お疲れさまでした!!!`
    } else {
        document.getElementById("dakoku_result").textContent = `[Error]: 退勤打刻に失敗しました。`
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