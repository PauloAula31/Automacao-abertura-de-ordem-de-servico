import pyautogui
import pyperclip
import time

time.sleep(1)

pyautogui.click(1872, 290) #abrir novo atendimento

time.sleep(1)

pyautogui.click(2009, 529) #assunto

time.sleep(0.3)

pyautogui.typewrite("169", interval=0.1) #assunto

time.sleep(0.3)

pyautogui.scroll(-1000) #rolar para baixo

time.sleep(1)

#descrição do atendimento

pyautogui.click(2180, 560) 

time.sleep(2)

pyautogui.hotkey("ctrl", "a")

time.sleep(0.4)

pyautogui.press("backspace")

time.sleep(0.4)

pyautogui.typewrite("Com quem conversou:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("Telefone de contato:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("Protocolo OPA/ Native:") 
pyautogui.hotkey("Enter")
pyautogui.typewrite("Descrição do Atendimento:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("Problema Real do Cliente:")

time.sleep(0.5)

pyautogui.click(1184, 364, clicks=3) #nome do quem conversou 
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2115, 511)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

time.sleep(0.2)

pyautogui.click(1163, 441,clicks=3) #numero de quem conversou
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2101, 528)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

time.sleep(0.2)

pyautogui.doubleClick(492, 205) #protocolo
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2114, 543)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

#LOS SCRIPT

time.sleep(0.2)

pyautogui.click(2122, 560)
pyautogui.press("space")
pyautogui.typewrite("CLIENTE ENTROU EM CONTATO COM LENTIDÃO RECORRENTE, TENTEI ACESSAR O ROTEADOR MAS NÃO TIVE ACESSO REMOTO. NECESSARIO TEC AO LOCAL.")

pyautogui.scroll(-500)

time.sleep(0.4)

pyautogui.click(2141, 578)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.typewrite("LENTIDÃO, SEM ACESSO.")

time.sleep(0.8)

pyautogui.click(1794, 184) #salvar 

time.sleep(0.4)

pyautogui.click(2356, 235) #OS

time.sleep(0.4)

pyautogui.click(2461, 295) #recarregar os

time.sleep(1.5)

pyautogui.doubleClick(2290, 385)

time.sleep(2)

pyautogui.click(2195, 192) #acoes
time.sleep(0.7)
pyautogui.click(2186, 344) #finalizar

time.sleep(1)

pyautogui.click(2088, 454)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("Backspace") #apagar o script padrão

time.sleep(0.3)

#colocar script
pyautogui.typewrite("QUEM VAI ACOMPANHAR:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("TELEFONE:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("PERIODO: MANHA  (  )  TARDE    (  )  - HORÁRIO LIMITE ")
pyautogui.hotkey("Enter")
pyautogui.typewrite("LOCALIZAÇÃO OU REFERÊNCIA: ")
pyautogui.hotkey("Enter")
pyautogui.typewrite("CONVERSOU COM O CLIENTE POR : PRESENCIAL(  ) LIGAÇÃO (  )    OPA (  ) ")
pyautogui.hotkey("Enter")
pyautogui.typewrite("PROTOCOLO:")
pyautogui.hotkey("Enter")
pyautogui.typewrite("MOTIVO DA VISITA: ")

pyautogui.scroll(+500)

pyautogui.click(1184, 364, clicks=3) #nome do quem conversou 
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2154, 429)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(1163, 441,clicks=3) #numero de quem conversou
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2062, 445)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

pyautogui.scroll(-500)

pyautogui.doubleClick(492, 205) #protocolo
pyautogui.hotkey("ctrl", "c")

pyautogui.click(2080, 475)
pyautogui.press("space")
time.sleep(0.2)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(2113, 495)
pyautogui.typewrite("LENTIDÃO SEM ACESSO REMOTO") # motivo

pyautogui.click(2023, 645) #diagnostico
pyautogui.typewrite("76")

pyautogui.scroll(-500)

time.sleep(0.4)

pyautogui.click(2031, 761) #prox tarefa
pyautogui.typewrite("24")
