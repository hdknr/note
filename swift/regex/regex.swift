// http://benscheirman.com/2014/06/regex-in-swift/
import Foundation

public class Regex {
  let _regex: NSRegularExpression?
  let pattern: String

  public init(_ pattern: String) {
    self.pattern = pattern
    var error: NSError?
    self._regex = NSRegularExpression(
        pattern: 
        pattern, options: .CaseInsensitive, error: &error)
  }

  public func test(input: String) -> Bool {
    let matches = self._regex!.matchesInString(
        input, options: nil, range:NSMakeRange(0, count(input)))
    return matches.count > 0
  }
}
