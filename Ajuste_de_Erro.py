import numpy as np
import matplotlib.pyplot as plt

def gerar_dados_artificiais(coef_angular, erro_percentual, n_dados=100):
    """
    Gera dados artificiais com erro gaussiano.
    """
    x = np.linspace(0, 10, n_dados)
    y_real = coef_angular * x
    erro_absoluto = erro_percentual / 100 * y_real
    erros_gaussianos = np.random.normal(0, erro_absoluto)
    y_com_erro = y_real + erros_gaussianos
    return x, y_com_erro

def ajustar_reta_origem(x, y):
    """
    Ajusta uma reta que passa pela origem usando mínimos quadrados.
    """
    coef_angular = np.sum(x * y) / np.sum(x ** 2)
    return coef_angular

def analisar_erros(coefs_angulares, erros_entrada, n_amostras=100):
    """
    Analisa a relação entre erros de entrada e saída para diferentes coeficientes.
    """
    erros_saida = {}
    
    for coef in coefs_angulares:
        erros = []
        for erro_entrada in erros_entrada:
            x, y = gerar_dados_artificiais(coef, erro_entrada, n_amostras)
            coef_ajustado = ajustar_reta_origem(x, y)
            erro_saida = abs(coef_ajustado - coef) / coef * 100
            erros.append(erro_saida)
        erros_saida[coef] = erros
    
    return erros_saida

def plotar_analise_erros(erros_entrada, erros_saida):
    """
    Plota o gráfico de erro de saída vs erro de entrada.
    """
    plt.figure(figsize=(12, 6))
    
    for coef in erros_saida:
        plt.plot(erros_entrada, erros_saida[coef], 
                label=f'Coeficiente Angular = {coef}')
    
    plt.xlabel('Erro de Entrada (%)')
    plt.ylabel('Erro de Saída (%)')
    plt.title('Erro de Saída em Função do Erro de Entrada')
    plt.grid(True)
    plt.legend()
    plt.show()

# Execução principal
if __name__ == "__main__":
    # Parâmetros da análise
    coefs_angulares = [0.5, 1, 2, 5]
    erros_entrada = np.linspace(1, 20, 40)
    
    # Realizar análise
    erros_saida = analisar_erros(coefs_angulares, erros_entrada)
    
    # Plotar resultados
    plotar_analise_erros(erros_entrada, erros_saida)
    
    # Exemplo de um único ajuste
    x, y = gerar_dados_artificiais(2, 10)
    coef_ajustado = ajustar_reta_origem(x, y)
    
    # Plotar exemplo individual
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, label='Dados com erro')
    plt.plot(x, coef_ajustado * x, 'r-', label=f'Ajuste (a={coef_ajustado:.3f})')
    plt.plot(x, 2 * x, 'g--', label='Reta original')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exemplo de Ajuste Individual')
    plt.legend()
    plt.grid(True)
    plt.show()
