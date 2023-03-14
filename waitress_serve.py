from waitress import serve
import app

serve(app.create_app(), host='0.0.0.0', port=8080)