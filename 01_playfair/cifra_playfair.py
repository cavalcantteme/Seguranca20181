#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 00:23:22 2018

@author: matheus
"""

def validar_key(key):
  for letra in key:
    if letra == "K":
      return False
    else:
      return True

def monta_matriz(key):
  letras = []

  for letra in key:
    if letra not in letras:
      letras.append(letra)

  for i in range(65, 91):
    if i != 75 and chr(i) not in letras:
      letras.append(chr(i))

  montada = []
  montada.append(letras[0:5])
  montada.append(letras[5:10])
  montada.append(letras[10:15])
  montada.append(letras[15:20])
  montada.append(letras[20:25])
  return montada

def cifrar_msg(msg):
  v = []
  for i in msg:
    if i != " ":
      v.append(i.upper())

################formar os bigramas respeitando a regra de repetição de letras #######
  i = 0
  while i < len(v) and i + 1 <= len(v) -1:
    if v[i] == v[i+1]:
      if v[i] != "X":
        v.insert(i+1, "X")
      else:
        v.insert(i+1, "Z")
    i+=1

    if len(v) % 2 != 0:
      if v[len(v) -1] != "X":
        v.append("X")
      else:
        v.append("Z")
#####################################################################################
####################### colocar de duas em duas no bi ###############################
  bi = []
  for i in range(0, len(v), 2):
    bi.append(v[i:i+2])

  for el in range(len(montada)):
    print ""
    for i in range(len(montada[el])):
      print montada[el][i],
  print ""

#####################################################################################
########## pegar as coordenadas de cada letra #####################
  pos = []
  for l in range(len(bi)):
    pos.append([])
    for c in range(len(bi[l])):
      for lin in range(len(montada)):
        for col in range(len(montada[lin])):
          if bi[l][c] == montada[lin][col]:
            pos[l].append(lin)
            pos[l].append(col)
####################################################################
  cifrado = []
  for i in range(len(pos)):
    if pos[i][0] != pos[i][2] and pos[i][1] != pos[i][3]:
      #print "estão em colunas e linhas diferentes"
      print montada[pos[i][0]][pos[i][3]] + montada[pos[i][2]][pos[i][1]],
      cifrado.append(montada[pos[i][0]][pos[i][3]])
      cifrado.append(montada[pos[i][2]][pos[i][1]])
    elif pos[i][0] == pos[i][2]:
      #print "estão nas mesma linha"
      if pos[i][1] == 4:
        print montada[pos[i][0]][0] + montada[pos[i][2]][pos[i][3]+1],
        cifrado.append(montada[pos[i][0]][0])
        cifrado.append(montada[pos[i][2]][pos[i][3]+1])
      elif pos[i][3] == 4:
        print montada[pos[i][0]][pos[i][1]+1] + montada[pos[i][2]][pos[i][0]],
        cifrado.append(montada[pos[i][0]][pos[i][1]+1])
        cifrado.append(montada[pos[i][2]][pos[i][0]])
      else:
        print montada[pos[i][0]][pos[i][1]+1] + montada[pos[i][2]][pos[i][3]+1],
        cifrado.append(montada[pos[i][0]][pos[i][1]+1])
        cifrado.append(montada[pos[i][2]][pos[i][3]+1])
    elif pos[i][1] == pos[i][3]:
      #print "estão nas mesma coluna"
      if pos[i][0] == 4:
        print montada[0][pos[i][1]] + montada[pos[i][2]+1][pos[i][3]],
        cifrado.append(montada[0][pos[i][1]])
        cifrado.append(montada[pos[i][2]+1][pos[i][3]])
      elif pos[i][2] == 4:
        print montada[pos[i][0]+1][pos[i][1]] + montada[pos[i][0]][pos[i][3]],
        cifrado.append(montada[pos[i][0]+1][pos[i][1]])
        cifrado.append(montada[pos[i][0]][pos[i][3]])
      else:
        print montada[pos[i][0]+1][pos[i][1]] + montada[pos[i][2]+1][pos[i][3]],
        cifrado.append(montada[pos[i][0]+1][pos[i][1]]) 
        cifrado.append(montada[pos[i][2]+1][pos[i][3]])
  return cifrado

def decifrar_msg(msg):
  v = []
  for i in msg:
    if i != " ":
      v.append(i.upper())

####################### colocar de duas em duas no bi ###############################
  bi = []
  for i in range(0, len(v), 2):
    bi.append(v[i:i+2])

  for el in range(len(montada)):
    print ""
    for i in range(len(montada[el])):
      print montada[el][i],
  print ""

########## pegar as coordenadas de cada letra #####################
  pos = []
  for l in range(len(bi)):
    pos.append([])
    for c in range(len(bi[l])):
      for lin in range(len(montada)):
        for col in range(len(montada[lin])):
          if bi[l][c] == montada[lin][col]:
            pos[l].append(lin)
            pos[l].append(col)
####################################################################
  cifrado = []
  for i in range(len(pos)):
    if pos[i][0] != pos[i][2] and pos[i][1] != pos[i][3]:
      #print "estão em colunas e linhas diferentes"
      print montada[pos[i][0]][pos[i][3]] + montada[pos[i][2]][pos[i][1]],
      cifrado.append(montada[pos[i][0]][pos[i][3]])
      cifrado.append(montada[pos[i][2]][pos[i][1]])

    elif pos[i][0] == pos[i][2]:
      #print "estão nas mesma linha"
      if pos[i][1] == 0:
        print montada[pos[i][0]][4] + montada[pos[i][2]][pos[i][3]-1],
        cifrado.append(montada[pos[i][0]][4])
        cifrado.append(montada[pos[i][2]][pos[i][3]-1])
      elif pos[i][3] == 0:
        print montada[pos[i][0]][pos[i][1]-1] + montada[pos[i][2]][4],
        cifrado.append(montada[pos[i][0]][pos[i][1]-1])
        cifrado.append(montada[pos[i][2]][4])
      else:
        print montada[pos[i][0]][pos[i][1]-1] + montada[pos[i][2]][pos[i][3]-1],
        cifrado.append(montada[pos[i][0]][pos[i][1]-1])
        cifrado.append(montada[pos[i][2]][pos[i][3]-1])
    elif pos[i][1] == pos[i][3]:
      #print "estão nas mesma coluna"
      if pos[i][0] == 0:
        print montada[4][pos[i][1]] + montada[pos[i][2]-1][pos[i][3]],
        cifrado.append(montada[4][pos[i][1]])
        cifrado.append(montada[pos[i][2]-1][pos[i][3]])
      elif pos[i][2] == 0:
        print montada[pos[i][0]-1][pos[i][1]] + montada[pos[i][4]][pos[i][3]],
        cifrado.append(montada[pos[i][0]-1][pos[i][1]])
        cifrado.append(montada[pos[i][4]][pos[i][3]])
      else:
        print montada[pos[i][0]-1][pos[i][1]] + montada[pos[i][2]-1][pos[i][3]],
        cifrado.append(montada[pos[i][0]-1][pos[i][1]]) 
        cifrado.append(montada[pos[i][2]-1][pos[i][3]])
  return cifrado

#####################################################################################
######################### APENAS O QUE NÃO É FUNÇÃO ########################################
montada = []
opt = int(raw_input("Digite 1 para cifrar\nDigite 2 para decifrar\n"))
if opt == 1:
  print "Você está cifrando uma mensagem"
  key = raw_input("Insira a chave! Por favor amigo, não use palavras com a letra K: ").upper()
  msg =  raw_input("Digite a mesangem e Não use a letra K: ")

  if validar_key(key):
    montada = (monta_matriz(key))
    cifrado = cifrar_msg(msg)
    print ""

elif opt == 2:
  print "Você está decifrando uma mensagem"
  key = raw_input("Insira a chave usada para a decifragem: ").upper()
  msg =  raw_input("Digite a mesangem que está cifrada: ")

  if validar_key(msg):
    montada = monta_matriz(key)
    decifrar_msg(msg)
    print ""

else:
  print("Opção não encontrada. Tente novamente.")
