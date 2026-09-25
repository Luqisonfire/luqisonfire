#!/usr/bin/env python3
"""Conta caracteres de um prompt (stdin ou arquivo) e avisa se passar de 2.000."""
import sys

LIMITE = 2000

texto = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
texto = texto.strip("\n")
n = len(texto)
status = "OK" if n <= LIMITE else f"EXCEDEU em {n - LIMITE}"
print(f"{n} caracteres ({status})")
sys.exit(0 if n <= LIMITE else 1)
