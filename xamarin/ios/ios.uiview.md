## 白く塗りつぶす

~~~csharp
public  void DrawBackground (CoreGraphics.CGRect rect)
{
  var context = UIGraphics.GetCurrentContext ();

  context.SetLineWidth(4);
  context.SetFillColor (UIColor.White.CGColor);
  context.FillRect (rect);
  context.DrawPath(CoreGraphics.CGPathDrawingMode.FillStroke);
}
~~~
