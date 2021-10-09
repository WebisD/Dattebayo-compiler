# Compiler
Compiler 

## GLC

Num ⇐ INT | FLOAT ;
Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;

NumOperation ⇐ (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ; 
StrOperation ⇐ STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;

VariableType ⇐ RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE ;
VariableDeclaration ⇐ VariableType , IDENTIFIER ;
Values ⇐ Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation;

VariableDefinition ⇐ [VariableType] , IDENTIFIER , HAKU , Values;

Expression ⇐ (VariableDeclaration | VariableDefinition) , ENDPOINT ;

ReturnParam ⇐ (KAMUI | KAMUI , Values) , ENDPOINT ;
FunctionParam ⇐ {[IDENTIFIER , ',']} , IDENTIFIER ;
FunctionDeclaration ⇐ CHAKRA , IDENTIFIER , '(' , [FunctionParam] , ')' , '{' (Expression | ReturnParam | Expression , ReturnParam) , '}'
FunctionCall ⇐ IDENTIFIER , '(' , [FunctionParam | Values] , ')' , ENDPOINT ;

Comparators ⇐ KUMOGAKURE , AMEGAKURE
Operator ⇐ KIRIGAKURE
ConditionParam ⇐ (Values , Comparators , Value)
MultipleConditionParam ⇐  {[ConditionParam , Comparators]} , ConditionParam
IfDeclaration ⇐ NINJUTSU , '(' , MultipleConditionParam , ')' , '{' , Expression , '}';

ElifDeclaration ⇐ GENJUTSU , '(' , MultipleConditionParam , ')' , '{' , Expression , '}' ;

ElseDeclaration ⇐ TAIJUTSU, '{' , Expression , '}';

ForDeclaration ⇐ KAGEBUNSHIN , '(' , [{VariableDefinition}] , ENDPOINT , [MultipleConditionParam] , ENDPOINT , VariableDefinition ')' , '{' , Expression , '}'

WhileDeclaration ⇐ TSUKUYOMI , '(' , MultipleConditionParam , ')' , '{' , Expression , '}' ;

PrintDeclaration ⇐ SHARINGAN , '(' , Values , ')' , ENDPOINT ;