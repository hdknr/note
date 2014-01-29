Date: 2013-11-20 06:00  
Title: Rails:テーブルにカラムを追加するマイグレーション
Type: post  
Excerpt:   



マイグレーションの用意:

    $ rails generate migration  AddJwkSetToProvider jwkset:text
          invoke  active_record
          create    db/migrate/20131119094759_add_jwk_set_to_provider.rb
      

Rails 3.1 から change １つで出来る。:

    1 class AddJwkSetToProvider < ActiveRecord::Migration
    2   def change
    3     add_column :providers, :jwkset, :text
    4   end
    5 end
      
デフォルトで :null => true なのでこれでよいのかな。
マイグレート:

    $ rake db:migrate
        ==  AddJwkSetToProvider: migrating ============================================
        -- add_column(:providers, :jwkset, :text)
           -> 0.0015s
        ==  AddJwkSetToProvider: migrated (0.0024s) ===================================


確認:

    $ echo ".schema providers" | rails dbconsole

    CREATE TABLE "providers" 
    ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     -- 途中省略
     "jwkset" text);
       
