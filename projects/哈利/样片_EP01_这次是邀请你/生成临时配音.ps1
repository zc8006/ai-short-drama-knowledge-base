$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$taskRoot = $PSScriptRoot
$taskLines = Get-Content -LiteralPath (Join-Path $taskRoot '对白.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$taskSynth = New-Object System.Speech.Synthesis.SpeechSynthesizer
foreach ($taskLine in $taskLines) {
  $taskVoice = if ($taskLine.role -eq '马尔福') { 'Microsoft Yaoyao' } else { 'Microsoft Kangkang' }
  $taskSynth.SelectVoice($taskVoice)
  $taskSynth.Rate = if ($taskLine.role -eq '高尔') { -1 } else { 0 }
  $taskSynth.SetOutputToWaveFile((Join-Path $taskRoot $taskLine.wav))
  $taskSynth.Speak($taskLine.text)
  $taskSynth.SetOutputToNull()
}
$taskSynth.Dispose()
