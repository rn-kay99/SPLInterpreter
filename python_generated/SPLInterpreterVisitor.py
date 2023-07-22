import sys
from antlr4 import *
from .SPLParser import SPLParser
from .SPLVisitor import SPLVisitor

class SPLInterpreterVisitor(SPLVisitor):
    def __init__(self):
        self.variables = {}


    # Visit a parse tree produced by SPLParser#ifStmt.
    def visitIfStmt(self, ctx:SPLParser.IfStmtContext):
        expression = self.visit(ctx.expression())
        statements = ctx.statement()

        if expression == True:
            self.visit(ctx.statement(0))
        elif expression == False:
            # else block is defined
            if ctx.getChildCount() == 7:
                self.visit(ctx.statement(1))
        else:
            raise SyntaxError("Error: if statement expects a boolean value.")
    
    # Visit a parse tree produced by SPLParser#printStmt.
    def visitPrintStmt(self, ctx:SPLParser.PrintStmtContext):
        expression = self.visit(ctx.expression())
        print(expression)

    # Visit a parse tree produced by SPLParser#whileStmt.
    def visitWhileStmt(self, ctx:SPLParser.WhileStmtContext):
        expression = self.visit(ctx.expression())

        if not isinstance(expression, bool):
            raise SyntaxError("Error: while statement expects a boolean value.")
        
        while self.visit(ctx.expression()):
            self.visit(ctx.statement())

    # Visit a parse tree produced by SPLParser#varDecl.
    def visitVarDecl(self, ctx:SPLParser.VarDeclContext):
        varName = ctx.IDENTIFIER().getText()
        
        # if varValue is not set, then set it to None
        varValue = None

        # var value is set
        if ctx.getChildCount() == 5:
            varValue = self.visit(ctx.expression())

        self.variables[varName] = varValue
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SPLParser#assignment.
    def visitAssignment(self, ctx:SPLParser.AssignmentContext):
        
        # var gets new value
        if ctx.getChildCount() > 2 and ctx.getChild(1).getText() == "=":
            varName = ctx.IDENTIFIER().getText()
            varValue = self.visit(ctx.getChild(2))
            self.variables[varName] = varValue
            
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by SPLParser#logic_or.
    def visitLogic_or(self, ctx:SPLParser.Logic_orContext):
        i = 0
        value = self.visit(ctx.logic_and(0))

        # if there is no 'or'
        if ctx.getChildCount() == 1:
            return value
        
        if not isinstance(value, bool):
            raise SyntaxError("ERROR: 'or' condition expects a bool.")
        
        if value == True:
            return True
        
        while i < ctx.getChildCount()-1:
            orOperator = ctx.getChild(i + 1).getText()
            value = self.visit(ctx.getChild(i + 2))

            if orOperator != "or":
                raise SyntaxError("ERROR: 'or' operator expected.")

            if not isinstance(value, bool):
                raise SyntaxError("ERROR: 'or' condition expects a bool.")

            if value == True:
                return True
            
            i = i + 2
        
        return False
    
    # Visit a parse tree produced by SPLParser#logic_and.
    def visitLogic_and(self, ctx:SPLParser.Logic_andContext):
        i = 0
        value = self.visit(ctx.equality(0))
        
        # if there is no 'and'
        if ctx.getChildCount() == 1:
            return value
        
        if not isinstance(value, bool):
            raise SyntaxError("ERROR: 'and' condition expects a bool.")
        
        if value == False:
            return False
        
        while i < ctx.getChildCount()-1:
            andOperator = ctx.getChild(i + 1).getText()
            value = self.visit(ctx.getChild(i + 2))

            if andOperator != "and":
                raise SyntaxError("ERROR: 'and' operator expected.")

            if not isinstance(value, bool):
                raise SyntaxError("ERROR: 'and' condition expects a bool.")
            
            if value == False:
                return False
        
            i = i + 2

        return True
    
    # Visit a parse tree produced by SPLParser#equality.
    def visitEquality(self, ctx:SPLParser.EqualityContext):
        i = 0
        equality = self.visit(ctx.comparison(0))
        result = True

        # if there is no '==' or '!='
        if ctx.getChildCount() == 1:
            return equality

        while i < ctx.getChildCount()-1:
            term1 = self.visit(ctx.getChild(i))
            operator = ctx.getChild(i + 1).getText()
            term2 = self.visit(ctx.getChild(i + 2))

            if ( not (isinstance(term1, float) and isinstance(term2, float)) and 
                 not (isinstance(term1, str) and isinstance(term2, str)) and 
                 not (isinstance(term1, bool) and isinstance(term2, bool))):
                raise SyntaxError("ERROR: Compare operator is only allowed for same datatypes.")

            if operator == "==":
                if not term1 == term2:
                    return False
            elif operator == "!=":
                if not term1 != term2:
                    return False
            
            i = i + 2
        return result
    
    # Visit a parse tree produced by SPLParser#comparison.
    def visitComparison(self, ctx:SPLParser.ComparisonContext):
        i = 0
        term = self.visit(ctx.getChild(i))
        result = True
        
        # if there is no '>', '>=', '<' or '<='
        if ctx.getChildCount() == 1 or not isinstance(term, float):
            return term

        while i < ctx.getChildCount()-1:
            term1 = self.visit(ctx.getChild(i))
            operator = ctx.getChild(i + 1).getText()
            term2 = self.visit(ctx.getChild(i + 2))

            if not isinstance(term2, float):
                raise SyntaxError("Error: Only numbers in comparison allowed.")
            
            if operator == ">":
                if not term1 > term2:
                    return False
            elif operator == ">=":
                if not term1 >= term2:
                    return False
            elif operator == "<":
                if not term1 < term2:
                    return False
            elif operator == "<=":
                if not term1 <= term2:
                    return False

            i = i + 2
        
        return result
    
    # Visit a parse tree produced by SPLParser#term.
    def visitTerm(self, ctx:SPLParser.TermContext):
        i = 0
        result = self.visit(ctx.getChild(i))

        # check if factor is a variable and is set
        if ctx.getChild(i).start.type == SPLParser.IDENTIFIER:
            varName = ctx.getChild(i).getText()
            result = self.variables[varName]
            if result == None:
                raise SyntaxError("ERROR: cannot use variable before declaration.")

        while i < ctx.getChildCount()-1:
            operator = ctx.getChild(i + 1).getText()
            factor = self.visit(ctx.getChild(i + 2))

            # check if factor is a variable
            if ctx.getChild(i + 2).start.type == SPLParser.IDENTIFIER:
                varName = ctx.getChild(i + 2).getText()
                factor = self.variables[varName]
                
                # check if factor is a number
                if not isinstance(factor, float):
                    raise SyntaxError("ERROR: Operators + and - only for numbers allowed")
            
            if operator == "+":
                result += factor
            elif operator == "-":
                result -= factor
        
            i = i + 2
        
        return result

    # Visit a parse tree produced by SPLParser#factor.
    def visitFactor(self, ctx:SPLParser.FactorContext):
        i = 0
        result = self.visit(ctx.getChild(i))

        while i < ctx.getChildCount()-1:
            operator = ctx.getChild(i + 1).getText()
            factor = self.visit(ctx.getChild(i + 2))

            # check if factor is a variable
            if ctx.getChild(i).start.type == SPLParser.IDENTIFIER:
                varName = ctx.getChild(i + 2).getText()
                factor = self.variables[varName]

                # check if factor is a number
                if not isinstance(factor, float):
                    raise SyntaxError("ERROR: Operators * and / only for numbers allowed.")
            
            if operator == "*":
                result *= factor
            elif operator == "/":
                result /= factor

            i = i + 2

        return result

    # Visit a parse tree produced by SPLParser#unary.
    def visitUnary(self, ctx:SPLParser.UnaryContext):
        if ctx.getChildCount() == 2:

            if ctx.getChild(0).getText() == "-":
                number = self.visit(ctx.getChild(1))

                # check if factor is a variable
                if ctx.getChild(1).start.type == SPLParser.IDENTIFIER:
                    number = self.variables[number]

                if not isinstance(number, float):
                    raise SyntaxError("ERROR: '-' operator only for numbers allowed.")
                return -number
            
            if ctx.getChild(0).getText() == "!":
                # NOT operator only for bool values allowed
                value = self.visit(ctx.getChild(1))

                # check if factor is a variable
                if ctx.getChild(1).start.type == SPLParser.IDENTIFIER:
                    value = self.variables[value]

                if not isinstance(value, bool):
                    raise SyntaxError("ERROR: '!' operator only for bool values allowed.")
                return not value

        return self.visitChildren(ctx)

    

    # Visit a parse tree produced by SPLParser#primary.
    def visitPrimary(self, ctx:SPLParser.PrimaryContext):
        if ctx.start.type == SPLParser.NUMBER:
            return float(ctx.getText())
        elif ctx.start.type == SPLParser.STRING:
            return str(ctx.getText()).replace('"','')
        elif ctx.start.type == SPLParser.IDENTIFIER:
            return str(ctx.getText())
        elif ctx.start.type == SPLParser.TRUE:
            return True
        elif ctx.start.type == SPLParser.FALSE:
            return False
        elif ctx.start.type == SPLParser.LPAREN:
            return self.visit(ctx.expression())
        
        return self.visitChildren(ctx)