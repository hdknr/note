import Foundation

public class Logger
{
    var prefix: String
    
    public init(_ prefix: String) 
    {
        self.prefix = prefix
    }
    
    public func log(msg: String)
    {
        print(prefix)
        println(msg)
    }
}
