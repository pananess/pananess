
# CSV to QIF Converter

Este proyecto es un simple convertidor de archivos CSV a QIF, escrito en Python. Está diseñado para tomar un archivo CSV con columnas específicas y convertirlo en un archivo QIF que puede ser importado en software financiero como Quicken.

## Requisitos

- Python 3.x

## Estructura del CSV

El archivo CSV debe tener el siguiente formato:

| Date       | Payee   | Memo    | Category  | Amount |
|------------|---------|---------|-----------|--------|
| 8/15/2024  | Example | Example | Example   | -121   |
| 8/16/2024  | Example | Example | Example   | 140.14 |

- **Date**: La fecha de la transacción en formato `MM/DD/YYYY`.
- **Payee**: El beneficiario o pagador de la transacción.
- **Memo**: Nota opcional sobre la transacción.
- **Category**: La categoría de la transacción.
- **Amount**: El monto de la transacción, donde los valores negativos representan egresos y los valores positivos ingresos.

## Cómo Usar

1. **Clonar el repositorio o descargar el script**:
   - Guarda el script como `convert_csv_to_qif.py`.

2. **Coloca el archivo CSV en el mismo directorio que el script** o ajusta la ruta en el código.

3. **Ejecuta el script**:

   ```bash
   python convert_csv_to_qif.py
   ```

4. **Modificar el código**:
   - Si tu archivo CSV tiene un nombre diferente, actualiza la variable `csv_file` en el script:
   
     ```python
     csv_file = 'nombre_de_tu_archivo.csv'
     ```

   - Puedes cambiar el nombre de salida del archivo QIF modificando la variable `qif_file`:

     ```python
     qif_file = 'nombre_de_salida.qif'
     ```

5. **Verifica el archivo QIF generado**:
   - El archivo QIF se guardará en la misma carpeta donde está el script, a menos que especifiques otra ruta.

## Formato del Archivo QIF

El archivo QIF generado tendrá el siguiente formato para cada transacción:

```
D[fecha]
P[beneficiario]
M[memo]
L[categoría]
T[monto]
^
```

- `D`: Fecha de la transacción.
- `P`: Beneficiario o pagador.
- `M`: Memo o nota (opcional).
- `L`: Categoría.
- `T`: Monto de la transacción.
- `^`: Marca el final de la transacción.

## Ejemplo

Si tienes un archivo `transactions.csv` con el siguiente contenido:

```csv
Date,Payee,Memo,Category,Amount
8/15/2024,Coffee Shop,Coffee,Food & Dining,-3.50
8/16/2024,Salary,August Salary,Income,2000.00
```

El script generará un archivo `transactions.qif` con el siguiente contenido:

```
!Type:Bank
D08/15/2024
PCoffee Shop
MCoffee
LFood & Dining
T-3.50
^
D08/16/2024
PSalary
MAugust Salary
LIncome
T2000.00
^
```

## Notas

- Asegúrate de que los datos en el archivo CSV estén en el formato correcto para evitar errores en la conversión.
- El script está configurado para manejar transacciones bancarias (`!Type:Bank`). Si necesitas otro tipo de cuenta, puedes modificar esta línea en el script.

## Licencia

Este proyecto es de uso libre y puede ser modificado según tus necesidades.
