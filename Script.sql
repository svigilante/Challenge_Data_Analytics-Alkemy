-- Unica Tabla
-- Table: public.Tabla Unica

-- DROP TABLE IF EXISTS public."Tabla Unica";

CREATE TABLE IF NOT EXISTS public."Tabla Unica"
(
    index bigint,
    cod_localidad bigint,
    id_provincia bigint,
    id_departamento bigint,
    categoria text COLLATE pg_catalog."default",
    provincia text COLLATE pg_catalog."default",
    localidad text COLLATE pg_catalog."default",
    nombre text COLLATE pg_catalog."default",
    domicilio text COLLATE pg_catalog."default",
    "codigo postal" text COLLATE pg_catalog."default",
    telefono text COLLATE pg_catalog."default",
    mail text COLLATE pg_catalog."default",
    web text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Tabla Unica"
    OWNER to santi;
-- Index: ix_Tabla Unica_index

-- DROP INDEX IF EXISTS public."ix_Tabla Unica_index";

CREATE INDEX IF NOT EXISTS "ix_Tabla Unica_index"
    ON public."Tabla Unica" USING btree
    (index ASC NULLS LAST)
    TABLESPACE pg_default;




-- Tabla Prov y Cat

-- Table: public.Tabla_Prov_Cat

-- DROP TABLE IF EXISTS public."Tabla_Prov_Cat";

CREATE TABLE IF NOT EXISTS public."Tabla_Prov_Cat"
(
    provincia text COLLATE pg_catalog."default",
    categoria text COLLATE pg_catalog."default",
    "Fecha de Carga" text COLLATE pg_catalog."default",
    "Cant. Total Fuentes" double precision,
    "Cant. Total categoria" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Tabla_Prov_Cat"
    OWNER to santi;
-- Index: ix_Tabla_Prov_Cat_categoria

-- DROP INDEX IF EXISTS public."ix_Tabla_Prov_Cat_categoria";

CREATE INDEX IF NOT EXISTS "ix_Tabla_Prov_Cat_categoria"
    ON public."Tabla_Prov_Cat" USING btree
    (categoria COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: ix_Tabla_Prov_Cat_provincia

-- DROP INDEX IF EXISTS public."ix_Tabla_Prov_Cat_provincia";

CREATE INDEX IF NOT EXISTS "ix_Tabla_Prov_Cat_provincia"
    ON public."Tabla_Prov_Cat" USING btree
    (provincia COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;





-- Tabla Cines

-- Table: public.Tabla_Cines

-- DROP TABLE IF EXISTS public."Tabla_Cines";

CREATE TABLE IF NOT EXISTS public."Tabla_Cines"
(
    provincia text COLLATE pg_catalog."default",
    "Fecha de Carga" text COLLATE pg_catalog."default",
    "Cantidad de Pantallas" bigint,
    "Cantidad de Butacas" bigint,
    "Cantidad de espacios INCAA" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Tabla_Cines"
    OWNER to santi;
-- Index: ix_Tabla_Cines_provincia

-- DROP INDEX IF EXISTS public."ix_Tabla_Cines_provincia";

CREATE INDEX IF NOT EXISTS "ix_Tabla_Cines_provincia"
    ON public."Tabla_Cines" USING btree
    (provincia COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;