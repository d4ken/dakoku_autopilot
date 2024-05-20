import webview
from backend.api.ieyasu_automation import Api

api = Api()
window = webview.create_window("勤怠打刻オペレーター", url="frontend/index.html", js_api=api)
webview.start(http_server=True, debug=True, private_mode=False, http_port=13377)
