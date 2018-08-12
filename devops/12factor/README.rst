https://12factor.net/ja/

- Best practic for Apps on Heroku.


.. list-table:: 12 Factor Application
    :widths: 30, 70
    :header-rows: 1

    *   - Factor
        - Content

    *   - コードベース
        - `バージョン管理されている1つのコードベースと複数のデプロイ <codebase.md>`_

    *   - 依存関係
        - `依存関係を明示的に宣言し分離する <dependencies.md>`_

    *   - 設定
        - `設定を環境変数に格納する <config.md>`_

    *   - バックエンドサービス
        - `バックエンドサービスをアタッチされたリソースとして扱う <backing-services.md>`_

    *   - ビルド、リリース、実行
        - `ビルド、リリース、実行の3つのステージを厳密に分離する <build-release-run.md>`_

    *   - プロセス
        - `アプリケーションを1つもしくは複数のステートレスなプロセスとして実行する <processes.md>`_

    *   - ポートバインディング
        - `ポートバインディングを通してサービスを公開する <port-binding.md>`_

    *   - 並行性
        - `プロセスモデルによってスケールアウトする <concurrency.md>`_

    *   - 廃棄容易性
        - `高速な起動とグレースフルシャットダウンで堅牢性を最大化する <disposability.md>`_

    *   - 開発/本番一致
        - `開発、ステージング、本番環境をできるだけ一致させた状態を保つ <dev-prod-parity.md>`_

    *   - ログ
        - `ログをイベントストリームとして扱う <logs.md>`_

    *   - 管理プロセス
        - `管理タスクを1回限りのプロセスとして実行する <admin-processes.md>`_