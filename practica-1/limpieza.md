# Práctica 1 · Limpieza de código

## Código original
```Smell	En el original	

Mysterious Name	d, proc, c, l, t, tot	
Magic Number	0.10, 0.20, 0.15
Long Function	proc hace todo
Global Data	Diccionario global d
Primitive Obsession	Claves "p", "s", "n"
Repeated Switches	if t == 1 / elif t == 2
Error Codes	Devuelve -1
Comments	# calcula, # isv```


## Versión refactorizada
```
En la versión limpia

inventario, realizar_pedido, cliente, lineas, tipo_descuento, total
Constantes TASA_ISV y PORCENTAJE_DESCUENTO
Funciones pequeñas: verificar, calcular, descontar, notificar
El inventario se pasa como parámetro
Clase Repuesto con campos con nombre
Un diccionario de porcentajes por tipo
Lanza la excepción StockInsuficiente
No hacen falta, porque los nombres ya explican