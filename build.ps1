$exclude = @("venv", "pyTest.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "pyTest.zip" -Force