protocol HumanProtocol {
    var name: String { get set  }
}

public class Adult : HumanProtocol {
    var _name : String = ""
    var name: String { 
        get { return _name }
        set { _name = newValue }
    }
}
