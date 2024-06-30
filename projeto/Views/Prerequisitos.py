import flet as ft
import Disciplinas


def view():
    linha = ft.Row(
        controls=[]
    )
    linha2 = ft.Row(
        controls=[]
    )
    tela = ft.Column(
        controls=[]
    )

    for c in range(0,len(Disciplinas.periodo1)):
        texto = ft.ElevatedButton(
            text = f"{Disciplinas.periodo1[c]["nome"]}",
            
        )
        linha.controls.append(texto)
    tela.controls.append(linha)

    for c in range(0,len(Disciplinas.periodo2)):
        texto = ft.ElevatedButton(
            text = f"{Disciplinas.periodo2[c]["nome"]}",
            
        )
        linha2.controls.append(texto)
    tela.controls.append(linha2)

    return tela