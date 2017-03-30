private void SetupAutoLayoutConstraints()
    {
        View.AddConstraints (new [] {
            // ラベルの幅をビューの幅マイナス20 にする
            NSLayoutConstraint.Create(
                lblHome, NSLayoutAttribute.Width, NSLayoutRelation.Equal, 
                View, NSLayoutAttribute.Width, 
                1, -20),

            // ラベルの高さはとにかく40
            NSLayoutConstraint.Create(
                lblHome, NSLayoutAttribute.Height, NSLayoutRelation.Equal, 
                null, NSLayoutAttribute.NoAttribute, 
                1, 40),

            // ラベルのトップ一は、Viewから100はなす
            NSLayoutConstraint.Create(
                lblHome, NSLayoutAttribute.Top, NSLayoutRelation.Equal, 
                View, NSLayoutAttribute.Top, 
                1, 100),

            // ラベルの水平中心をビューと同じにする 
            NSLayoutConstraint.Create(
                lblHome, NSLayoutAttribute.CenterX, NSLayoutRelation.Equal, 
                View, NSLayoutAttribute.CenterX, 1, 0)
        });


        View.AddConstraints (new [] {
            // ボタンの幅は、 ラベルの幅と同じ
            NSLayoutConstraint.Create(
                btnSignIn, NSLayoutAttribute.Width, NSLayoutRelation.Equal, 
                lblHome, NSLayoutAttribute.Width, 1, 0),

            // ボタンの高さは ラベルの高さと同じ
            NSLayoutConstraint.Create(
                btnSignIn, NSLayoutAttribute.Height, NSLayoutRelation.Equal, 
                lblHome, NSLayoutAttribute.Height, 1, 0),

            // ボタンのトップは ラベルの底から60話す
            NSLayoutConstraint.Create(
                btnSignIn, NSLayoutAttribute.Top, NSLayoutRelation.Equal, 
                lblHome, NSLayoutAttribute.Bottom, 1, 60),

            // ボタンの水平センターはビューの水平センターに合わせる
            NSLayoutConstraint.Create(
                btnSignIn, NSLayoutAttribute.CenterX, NSLayoutRelation.Equal, 
                View, NSLayoutAttribute.CenterX, 
                1, 0)
        });
    }
}
