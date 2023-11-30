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

# Itera sobre cada stream e baixa os logs
foreach ($stream in $streams) {
    Write-Host "Baixando logs de $stream"
    $safeStreamName = $stream -replace '[\\/:*?"<>|]', '_'
    $filePath = "C:\Users\RenanAlcolea\OneDrive\Desktop\Oi\Logs CloudWatch\Logs_$safeStreamName.csv"
    try {
        $logEvents = aws logs get-log-events --log-group-name $GroupName --log-stream-name $stream --output json | ConvertFrom-Json
        $formattedEvents = $logEvents.events | ForEach-Object {
            $timestamp = [datetimeoffset]::FromUnixTimeMilliseconds($_.timestamp).ToLocalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffK')
            [PSCustomObject]@{
                Timestamp = $timestamp
                Message = $_.message
            }
        }
        $formattedEvents | Export-Csv -Path $filePath -NoTypeInformation
    } catch {
        Write-Host "Erro ao baixar logs do stream ${stream}: $_"
    }
}
