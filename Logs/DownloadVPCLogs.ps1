# Nome do Grupo de Logs na AWS
$GroupName = "VPC-FlowLogs"

# Lista de Streams em Formato JSON
try {
    $jsonStreams = aws logs describe-log-streams --log-group-name $GroupName --query "logStreams[].logStreamName" --output json
    $streams = $jsonStreams | ConvertFrom-Json
} catch {
    Write-Host "Erro ao obter os streams de log: $_"
    exit
}

foreach ($stream in $streams) {
    Write-Host "Baixando logs de $stream"
    $filePath = "C:\Users\RenanAlcolea\OneDrive\Desktop\HackatonIA\Logs\Logs_$stream.csv"
    try {
        $logEvents = aws logs get-log-events --log-group-name $GroupName --log-stream-name $stream --output json | ConvertFrom-Json
        $formattedEvents = $logEvents.events | ForEach-Object {
            $timestamp = [datetimeoffset]::FromUnixTimeMilliseconds($_.timestamp).ToLocalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffK')
            $concatenatedString = "$timestamp $($_.message)"
            $concatenatedString.Replace(" ", ",")
        }
        $formattedEvents | Out-File -FilePath $filePath -Encoding UTF8
    } catch {
        Write-Host "Erro ao baixar logs do stream ${stream}: $_"
    }
}
