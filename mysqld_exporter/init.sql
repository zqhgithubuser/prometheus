CREATE USER 'exporter'@'172.31.0.%' IDENTIFIED BY 'exporter';
GRANT PROCESS, REPLICATION CLIENT ON *.* TO 'exporter'@'172.31.0.%';
GRANT SELECT ON performance_schema.* TO 'exporter'@'172.31.0.%'
