.. list-table::

    *   - Engine
        - MySQL
        - PostgreSQL

    *   - テーブル一覧
        - `show tables`
        - `\dt`

          `SELECT * FROM pg_catalog.pg_tables where schemaname = 'public';`

    *   - スキーマ
        - `desc yourtable`
        - `\d+ yourtable`

    *   - ホスト名
        - `show variables like 'hostname';`
        - 
