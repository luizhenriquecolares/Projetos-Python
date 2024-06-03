
# ### 1- Imposto a pagar no Lucro Presumido
# 
# - 5% sobre faturamento de ISS (mensal)
# - 0,65% de PIS sobre faturamento, (mensal)
# - 3% de COFINS sobre faturmaneto, (mensal)
# - 4.8% de IR (trimestral)
# - 10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
# - CSLL: 2,88% sobre faturamento (trimestral)

# %%
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# você precisa inserir no sistema um dicionário no formato:

# resultado = {
#     'mes': (faturamento, imposto_mensal, imposto_trimestral),
# }
def transformar_numero(num):
    num = num.replace('R$', '')
    num = num.strip()
    num = num.replace('.','')
    num = num.replace(',', '.')
    num = float(num)
    return num

def calcular_imposto_mensal(valor):
    iss = valor * 0.05
    pis = valor * 0.0065
    cofins = valor *  0.03
    imposto_mensal = iss + pis + cofins
    return imposto_mensal
    
def calcular_imposto_trimestral(valor):
    ir =  valor * 0.048
    csll = valor * 0.0288
    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1
    else:
        ir_adicional = 0
    imposto_trimestral = ir + csll + ir_adicional
    return imposto_trimestral

faturamentoo = {}
for mes in faturamento:
    valor1 = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor1)
    imposto_trimestral = calcular_imposto_trimestral(valor1)
    faturamentoo[mes] = (valor1, imposto_mensal,imposto_trimestral)
    print(faturamentoo[mes])
    
    # print(valor)


    

#

