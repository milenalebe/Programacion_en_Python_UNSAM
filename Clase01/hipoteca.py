pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
while saldo > 0:
    mes+=1
    # verifico el pago segun el mes y excepcion
    if(mes == pago_extra_mes_comienzo):
        pago_mensual += pago_extra
    if(mes == pago_extra_mes_fin):
        pago_mensual -= pago_extra
    if(saldo * (1+tasa/12) - pago_mensual<0):
        pago_mensual = saldo
        total_pagado += pago_mensual
        saldo = 0
    else:
         saldo = saldo * (1+tasa/12) - pago_mensual    
    total_pagado = total_pagado + pago_mensual
    print(f'mes: {mes} \t pagado: {pago_mensual} \t total: {round(total_pagado, 2)} \t restante: {round(saldo)}')


print(f'Total pagado: {round(total_pagado, 2)} en {mes} meses')