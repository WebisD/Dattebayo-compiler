# Compiler
Compiler 

## GLC

**Expression** ⇐ ExpressionVariable | ConditionExpr | WhileDeclaration | PrintDeclaration ;

<br/><br/><br/>

**ExpressionVariable** ⇐ (VariableDeclaration | VariableInitialization) , ENDPOINT ;

**ConditionExpr** ⇐ IfDeclaration | IfDeclaration , ElseDeclaration;

**WhileDeclaration** ⇐ TSUKUYOMI , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

**PrintDeclaration** ⇐ SHARINGAN , LPAREN , Values , RPAREN , ENDPOINT ;

<br/><br/><br/>

**VariableDeclaration** ⇐ VariableType , IDENTIFIER ;

**VariableType** ⇐ RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE ;

**VariableInitialization** ⇐ [VariableType] , IDENTIFIER , HAKU , Values;

<br/><br/><br/>

**IfDeclaration** ⇐ NINJUTSU , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK;
Num ⇐ INT | FLOAT ;

**ElseDeclaration** ⇐ TAIJUTSU, LBRACK , Expression , RBRACK;

<br/><br/><br/>

**MultipleConditionParam** ⇐  {[ConditionParam , Operator]} , ConditionParam ;

**ConditionParam** ⇐ (Values , Comparators , Value) ;

**Comparators** ⇐ KIRIGAKURE ;

**Operator** ⇐ KUMOGAKURE , AMEGAKURE ;

<br/><br/><br/>

**Values** ⇐ Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation ;

**Num** : INT | FLOAT

**NumOperation** ⇐ (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ;

**Operation** ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;

**StrOperation** ⇐ STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;

