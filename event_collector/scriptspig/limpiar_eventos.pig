-- 1. Cargar datos crudos
eventos = LOAD '/data/eventos.csv'
    USING PigStorage(',')
    AS (uuid:chararray, tipo:chararray, subtipo:chararray, ciudad:chararray, calle:chararray, lat:float, lon:float, fecha:long);

-- 2. Eliminar encabezado (el registro donde uuid = "uuid")
eventos_sin_encabezado = FILTER eventos BY uuid != 'uuid';

-- 3. Filtrar registros con datos faltantes
eventos_limpios = FILTER eventos_sin_encabezado BY 
    tipo IS NOT NULL AND tipo != '' AND
    subtipo IS NOT NULL AND subtipo != '' AND
    ciudad IS NOT NULL AND ciudad != '' AND
    lat IS NOT NULL AND
    lon IS NOT NULL AND
    fecha IS NOT NULL;

-- 4. Guardar datos limpios
STORE eventos_limpios INTO '/data/eventos_limpios' USING PigStorage(',');
