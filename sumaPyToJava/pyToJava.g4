grammar pyToJava;
// Reglas del Lexer
DEF: 'def';
RETURN: 'return';
PRINT: 'print';
COLON: ':';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;

// Reglas del Parser

program: statement+ EOF;

statement: function| returnStatement| printStatement| expression;

function: DEF ID LPAREN parameters? RPAREN COLON block;

parameters: ID (COMMA ID)*;

block: statement+;

returnStatement: RETURN expression;

printStatement: PRINT LPAREN expression RPAREN;

expression: ID| NUMBER| functionCall | expression operator expression | LPAREN expression RPAREN;

functionCall: ID LPAREN (expression (COMMA expression)*)? RPAREN;

operator: PLUS| MINUS| MULT| DIV;

