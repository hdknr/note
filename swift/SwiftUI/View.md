# View


## 表示非表示

~~~swift
// モディファイア(表示/非表示を切り替える)
struct Show: ViewModifier {
    @Binding var isVisible: Bool

    @ViewBuilder
    func body(content: Content) -> some View {
        if isVisible {
            content
        } else {
            content.hidden()
        }
    }
}
~~~

~~~swift
//　モディファイアを設定する拡張メソッド
extension View {
    func show(isVisible: Binding<Bool>) -> some View {
        ModifiedContent(content: self, modifier: Show(isVisible: isVisible))
    }
}
~~~

~~~swift
struct Scenes: View {
     
    @State var isMenuVisible: Bool = false  // 最初は表示しない
    
    var body: some View {
        
        return ZStack(alignment: .bottomLeading) {
            // メニュー表示
            HStack {
                Button(action: { showMenu() }) {Text("?")}
            }.padding()
        
            // メニュー内容
            HStack(spacing:10) {    // ボタン間に間を開ける
                Button(action: { doCommand(index: 0) }) {Text("#1")}
                // .....
            }
            .padding()
            .show(isVisible: $isMenuVisible)   // 表示/非表示きりかえ
        }
    }
    
    func showMenu() {
        isMenuVisible.toggle() // 表示させる
    }

    func doCommand(index: Int) {
        // TODO メニュー実行 
        
        isMenuVisible.toggle()   // 非表示
    }
}
~~~

