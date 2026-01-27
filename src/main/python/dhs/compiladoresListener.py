# Generated from /home/andres/Documents/DHS/DHSBidoneFiesen/DHS/src/main/python/dhs/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#s.
    def enterS(self, ctx:compiladoresParser.SContext):
        pass

    # Exit a parse tree produced by compiladoresParser#s.
    def exitS(self, ctx:compiladoresParser.SContext):
        pass


    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#puntoYComa.
    def enterPuntoYComa(self, ctx:compiladoresParser.PuntoYComaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#puntoYComa.
    def exitPuntoYComa(self, ctx:compiladoresParser.PuntoYComaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#if.
    def enterIf(self, ctx:compiladoresParser.IfContext):
        pass

    # Exit a parse tree produced by compiladoresParser#if.
    def exitIf(self, ctx:compiladoresParser.IfContext):
        pass


    # Enter a parse tree produced by compiladoresParser#else.
    def enterElse(self, ctx:compiladoresParser.ElseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#else.
    def exitElse(self, ctx:compiladoresParser.ElseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opal.
    def enterOpal(self, ctx:compiladoresParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opal.
    def exitOpal(self, ctx:compiladoresParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oplo.
    def enterOplo(self, ctx:compiladoresParser.OploContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oplo.
    def exitOplo(self, ctx:compiladoresParser.OploContext):
        pass


    # Enter a parse tree produced by compiladoresParser#or.
    def enterOr(self, ctx:compiladoresParser.OrContext):
        pass

    # Exit a parse tree produced by compiladoresParser#or.
    def exitOr(self, ctx:compiladoresParser.OrContext):
        pass


    # Enter a parse tree produced by compiladoresParser#and.
    def enterAnd(self, ctx:compiladoresParser.AndContext):
        pass

    # Exit a parse tree produced by compiladoresParser#and.
    def exitAnd(self, ctx:compiladoresParser.AndContext):
        pass


    # Enter a parse tree produced by compiladoresParser#a.
    def enterA(self, ctx:compiladoresParser.AContext):
        pass

    # Exit a parse tree produced by compiladoresParser#a.
    def exitA(self, ctx:compiladoresParser.AContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cmp.
    def enterCmp(self, ctx:compiladoresParser.CmpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cmp.
    def exitCmp(self, ctx:compiladoresParser.CmpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#c.
    def enterC(self, ctx:compiladoresParser.CContext):
        pass

    # Exit a parse tree produced by compiladoresParser#c.
    def exitC(self, ctx:compiladoresParser.CContext):
        pass


    # Enter a parse tree produced by compiladoresParser#e.
    def enterE(self, ctx:compiladoresParser.EContext):
        pass

    # Exit a parse tree produced by compiladoresParser#e.
    def exitE(self, ctx:compiladoresParser.EContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#t.
    def enterT(self, ctx:compiladoresParser.TContext):
        pass

    # Exit a parse tree produced by compiladoresParser#t.
    def exitT(self, ctx:compiladoresParser.TContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#paramFor.
    def enterParamFor(self, ctx:compiladoresParser.ParamForContext):
        pass

    # Exit a parse tree produced by compiladoresParser#paramFor.
    def exitParamFor(self, ctx:compiladoresParser.ParamForContext):
        pass


    # Enter a parse tree produced by compiladoresParser#init.
    def enterInit(self, ctx:compiladoresParser.InitContext):
        pass

    # Exit a parse tree produced by compiladoresParser#init.
    def exitInit(self, ctx:compiladoresParser.InitContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#char.
    def enterChar(self, ctx:compiladoresParser.CharContext):
        pass

    # Exit a parse tree produced by compiladoresParser#char.
    def exitChar(self, ctx:compiladoresParser.CharContext):
        pass


    # Enter a parse tree produced by compiladoresParser#cond.
    def enterCond(self, ctx:compiladoresParser.CondContext):
        pass

    # Exit a parse tree produced by compiladoresParser#cond.
    def exitCond(self, ctx:compiladoresParser.CondContext):
        pass


    # Enter a parse tree produced by compiladoresParser#condicionales.
    def enterCondicionales(self, ctx:compiladoresParser.CondicionalesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#condicionales.
    def exitCondicionales(self, ctx:compiladoresParser.CondicionalesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iter.
    def enterIter(self, ctx:compiladoresParser.IterContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iter.
    def exitIter(self, ctx:compiladoresParser.IterContext):
        pass


    # Enter a parse tree produced by compiladoresParser#proto.
    def enterProto(self, ctx:compiladoresParser.ProtoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#proto.
    def exitProto(self, ctx:compiladoresParser.ProtoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#func.
    def enterFunc(self, ctx:compiladoresParser.FuncContext):
        pass

    # Exit a parse tree produced by compiladoresParser#func.
    def exitFunc(self, ctx:compiladoresParser.FuncContext):
        pass


    # Enter a parse tree produced by compiladoresParser#var_func.
    def enterVar_func(self, ctx:compiladoresParser.Var_funcContext):
        pass

    # Exit a parse tree produced by compiladoresParser#var_func.
    def exitVar_func(self, ctx:compiladoresParser.Var_funcContext):
        pass


    # Enter a parse tree produced by compiladoresParser#callFunc.
    def enterCallFunc(self, ctx:compiladoresParser.CallFuncContext):
        pass

    # Exit a parse tree produced by compiladoresParser#callFunc.
    def exitCallFunc(self, ctx:compiladoresParser.CallFuncContext):
        pass


    # Enter a parse tree produced by compiladoresParser#var.
    def enterVar(self, ctx:compiladoresParser.VarContext):
        pass

    # Exit a parse tree produced by compiladoresParser#var.
    def exitVar(self, ctx:compiladoresParser.VarContext):
        pass


    # Enter a parse tree produced by compiladoresParser#incremento.
    def enterIncremento(self, ctx:compiladoresParser.IncrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#incremento.
    def exitIncremento(self, ctx:compiladoresParser.IncrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#decremento.
    def enterDecremento(self, ctx:compiladoresParser.DecrementoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decremento.
    def exitDecremento(self, ctx:compiladoresParser.DecrementoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#return.
    def enterReturn(self, ctx:compiladoresParser.ReturnContext):
        pass

    # Exit a parse tree produced by compiladoresParser#return.
    def exitReturn(self, ctx:compiladoresParser.ReturnContext):
        pass



del compiladoresParser