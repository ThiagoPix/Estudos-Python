# Um trem se move com velocidade constante de 144 km/h e atravessa 
# uma ponte de 90  m de comprimento em 4,5 s. Qual é o comprimento do trem?

v = (144*1000)/3600
t = 4.5
ponte = 90

d = v * t

tamanhaTrem = d - ponte
print(f'Tamanho do trem é {tamanhaTrem}m')