
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID OP_DIFDE OP_DIV OP_DOBLEIGUAL OP_IGUAL OP_MAS OP_MAYOROIGUAL OP_MAYORQUE OP_MENOROIGUAL OP_MENORQUE OP_MENOS OP_MULT OP_RESID PR_black PR_blue PR_bool PR_circle PR_color PR_draw PR_else PR_end PR_false PR_flot PR_function PR_green PR_home PR_if PR_interseccion PR_kameBack PR_kameForw PR_kameRot PR_loop PR_main PR_negacion PR_num PR_orange PR_program PR_red PR_return PR_size PR_square PR_true PR_union PR_var PR_violet PR_void PR_white PR_yellow TO_COMA TO_CORABRE TO_CORCIERRA TO_DIGIT TO_DOSPTOS TO_FLOT TO_LLAABRE TO_LLACIERRA TO_NUM TO_PARABRE TO_PARCIERRA TO_UWUprog : PR_program TO_LLAABRE declare mainBlock TO_LLACIERRAval : TO_NUM\n\t\t\t| TO_FLOT\n\t\t\t| PR_true\n\t\t\t| PR_false\n\t\t\t| IDdeclare : decVar decFunc decVar : var decVar \n\t\t\t\t| empty decFunc : func decFunc \n\t\t\t\t| emptyvar : PR_var tipo ID arrayCreatearrayCreate : TO_CORABRE TO_NUM TO_CORCIERRA \n\t\t\t\t   | TO_CORABRE TO_NUM TO_CORCIERRA TO_CORABRE TO_NUM TO_CORCIERRA \n\t\t\t\t   | emptyarrayIndex : TO_CORABRE exp TO_CORCIERRA \n\t\t\t\t  | TO_CORABRE exp TO_CORCIERRA TO_CORABRE exp TO_CORCIERRA \n\t\t\t\t  | emptytipo : PR_num \n\t\t\t| PR_flot\n\t\t\t| PR_bool assign : assignTo OP_IGUAL megaExpassignTo : ID arrayIndex\n\t\t\t\t| PR_kameForw\n\t\t\t\t| PR_kameBack\n\t\t\t\t| PR_kameRotfunc : func1 func2func1 : func11 func12func11 : PR_function decideType ID TO_PARABREfunc12 : params TO_PARCIERRA TO_LLAABREfunc2 : decVar bloque TO_LLACIERRAdecideType : tipo \n\t\t\t\t  | PR_voidparams : tipo ID moreParams\n\t\t\t  | emptymoreParams : TO_COMA tipo ID moreParams \n\t\t\t  | emptymainBlock : mainBlock1 bloque TO_LLACIERRAmainBlock1 : PR_main TO_LLAABREopLogico : PR_interseccion \n\t\t\t\t| PR_unionloop : loop1 loop2 loop3loop1 : PR_looploop2 : TO_PARABRE exp TO_PARCIERRAloop3 : TO_LLAABRE bloque TO_LLACIERRAopRelacional : OP_DOBLEIGUAL \n\t\t\t\t\t\t| OP_DIFDE \n\t\t\t\t\t\t| OP_MENORQUE \n\t\t\t\t\t\t| OP_MENOROIGUAL \n\t\t\t\t\t\t| OP_MAYORQUE \n\t\t\t\t\t\t| OP_MAYOROIGUALbloque : estructura bloque \n\t\t\t  | TO_UWUestructura : assign \n\t\t\t\t  | loop \n\t\t\t\t  | comparacion\n\t\t\t\t  | return \n\t\t\t\t  | funcCall \n\t\t\t\t  | decVarfuncCall : funcCall1 funcCall2\n\t\t\t\t| PR_draw TO_PARABRE megaExp TO_PARCIERRA \n\t\t\t\t| PR_circle TO_PARABRE exp TO_PARCIERRA \n\t\t\t\t| PR_square TO_PARABRE exp TO_PARCIERRA \n\t\t\t\t| PR_size TO_PARABRE exp TO_PARCIERRA \n\t\t\t\t| PR_color TO_PARABRE colorChoice TO_PARCIERRA funcCall1 : ID TO_PARABREfuncCall2 : paramVals TO_PARCIERRAbool : PR_true \n\t\t\t| PR_falsecolorChoice : PR_red \n\t\t\t\t   | PR_green\n\t\t\t\t   | PR_blue \n\t\t\t\t   | PR_violet \n\t\t\t\t   | PR_orange \n\t\t\t\t   | PR_yellow \n\t\t\t\t   | PR_white \n\t\t\t\t   | PR_blackparamVals : unParam moreParamVals \n\t\t\t\t | emptymoreParamVals : TO_COMA unParam moreParamVals \n\t\t\t\t \t | emptyunParam : ID TO_DOSPTOS  megaExpreturn : PR_return megaExpcomparacion : compara1 compara2compara1 : PR_if TO_PARABRE megaExp TO_PARCIERRA TO_LLAABREcompara2 : bloque TO_LLACIERRA maybeElsemaybeElse : checkElse doElse \n\t\t\t\t | emptycheckElse : PR_else TO_LLAABREdoElse : bloque TO_LLACIERRAmegaExp : maybeNot superExp anotherMegamaybeNot : PR_negacion \n\t\t\t\t| emptyanotherMega : opLogico megaExp \n\t\t\t\t   | emptysuperExp : exp maybeRelmaybeRel : opRelacional exp \n\t\t\t\t| emptyexp : term anotherExpanotherExp : OP_MAS exp \n\t\t\t\t  | OP_MENOS exp \n\t\t\t\t  | emptyterm : fact anotherTermanotherTerm : OP_MULT term \n\t\t\t\t   | OP_DIV term\n\t\t\t\t   | OP_RESID term\n\t\t\t\t   | emptyfact : TO_PARABRE megaExp TO_PARCIERRA \n\t\t\t| ID arrayIndex \n\t\t\t| valempty :'
    
_lr_action_items = {'PR_function':([3,4,6,8,12,19,23,33,66,67,94,138,200,],[-111,10,-111,-9,10,-8,-27,-111,-12,-15,-31,-13,-14,]),'PR_union':([84,112,113,114,115,116,117,120,121,123,124,142,144,147,148,152,160,167,170,181,182,183,184,185,186,188,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,156,-111,-99,-102,-109,-103,-107,-96,-98,-16,-100,-101,-108,-106,-104,-105,-97,-17,]),'PR_draw':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,37,37,-28,-111,-59,37,-57,-56,-58,37,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,37,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,37,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_else':([136,],[175,]),'PR_kameRot':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,43,43,-28,-111,-59,43,-57,-56,-58,43,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,43,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,43,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_true':([45,68,69,72,73,75,77,78,79,81,85,86,119,135,141,143,149,150,151,154,155,156,159,161,162,163,164,165,166,190,],[-111,-111,-111,115,115,115,-92,-93,115,115,115,-111,-111,-111,115,115,115,115,115,-111,-40,-41,-47,-49,-51,115,-46,-50,-48,115,]),'TO_FLOT':([45,68,69,72,73,75,77,78,79,81,85,86,119,135,141,143,149,150,151,154,155,156,159,161,162,163,164,165,166,190,],[-111,-111,-111,116,116,116,-92,-93,116,116,116,-111,-111,-111,116,116,116,116,116,-111,-40,-41,-47,-49,-51,116,-46,-50,-48,116,]),'PR_interseccion':([84,112,113,114,115,116,117,120,121,123,124,142,144,147,148,152,160,167,170,181,182,183,184,185,186,188,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,155,-111,-99,-102,-109,-103,-107,-96,-98,-16,-100,-101,-108,-106,-104,-105,-97,-17,]),'TO_UWU':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,36,36,-28,-111,-59,36,-57,-56,-58,36,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,36,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,36,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_var':([3,6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[5,5,-9,5,-8,5,5,-28,-111,-59,5,-57,-56,-58,5,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,5,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,5,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'OP_DOBLEIGUAL':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,164,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'TO_LLAABRE':([1,22,64,80,168,172,175,],[3,60,99,127,-44,191,193,]),'OP_MENOS':([84,112,113,114,115,116,117,120,121,147,148,152,170,183,184,185,186,201,],[-18,143,-5,-110,-4,-3,-2,-6,-111,-109,-103,-107,-16,-108,-106,-104,-105,-17,]),'PR_void':([10,],[25,]),'PR_square':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,52,52,-28,-111,-59,52,-57,-56,-58,52,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,52,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,52,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_color':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,40,40,-28,-111,-59,40,-57,-56,-58,40,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,40,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,40,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'OP_DIV':([84,113,114,115,116,117,120,121,147,170,183,201,],[-18,-5,-110,-4,-3,-2,-6,151,-109,-16,-108,-17,]),'PR_circle':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,41,41,-28,-111,-59,41,-57,-56,-58,41,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,41,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,41,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_size':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,42,42,-28,-111,-59,42,-57,-56,-58,42,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,42,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,42,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'OP_IGUAL':([35,43,47,48,51,82,84,170,201,],[68,-26,-24,-25,-111,-23,-18,-16,-17,]),'TO_CORCIERRA':([84,100,112,113,114,115,116,117,120,121,128,142,144,147,148,152,170,181,182,183,184,185,186,197,198,201,],[-18,138,-111,-5,-110,-4,-3,-2,-6,-111,170,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,200,201,-17,]),'TO_COMA':([63,84,88,112,113,114,115,116,117,120,121,123,124,142,144,147,148,152,157,158,160,167,170,173,174,179,181,182,183,184,185,186,187,188,201,],[96,-18,132,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-99,-102,-109,-103,-107,-91,-95,-96,-98,-16,132,-82,96,-100,-101,-108,-106,-104,-105,-94,-97,-17,]),'OP_DIFDE':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,159,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'OP_MENOROIGUAL':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,161,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'OP_MAYOROIGUAL':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,162,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'PR_false':([45,68,69,72,73,75,77,78,79,81,85,86,119,135,141,143,149,150,151,154,155,156,159,161,162,163,164,165,166,190,],[-111,-111,-111,113,113,113,-92,-93,113,113,113,-111,-111,-111,113,113,113,113,113,-111,-40,-41,-47,-49,-51,113,-46,-50,-48,113,]),'TO_PARABRE':([37,40,41,42,45,50,51,52,53,56,62,68,69,72,73,75,77,78,79,81,85,86,119,135,141,143,149,150,151,154,155,156,159,161,162,163,164,165,166,190,],[69,71,72,73,-111,79,83,85,86,-43,95,-111,-111,119,119,119,-92,-93,119,119,119,-111,-111,-111,119,119,119,119,119,-111,-40,-41,-47,-49,-51,119,-46,-50,-48,119,]),'PR_main':([3,4,6,7,8,12,13,14,19,23,32,33,66,67,94,138,200,],[-111,-111,-111,22,-9,-111,-7,-11,-8,-27,-10,-111,-12,-15,-31,-13,-14,]),'PR_return':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,45,45,-28,-111,-59,45,-57,-56,-58,45,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,45,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,45,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'$end':([2,34,],[0,-1,]),'OP_RESID':([84,113,114,115,116,117,120,121,147,170,183,201,],[-18,-5,-110,-4,-3,-2,-6,149,-109,-16,-108,-17,]),'PR_white':([71,],[104,]),'PR_num':([5,10,11,95,96,],[15,15,15,-29,15,]),'TO_CORABRE':([33,51,120,138,170,],[65,81,81,180,190,]),'TO_NUM':([45,65,68,69,72,73,75,77,78,79,81,85,86,119,135,141,143,149,150,151,154,155,156,159,161,162,163,164,165,166,180,190,],[-111,100,-111,-111,117,117,117,-92,-93,117,117,117,-111,-111,-111,117,117,117,117,117,-111,-40,-41,-47,-49,-51,117,-46,-50,-48,197,117,]),'TO_DOSPTOS':([90,],[135,]),'OP_MAS':([84,112,113,114,115,116,117,120,121,147,148,152,170,183,184,185,186,201,],[-18,141,-5,-110,-4,-3,-2,-6,-111,-109,-103,-107,-16,-108,-106,-104,-105,-17,]),'PR_blue':([71,],[109,]),'PR_kameForw':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,47,47,-28,-111,-59,47,-57,-56,-58,47,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,47,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,47,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'PR_program':([0,],[1,]),'PR_green':([71,],[110,]),'PR_flot':([5,10,11,95,96,],[18,18,18,-29,18,]),'PR_negacion':([45,68,69,86,119,135,154,155,156,],[77,77,77,77,77,77,77,-40,-41,]),'ID':([6,8,9,15,16,17,18,19,21,24,25,26,27,28,29,33,39,44,45,46,49,54,55,57,58,59,60,66,67,68,69,72,73,75,76,77,78,79,81,83,84,85,86,87,93,99,101,112,113,114,115,116,117,119,120,121,123,124,126,127,132,134,135,136,137,138,139,140,141,142,143,144,145,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,190,191,193,195,199,200,201,],[-111,-9,-111,-19,33,-21,-20,-8,51,51,-33,-32,62,-28,63,-111,-59,51,-111,-57,-56,-58,90,51,-54,-55,-39,-12,-15,-111,-111,120,120,120,-83,-92,-93,120,120,-66,-18,120,-111,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-111,-6,-111,-111,-111,-42,51,90,-67,-111,-111,179,-13,-61,-65,120,-99,120,-102,-62,-109,-103,120,120,120,-107,-64,-111,-40,-41,-91,-95,-47,-96,-49,-51,120,-46,-50,-48,-98,-16,-63,-86,51,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,120,-85,-89,-87,-90,-14,-17,]),'OP_MULT':([84,113,114,115,116,117,120,121,147,170,183,201,],[-18,-5,-110,-4,-3,-2,-6,150,-109,-16,-108,-17,]),'TO_LLACIERRA':([20,36,38,61,70,74,92,169,194,],[34,-53,70,94,-38,-52,136,189,199,]),'PR_orange':([71,],[103,]),'PR_if':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,53,53,-28,-111,-59,53,-57,-56,-58,53,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,53,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,53,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'OP_MAYORQUE':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,165,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'PR_black':([71,],[108,]),'PR_red':([71,],[106,]),'PR_bool':([5,10,11,95,96,],[17,17,17,-29,17,]),'PR_loop':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,56,56,-28,-111,-59,56,-57,-56,-58,56,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,56,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,56,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),'TO_PARCIERRA':([11,30,31,55,63,83,84,88,89,91,95,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,129,130,131,133,142,144,146,147,148,152,157,158,160,167,170,173,174,179,181,182,183,184,185,186,187,188,192,196,201,],[-111,64,-35,-111,-111,-66,-18,-111,134,-79,-29,-37,-34,139,-74,-76,140,-70,-73,-77,-72,-71,-75,-111,-5,-110,-4,-3,-2,145,-6,-111,153,-111,-111,168,171,172,-78,-81,-99,-102,183,-109,-103,-107,-91,-95,-96,-98,-16,-111,-82,-111,-100,-101,-108,-106,-104,-105,-94,-97,-80,-36,-17,]),'PR_violet':([71,],[107,]),'PR_yellow':([71,],[111,]),'OP_MENORQUE':([84,112,113,114,115,116,117,120,121,124,142,144,147,148,152,170,181,182,183,184,185,186,201,],[-18,-111,-5,-110,-4,-3,-2,-6,-111,166,-99,-102,-109,-103,-107,-16,-100,-101,-108,-106,-104,-105,-17,]),'PR_kameBack':([6,8,9,19,21,24,28,33,39,44,46,49,54,57,58,59,60,66,67,76,84,87,93,99,101,112,113,114,115,116,117,120,121,123,124,126,127,134,136,138,139,140,142,144,145,147,148,152,153,157,158,160,167,170,171,176,177,178,181,182,183,184,185,186,187,188,189,191,193,195,199,200,201,],[-111,-9,-111,-8,48,48,-28,-111,-59,48,-57,-56,-58,48,-54,-55,-39,-12,-15,-83,-18,-60,-84,-30,-22,-111,-5,-110,-4,-3,-2,-6,-111,-111,-111,-42,48,-67,-111,-13,-61,-65,-99,-102,-62,-109,-103,-107,-64,-91,-95,-96,-98,-16,-63,-86,48,-88,-100,-101,-108,-106,-104,-105,-94,-97,-45,-85,-89,-87,-90,-14,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'decideType':([10,],[27,]),'megaExp':([45,68,69,86,119,135,154,],[76,101,102,130,146,174,187,]),'maybeElse':([136,],[176,]),'mainBlock':([7,],[20,]),'assignTo':([21,24,44,57,127,177,],[35,35,35,35,35,35,]),'arrayIndex':([51,120,],[82,147,]),'superExp':([75,],[123,]),'mainBlock1':([7,],[21,]),'unParam':([55,132,],[88,173,]),'anotherMega':([123,],[157,]),'bloque':([21,24,44,57,127,177,],[38,61,74,92,169,194,]),'maybeNot':([45,68,69,86,119,135,154,],[75,75,75,75,75,75,75,]),'checkElse':([136,],[177,]),'func12':([11,],[28,]),'func11':([4,12,],[11,11,]),'decVar':([3,6,9,21,24,44,57,127,177,],[4,19,24,39,39,39,39,39,39,]),'tipo':([5,10,11,96,],[16,26,29,137,]),'opRelacional':([124,],[163,]),'colorChoice':([71,],[105,]),'estructura':([21,24,44,57,127,177,],[44,44,44,44,44,44,]),'params':([11,],[30,]),'var':([3,6,9,21,24,44,57,127,177,],[6,6,6,6,6,6,6,6,6,]),'paramVals':([55,],[89,]),'empty':([3,4,6,9,11,12,21,24,33,44,45,51,55,57,63,68,69,86,88,112,119,120,121,123,124,127,135,136,154,173,177,179,],[8,14,8,8,31,14,8,8,67,8,78,84,91,8,97,78,78,78,133,144,78,84,152,158,167,8,78,178,78,133,8,97,]),'func2':([9,],[23,]),'func1':([4,12,],[9,9,]),'return':([21,24,44,57,127,177,],[46,46,46,46,46,46,]),'opLogico':([123,],[154,]),'doElse':([177,],[195,]),'prog':([0,],[2,]),'func':([4,12,],[12,12,]),'compara2':([57,],[93,]),'loop3':([80,],[126,]),'loop2':([50,],[80,]),'loop1':([21,24,44,57,127,177,],[50,50,50,50,50,50,]),'decFunc':([4,12,],[13,32,]),'anotherTerm':([121,],[148,]),'term':([72,73,75,79,81,85,141,143,149,150,151,163,190,],[112,112,112,112,112,112,112,112,184,185,186,112,112,]),'val':([72,73,75,79,81,85,141,143,149,150,151,163,190,],[114,114,114,114,114,114,114,114,114,114,114,114,114,]),'funcCall':([21,24,44,57,127,177,],[54,54,54,54,54,54,]),'maybeRel':([124,],[160,]),'arrayCreate':([33,],[66,]),'declare':([3,],[7,]),'funcCall2':([55,],[87,]),'funcCall1':([21,24,44,57,127,177,],[55,55,55,55,55,55,]),'anotherExp':([112,],[142,]),'fact':([72,73,75,79,81,85,141,143,149,150,151,163,190,],[121,121,121,121,121,121,121,121,121,121,121,121,121,]),'exp':([72,73,75,79,81,85,141,143,163,190,],[118,122,124,125,128,129,181,182,188,198,]),'moreParams':([63,179,],[98,196,]),'comparacion':([21,24,44,57,127,177,],[49,49,49,49,49,49,]),'compara1':([21,24,44,57,127,177,],[57,57,57,57,57,57,]),'moreParamVals':([88,173,],[131,192,]),'assign':([21,24,44,57,127,177,],[58,58,58,58,58,58,]),'loop':([21,24,44,57,127,177,],[59,59,59,59,59,59,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> PR_program TO_LLAABRE declare mainBlock TO_LLACIERRA','prog',5,'p_prog','compisv2.py',248),
  ('val -> TO_NUM','val',1,'p_val','compisv2.py',254),
  ('val -> TO_FLOT','val',1,'p_val','compisv2.py',255),
  ('val -> PR_true','val',1,'p_val','compisv2.py',256),
  ('val -> PR_false','val',1,'p_val','compisv2.py',257),
  ('val -> ID','val',1,'p_val','compisv2.py',258),
  ('declare -> decVar decFunc','declare',2,'p_declare','compisv2.py',283),
  ('decVar -> var decVar','decVar',2,'p_decVar','compisv2.py',288),
  ('decVar -> empty','decVar',1,'p_decVar','compisv2.py',289),
  ('decFunc -> func decFunc','decFunc',2,'p_decFunc','compisv2.py',293),
  ('decFunc -> empty','decFunc',1,'p_decFunc','compisv2.py',294),
  ('var -> PR_var tipo ID arrayCreate','var',4,'p_var','compisv2.py',298),
  ('arrayCreate -> TO_CORABRE TO_NUM TO_CORCIERRA','arrayCreate',3,'p_arrayCreate','compisv2.py',311),
  ('arrayCreate -> TO_CORABRE TO_NUM TO_CORCIERRA TO_CORABRE TO_NUM TO_CORCIERRA','arrayCreate',6,'p_arrayCreate','compisv2.py',312),
  ('arrayCreate -> empty','arrayCreate',1,'p_arrayCreate','compisv2.py',313),
  ('arrayIndex -> TO_CORABRE exp TO_CORCIERRA','arrayIndex',3,'p_arrayIndex','compisv2.py',316),
  ('arrayIndex -> TO_CORABRE exp TO_CORCIERRA TO_CORABRE exp TO_CORCIERRA','arrayIndex',6,'p_arrayIndex','compisv2.py',317),
  ('arrayIndex -> empty','arrayIndex',1,'p_arrayIndex','compisv2.py',318),
  ('tipo -> PR_num','tipo',1,'p_tipo','compisv2.py',320),
  ('tipo -> PR_flot','tipo',1,'p_tipo','compisv2.py',321),
  ('tipo -> PR_bool','tipo',1,'p_tipo','compisv2.py',322),
  ('assign -> assignTo OP_IGUAL megaExp','assign',3,'p_assign','compisv2.py',326),
  ('assignTo -> ID arrayIndex','assignTo',2,'p_assignTo','compisv2.py',356),
  ('assignTo -> PR_kameForw','assignTo',1,'p_assignTo','compisv2.py',357),
  ('assignTo -> PR_kameBack','assignTo',1,'p_assignTo','compisv2.py',358),
  ('assignTo -> PR_kameRot','assignTo',1,'p_assignTo','compisv2.py',359),
  ('func -> func1 func2','func',2,'p_func','compisv2.py',365),
  ('func1 -> func11 func12','func1',2,'p_func1','compisv2.py',369),
  ('func11 -> PR_function decideType ID TO_PARABRE','func11',4,'p_func11','compisv2.py',373),
  ('func12 -> params TO_PARCIERRA TO_LLAABRE','func12',3,'p_func12','compisv2.py',384),
  ('func2 -> decVar bloque TO_LLACIERRA','func2',3,'p_func2','compisv2.py',387),
  ('decideType -> tipo','decideType',1,'p_decideType','compisv2.py',391),
  ('decideType -> PR_void','decideType',1,'p_decideType','compisv2.py',392),
  ('params -> tipo ID moreParams','params',3,'p_params','compisv2.py',397),
  ('params -> empty','params',1,'p_params','compisv2.py',398),
  ('moreParams -> TO_COMA tipo ID moreParams','moreParams',4,'p_moreParams','compisv2.py',404),
  ('moreParams -> empty','moreParams',1,'p_moreParams','compisv2.py',405),
  ('mainBlock -> mainBlock1 bloque TO_LLACIERRA','mainBlock',3,'p_mainBlock','compisv2.py',410),
  ('mainBlock1 -> PR_main TO_LLAABRE','mainBlock1',2,'p_mainBlock1','compisv2.py',413),
  ('opLogico -> PR_interseccion','opLogico',1,'p_opLogico','compisv2.py',420),
  ('opLogico -> PR_union','opLogico',1,'p_opLogico','compisv2.py',421),
  ('loop -> loop1 loop2 loop3','loop',3,'p_loop','compisv2.py',429),
  ('loop1 -> PR_loop','loop1',1,'p_loop1','compisv2.py',438),
  ('loop2 -> TO_PARABRE exp TO_PARCIERRA','loop2',3,'p_loop2','compisv2.py',442),
  ('loop3 -> TO_LLAABRE bloque TO_LLACIERRA','loop3',3,'p_loop3','compisv2.py',457),
  ('opRelacional -> OP_DOBLEIGUAL','opRelacional',1,'p_opRelacional','compisv2.py',460),
  ('opRelacional -> OP_DIFDE','opRelacional',1,'p_opRelacional','compisv2.py',461),
  ('opRelacional -> OP_MENORQUE','opRelacional',1,'p_opRelacional','compisv2.py',462),
  ('opRelacional -> OP_MENOROIGUAL','opRelacional',1,'p_opRelacional','compisv2.py',463),
  ('opRelacional -> OP_MAYORQUE','opRelacional',1,'p_opRelacional','compisv2.py',464),
  ('opRelacional -> OP_MAYOROIGUAL','opRelacional',1,'p_opRelacional','compisv2.py',465),
  ('bloque -> estructura bloque','bloque',2,'p_bloque','compisv2.py',472),
  ('bloque -> TO_UWU','bloque',1,'p_bloque','compisv2.py',473),
  ('estructura -> assign','estructura',1,'p_estructura','compisv2.py',476),
  ('estructura -> loop','estructura',1,'p_estructura','compisv2.py',477),
  ('estructura -> comparacion','estructura',1,'p_estructura','compisv2.py',478),
  ('estructura -> return','estructura',1,'p_estructura','compisv2.py',479),
  ('estructura -> funcCall','estructura',1,'p_estructura','compisv2.py',480),
  ('estructura -> decVar','estructura',1,'p_estructura','compisv2.py',481),
  ('funcCall -> funcCall1 funcCall2','funcCall',2,'p_funcCall','compisv2.py',485),
  ('funcCall -> PR_draw TO_PARABRE megaExp TO_PARCIERRA','funcCall',4,'p_funcCall','compisv2.py',486),
  ('funcCall -> PR_circle TO_PARABRE exp TO_PARCIERRA','funcCall',4,'p_funcCall','compisv2.py',487),
  ('funcCall -> PR_square TO_PARABRE exp TO_PARCIERRA','funcCall',4,'p_funcCall','compisv2.py',488),
  ('funcCall -> PR_size TO_PARABRE exp TO_PARCIERRA','funcCall',4,'p_funcCall','compisv2.py',489),
  ('funcCall -> PR_color TO_PARABRE colorChoice TO_PARCIERRA','funcCall',4,'p_funcCall','compisv2.py',490),
  ('funcCall1 -> ID TO_PARABRE','funcCall1',2,'p_funcCall1','compisv2.py',492),
  ('funcCall2 -> paramVals TO_PARCIERRA','funcCall2',2,'p_funcCall2','compisv2.py',503),
  ('bool -> PR_true','bool',1,'p_bool','compisv2.py',511),
  ('bool -> PR_false','bool',1,'p_bool','compisv2.py',512),
  ('colorChoice -> PR_red','colorChoice',1,'p_colorChoice','compisv2.py',515),
  ('colorChoice -> PR_green','colorChoice',1,'p_colorChoice','compisv2.py',516),
  ('colorChoice -> PR_blue','colorChoice',1,'p_colorChoice','compisv2.py',517),
  ('colorChoice -> PR_violet','colorChoice',1,'p_colorChoice','compisv2.py',518),
  ('colorChoice -> PR_orange','colorChoice',1,'p_colorChoice','compisv2.py',519),
  ('colorChoice -> PR_yellow','colorChoice',1,'p_colorChoice','compisv2.py',520),
  ('colorChoice -> PR_white','colorChoice',1,'p_colorChoice','compisv2.py',521),
  ('colorChoice -> PR_black','colorChoice',1,'p_colorChoice','compisv2.py',522),
  ('paramVals -> unParam moreParamVals','paramVals',2,'p_paramVals','compisv2.py',525),
  ('paramVals -> empty','paramVals',1,'p_paramVals','compisv2.py',526),
  ('moreParamVals -> TO_COMA unParam moreParamVals','moreParamVals',3,'p_moreParamVals','compisv2.py',529),
  ('moreParamVals -> empty','moreParamVals',1,'p_moreParamVals','compisv2.py',530),
  ('unParam -> ID TO_DOSPTOS megaExp','unParam',3,'p_unParam','compisv2.py',533),
  ('return -> PR_return megaExp','return',2,'p_return','compisv2.py',550),
  ('comparacion -> compara1 compara2','comparacion',2,'p_comparacion','compisv2.py',553),
  ('compara1 -> PR_if TO_PARABRE megaExp TO_PARCIERRA TO_LLAABRE','compara1',5,'p_compara1','compisv2.py',557),
  ('compara2 -> bloque TO_LLACIERRA maybeElse','compara2',3,'p_compara2','compisv2.py',569),
  ('maybeElse -> checkElse doElse','maybeElse',2,'p_maybeElse','compisv2.py',576),
  ('maybeElse -> empty','maybeElse',1,'p_maybeElse','compisv2.py',577),
  ('checkElse -> PR_else TO_LLAABRE','checkElse',2,'p_checkElse','compisv2.py',581),
  ('doElse -> bloque TO_LLACIERRA','doElse',2,'p_doElse','compisv2.py',590),
  ('megaExp -> maybeNot superExp anotherMega','megaExp',3,'p_megaExp','compisv2.py',593),
  ('maybeNot -> PR_negacion','maybeNot',1,'p_maybeNot','compisv2.py',625),
  ('maybeNot -> empty','maybeNot',1,'p_maybeNot','compisv2.py',626),
  ('anotherMega -> opLogico megaExp','anotherMega',2,'p_anotherMega','compisv2.py',632),
  ('anotherMega -> empty','anotherMega',1,'p_anotherMega','compisv2.py',633),
  ('superExp -> exp maybeRel','superExp',2,'p_superExp','compisv2.py',636),
  ('maybeRel -> opRelacional exp','maybeRel',2,'p_maybeRel','compisv2.py',640),
  ('maybeRel -> empty','maybeRel',1,'p_maybeRel','compisv2.py',641),
  ('exp -> term anotherExp','exp',2,'p_exp','compisv2.py',664),
  ('anotherExp -> OP_MAS exp','anotherExp',2,'p_anotherExp','compisv2.py',691),
  ('anotherExp -> OP_MENOS exp','anotherExp',2,'p_anotherExp','compisv2.py',692),
  ('anotherExp -> empty','anotherExp',1,'p_anotherExp','compisv2.py',693),
  ('term -> fact anotherTerm','term',2,'p_term','compisv2.py',699),
  ('anotherTerm -> OP_MULT term','anotherTerm',2,'p_anotherTerm','compisv2.py',722),
  ('anotherTerm -> OP_DIV term','anotherTerm',2,'p_anotherTerm','compisv2.py',723),
  ('anotherTerm -> OP_RESID term','anotherTerm',2,'p_anotherTerm','compisv2.py',724),
  ('anotherTerm -> empty','anotherTerm',1,'p_anotherTerm','compisv2.py',725),
  ('fact -> TO_PARABRE megaExp TO_PARCIERRA','fact',3,'p_fact','compisv2.py',731),
  ('fact -> ID arrayIndex','fact',2,'p_fact','compisv2.py',732),
  ('fact -> val','fact',1,'p_fact','compisv2.py',733),
  ('empty -> <empty>','empty',0,'p_empty','compisv2.py',738),
]
