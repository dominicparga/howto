#!/usr/bin/env sh

echo '#------------------------------------------------------------------------------#'
echo '# gitignore'
curl -L -s 'https://www.gitignore.io/api/linux,macos,windows,visualstudiocode,tex,latex'
echo ''
echo '#------------------------------------------------------------------------------#'
echo '# custom'
echo ''
echo '/build/'
echo '/custom/'
echo ''
echo '.vscode/'
