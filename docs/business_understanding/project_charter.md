# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Detección de Transacciones Ilícitas en Redes de Bitcoin mediante Graph Neural Networks

## Objetivo del Proyecto

Desarrollar un sistema basado en Graph Neural Networks (GNN) para la detección de transacciones fraudulentas o ilícitas (como lavado de dinero) dentro de redes de transacciones de Bitcoin. El proyecto busca aprovechar la estructura relacional de los datos para mejorar la identificación de comportamientos sospechosos en un contexto de alto volumen transaccional y anonimidad relativa de los usuarios.

## Alcance del Proyecto

### Incluye:

- **Datos disponibles:** Elliptic Dataset, un conjunto de datos públicos con 203,769 transacciones de Bitcoin representadas como un grafo dirigido con 167 características por nodo, 234,355 aristas (conexiones entre transacciones) y etiquetas de clase (ilícita, legítima o desconocida).
- **Resultados esperados:** Un modelo GNN entrenado capaz de clasificar transacciones como ilícitas o legítimas, junto con una comparación de diferentes arquitecturas (GCN, GraphSAGE, GAT, entre otras) para identificar la más adecuada al problema.
- **Criterios de éxito:** Obtener un F1-score competitivo en la detección de transacciones ilícitas, considerando el desbalance de clases y la naturaleza semi-supervisada del dataset.

### Excluye:

- Recolección de datos directamente desde la blockchain (se utiliza un dataset público ya procesado).
- Análisis de criptomonedas distintas a Bitcoin.
- Integración con sistemas de monitoreo de terceros.

## Metodología

Se utilizará una metodología basada en CRISP-DM adaptada a proyectos de Deep Learning, que incluye las siguientes fases: entendimiento del negocio, adquisición y exploración de datos, preparación de datos y construcción del grafo, modelamiento con diferentes arquitecturas de GNN, evaluación comparativa de modelos y despliegue. Se emplearán técnicas de aprendizaje semi-supervisado sobre grafos para aprovechar tanto los nodos etiquetados como los no etiquetados.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 14 de mayo al 21 de mayo de 2026 |
| Exploración de los datos | 1 semana | del 21 de mayo al 28 de mayo de 2026 |
| Preparación de los datos | 1 semana | del 28 de mayo al 4 de junio de 2026 |
| Modelamiento y evaluación | 1 semana | del 4 de junio al 11 de junio de 2026 |
| Entrega final del proyecto | 1 semana | del 11 de junio al 18 de junio de 2026 |

## Equipo del Proyecto

- Josue Alexander Nuñez Prada
- Iveth Dayana Diaz Carabali
- Adriana Dorado Soler

## Presupuesto

- **Infraestructura:** uso de recursos locales y/o notebooks académicos (sin costo incremental para Entrega 1).
- **Licenciamiento:** herramientas open-source.
- **Costo estimado Entrega 1:** 0 COP en servicios externos.

## Stakeholders

- **Programa MLDS (Universidad):** Evaluador académico del proyecto. Espera un desarrollo riguroso que demuestre competencias en Deep Learning aplicado.
- **Sector financiero y tecnológico (beneficiarios potenciales):** Plataformas de intercambio de criptomonedas, empresas de análisis blockchain y organizaciones de prevención de fraude que podrían beneficiarse de los resultados del modelo.

## Aprobaciones

- Docente del curso MLDS - Módulo 6
- Estado: En revisión académica
- Fecha: Mayo 2026
