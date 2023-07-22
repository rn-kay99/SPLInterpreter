grammar SPL;

/*
 * Parser Rules
 */

program      : declaration* EOF;
declaration  : varDecl | statement;
varDecl      : VAR IDENTIFIER (EQUAL expression)? SEMICOLON;
statement    : exprStmt | ifStmt | printStmt | whileStmt | block;
exprStmt     : expression SEMICOLON;
ifStmt       : IF LPAREN expression RPAREN statement (ELSE statement)?;
printStmt    : PRINT expression SEMICOLON;
whileStmt    : WHILE LPAREN expression RPAREN statement;
block        : LBRACE declaration* RBRACE;
expression   : assignment;
assignment   : IDENTIFIER EQUAL assignment | logic_or;

logic_or     : logic_and (OR logic_and)*;
logic_and    : equality (AND equality)*;
equality     : comparison ( (NOT_EQUAL | COMPARE) comparison)*;
comparison   : term ( (GREATER | GREATER_THEN | LESS | LESS_THEN) term)*;
term         : factor ( (MINUS | PLUS) factor)*;
factor       : unary ( (MULTIPLY | DIVIDE) unary)*;
unary        : (NOT | MINUS) unary | primary;
primary      : TRUE | FALSE | NUMBER | STRING | LPAREN expression RPAREN | IDENTIFIER;


/*
 * Lexer Rules
 */
 // keywords
 TRUE        : 'true';
 FALSE       : 'false';
 AND         : 'and';
 OR          : 'or';
 VAR         : 'var';
 PRINT       : 'print';
 IF          : 'if';
 ELSE        : 'else';
 WHILE       : 'while';

// special characters
SEMICOLON    : ';';
LPAREN       : '(';
RPAREN       : ')';
LBRACE       : '{';
RBRACE       : '}';

// operators
PLUS         : '+';
MINUS        : '-';
MULTIPLY     : '*';
DIVIDE       : '/';
NOT          : '!';
EQUAL        : '=';
COMPARE      : '==';
NOT_EQUAL    : '!=';
GREATER      : '>';
LESS         : '<';
GREATER_THEN : '>=';
LESS_THEN    : '<=';

// values
STRING       : '"' ~["]* '"';
NUMBER       : [0-9]+ ('.' [0-9]+)?;
IDENTIFIER   : [A-Za-z][A-Za-z0-9]*;

// ignore
COMMENT      : '//' ~[\r\n]* -> skip;
WS           : [ \t\r\n]+ -> skip;