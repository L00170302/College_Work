rem Google is making release notes compulsory for every new release of the app versions
echo off
if exist home.html goto yesfile
if not exist home.html goto nofile
goto end
:yesfile
echo FILE EXISTS PROCESSING
goto end
:nofile
echo FILE DOES NOT EXIST PROCESSING. BUILD FAILED.
goto end
:end