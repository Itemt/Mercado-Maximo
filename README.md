# 🛒 Sistema de Gestión de Ventas - Mercado Máximo

Un sistema completo de gestión de ventas desarrollado con Flask para la Universidad de Investigación y Desarrollo. Permite administrar clientes, productos, ventas y generar reportes detallados de manera eficiente.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API Endpoints](#-api-endpoints)
- [Base de Datos](#-base-de-datos)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Autor](#-autor)

## ✨ Características

### 🏪 Gestión de Productos
- ➕ Crear, editar y eliminar productos
- 📊 Control de inventario y stock
- 🏷️ Categorización de productos
- 💰 Gestión de precios
- 📈 Estadísticas de ventas por producto

### 👥 Gestión de Clientes
- 👤 Registro completo de clientes
- 📧 Información de contacto
- 🛍️ Historial de compras
- 📊 Estadísticas de compras por cliente
- 🔍 Búsqueda y filtrado

### 💳 Gestión de Ventas
- 🛒 Proceso de venta intuitivo
- 📋 Múltiples productos por venta
- 🔄 Estados de venta (Pendiente, Completada, Cancelada)
- 🧾 Generación de facturas
- 📱 Interfaz responsive

### 📊 Reportes y Análisis
- 📈 Dashboard con métricas principales
- 🏆 Top productos más vendidos
- ⭐ Mejores clientes
- 📋 Análisis de rendimiento
- 🖨️ Exportación e impresión de reportes

### 🎨 Interfaz de Usuario
- 🌟 Diseño moderno con Bootstrap 5
- 📱 Completamente responsive
- 🎯 Navegación intuitiva
- ⚡ Carga rápida y optimizada
- 🖨️ Estilos optimizados para impresión

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.13+** - Lenguaje de programación principal
- **Flask 3.1.2** - Framework web minimalista
- **Flask-SQLAlchemy 3.1.1** - ORM para base de datos
- **SQLite** - Base de datos ligera

### Frontend
- **HTML5** - Estructura de páginas
- **CSS3** - Estilos personalizados
- **JavaScript ES6+** - Interactividad del cliente
- **Bootstrap 5.1.3** - Framework CSS
- **Font Awesome 6.0.0** - Iconografía

### Herramientas de Desarrollo
- **Git** - Control de versiones
- **Virtual Environment** - Aislamiento de dependencias

## 📋 Requisitos del Sistema

- Python 3.13 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonación)
- Navegador web moderno

## 🚀 Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/PROYECTOCOMERCIALGESTIONVENTAS.git
cd PROYECTOCOMERCIALGESTIONVENTAS
```

### 2. Crear Entorno Virtual
```bash
# En Windows
python -m venv env
env\Scripts\activate

# En macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
```bash
python app.py
```
La base de datos SQLite se creará automáticamente en `instance/gestion_ventas.db`

### 5. Ejecutar la Aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📖 Uso

### Acceso al Sistema
1. Abrir navegador web
2. Navegar a `http://localhost:5000`
3. Utilizar la barra de navegación para acceder a las diferentes secciones

### Flujo de Trabajo Típico
1. **Registrar Productos**: Agregar productos al inventario
2. **Registrar Clientes**: Crear perfiles de clientes
3. **Crear Ventas**: Procesar nuevas ventas
4. **Generar Reportes**: Analizar el rendimiento

## 📁 Estructura del Proyecto

```
PROYECTOCOMERCIALGESTIONVENTAS/
│
├── 📁 env/                     # Entorno virtual
├── 📁 instance/                # Base de datos
│   └── gestion_ventas.db      # Base de datos SQLite
├── 📁 static/                  # Archivos estáticos
│   └── style.css              # Estilos CSS personalizados
├── 📁 templates/               # Plantillas HTML
│   ├── 📁 clientes/           # Templates de clientes
│   ├── 📁 productos/          # Templates de productos
│   ├── 📁 ventas/             # Templates de ventas
│   ├── 📁 reportes/           # Templates de reportes
│   ├── base.html              # Plantilla base
│   └── dashboard.html         # Dashboard principal
├── app.py                     # Aplicación principal
├── README.md                  # Este archivo
└── requirements.txt           # Dependencias del proyecto
```

## 🔌 API Endpoints

### Clientes
- `GET /` - Dashboard principal
- `GET /clientes` - Lista de clientes
- `GET /clientes/nuevo` - Formulario nuevo cliente
- `POST /clientes/nuevo` - Crear cliente
- `GET /clientes/<id>` - Ver cliente
- `GET /clientes/<id>/editar` - Formulario editar cliente
- `POST /clientes/<id>/editar` - Actualizar cliente
- `POST /clientes/<id>/eliminar` - Eliminar cliente

### Productos
- `GET /productos` - Lista de productos
- `GET /productos/nuevo` - Formulario nuevo producto
- `POST /productos/nuevo` - Crear producto
- `GET /productos/<id>` - Ver producto
- `GET /productos/<id>/editar` - Formulario editar producto
- `POST /productos/<id>/editar` - Actualizar producto
- `POST /productos/<id>/eliminar` - Eliminar producto

### Ventas
- `GET /ventas` - Lista de ventas
- `GET /ventas/nueva` - Formulario nueva venta
- `POST /ventas/nueva` - Crear venta
- `GET /ventas/<id>` - Ver venta
- `POST /ventas/<id>/estado` - Actualizar estado

### Reportes
- `GET /reportes` - Dashboard de reportes

## 🗄️ Base de Datos

### Modelo de Datos

#### Tabla: clientes
- `id` (INTEGER, PK) - Identificador único
- `nombre` (VARCHAR(100)) - Nombre del cliente
- `apellido` (VARCHAR(100)) - Apellido del cliente
- `email` (VARCHAR(120), UNIQUE) - Email único
- `telefono` (VARCHAR(20)) - Teléfono de contacto
- `direccion` (TEXT) - Dirección completa
- `fecha_registro` (DATETIME) - Fecha de registro

#### Tabla: productos
- `id` (INTEGER, PK) - Identificador único
- `nombre` (VARCHAR(200)) - Nombre del producto
- `descripcion` (TEXT) - Descripción detallada
- `precio` (DECIMAL(10,2)) - Precio unitario
- `stock` (INTEGER) - Cantidad en inventario
- `categoria` (VARCHAR(100)) - Categoría del producto
- `fecha_creacion` (DATETIME) - Fecha de creación

#### Tabla: ventas
- `id` (INTEGER, PK) - Identificador único
- `cliente_id` (INTEGER, FK) - Referencia al cliente
- `fecha_venta` (DATETIME) - Fecha y hora de venta
- `total` (DECIMAL(10,2)) - Total de la venta
- `estado` (VARCHAR(20)) - Estado (Pendiente/Completada/Cancelada)

#### Tabla: detalle_ventas
- `id` (INTEGER, PK) - Identificador único
- `venta_id` (INTEGER, FK) - Referencia a la venta
- `producto_id` (INTEGER, FK) - Referencia al producto
- `cantidad` (INTEGER) - Cantidad vendida
- `precio_unitario` (DECIMAL(10,2)) - Precio al momento de venta
- `subtotal` (DECIMAL(10,2)) - Subtotal del item

## 📸 Capturas de Pantalla

### Dashboard Principal
El dashboard muestra métricas clave y accesos rápidos a las funcionalidades principales.

### Gestión de Productos
Interfaz intuitiva para administrar el inventario con control de stock en tiempo real.

### Proceso de Ventas
Sistema de ventas paso a paso con cálculo automático de totales y validación de stock.

### Reportes Detallados
Análisis completo con gráficos y estadísticas de rendimiento del negocio.

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

### Guías de Contribución
- Seguir las convenciones de código existentes
- Agregar tests para nuevas funcionalidades
- Actualizar la documentación según sea necesario
- Usar mensajes de commit descriptivos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Cristian Ramos**
- Universidad de Investigación y Desarrollo
- Proyecto Académico - Sistema de Gestión de Ventas

---

## 🚀 Próximas Mejoras

- [ ] Autenticación de usuarios
- [ ] Exportación de reportes a PDF/Excel
- [ ] Sistema de notificaciones
- [ ] API REST completa
- [ ] Integración con sistemas de pago
- [ ] Módulo de facturación electrónica
- [ ] Dashboard con gráficos interactivos
- [ ] Sistema de backup automático

---

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**
