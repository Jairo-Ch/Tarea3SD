-- Cargar los eventos con su fecha
eventos = LOAD '/data/eventos_con_fecha/part-m-00000' 
    USING PigStorage(',') 
    AS (id:chararray, type:chararray, subtype:chararray, city:chararray, street:chararray, 
        lat:double, lon:double, timestamp:long, fecha_iso:chararray, fecha:chararray);

-- Agrupar por tipo de evento (subtype)
agrupados = GROUP eventos BY subtype;

-- Contar la cantidad de eventos por tipo
conteo = FOREACH agrupados GENERATE group AS tipo_evento, COUNT(eventos) AS cantidad;

-- Guardar los resultados
STORE conteo INTO '/data/eventos_por_tipo' USING PigStorage(',');
