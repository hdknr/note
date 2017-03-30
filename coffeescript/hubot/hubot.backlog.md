## backlog メッセージリレー

~~~coffee
backlogUrl = 'https://project.backlog.jp/'
key='274a8076b74a5dcfa08d492552bc04a9'

module.exports = (robot) ->
  robot.router.post "/#{key}/:room", (req, res) ->
    { room } = req.params
    { body } = req
    try
      label = body.type
      url = "#{backlogUrl}view/#{body.project.projectKey}-#{body.content.key_id}"
      if body.content.comment?.id?
        url += "#comment-#{body.content.comment.id}"

      message = "*Backlog #{label}*\n"
      message += "[#{body.project.projectKey}-#{body.content.key_id}] - "
      message += "#{body.content.summary} _by #{body.createdUser.name}_\n>>> "
      if body.content.comment?.content?
        message += "#{body.content.comment.content}\n"
      message += "#{url}"

      if message?
        robot.messageRoom room, message
        res.end "OK"
      else
        robot.messageRoom room, "Error."
        res.end "Error"
    catch error
      robot.send
      res.end "Error"
~~~
