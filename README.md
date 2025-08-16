# MILO – Agente Logístico en n8n (Hackathon Haceb)

Asistente conversacional para Contact Center que consulta y actualiza estado de pedidos (EAD) y verifica inventario con PostgreSQL; además usa RAG para políticas/procedimientos mediante Supabase Vector + OpenAI. Todo orquestado en n8n.

## ¿Qué hace?

- Chat web (widget de n8n) llamado MILO con reglas de negocio logísticas.

- Tools hacia Postgres:

  > EAD LookUp: consulta por numero_pedido y/o cedula.

  > EAD Update: reprograma/cancela pedidos con confirmación.

  > Inventory LookUp: disponibilidad y próxima reposición (ETA). 

- RAG: indexa docs (CSV/Excel/PDF) de Google Drive en Supabase para respuestas con contexto. 

## Estructura del repositorio

- **HACEB RAG.json** → Agente conversacional MILO (chatTrigger + herramientas a Postgres + RAG). 

- **HACEB PIPELINE.json** → Ingesta a vector DB (trigger de Google Drive → extracción → embeddings → Supabase). 

- **HACEB DB.json** → Esquema Postgres para ead e inventory con índices. 

> Importa cada JSON como workflow en n8n.

## Base de datos (dummy)

Se crean dos tablas:

```sql
ead(numero_pedido PK, numero_transporte, cedula, estado_pedido, fecha_entrega, fecha_estimada_entrega)
```

  > estado_pedido con estados válidos: Pendiente, Entregado, No Entregado, Entrega Parcial, Atraso, Inicio de Ruta, Cancelado, Reprogramado. 

```sql
inventory(sku PK, categoria, producto, agosto16…agosto31, stock_actual) + índices de búsqueda.
```

  > Columnas de agosto son fechas de llegada simuladas (demo) para calcular ETA. 

Nota sobre consistencia: el tool de EAD Update permite Reprogramado/Cancelado (y menciona “Incidencia”) pero la restricción CHECK de la tabla no incluye “Incidencia”. Si quieres usar ese estado, agrega al CHECK del esquema.

## Requisitos

- n8n (self-hosted, Desktop o Cloud)

- PostgreSQL accesible desde n8n

- Supabase (tabla documents con función de similitud configurada; tabla document_metadata)

- OpenAI API Key

- Google Drive OAuth (para el pipeline de ingesta)

## Tecnologías

> n8n
> PostgreSQL
> Supabase (Vector)
> OpenAI (Chat + Embeddings)
> Google Drive Trigger
