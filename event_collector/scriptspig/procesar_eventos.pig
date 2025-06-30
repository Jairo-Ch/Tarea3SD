-- Cargar los eventos crudos desde el CSV
eventos = LOAD '/data/eventos_crudo.csv' USING PigStorage(',') AS (
    uuid:chararray,
    tipo:chararray,
    subtipo:chararray,
    ciudad:chararray,
    calle:chararray,
    lat:double,
    lon:double,
    fecha:long
);

-- Filtrar eventos válidos (sin campos críticos vacíos)
eventos_filtrados = FILTER eventos BY 
    (uuid IS NOT NULL AND uuid != '') AND
    (tipo IS NOT NULL AND tipo != '') AND
    (ciudad IS NOT NULL AND ciudad != '') AND
    (lat IS NOT NULL) AND
    (lon IS NOT NULL);

-- Agrupar por comuna y tipo
agrupados = GROUP eventos_filtrados BY (ciudad, tipo);

-- Contar cuántos eventos por cada comuna/tipo
conteo = FOREACH agrupados GENERATE 
    group.ciudad AS comuna, 
    group.tipo AS tipo_incidente,
    COUNT(eventos_filtrados) AS total_eventos;

-- Guardar el resultado en archivo CSV
STORE conteo INTO '/data/resultados_agrupados' USING PigStorage(',');
