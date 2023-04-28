PGDMP     +    4                {            ZXC    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            
           1262    24905    ZXC    DATABASE     |   CREATE DATABASE "ZXC" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "ZXC";
                postgres    false            �            1259    24933    Departamento    TABLE     r   CREATE TABLE public."Departamento" (
    "ID_Dep" integer NOT NULL,
    "Nome" character varying(255) NOT NULL
);
 "   DROP TABLE public."Departamento";
       public         heap    postgres    false            �            1259    24932    Departamento_ID_Dep_seq    SEQUENCE     �   CREATE SEQUENCE public."Departamento_ID_Dep_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public."Departamento_ID_Dep_seq";
       public          postgres    false    217                       0    0    Departamento_ID_Dep_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public."Departamento_ID_Dep_seq" OWNED BY public."Departamento"."ID_Dep";
          public          postgres    false    216            �            1259    24924    Funcionario    TABLE       CREATE TABLE public."Funcionario" (
    "ID_Fun" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Salario" money DEFAULT 0.00 NOT NULL,
    "Cargo" character varying(225) DEFAULT 'Autônomo'::character varying NOT NULL,
    "Id_Dep" integer NOT NULL
);
 !   DROP TABLE public."Funcionario";
       public         heap    postgres    false            �            1259    24923    Funcionario_ID_Fun_seq    SEQUENCE     �   CREATE SEQUENCE public."Funcionario_ID_Fun_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."Funcionario_ID_Fun_seq";
       public          postgres    false    215                       0    0    Funcionario_ID_Fun_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Funcionario_ID_Fun_seq" OWNED BY public."Funcionario"."ID_Fun";
          public          postgres    false    214            m           2604    24936    Departamento ID_Dep    DEFAULT     �   ALTER TABLE ONLY public."Departamento" ALTER COLUMN "ID_Dep" SET DEFAULT nextval('public."Departamento_ID_Dep_seq"'::regclass);
 F   ALTER TABLE public."Departamento" ALTER COLUMN "ID_Dep" DROP DEFAULT;
       public          postgres    false    217    216    217            j           2604    24927    Funcionario ID_Fun    DEFAULT     ~   ALTER TABLE ONLY public."Funcionario" ALTER COLUMN "ID_Fun" SET DEFAULT nextval('public."Funcionario_ID_Fun_seq"'::regclass);
 E   ALTER TABLE public."Funcionario" ALTER COLUMN "ID_Fun" DROP DEFAULT;
       public          postgres    false    215    214    215                      0    24933    Departamento 
   TABLE DATA           :   COPY public."Departamento" ("ID_Dep", "Nome") FROM stdin;
    public          postgres    false    217   !                 0    24924    Funcionario 
   TABLE DATA           W   COPY public."Funcionario" ("ID_Fun", "Nome", "Salario", "Cargo", "Id_Dep") FROM stdin;
    public          postgres    false    215   G                  0    0    Departamento_ID_Dep_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."Departamento_ID_Dep_seq"', 1, true);
          public          postgres    false    216                       0    0    Funcionario_ID_Fun_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."Funcionario_ID_Fun_seq"', 1, true);
          public          postgres    false    214            q           2606    24938    Departamento Departamento_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public."Departamento"
    ADD CONSTRAINT "Departamento_pkey" PRIMARY KEY ("ID_Dep");
 L   ALTER TABLE ONLY public."Departamento" DROP CONSTRAINT "Departamento_pkey";
       public            postgres    false    217            o           2606    24931    Funcionario Funcionario_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public."Funcionario"
    ADD CONSTRAINT "Funcionario_pkey" PRIMARY KEY ("ID_Fun");
 J   ALTER TABLE ONLY public."Funcionario" DROP CONSTRAINT "Funcionario_pkey";
       public            postgres    false    215            r           2606    24939    Funcionario fk_departamento    FK CONSTRAINT     �   ALTER TABLE ONLY public."Funcionario"
    ADD CONSTRAINT fk_departamento FOREIGN KEY ("Id_Dep") REFERENCES public."Departamento"("ID_Dep");
 G   ALTER TABLE ONLY public."Funcionario" DROP CONSTRAINT fk_departamento;
       public          postgres    false    217    3185    215                  x�3�K�KI,����� �N         )   x�3���O��RQ����10�,K�KIM�/�4����� �_     