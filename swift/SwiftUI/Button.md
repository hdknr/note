# Button

## ボタンにスタイルを当てる

~~~swift
struct GradientButtonStyle: ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some
    View {
        let gradient = Gradient(colors: [Color.red, Color.yellow])

        return configuration.label
            .foregroundColor(Color.white)
            .padding()
            .background(LinearGradient(gradient:gradient , startPoint: .leading, endPoint: .trailing))
            .cornerRadius(15.0)
            .scaleEffect(configuration.isPressed ? 1.3 : 1.0)
    }
}
~~~

~~~swift
struct Scenes: View {
     
    var body: some View {
        
        ZStack(alignment: .bottomLeading) {
            // メニュー表示
            HStack {
                Button(action: { showMenu() }) {
                    Text("?")
                }.buttonStyle(GradientButtonStyle())
            }.padding()
        }
    }
}
~~~