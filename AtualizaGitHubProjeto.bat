@echo oFF
Mode 78,23
color 0a
echo.
cd %CD%
net session >nul 2>&1

:TOPO
@TITLE Script Atualiza Projeto GitHub

cls
 echo.
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo      같                                                               같
 echo      같 �袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴敲 같
 echo      같 �             SCRIPT ATUALIZA PROJETO GITHUB                � 같
 echo      같 훤袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴� 같
 echo      같                                                               같
 echo      같                                                               같
 CECHO      같                                              {red}By: MARDONIO{#}     같{\n}
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo.

git add *
git status
set COMMIT=
set /p COMMIT=Quais foram as alteracoes feitas no projeto:

git commit -a -m "%COMMIT%"
echo.
echo.
echo.
echo.
git push
echo.
echo.
echo.
echo. Atualizacao concluida!

@PAUSE