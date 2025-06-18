#!/usr/bin/env python3
"""
Servidor proxy simple para evitar problemas de CORS con Ultravox API
"""
import json
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import logging

# Configuración
ULTRAVOX_API_URL = "https://api.ultravox.ai/api/calls"
PORT = 8081

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProxyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Manejar preflight requests de CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-API-Key')
        self.send_header('Access-Control-Max-Age', '3600')
        self.end_headers()

    def do_GET(self):
        """Manejar peticiones GET con mensaje informativo"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        message = """
        <html>
        <head><title>Proxy Server Ultravox</title></head>
        <body>
        <h1>🚀 Servidor Proxy Ultravox</h1>
        <p>Este servidor proxy está funcionando correctamente.</p>
        <p><strong>Para usar la demo:</strong></p>
        <ol>
        <li>Ve a: <a href="http://localhost:8080">http://localhost:8080</a></li>
        <li>Haz clic en <code>index.html</code></li>
        <li>¡Disfruta la demo!</li>
        </ol>
        <p>El proxy manejará automáticamente las peticiones de la API.</p>
        </body>
        </html>
        """
        self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        """Proxy la petición a Ultravox API"""
        try:
            # Leer el body de la petición
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Obtener la API key del header
            api_key = self.headers.get('X-API-Key')
            if not api_key:
                logger.error("Missing X-API-Key header")
                self.send_error(400, "Missing X-API-Key header")
                return
            
            # Log de la petición
            logger.info(f"API Key: {api_key[:8]}...")
            logger.info(f"Request body: {post_data.decode('utf-8')}")
            
            # Hacer la petición a Ultravox
            headers = {
                'X-API-Key': api_key,
                'Content-Type': 'application/json'
            }
            
            logger.info(f"Proxying request to Ultravox API: {ULTRAVOX_API_URL}")
            
            response = requests.post(
                ULTRAVOX_API_URL,
                headers=headers,
                data=post_data,
                timeout=30
            )
            
            logger.info(f"Response status: {response.status_code}")
            logger.info(f"Response headers: {dict(response.headers)}")
            logger.info(f"Response body: {response.text}")
            
            # Enviar la respuesta de vuelta
            self.send_response(response.status_code)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            self.wfile.write(response.content)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": f"Request failed: {str(e)}"})
            self.wfile.write(error_response.encode('utf-8'))
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_response = json.dumps({"error": f"Server error: {str(e)}"})
            self.wfile.write(error_response.encode('utf-8'))

    def log_message(self, format, *args):
        """Sobrescribir para usar nuestro logger"""
        logger.info(format % args)

if __name__ == '__main__':
    server = HTTPServer(('localhost', PORT), ProxyHandler)
    logger.info(f"🚀 Servidor proxy iniciado en http://localhost:{PORT}")
    logger.info("🔧 Ahora cambia la URL en tu HTML a: http://localhost:8081")
    logger.info("⏹️  Presiona Ctrl+C para parar")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n👋 Servidor proxy detenido")
        server.shutdown() 