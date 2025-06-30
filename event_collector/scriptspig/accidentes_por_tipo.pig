-- Cargar datos con formato ya transformado que incluye fecha legible
eventos_con_fecha = LOAD '/data/eventos_con_fecha/part-m-00000' 
    USING PigStorage(',') 
    AS (id:chararray, tipo:chararray, subtipo:chararray, ciudad:chararray, calle:chararray, 
        lat:double, lon:double, timestamp:long, fecha_iso:chararray, fecha:chararray);

-- Agrupar los eventos por subtipo
agrupados_por_subtipo = GROUP eventos_con_fecha BY subtipo;

-- Contar cuantos eventos hay de cada subtipo
conteo_eventos = FOREACH agrupados_por_subtipo 
    GENERATE group AS subtipo_evento, COUNT(eventos_con_fecha) AS total;

-- Guardar resultados en CSV
STORE conteo_eventos INTO '/data/eventos_por_tipo' USING PigStorage(',');