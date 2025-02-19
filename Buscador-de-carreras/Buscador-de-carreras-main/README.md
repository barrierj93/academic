
# Degree Search Tool

## Descripción
Desarrollado para simplificar la consulta de notas de corte y facilitar el acceso a información universitaria.
**Degree Search Tool** es una herramienta diseñada para consultar las notas de corte de distintas carreras universitarias a partir de un archivo Excel o CSV. Es útil para buscar información específica sobre universidades y grados, mostrando los resultados de forma clara y estructurada.

El proyecto incluye **dos versiones**:
   &nbsp;

1. Una versión **gráfica** con interfaz amigable, ideal para usuarios no técnicos.
   https://github.com/barrierj93/Buscador-de-carreras/tree/main/v2_Interfaz-Gr%C3%A1fica

   &nbsp;

2. Una versión basada en **terminal**, más sencilla y rápida para quienes prefieren un enfoque minimalista.
   https://github.com/barrierj93/Buscador-de-carreras/tree/main/v1_Terminal 

---

## Características principales
- **Carga de archivo**: Compatible con archivos en formato `.xlsx` y `.csv`.
- **Búsqueda específica**: Permite buscar por el nombre exacto de la carrera.
- **Mensajes informativos**: Retroalimentación en caso de errores o búsquedas sin resultados.
- **Visualización estructurada**: Presenta los datos en formato tabla (en la terminal) o en un `TreeView` (en la interfaz gráfica).

---

## Requisitos
- **Python 3.11** o superior.
- Bibliotecas requeridas:
  - `pandas`
  - `tkinter` (para la versión gráfica)
  - `tabulate` (para la versión terminal).

---

## Instrucciones de uso

### **Versión 1: Interfaz gráfica (`career_search.py`)**

1. **Ejecución**: 
   - Puedes ejecutar el archivo `career_search.py` directamente desde la terminal o utilizar su versión compilada como ejecutable.
   - Si usas Python:
     ```bash
     python career_search.py
     ```
2. **Carga de archivo**: Haz clic en el botón **"Cargar Archivo"** y selecciona un archivo `.xlsx` o `.csv` con las columnas:
   - `Universidad`
   - `Grado`
   - `Corte Grupo 1`
   - `Corte Grupo 2`

3. **Búsqueda de carreras**:
   - Escribe el nombre o parte del nombre de la carrera en el campo de texto.
   - Selecciona una opción del menú desplegable que aparece automáticamente.
   - Haz clic en **"Buscar Carrera"** para visualizar los resultados.

4. **Resultados**: 
   - Se mostrarán las universidades, grados y notas de corte relacionadas en la tabla inferior.

---

### **Versión 2: Basada en terminal (`career_finder.py`)**

1. **Ejecución**: Ejecuta el archivo `career_finder.py` desde la terminal:
   ```bash
   python career_finder.py
   ```

2. **Carga de archivo**: 
   - El programa cargará automáticamente el archivo `notas_de_corte_2024-25_-_ordinaria.xlsx` ubicado en el mismo directorio.
   - Si no se encuentra, mostrará un mensaje de error.

3. **Búsqueda de carreras**:
   - Introduce el nombre exacto de la carrera cuando el programa lo solicite.
   - Ejemplo:
     ```
     Introduce el nombre completo de la carrera: Historia
     ```

4. **Resultados**:
   - El programa mostrará los resultados en un formato tabular estructurado.
   - Si la carrera no se encuentra, sugerirá verificar el nombre.

---

## Ejemplo de funcionamiento

### **Interfaz gráfica**:
- Al buscar "Historia", las opciones como "Historia del Arte" y "Historia - Filología Clásica" aparecen en el menú desplegable.
- Seleccionas una carrera y los resultados aparecen en una tabla en la parte inferior.

### **Terminal**:
- Ingresas "Historia" y el programa muestra los resultados:
  ```
  +-----------------------------------+------------------------+-----------------+-----------------+
  | Universidad                       | Grado                  | Corte Grupo 1   | Corte Grupo 2   |
  +===================================+========================+=================+=================+
  | UNIVERSIDAD COMPLUTENSE DE MADRID | Historia               | 5.0             | 5.0             |
  | UNIVERSIDAD AUTÓNOMA DE MADRID    | Historia               | 6.0             | 5.5             |
  +-----------------------------------+------------------------+-----------------+-----------------+
  ```

---

## Autor
@barrierj93

## Licencia
Uso personal o educativo.

---
