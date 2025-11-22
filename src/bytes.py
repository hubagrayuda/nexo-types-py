from typing import Sequence, TypeVar


OptBytes = bytes | None
OptBytesT = TypeVar("OptBytesT", bound=OptBytes)

ListOfBytes = list[bytes]
ListOfBytesT = TypeVar("ListOfBytesT", bound=ListOfBytes)

OptListOfBytes = ListOfBytes | None
OptListOfBytesT = TypeVar("OptListOfBytesT", bound=OptListOfBytes)

SeqOfBytes = Sequence[bytes]
SeqOfBytesT = TypeVar("SeqOfBytesT", bound=SeqOfBytes)

OptSeqOfBytes = SeqOfBytes | None
OptSeqOfBytesT = TypeVar("OptSeqOfBytesT", bound=OptSeqOfBytes)

# Bytes tuple
DoubleBytes = tuple[bytes, bytes]
OptDoubleBytes = DoubleBytes | None
ListOfDoubleBytes = list[DoubleBytes]
OptListOfDoubleBytes = ListOfDoubleBytes | None
SeqOfDoubleBytes = Sequence[DoubleBytes]
OptSeqOfDoubleBytes = SeqOfDoubleBytes | None

TripleBytes = tuple[bytes, bytes, bytes]
OptTripleBytes = TripleBytes | None
ListOfTripleBytes = list[TripleBytes]
OptListOfTripleBytes = ListOfTripleBytes | None
SeqOfTripleBytes = Sequence[TripleBytes]
OptSeqOfTripleBytes = SeqOfTripleBytes | None

QuintupleBytes = tuple[bytes, bytes, bytes, bytes]
OptQuintupleBytes = QuintupleBytes | None
ListOfQuintupleBytes = list[QuintupleBytes]
OptListOfQuintupleBytes = ListOfQuintupleBytes | None
SeqOfQuintupleBytes = Sequence[QuintupleBytes]
OptSeqOfQuintupleBytes = SeqOfQuintupleBytes | None

QuintupleBytes = tuple[bytes, bytes, bytes, bytes, bytes]
OptQuintupleBytes = QuintupleBytes | None
ListOfQuintupleBytes = list[QuintupleBytes]
OptListOfQuintupleBytes = ListOfQuintupleBytes | None
SeqOfQuintupleBytes = Sequence[QuintupleBytes]
OptSeqOfQuintupleBytes = SeqOfQuintupleBytes | None

ManyBytes = tuple[bytes, ...]
OptManyBytes = ManyBytes | None
ListOfManyBytes = list[ManyBytes]
OptListOfManyBytes = ListOfManyBytes | None
SeqOfManyBytes = Sequence[ManyBytes]
OptSeqOfManyBytes = SeqOfManyBytes | None

# Opt Bytes tuple
DoubleOptBytes = tuple[OptBytes, OptBytes]
OptDoubleOptBytes = DoubleOptBytes | None
ListOfDoubleOptBytes = list[DoubleOptBytes]
OptListOfDoubleOptBytes = ListOfDoubleOptBytes | None
SeqOfDoubleOptBytes = Sequence[DoubleOptBytes]
OptSeqOfDoubleOptBytes = SeqOfDoubleOptBytes | None

TripleOptBytes = tuple[OptBytes, OptBytes, OptBytes]
OptTripleOptBytes = TripleOptBytes | None
ListOfTripleOptBytes = list[TripleOptBytes]
OptListOfTripleOptBytes = ListOfTripleOptBytes | None
SeqOfTripleOptBytes = Sequence[TripleOptBytes]
OptSeqOfTripleOptBytes = SeqOfTripleOptBytes | None

QuintupleOptBytes = tuple[OptBytes, OptBytes, OptBytes, OptBytes]
OptQuintupleOptBytes = QuintupleOptBytes | None
ListOfQuintupleOptBytes = list[QuintupleOptBytes]
OptListOfQuintupleOptBytes = ListOfQuintupleOptBytes | None
SeqOfQuintupleOptBytes = Sequence[QuintupleOptBytes]
OptSeqOfQuintupleOptBytes = SeqOfQuintupleOptBytes | None

QuintupleOptBytes = tuple[OptBytes, OptBytes, OptBytes, OptBytes, OptBytes]
OptQuintupleOptBytes = QuintupleOptBytes | None
ListOfQuintupleOptBytes = list[QuintupleOptBytes]
OptListOfQuintupleOptBytes = ListOfQuintupleOptBytes | None
SeqOfQuintupleOptBytes = Sequence[QuintupleOptBytes]
OptSeqOfQuintupleOptBytes = SeqOfQuintupleOptBytes | None

ManyOptBytes = tuple[OptBytes, ...]
OptManyOptBytes = ManyOptBytes | None
ListOfManyOptBytes = list[ManyOptBytes]
OptListOfManyOptBytes = ListOfManyOptBytes | None
SeqOfManyOptBytes = Sequence[ManyOptBytes]
OptSeqOfManyOptBytes = SeqOfManyOptBytes | None
