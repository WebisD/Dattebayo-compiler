# Compiler
Compiler 

## GLC

Num ⇐ INT | FLOAT ;

Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;

Values ⇐ Num | STRING | BOOLEAN | IDENTIFIER | NumOperation | StrOperation ;

VariableType ⇐ RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE ;




VariableDeclaration ⇐ VariableType , IDENTIFIER ;

VariableDefinition ⇐ [VariableType] , IDENTIFIER , HAKU , Values;

ExpressionVariable ⇐ (VariableDeclaration | VariableDefinition) , ENDPOINT ;



Operator ⇐ KUMOGAKURE , AMEGAKURE ;

Comparators ⇐ KIRIGAKURE ;



NumOperation ⇐ (Num | IDENTIFIER) , Operation , (Num | IDENTIFIER) , [{Operation , (Num | IDENTIFIER)}] ;

StrOperation ⇐ STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;


 
Expression ⇐ ExpressionVariable | ConditionExpr | ForDeclaration | WhileDeclaration | PrintDeclaration ; 



ReturnParam ⇐ (KAMUI | KAMUI , Values) , ENDPOINT ;

FunctionParam ⇐ {[IDENTIFIER , ',']} , IDENTIFIER ;

FunctionDeclaration ⇐ CHAKRA , IDENTIFIER , LPAREN , [FunctionParam] , RPAREN , LBRACK , (Expression | ReturnParam | Expression , ReturnParam) , RBRACK

FunctionCall ⇐ IDENTIFIER , LPAREN , [FunctionParam | Values] , RPAREN , ENDPOINT ;



ConditionParam ⇐ (Values , Comparators , Value) ;

MultipleConditionParam ⇐  {[ConditionParam , Operator]} , ConditionParam ;

IfDeclaration ⇐ NINJUTSU , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK;

ElifDeclaration ⇐ GENJUTSU , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

ElseDeclaration ⇐ TAIJUTSU, LBRACK , Expression , RBRACK;

ForDeclaration ⇐ KAGEBUNSHIN , LPAREN , [{VariableDefinition}] , ENDPOINT , [MultipleConditionParam] , ENDPOINT , VariableDefinition RPAREN , LBRACK , Expression , RBRACK

WhileDeclaration ⇐ TSUKUYOMI , LPAREN , MultipleConditionParam , RPAREN , LBRACK , Expression , RBRACK ;

PrintDeclaration ⇐ SHARINGAN , LPAREN , Values , RPAREN , ENDPOINT ;



ConditionExpr ⇐ IfDeclaration | IfDeclaration , {ElifDeclaration} | IfDeclaration , {ElifDeclaration} , ElseDeclaration | IfDeclaration , ElseDeclaration;


