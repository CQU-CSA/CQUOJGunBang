@echo off
rem
rem Purpose: to run a standalone resolver
rem   or to connect to a CDS and control the resolution
rem   or to connect to a CDS and view the resolution
rem

set LIBDIR=%~dp0\lib

set params=

:loop
if %1. == . goto :continue
set params=%params% %1
shift
goto :loop

:continue

java -Xmx1024m -cp "%LIBDIR%\resolver.jar";"%LIBDIR%\tyrus-standalone-client-1.12.jar" org.acmicpc.resolver.Resolver %params%
