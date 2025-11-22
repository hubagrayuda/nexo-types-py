from typing import Sequence, TypeVar


StrT = TypeVar("StrT", bound=str)

OptStr = str | None
OptStrT = TypeVar("OptStrT", bound=OptStr)

ListOfStrs = list[str]
ListOfStrsT = TypeVar("ListOfStrsT", bound=ListOfStrs)

OptListOfStrs = ListOfStrs | None
OptListOfStrsT = TypeVar("OptListOfStrsT", bound=OptListOfStrs)

SeqOfStrs = Sequence[str]
SeqOfStrsT = TypeVar("SeqOfStrsT", bound=SeqOfStrs)

OptSeqOfStrs = SeqOfStrs | None
OptSeqOfStrsT = TypeVar("OptSeqOfStrsT", bound=OptSeqOfStrs)

# Strs tuple
DoubleStrs = tuple[str, str]
OptDoubleStrs = DoubleStrs | None
ListOfDoubleStrs = list[DoubleStrs]
OptListOfDoubleStrs = ListOfDoubleStrs | None
SeqOfDoubleStrs = Sequence[DoubleStrs]
OptSeqOfDoubleStrs = SeqOfDoubleStrs | None

TripleStrs = tuple[str, str, str]
OptTripleStrs = TripleStrs | None
ListOfTripleStrs = list[TripleStrs]
OptListOfTripleStrs = ListOfTripleStrs | None
SeqOfTripleStrs = Sequence[TripleStrs]
OptSeqOfTripleStrs = SeqOfTripleStrs | None

QuadrupleStrs = tuple[str, str, str, str]
OptQuadrupleStrs = QuadrupleStrs | None
ListOfQuadrupleStrs = list[QuadrupleStrs]
OptListOfQuadrupleStrs = ListOfQuadrupleStrs | None
SeqOfQuadrupleStrs = Sequence[QuadrupleStrs]
OptSeqOfQuadrupleStrs = SeqOfQuadrupleStrs | None

QuintupleStrs = tuple[str, str, str, str, str]
OptQuintupleStrs = QuintupleStrs | None
ListOfQuintupleStrs = list[QuintupleStrs]
OptListOfQuintupleStrs = ListOfQuintupleStrs | None
SeqOfQuintupleStrs = Sequence[QuintupleStrs]
OptSeqOfQuintupleStrs = SeqOfQuintupleStrs | None

ManyStrs = tuple[str, ...]
OptManyStrs = ManyStrs | None
ListOfManyStrs = list[ManyStrs]
OptListOfManyStrs = ListOfManyStrs | None
SeqOfManyStrs = Sequence[ManyStrs]
OptSeqOfManyStrs = SeqOfManyStrs | None

# Opt Strs tuple
DoubleOptStrs = tuple[OptStr, OptStr]
OptDoubleOptStrs = DoubleOptStrs | None
ListOfDoubleOptStrs = list[DoubleOptStrs]
OptListOfDoubleOptStrs = ListOfDoubleOptStrs | None
SeqOfDoubleOptStrs = Sequence[DoubleOptStrs]
OptSeqOfDoubleOptStrs = SeqOfDoubleOptStrs | None

TripleOptStrs = tuple[OptStr, OptStr, OptStr]
OptTripleOptStrs = TripleOptStrs | None
ListOfTripleOptStrs = list[TripleOptStrs]
OptListOfTripleOptStrs = ListOfTripleOptStrs | None
SeqOfTripleOptStrs = Sequence[TripleOptStrs]
OptSeqOfTripleOptStrs = SeqOfTripleOptStrs | None

QuadrupleOptStrs = tuple[OptStr, OptStr, OptStr, OptStr]
OptQuadrupleOptStrs = QuadrupleOptStrs | None
ListOfQuadrupleOptStrs = list[QuadrupleOptStrs]
OptListOfQuadrupleOptStrs = ListOfQuadrupleOptStrs | None
SeqOfQuadrupleOptStrs = Sequence[QuadrupleOptStrs]
OptSeqOfQuadrupleOptStrs = SeqOfQuadrupleOptStrs | None

QuintupleOptStrs = tuple[OptStr, OptStr, OptStr, OptStr, OptStr]
OptQuintupleOptStrs = QuintupleOptStrs | None
ListOfQuintupleOptStrs = list[QuintupleOptStrs]
OptListOfQuintupleOptStrs = ListOfQuintupleOptStrs | None
SeqOfQuintupleOptStrs = Sequence[QuintupleOptStrs]
OptSeqOfQuintupleOptStrs = SeqOfQuintupleOptStrs | None

ManyOptStrs = tuple[OptStr, ...]
OptManyOptStrs = ManyOptStrs | None
ListOfManyOptStrs = list[ManyOptStrs]
OptListOfManyOptStrs = ListOfManyOptStrs | None
SeqOfManyOptStrs = Sequence[ManyOptStrs]
OptSeqOfManyOptStrs = SeqOfManyOptStrs | None
