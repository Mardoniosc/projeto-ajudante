@echo oFF
Mode 78,23
color 0A
echo.
cd %CD%
net session >nul 2>&1

:TOPO
@TITLE Sincroniza Projeto com o GitHub

cls
 echo.
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo      같                                                               같
 echo      같 �袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴敲 같
 echo      같 �        SCRIPT SINCRONIZA PROJETO COM O GITHUB             � 같
 echo      같 훤袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴袴� 같
 echo      같                                                               같
 echo      같                                                               같
 CECHO      같                                              {red}BY: MARDONIO{#}     같{\n}
 echo      같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같같�
 echo.

CECHO {0C}Sincronizando, aguarde...{#}{\n}
git pull


@PAUSE