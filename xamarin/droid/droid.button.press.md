Android: ボタンに押された感を出してみる

- 条件によってボタンの色が変わるユースケース
- 今回は色ですがイメージとかも可能

## 色をDrawable化

~~~csharp
public static Android.Graphics.Drawables.ColorDrawable ToDrawable(
  this Android.Graphics.Color color){

  return  new Android.Graphics.Drawables.ColorDrawable (color);
}
~~~

## アルファ値を変えた色を背景色として押された効果を作る

~~~csharp

using System.Linq;
...

public static Android.Graphics.Drawables.StateListDrawable ToButtonPressEffect(
  this Android.Graphics.Color color, byte alpha=200
){

  var pressed = new Android.Graphics.Color (
    color.R, color.G, color.B, alpha);

  var effect = new  Android.Graphics.Drawables.StateListDrawable ();
  effect.AddState (
    new int[]{ Android.Resource.Attribute.StatePressed }, pressed.ToDrawable ());

  effect.AddState (
    Android.Util.StateSet.WildCard.ToArray (), color.ToDrawable ());
  return effect;
}

~~~

## Buttonの背景にエフェクトを設定する

~~~csharp
...
var ok_button = new Button (this) {   // this = Activity
  Background=ok_button_color.ToButtonPressEffect()
};
~~~
