-- Cargar los eventos con fecha incluida
eventos = LOAD '/data/eventos_con_fecha/part-m-00000'
    USING PigStorage(',')
    AS (
        uuid: chararray,
        type: chararray,
        subtype: chararray,
        city: chararray,
        street: chararray,
        lat: double,
        lon: double,
        timestamp: long,
        datetime_iso: chararray,
        fecha: chararray
    );

-- Filtrar solo los eventos de tipo "ACCIDENT"
accidentes = FILTER eventos BY type == 'ACCIDENT';

-- Agrupar por fecha
agrupados = GROUP accidentes BY fecha;

-- Contar cuántos hay por cada fecha
conteo = FOREACH agrupados GENERATE group AS fecha, COUNT(accidentes) AS cantidad;

-- Ordenar por fecha (opcional)
ordenado = ORDER conteo BY fecha;

-- Guardar resultados
STORE ordenado INTO '/data/eventos_accidente_por_fecha' USING PigStorage(',');
