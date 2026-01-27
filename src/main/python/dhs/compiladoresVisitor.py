# Generated from /home/andres/Documents/DHS/DHSBidoneFiesen/DHS/src/main/python/dhs/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#puntoYComa.
    def visitPuntoYComa(self, ctx:compiladoresParser.PuntoYComaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iwhile.
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if.
    def visitIf(self, ctx:compiladoresParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#else.
    def visitElse(self, ctx:compiladoresParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opal.
    def visitOpal(self, ctx:compiladoresParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oplo.
    def visitOplo(self, ctx:compiladoresParser.OploContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#or.
    def visitOr(self, ctx:compiladoresParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#and.
    def visitAnd(self, ctx:compiladoresParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#a.
    def visitA(self, ctx:compiladoresParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cmp.
    def visitCmp(self, ctx:compiladoresParser.CmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#c.
    def visitC(self, ctx:compiladoresParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#e.
    def visitE(self, ctx:compiladoresParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#t.
    def visitT(self, ctx:compiladoresParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifor.
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#paramFor.
    def visitParamFor(self, ctx:compiladoresParser.ParamForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#init.
    def visitInit(self, ctx:compiladoresParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#char.
    def visitChar(self, ctx:compiladoresParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#cond.
    def visitCond(self, ctx:compiladoresParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#condicionales.
    def visitCondicionales(self, ctx:compiladoresParser.CondicionalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iter.
    def visitIter(self, ctx:compiladoresParser.IterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#proto.
    def visitProto(self, ctx:compiladoresParser.ProtoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#func.
    def visitFunc(self, ctx:compiladoresParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#var_func.
    def visitVar_func(self, ctx:compiladoresParser.Var_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#callFunc.
    def visitCallFunc(self, ctx:compiladoresParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#var.
    def visitVar(self, ctx:compiladoresParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#incremento.
    def visitIncremento(self, ctx:compiladoresParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#decremento.
    def visitDecremento(self, ctx:compiladoresParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#return.
    def visitReturn(self, ctx:compiladoresParser.ReturnContext):
        return self.visitChildren(ctx)



del compiladoresParser