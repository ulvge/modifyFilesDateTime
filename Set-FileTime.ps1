# 修改文件创建时间
param(
    [string]$filePath,
    [datetime]$creationTime
)

$(Get-Item $filePath).CreationTime = $creationTime
$(Get-Item $filePath).LastWriteTime = $creationTime
$(Get-Item $filePath).LastAccessTime = $creationTime
