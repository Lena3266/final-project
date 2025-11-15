# Set your backend URL
$BackendUrl = "http://localhost:8000/detect"

# Folder with images to test (update this path to where your test images are)
# For now, we'll create a test folder or use an existing one
$ImageFolder = "$env:USERPROFILE\Downloads\test_images"

# Check if folder exists; if not, skip or create it
if (-not (Test-Path -Path $ImageFolder)) {
    Write-Host "Image folder not found: $ImageFolder"
    Write-Host "Please create this folder and add test images (.jpg, .png, .jpeg)"
    exit 1
}

# Get all jpg/png/jpeg files from folder
$Images = @(Get-ChildItem -Path $ImageFolder -Include *.jpg, *.png, *.jpeg -File)

if ($Images.Count -eq 0) {
    Write-Host "No images found in $ImageFolder"
    exit 1
}

Write-Host "Testing backend responses..."
Write-Host "Backend URL: $BackendUrl"
Write-Host "Images to test: $($Images.Count)`n"

# Optional: Test health endpoint first
$HealthUrl = $BackendUrl -replace '/detect$', '/health'
Write-Host "Checking backend health at $HealthUrl ..."
try {
    $HealthCheck = Invoke-RestMethod -Uri $HealthUrl -Method Get -TimeoutSec 5
    Write-Host "Backend status: $($HealthCheck.status)"
    Write-Host "Multipart available: $($HealthCheck.multipart_available)`n"
} catch {
    Write-Warning "Health check failed. Backend may not be running at $HealthUrl"
}

foreach ($img in $Images) {
    Write-Host "Uploading $($img.FullName) ..."

    # Wrap path in FileInfo object
    $FileInfo = New-Object System.IO.FileInfo $img.FullName
    $Form = @{ file = $FileInfo }

    try {
        $Response = Invoke-RestMethod -Uri $BackendUrl -Method Post -Form $Form
        Write-Host "Response for $($img.Name):"
        $Response | ConvertTo-Json -Depth 10
    } catch {
        Write-Error "Failed for $($img.Name) : $_"
    }

    Write-Host "`n-----------------------------`n"
}
