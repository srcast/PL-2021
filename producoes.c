

p1:	File 	   -> Inic BlocoInst

p2:	Inic 	   -> DeclVar Inic
p3:		   		| E
p4:	DeclVar    -> INT ID OpcDeclInt
p5:				| FLOAT ID OpcDeclFloat
p6:	OpcDeclInt  -> IGUAL SegueIgual
p7:				| PV	
p8:	OpcDeclFloat  -> IGUAL SegueIgual
p9:				| PV		
p10:SegueIgual -> NUM PV
p11:			| REAL PV



p12: BlocoInst -> Inst BlocoInst
P13:			| E
p14: Inst -> Atribuicao
p15:		| Printf
p16:		| Scanf
p17:		| If
p18:		| DoWhile



---------------------------------------------------------------
p19: Atribuicao -> ID IGUAL RestoAtri
p20: RestoAtri -> ID Operacao 
p21:			| NUM Operacao
P22:			| REAL Operacao

p23:Operacao -> ADD RestoAtri
p24:			|SUB RestoAtri
p25:			|MUL RestoAtri
p26:			|DIV RestoAtri
P27:			|PV
----------------------------------------------------------------


p19: Atribuicao -> ID IGUAL RestoAtri PV
p20:			| Exp SUB Exp PV
P21:			| Exp PV

p23:Exp -> Exp2 MUL Exp2
p24:	|Exp2 DIV Exp2
p25:	|Exp2

p26: Exp2 -> ID
p27:		|NUM
p28:		|REAL



----------------------------------------------------------------

P28: Printf 	 -> PRINT PE TEXTO RestoPrintf
p29: RestoPrintf -> PD PV
p30:			| VIR ID RestoPrintf
----------------------------------------------------------------

P28: Printf 	 -> PRINT PE TEXTO RestoPrintf
p29: RestoPrintf -> PD PV
p30:			| VIR ID PD PV

p31: Scanf		-> SCAN PE TEXTO VIR ENDID RestoScanf
p32: RestoScanf ->  PD PV












p34: If -> IF PE Cond PD CE BlocoInstIf CD
p35: Cond  -> Cond OR Cond2
p36:       | Cond2
p37: Cond2 -> Cond3 AND Cond3 
p38:	   | Cond3
p39: Cond3 -> NOT Cond
p40:	   | ExpRel
p42: ExpRel -> Exp RestoExpRel
p43: RestoExpRel ->   GT Exp       '>'
p44: 				| GE Exp       '>='
p45:				| LT Exp       '<'
p46: 				| LE Exp       '<='
p47:				| EQ Exp       '=='
p48:				| DIF Exp      '!='

p49: BlocoInstIf -> Inst BlocoInstIf
p50: 				| E


p51: DoWhile -> DO CE BlocoDoWhile CD WHILE PE Cond PD PV
p52:BlocoDoWhile -> Inst BlocoDoWhile
p53:				| E





