# Demo Ultravox AI - Agente de Voz

Esta es una demo completa que te permite hablar con un agente de IA usando la tecnología Ultravox.AI. La aplicación funciona completamente en el navegador y te permite tener conversaciones de voz en tiempo real con un agente inteligente.

## 🚀 Características

- **Conversación por voz en tiempo real**: Habla directamente con el agente de IA
- **Interfaz moderna y fácil de usar**: Diseño responsive y atractivo
- **Configuración personalizable**: Ajusta las instrucciones del sistema y la voz
- **Transcripciones en vivo**: Ve lo que dices y lo que responde el agente
- **Múltiples voces disponibles**: Elige entre 5 voces diferentes
- **Persistencia de configuración**: Tus ajustes se guardan automáticamente

## 📋 Requisitos Previos

1. **API Key de Ultravox**: Necesitas registrarte en [Ultravox.AI](https://app.ultravox.ai) y obtener tu API key
2. **Navegador moderno**: Chrome, Firefox, Safari o Edge (con soporte para WebRTC)
3. **Micrófono**: Para poder hablar con el agente
4. **Conexión a internet**: Para conectar con los servicios de Ultravox

## 🛠️ Configuración

### Obtener tu API Key

1. Ve a [Ultravox Console](https://app.ultravox.ai)
2. Regístrate o inicia sesión
3. Ve a Settings (Configuración)
4. Genera una nueva API Key
5. Copia y guarda tu API key de forma segura

### Usar la Demo

1. Abre el archivo `index.html` en tu navegador
2. Ingresa tu API Key de Ultravox en el campo correspondiente
3. (Opcional) Personaliza las instrucciones del sistema para el agente
4. (Opcional) Selecciona una voz diferente
5. Haz clic en "🎤 Iniciar Llamada"
6. Permite el acceso al micrófono cuando el navegador lo solicite
7. ¡Empieza a hablar con el agente!

## 🎯 Instrucciones del Sistema

Las instrucciones del sistema definen cómo se comportará el agente. Puedes personalizarlas para diferentes casos de uso:

### Ejemplos de Instrucciones

**Asistente General:**
```
Eres un asistente de IA útil y amigable. Tu trabajo es ayudar a resolver dudas y proporcionar información útil. Responde en español y mantén un tono conversacional y profesional.
```

**Tutor de Matemáticas:**
```
Eres un tutor de matemáticas experto. Ayuda a los estudiantes a entender conceptos matemáticos explicando paso a paso. Usa ejemplos prácticos y sé paciente. Responde en español.
```

**Asistente de Cocina:**
```
Eres un chef experto que ayuda con recetas y técnicas de cocina. Proporciona instrucciones claras y consejos útiles. Sugiere sustituciones de ingredientes cuando sea necesario. Responde en español.
```

## 🔧 Personalización

### Voces Disponibles

- **Alloy**: Voz equilibrada y profesional
- **Echo**: Voz clara y directa
- **Onyx**: Voz profunda y autoritaria
- **Nova**: Voz amigable y energética
- **Shimmer**: Voz suave y cálida

### Estados de la Conversación

La aplicación muestra diferentes estados durante la conversación:

- **🎧 Escuchando**: El agente está esperando que hables
- **🤔 Procesando**: El agente está pensando en su respuesta
- **🔊 El agente está hablando**: El agente está respondiendo

## 🎮 Controles

- **Iniciar Llamada**: Comienza una nueva sesión con el agente
- **Terminar Llamada**: Finaliza la sesión actual
- **Escape**: Tecla rápida para terminar la llamada
- **Scroll en transcripciones**: Revisa el historial de la conversación

## 🔐 Seguridad

- Tu API key se almacena localmente en tu navegador
- No se envía información a servidores terceros (excepto Ultravox)
- Las conversaciones son procesadas por Ultravox y no se almacenan localmente
- Usa siempre HTTPS en producción

## 🐛 Solución de Problemas

### Errores Comunes

**"Por favor ingresa tu API key de Ultravox"**
- Verifica que hayas ingresado tu API key correctamente
- Asegúrate de que la API key sea válida y activa

**"Error al crear llamada: 401"**
- Tu API key es inválida o ha expirado
- Verifica tu API key en el dashboard de Ultravox

**"Error accessing mic"**
- Permite el acceso al micrófono en tu navegador
- Verifica que tu micrófono esté funcionando
- Prueba en una conexión HTTPS (requerida para micrófono)

**No escucho al agente**
- Verifica que tu volumen esté activado
- Revisa la configuración de audio de tu navegador
- Algunos navegadores requieren interacción del usuario antes de reproducir audio

### Depuración

1. Abre las herramientas de desarrollo (F12)
2. Ve a la consola para ver logs detallados
3. Verifica la pestaña Network para problemas de conexión
4. Revisa que WebRTC esté disponible en tu navegador

## 📱 Compatibilidad

### Navegadores Soportados
- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 14+
- ✅ Edge 80+

### Sistemas Operativos
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu, Fedora, etc.)
- ✅ Android 8+
- ✅ iOS 14+

## 🚀 Mejoras Futuras

- [ ] Soporte para múltiples idiomas
- [ ] Integración con herramientas externas
- [ ] Historial persistente de conversaciones
- [ ] Modo offline con modelos locales
- [ ] Análisis de sentimientos en tiempo real
- [ ] Integración con calendarios y tareas

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la [documentación oficial de Ultravox](https://docs.ultravox.ai)
2. Verifica que tu configuración sea correcta
3. Consulta los logs de la consola del navegador
4. Asegúrate de estar usando una versión compatible del navegador

## 📄 Licencia

Este proyecto es un ejemplo educativo. Ultravox.AI tiene sus propios términos de servicio que debes cumplir al usar su API.

---

¡Disfruta conversando con tu agente de IA! 🤖💬 