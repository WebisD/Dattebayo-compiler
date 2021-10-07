# Compiler
Compiler 

## GLC

Num ⇐ INT | FLOAT ;
Operation ⇐ FUUMASHURIKEN | KUNAI | SHURIKEN | KATANA ;

NumOperation ⇐ Num , Operation , Num , [{Operation , Num}] ;
StrOperation ⇐ STRING , FUUMASHURIKEN , STRING , [{FUUMASHURIKEN , STRING}] ;

VariableType ⇐ RASENGAN | RAIKIRI | ZETSU | KUCHIYOSE ;

VariableDeclaration ⇐ Variable , IDENTIFIER , ENDPOINT ;

VariableDefinition ⇐ IDENTIFIER HAKU 