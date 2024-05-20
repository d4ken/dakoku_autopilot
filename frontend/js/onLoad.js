// 画面読み込み時に入力情報を読み込み
window.onload = function () {
    if (localStorage.getItem('username'))
        document.getElementById("username").value = localStorage.getItem('username')
    if (localStorage.getItem('password'))
        document.getElementById("password").value = localStorage.getItem('password')
}