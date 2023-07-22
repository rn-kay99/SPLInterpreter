# Generated from SPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SPLParser import SPLParser
else:
    from SPLParser import SPLParser

# This class defines a complete generic visitor for a parse tree produced by SPLParser.

class SPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SPLParser#program.
    def visitProgram(self, ctx:SPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#declaration.
    def visitDeclaration(self, ctx:SPLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#varDecl.
    def visitVarDecl(self, ctx:SPLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#statement.
    def visitStatement(self, ctx:SPLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#exprStmt.
    def visitExprStmt(self, ctx:SPLParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#ifStmt.
    def visitIfStmt(self, ctx:SPLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#printStmt.
    def visitPrintStmt(self, ctx:SPLParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#whileStmt.
    def visitWhileStmt(self, ctx:SPLParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#block.
    def visitBlock(self, ctx:SPLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#expression.
    def visitExpression(self, ctx:SPLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#assignment.
    def visitAssignment(self, ctx:SPLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#logic_or.
    def visitLogic_or(self, ctx:SPLParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#logic_and.
    def visitLogic_and(self, ctx:SPLParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#equality.
    def visitEquality(self, ctx:SPLParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#comparison.
    def visitComparison(self, ctx:SPLParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#term.
    def visitTerm(self, ctx:SPLParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#factor.
    def visitFactor(self, ctx:SPLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#unary.
    def visitUnary(self, ctx:SPLParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLParser#primary.
    def visitPrimary(self, ctx:SPLParser.PrimaryContext):
        return self.visitChildren(ctx)



del SPLParser