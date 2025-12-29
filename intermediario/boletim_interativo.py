"""Ferramenta intermediária para registrar alunos e calcular estatísticas de notas."""
from __future__ import annotations

from dataclasses import dataclass, field
from statistics import fmean, median
from typing import List


@dataclass
class Aluno:
    nome: str
    notas: List[float] = field(default_factory=list)

    def media(self) -> float:
        return fmean(self.notas)

    def mediana(self) -> float:
        return median(self.notas)

    def situacao(self, media_aprovacao: float) -> str:
        return "Aprovado" if self.media() >= media_aprovacao else "Recuperação"


def coletar_notas() -> list[Aluno]:
    alunos: list[Aluno] = []
    print("Cadastro de alunos (digite ENTER no nome para encerrar)")
    while True:
        nome = input("Nome do aluno: ").strip()
        if not nome:
            break
        notas: list[float] = []
        print("Digite as notas separadas por espaço (ex: 7 8.5 10)")
        raw = input(f"Notas de {nome}: ")
        try:
            notas = [float(item) for item in raw.split()]
        except ValueError:
            print("Entrada inválida, tente novamente.")
            continue
        if not notas:
            print("É necessário ao menos uma nota.")
            continue
        alunos.append(Aluno(nome=nome, notas=notas))
    return alunos


def gerar_relatorio(alunos: list[Aluno], media_aprovacao: float = 7.0) -> None:
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\nRelatório de desempenho")
    print("-" * 40)
    melhores = sorted(alunos, key=lambda aluno: aluno.media(), reverse=True)
    for aluno in melhores:
        media_aluno = aluno.media()
        print(f"Aluno: {aluno.nome}")
        print(f"  Notas: {', '.join(f'{n:.1f}' for n in aluno.notas)}")
        print(f"  Média: {media_aluno:.2f} | Mediana: {aluno.mediana():.2f}")
        print(f"  Situação: {aluno.situacao(media_aprovacao)}")
    geral = [nota for aluno in alunos for nota in aluno.notas]
    print("-" * 40)
    print(f"Média geral da turma: {fmean(geral):.2f}")
    print(f"Mediana geral: {median(geral):.2f}")
    print(f"Melhor média: {melhores[0].nome} ({melhores[0].media():.2f})")


if __name__ == "__main__":
    relacao = coletar_notas()
    gerar_relatorio(relacao)
