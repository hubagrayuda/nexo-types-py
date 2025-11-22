from typing import Any, Sequence

ListOfAny = list[Any]
OptListOfAny = ListOfAny | None
SeqOfAny = Sequence[Any]
OptSeqOfAny = SeqOfAny | None

# Any tuple
DoubleAny = tuple[Any, Any]
OptDoubleAny = DoubleAny | None
ListOfDoubleAny = list[DoubleAny]
OptListOfDoubleAny = ListOfDoubleAny | None
SeqOfDoubleAny = Sequence[DoubleAny]
OptSeqOfDoubleAny = SeqOfDoubleAny | None

TripleAny = tuple[Any, Any, Any]
OptTripleAny = TripleAny | None
ListOfTripleAny = list[TripleAny]
OptListOfTripleAny = ListOfTripleAny | None
SeqOfTripleAny = Sequence[TripleAny]
OptSeqOfTripleAny = SeqOfTripleAny | None

QuadrupleAny = tuple[Any, Any, Any, Any]
OptQuadrupleAny = QuadrupleAny | None
ListOfQuadrupleAny = list[QuadrupleAny]
OptListOfQuadrupleAny = ListOfQuadrupleAny | None
SeqOfQuadrupleAny = Sequence[QuadrupleAny]
OptSeqOfQuadrupleAny = SeqOfQuadrupleAny | None

QuintupleAny = tuple[Any, Any, Any, Any, Any]
OptQuintupleAny = QuintupleAny | None
ListOfQuintupleAny = list[QuintupleAny]
OptListOfQuintupleAny = ListOfQuintupleAny | None
SeqOfQuintupleAny = Sequence[QuintupleAny]
OptSeqOfQuintupleAny = SeqOfQuintupleAny | None

ManyAny = tuple[Any, ...]
OptManyAny = ManyAny | None
ListOfManyAny = list[ManyAny]
OptListOfManyAny = ListOfManyAny | None
SeqOfManyAny = Sequence[ManyAny]
OptSeqOfManyAny = SeqOfManyAny | None
