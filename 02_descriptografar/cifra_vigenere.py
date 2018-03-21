#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:06:12 2018

@author: matheus
"""

import time

def desc(chave, v):
  alfa = []
  for letra in range(97, 123):
    alfa.append(chr(letra))

  nf = []
  cont = 0
  for i in range(len(v)):
    nf.append([])
    for j in range(len(v[i])):
      if cont == len(chave):
        cont = 0

      if v[i][j] != "," and v[i][j] != " " and v[i][j] != "!" and v[i][j] != "?": 
        if (alfa.index(v[i][j]) - alfa.index(chave[cont])) < 0:
          valor = alfa.index(v[i][j]) - alfa.index(chave[cont])
          pos = (26 + valor)
          cont += 1
          nf[i].append(alfa[pos])
        else:
          pos = (alfa.index(v[i][j]) - alfa.index(chave[cont]))
          cont += 1
          nf[i].append(alfa[pos])

  for l in range(len(nf)):
    if "".join(nf[l]) == "amor":
      print
      print ("Achei")
      print (nf)
      return True

def quebra_senha(v):
    #achou = False
    key = ['0', '0', '0', '0', '0', '0', '0', '0']
    for a in range(97, 123):
        #if achou == True:
            #break
        if chr(a) not in key[0]:
            key[0] = chr(a)

        for b in range(97, 123):
            #if achou == True:
                #break
            if chr(b) not in key[1]:
                key[1] = chr(b)

            for c in range(97,123):
                #if achou == True:
                    #break
                if chr(c) not in key[2]:
                    key[2] = chr(c)

                for d in range(97,123):
                    #if achou == True:
                        #break
                    if chr(d) not in key[3]:
                        key[3] = chr(d)

                    for e in range(97,123):
                        #if achou == True:
                            #break
                        if chr(e) not in key[4]:
                            key[4] = chr(e)

                        for f in range(97,123):
                            #if achou == True:
                                #break
                            if chr(f) not in key[5]:
                                key[5] = chr(f)

                            for g in range(97,123):
                                #if achou == True:
                                    #break
                                if chr(g) not in key[6]:
                                    key[6] = chr(g)

                                for h in range(97,123):
                                    #if achou == True:
                                        #break
                                    if chr(h) not in key[7]:
                                        key[7] = chr(h)
                                    #print ("".join(key))

                                    if desc("".join(key), v):
                                        print ("A senha é: ")
                                        print ("".join(key))
                                        #achou = True
                                        #break

inicio = time.time()
fim = time.time()

msg = "mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy"
#msg = "bost cptu"
v = msg.split(" ")
quebra_senha(v)

print(fim - inicio)
#9.2909579277

