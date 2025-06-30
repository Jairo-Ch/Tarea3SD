-- Cargar los eventos con fecha ya convertida
eventos = LOAD '/data/eventos_con_fecha/part-m-00000' 
  USING PigStorage(',') 
  AS (
    uuid:chararray, 
    tipo:chararray, 
    subtipo:chararray, 
    comuna:chararray, 
    calle:chararray, 
    lat:double, 
    lon:double, 
    timestamp:long, 
    fecha_completa:chararray, 
    fecha:chararray
  );

-- Agrupar por fecha
agrupados = GROUP eventos BY fecha;

-- Contar eventos por fecha
conteo = FOREACH agrupados GENERATE 
  group AS fecha, 
  COUNT(eventos) AS total_eventos;

-- Ordenar por fecha ascendente (opcional)
ordenados = ORDER conteo BY fecha;

-- Guardar el resultado
STORE ordenados INTO '/data/eventos_por_fecha' 
  USING PigStorage(',');
