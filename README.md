# Data Warehousing with Databricks DLT

## 📖 Project Overview
Welcome to the **DLT Project** repository! 🚀

This project demonstrates how to build a Data Warehouse using Databricks Declarative Live Tables (DLT) pipelines. It showcases key DLT features such as:

- **Flows** for orchestration
- **Streaming tables** for incremental data processing
- **Materialized views** for optimized query performance
- **Views for transformations** and logic abstraction
- **Change Data Capture (CDC)** and **Slowly Changing Dimensions (SCD Types 1 & 2)**

The project also applies the **Medallion Architecture (Bronze, Silver, Gold layers)** to design a structured DWH pipeline.

In addition, detailed **step-by-step documentation** is provided with screenshots, making it easy to follow and understand the design, implementation, and execution of each stage.

## 🚀 Project Requirements

### Building the Data Warehouse (Data Engineering)

#### Objective
Develop a modern data warehouse using DLT Pipelines to consolidate sales data, enabling analytical reporting and informed decision-making.

#### Specifications
- **Data Sources**: Data is imported using SQL queries, which are provided as separate **.sql** files.
- **Data Quality**: Cleanse and resolve data quality issues with Expecations and other industry best practices prior to analysis.
- **Integration**: Combine both sources into a single, user-friendly data model designed for analytical queries.
- **Scope**: Focus on the latest dataset only; historization of data is not required.
- **Documentation**: Provide clear documentation of the data model to support both business stakeholders and analytics teams.

---
## 🏗️ Data Architecture
The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
![Data Architecture](docs/data_architecture.png)

The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
---

## 📂 Repository Structure
```
data-warehouse-project/
│
├── datasets/                           # Raw datasets used for the project (ERP and CRM data)
│
├── docs/                               # Project documentation and architecture details
│   ├── etl.drawio                      # Draw.io file shows all different techniquies and methods of ETL
│   ├── data_architecture.drawio        # Draw.io file shows the project's architecture
│   ├── data_catalog.md                 # Catalog of datasets, including field descriptions and metadata
│   ├── data_flow.drawio                # Draw.io file for the data flow diagram
│   ├── data_models.drawio              # Draw.io file for data models (star schema)
│   ├── naming-conventions.md           # Consistent naming guidelines for tables, columns, and files

│
├── scripts/                            # SQL scripts for ETL and transformations
│   ├── bronze/                         # Scripts for extracting and loading raw data
│   ├── silver/                         # Scripts for cleaning and transforming data
│   ├── gold/                           # Scripts for creating analytical models
│   ├── EDA/                            # Scripts for performing EDA
│   ├── data_analytics/                 # Scripts for creating reports  
│
├── tests/                              # Test scripts and quality files
│
├── README.md                           # Project overview and instructions
├── LICENSE                             # License information for the repository
├── .gitignore                          # Files and directories to be ignored by Git
└── requirements.txt                    # Dependencies and requirements for the project
```
---
