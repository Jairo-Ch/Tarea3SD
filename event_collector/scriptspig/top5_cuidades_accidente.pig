cat << 'EOF' > /data/top5_ciudades_accidente.pig
-- Cargar eventos con fecha
eventos = LOAD '/data/eventos_con_fecha/part-m-00000' USING PigStorage(',')
    AS (uuid:chararray, tipo:chararray, subtipo:chararray, ciudad:chararray,
        calle:chararray, lat:float, lon:float, timestamp:long,
        fecha_iso:chararray, fecha:chararray);

-- Filtrar accidentes
accidentes = FILTER eventos BY tipo == 'ACCIDENT';

-- Agrupar por ciudad
agrupados = GROUP accidentes BY ciudad;

-- Contar por ciudad
conteo = FOREACH agrupados GENERATE group AS ciudad, COUNT(accidentes) AS total;

-- Ordenar y limitar a top 5
ordenados = ORDER conteo BY total DESC;
top5 = LIMIT ordenados 5;

-- Guardar resultados
STORE top5 INTO '/data/top5_ciudades_accidente' USING PigStorage(',');
EOF
