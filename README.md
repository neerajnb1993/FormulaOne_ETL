# FormulaOne_ETL
In this poc I have performed ETL where i have extracted data from Ergast api and then performed transformation and analysis and then loaded the data to presentable layer using Pspark.
In this repo there are 5 folders Raw_Data(data), Data_Ingestion(code files), Processed_data(data), Data_Transformation(code file), Presentation_Data(data) 
The folder Raw_Data contains raw data in the form of csv, json, json multiline multiplr files, csv multiple files.
The folder Data_Ingestion contains python files which consists of script to read data from Raw_Data and then write it to Processed_data folder in a parquet format.
The folder Data_Transformation contains python files which consists of script to read data from Processed_Data and then write it to Presentation_data folder in a parquet format. Here I have performed joins between dataframes and also done the analysis on data. 
