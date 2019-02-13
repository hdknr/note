# UDP 送信

~~~ps1
using namespace System.Net;
using namespace System.Net.Sockets;
using namespace System.Text;

param (
    [string]$ip = $( Read-Host "IP Address, please" ),
    [int]$port = $(Read-Host "UPD Port, please" ),
    [string]$msg = $( Read-Host "Messaage, please" )
)

$SP = @{
    FAMILY  =  [AddressFamily]::InterNetwork;
    TYPE = [SocketType]::Dgram;
    PROTO = [ProtocolType]::Udp;
    TTL = 26;
}

$buffer = [Encoding]::ASCII.GetBytes($msg);
$address = [IPAddress]::Parse( $ip )
$end = New-Object IPEndpoint $address, $port;
#
$socket = New-Object Socket $SP.FAMILY, $SP.TYPE, $SP.PROTO;
$socket.TTL = $SP.TTL;

$result = $socket.SendTo($buffer, $end)
#
Write-Host("Message was sent.", $result, $end)
~~~