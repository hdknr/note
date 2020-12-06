# ARKit 



## 前回設定したアンカーをリセットしてセッションを開始する

- ラッキングリセット: `.resetTracking`
- 既存アンカーの削除: `.removeExistingAnchors`

~~~swift

// ARSCNViewのビューコントローラ

final class ArInteractor: NSObject, ARSCNViewDelegate {

 // https://developer.apple.com/documentation/arkit/arscnview
 private let sceneView = ARSCNView()
 var scene_node: SCNNode?


 func setupAR() -> CALayer {
    // https://developer.apple.com/documentation/scenekit/scnscene
    sceneView.scene = SCNScene()
    sceneView.autoenablesDefaultLighting = true
    sceneView.delegate = self

    return sceneView.layer
 }
 
 func startSession(scene: SCNNode, marker: String) {
    scene_node = scene  // シーンノード

    // https://developer.apple.com/documentation/arkit/arreferenceimage
    let images = ARReferenceImage.referenceImages(
      inGroupNamed: marker, bundle: nil
    )

    let configuration = ARWorldTrackingConfiguration()
    configuration.isLightEstimationEnabled = true
    configuration.environmentTexturing = .automatic
    configuration.detectionImages = images

    configuration.planeDetection = [.vertical, .horizontal]
    configuration.automaticImageScaleEstimationEnabled = true
    // configuration.worldAlignment = .gravity

    // トラッキングリセット && 既存アンカーの削除を optionsで指定します
    sceneView.session.run(
        configuration, 
        options: [.resetTracking, .removeExistingAnchors])
  }

  func renderer(_: SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor) {
    if let anchor = anchor as? ARImageAnchor {
      // ARImageAnchor が見つかったら
      if scene_node != nil {
        // シーンノードをARに追加
        node.addChildNode(scene_node!)
      }
    }
  }
}
~~~
