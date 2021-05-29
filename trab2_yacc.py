import sys

import ply.yacc as yacc
import sys

from trab2_lex import tokens


#Production rules
def p_File(p): #############################################
    "File : Inic BlocoInst"
    p[0] = p[1] + p[2]

def p_Inic(p):
    "Inic : DeclVar Inic"
    p[0] = p[1]

def p_Inic_vazio(p):
    "Inic : "
    p[0] = ""

def p_DeclVar_int(p):
    "DeclVar : INT ID OpcDeclInt"
    p.parser.registos.update({p[2]: p.parser.soma})
    p.parser.tipos.update({p[2]: p[1]})
    p.parser.soma += 1
    p[0] = "PUSHI " + p[3]

def p_DeclVar_char(p):
    "DeclVar : FLOAT ID OpcDeclFloat"
    p.parser.registos.update({p[2]: p.parser.soma})
    p.parser.tipos.update({p[2]: p[1]})
    p.parser.soma += 1
    p[0] = "PUSHF " + p[3]

def p_OpcDeclInt_igual(p):
    "OpcDeclInt : IGUAL SegueIgual"
    p[0] = p[2]

def p_OpcDeclInt_pv(p):
    "OpcDeclInt : PV"
    p[0] = "0\n"

def p_OpcDeclFloat_igual(p): ##########################################333
    "OpcDeclFloat : IGUAL SegueIgual"
    p[0] = p[2]

def p_OpcDeclFloat_pv(p):
    "OpcDeclFloat : PV"
    p[0] = "0.0\n"

def p_SegueIgual_num(p):
    "SegueIgual : NUM PV"
    p[0] = p[1] + "\n"

def p_SegueIgual_real(p):
    "SegueIgual : REAL PV"
    p[0] = p[1] + "\n"





def p_BlocoInst_inst(p):
    "BlocoInst : Inst BlocoInst"
    p[0] = p[1] + p[2]

def p_BlocoInst_vazio(p): ##############################3
    "BlocoInst : "
    p[0] = ""

def p_Inst_atribuicao(p):
    "Inst : Atribuicao"
    p[0] = p[1]

def p_Inst_print(p):
    "Inst : Printf"
    p[0] = p[1]

def p_Inst_ler(p):
    "Inst : Scanf"
    p[0] = p[1]

def p_Inst_if(p):
    "Inst : If"
    p[0] = p[1]

#def p_Inst_dowhile(p):
#    "Inst : DoWhile"
#    p[0] = p[1]



def p_Atribuicao(p):
    "Atribuicao : ID IGUAL RestoAtrib"
    p[0] = p[3] + "STOREG " + str(p.parser.registos.get(p[1])) + "\n"

def p_RestoAtrib_add(p):
    "RestoAtrib : Exp ADD Exp PV"
    p[0] = p[1] + p[3] + "ADD\n"

def p_RestoAtrib_sub(p):
    "RestoAtrib : Exp SUB Exp PV"
    p[0] = p[1] + p[3] + "SUB\n"

def p_RestoAtrib_exp(p):
    "RestoAtrib : Exp PV"
    p[0] = p[1]


def p_Exp_mul(p):
    "Exp : Exp2 MUL Exp2"
    p[0] = p[1] + p[3] + "MUL\n"

def p_Exp_div(p):
    "Exp : Exp2 DIV Exp2"
    p[0] = p[1] + p[3] + "DIV\n"

def p_Exp_exp2(p):
    "Exp : Exp2"
    p[0] = p[1]

def p_Exp2_id(p):
    "Exp2 : ID"
    p[0] = "PUSHG " + str(p.parser.registos.get(p[1])) + "\n"

def p_Exp2_num(p):
    "Exp2 : NUM"
    p[0] = "PUSHI " + str(p[1]) + "\n"

def p_Exp2_real(p):
    "Exp2 : REAL"
    p[0] = "PUSHF " + str(p[1]) + "\n"

def p_Printf_print(p):
    "Printf : PRINT PE TEXTO RestoPrintf"
    p[0] = "PUSHS " + p[3] + "\n" + "WRITES" + "\n" + p[4]

def p_RestoPrintf_pd(p):
    "RestoPrintf : PD PV"
    p[0] = ""

def p_RestoPrintf_id(p):
    "RestoPrintf : VIR ID PD PV"
    if(str(p.parser.tipos.get(p[2])) == "int"):
        p[0] = "PUSHG " + str(p.parser.registos.get(p[2])) + "\n" + "WRITEI" + "\n"
    else:
        p[0] = "PUSHG " + str(p.parser.registos.get(p[2])) + "\n" + "WRITEF" + "\n"


def p_Scanf_scanf(p):
    "Scanf : SCAN PE TEXTO VIR ENDID RestoScanf"
    nome = p[5]
    if (str(p.parser.tipos.get(nome[1:])) == "int"):
        p[0] = "READ\n" + "ATOI\n" + "STOREG " + str(p.parser.registos.get(nome[1:])) + p[6]
    else:
        p[0] = "READ\n" + "ATOF\n" + "STOREG " + str(p.parser.registos.get(nome[1:])) + p[6]

def p_RestoScanf_pd(p):
    "RestoScanf : PD PV"
    p[0] = "\n"






def p_If_if(p):
    "If : IF Cond CE BlocoInstIf CD"
    parser.somaIf += 1
    p[0] = p[2] + "\nJZ ENDIF" + str(parser.somaIf) + "\n" + p[4] + "\nENDIF" + str(parser.somaIf) + ":\n"

def p_Cond_exp(p):
    "Cond : PE Conta ExpRel Conta PD"
    p[0] = p[2] + p[4] + p[3]

def p_Cond_conta(p):
    "Cond : Conta"
    p[0] = p[1]

def p_ExpRel_gt(p):
    "ExpRel : GT"
    p[0] = "SUP\n"

def p_ExpRel_ge(p):
    "ExpRel : GE"
    p[0] = "SUPEQ\n"

def p_ExpRel_lt(p):
    "ExpRel : LT"
    p[0] = "INF\n"

def p_ExpRel_le(p):
    "ExpRel : LE"
    p[0] = "INFEQ\n"

def p_ExpRel_eq(p):
    "ExpRel : EQ"
    p[0] = "EQUAL\n"

def p_ExpRel_dif(p): #########################################################
    "ExpRel : DIF"
    p[0] = "EQUAL\n" + "NOT\n"

def p_Conta_pe(p):
    "Conta : PE Conta2 PD"
    p[0] = p[2]

def p_Conta_conta2(p):
    "Conta : Conta2"
    p[0] = p[1]

def p_Conta2_sub(p):
    "Conta2 : Exp SUB Exp"
    p[0] = p[1] + p[3] + "SUB\n"

def p_Conta2_add(p):
    "Conta2 : Exp ADD Exp"
    p[0] = p[1] + p[3] + "ADD\n"

def p_Conta2_exp(p):
    "Conta2 : Exp"
    p[0] = p[1]

def p_BlocoInstIf_inst(p):
    "BlocoInstIf : InstBlocoIf BlocoInstIf"
    p[0] = p[1] + p[2]

def p_BlocoInstIf_vazio(p):
    "BlocoInstIf : "
    p[0] = ""

def p_InstBlocoIf_atr(p):
    "InstBlocoIf : Atribuicao"
    p[0] = p[1]

def p_InstBlocoIf_print(p):
    "InstBlocoIf : Printf"
    p[0] = p[1]

def p_InstBlocoIf_scan(p):
    "InstBlocoIf : Scanf"
    p[0] = p[1]

#error rule for syntax errors
def p_error(p):
    print("Syntax error in input: ", p)

#build the parser
parser = yacc.yacc()

parser.registos = {}
parser.tipos = {}
parser.soma = 0
parser.somaIf = 0
parser.somaDoWhile = 0

f = open("teste.txt", "r")

res = open("res.txt", "w")

#reading input
for linha in f:
    resultado = parser.parse(linha)
    res.write(resultado)

for elem in parser.registos:
    print(elem + ": " + str(parser.registos.get(elem)))