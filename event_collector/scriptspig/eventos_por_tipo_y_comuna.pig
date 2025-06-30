-- Cargar los datos
eventos = LOAD '/data/eventos_con_fecha/part-m-00000' 
        USING PigStorage(',') 
        AS (uuid:chararray, tipo:chararray, subtipo:chararray, ciudad:chararray, comuna:chararray,
            lat:double, lon:double, timestamp:long, fecha_iso:chararray, fecha_solo:chararray);

-- Filtrar solo si comuna y tipo no están vacíos (opcional)
limpios = FILTER eventos BY (comuna IS NOT NULL) AND (tipo IS NOT NULL);

-- Agrupar por tipo y comuna
agrupados = GROUP limpios BY (tipo, comuna);

-- Contar cuántos eventos por tipo y comuna
conteo = FOREACH agrupados GENERATE 
            FLATTEN(group) AS (tipo, comuna), 
            COUNT(limpios) AS cantidad;

-- Ordenar por cantidad descendente
ordenados = ORDER conteo BY cantidad DESC;

-- Guardar resultado
STORE ordenados INTO '/data/eventos_por_tipo_y_comuna' USING PigStorage(',');
