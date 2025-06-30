-- Cargar archivo de eventos con campo de fecha ya incluido
datos_eventos = LOAD '/data/eventos_con_fecha/part-m-00000' 
    USING PigStorage(',') 
    AS (id:chararray, tipo:chararray, subtipo:chararray, 
        comuna:chararray, calle:chararray, lat:double, lon:double, 
        timestamp:long, fecha_iso:chararray, solo_dia:chararray);

-- Filtrar unicamente eventos de tipo ACCIDENTE
solo_accidentes = FILTER datos_eventos BY tipo == 'ACCIDENT';

-- Agrupar todos los accidentes para contar total
agrupado_total = GROUP solo_accidentes ALL;
cantidad_accidentes = FOREACH agrupado_total GENERATE COUNT(solo_accidentes);

-- Guardar el resultado como CSV
STORE cantidad_accidentes INTO '/data/total_accidentes' USING PigStorage(',');
