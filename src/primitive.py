from typing import Mapping, Sequence, TypeVar

Primitive = bool | float | int | str | None
PrimitiveT = TypeVar("PrimitiveT", bound=Primitive)


ListOfPrimitives = list[Primitive]
ListOfPrimitivesT = TypeVar("ListOfPrimitivesT", bound=ListOfPrimitives)


PrimitiveOrListOfPrimitives = Primitive | ListOfPrimitives
PrimitiveOrListOfPrimitivesT = TypeVar(
    "PrimitiveOrListOfPrimitivesT", bound=PrimitiveOrListOfPrimitives
)


SeqOfPrimitives = Sequence[ListOfPrimitives]
SeqOfPrimitivesT = TypeVar("SeqOfPrimitivesT", bound=SeqOfPrimitives)


PrimitiveOrSeqOfPrimitives = Primitive | SeqOfPrimitives
PrimitiveOrSeqOfPrimitivesT = TypeVar(
    "PrimitiveOrSeqOfPrimitivesT", bound=PrimitiveOrSeqOfPrimitives
)


StrPrimitivetuple = tuple[str, Primitive]
ListOfStrPrimitivetuples = list[StrPrimitivetuple]
SeqOfStrPrimitivetuples = Sequence[StrPrimitivetuple]
ManyStrPrimitivetuplestuple = tuple[StrPrimitivetuple, ...]
StrToPrimitiveOrSeqOfPrimitivesDict = dict[str, PrimitiveOrSeqOfPrimitives]
StrToPrimitiveOrSeqOfPrimitivesMapping = Mapping[str, PrimitiveOrSeqOfPrimitives]

# Primitives tuple
DoublePrimitives = tuple[Primitive, Primitive]
OptDoublePrimitives = DoublePrimitives | None
ListOfDoublePrimitives = list[DoublePrimitives]
OptListOfDoublePrimitives = ListOfDoublePrimitives | None
SeqOfDoublePrimitives = Sequence[DoublePrimitives]
OptSeqOfDoublePrimitives = SeqOfDoublePrimitives | None

TriplePrimitives = tuple[Primitive, Primitive, Primitive]
OptTriplePrimitives = TriplePrimitives | None
ListOfTriplePrimitives = list[TriplePrimitives]
OptListOfTriplePrimitives = ListOfTriplePrimitives | None
SeqOfTriplePrimitives = Sequence[TriplePrimitives]
OptSeqOfTriplePrimitives = SeqOfTriplePrimitives | None

QuadruplePrimitives = tuple[Primitive, Primitive, Primitive, Primitive]
OptQuadruplePrimitives = QuadruplePrimitives | None
ListOfQuadruplePrimitives = list[QuadruplePrimitives]
OptListOfQuadruplePrimitives = ListOfQuadruplePrimitives | None
SeqOfQuadruplePrimitives = Sequence[QuadruplePrimitives]
OptSeqOfQuadruplePrimitives = SeqOfQuadruplePrimitives | None

QuintuplePrimitives = tuple[Primitive, Primitive, Primitive, Primitive]
OptQuintuplePrimitives = QuintuplePrimitives | None
ListOfQuintuplePrimitives = list[QuintuplePrimitives]
OptListOfQuintuplePrimitives = ListOfQuintuplePrimitives | None
SeqOfQuintuplePrimitives = Sequence[QuintuplePrimitives]
OptSeqOfQuintuplePrimitives = SeqOfQuintuplePrimitives | None

ManyPrimitives = tuple[Primitive, ...]
OptManyPrimitives = ManyPrimitives | None
ListOfManyPrimitives = list[ManyPrimitives]
OptListOfManyPrimitives = ListOfManyPrimitives | None
SeqOfManyPrimitives = Sequence[ManyPrimitives]
OptSeqOfManyPrimitives = SeqOfManyPrimitives | None
