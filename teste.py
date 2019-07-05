import subprocess

def conectarnaEC(nomelogico):
    # print("Senha a ser utilizada: c41x4l1vr3d3b14n6")
    # subprocess.call("pause", shell=True)

    if nomelogico.__contains__('ec'):
        putty = ("start putty.exe -t -ssh caixa@%s -pw estacaolivredebian" % nomelogico)

    else:
        putty = ("start putty.exe -ssh root@%s -pw caixa -m C:\comando_putty\\reiniciarTO_TH.txt" % nomelogico)

    try:
        resultado  = subprocess.check_call(putty, shell=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        putty = ("start putty.exe -ssh caixa@%s -pw caixa -m C:\comando_putty\\reiniciarTO_TH.txt" % nomelogico)


        try:
            subprocess.call(putty, shell=True)
        except subprocess.CalledProcessError as e:
            # gerar um txt com nome logico que deu erro
            print(nomelogico)
            print("error code: {}".format(e.returncode))


if __name__ == '__main__':
    subprocess.call(['notepad.exe', 'nomelogico.txt'])

    with open("nomelogico.txt") as file:
        for line in file:
            line = line[:-1]
            conectarnaEC(line)

