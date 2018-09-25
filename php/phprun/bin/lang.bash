BASE="$HOME"
export PATH="$BASE/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $BASE/.anyenv/envs`; do
    export PATH="$BASE/.anyenv/envs/$D/shims:$PATH"
done

function OPEN_SSH()
{
  PARAMS="$@"; [ -n "$PARAMS" ] || PARAMS="default";
  if [ -f ssh.conf ]; then
    # macOS
    SCRIPT="cd $PWD;$SUDO ssh -F ssh.conf $PARAMS"; 
    AS="osascript -e 'tell application \"Terminal\" to do script \"$SCRIPT\"'";
    eval $AS;
  fi
}

function SCP()
{
  PARAMS="$@"; [ -n "$PARAMS" ] || PARAMS="default";
  if [ -f ssh.conf ]; then
    echo "scp -F ssh.conf $PARAMS"; 
    scp -F ssh.conf $PARAMS; 
  fi
}