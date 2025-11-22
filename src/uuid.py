from typing import Sequence, TypeVar
from uuid import UUID


UUIDT = TypeVar("UUIDT", bound=UUID)

OptUUID = UUID | None
OptUUIDT = TypeVar("OptUUIDT", bound=OptUUID)

ListOfUUIDs = list[UUID]
ListOfUUIDsT = TypeVar("ListOfUUIDsT", bound=ListOfUUIDs)

OptListOfUUIDs = ListOfUUIDs | None
OptListOfUUIDsT = TypeVar("OptListOfUUIDsT", bound=OptListOfUUIDs)

SeqOfUUIDs = Sequence[UUID]
SeqOfUUIDsT = TypeVar("SeqOfUUIDsT", bound=SeqOfUUIDs)

OptSeqOfUUIDs = SeqOfUUIDs | None
OptSeqOfUUIDsT = TypeVar("OptSeqOfUUIDsT", bound=OptSeqOfUUIDs)

# UUIDs tuple
DoubleUUIDs = tuple[UUID, UUID]
OptDoubleUUIDs = DoubleUUIDs | None
ListOfDoubleUUIDs = list[DoubleUUIDs]
OptListOfDoubleUUIDs = ListOfDoubleUUIDs | None
SeqOfDoubleUUIDs = Sequence[DoubleUUIDs]
OptSeqOfDoubleUUIDs = SeqOfDoubleUUIDs | None

TripleUUIDs = tuple[UUID, UUID, UUID]
OptTripleUUIDs = TripleUUIDs | None
ListOfTripleUUIDs = list[TripleUUIDs]
OptListOfTripleUUIDs = ListOfTripleUUIDs | None
SeqOfTripleUUIDs = Sequence[TripleUUIDs]
OptSeqOfTripleUUIDs = SeqOfTripleUUIDs | None

QuadrupleUUIDs = tuple[UUID, UUID, UUID, UUID]
OptQuadrupleUUIDs = QuadrupleUUIDs | None
ListOfQuadrupleUUIDs = list[QuadrupleUUIDs]
OptListOfQuadrupleUUIDs = ListOfQuadrupleUUIDs | None
SeqOfQuadrupleUUIDs = Sequence[QuadrupleUUIDs]
OptSeqOfQuadrupleUUIDs = SeqOfQuadrupleUUIDs | None

QuintupleUUIDs = tuple[UUID, UUID, UUID, UUID]
OptQuintupleUUIDs = QuintupleUUIDs | None
ListOfQuintupleUUIDs = list[QuintupleUUIDs]
OptListOfQuintupleUUIDs = ListOfQuintupleUUIDs | None
SeqOfQuintupleUUIDs = Sequence[QuintupleUUIDs]
OptSeqOfQuintupleUUIDs = SeqOfQuintupleUUIDs | None

ManyUUIDs = tuple[UUID, ...]
OptManyUUIDs = ManyUUIDs | None
ListOfManyUUIDs = list[ManyUUIDs]
OptListOfManyUUIDs = ListOfManyUUIDs | None
SeqOfManyUUIDs = Sequence[ManyUUIDs]
OptSeqOfManyUUIDs = SeqOfManyUUIDs | None

# Opt UUIDs tuple
DoubleOptUUIDs = tuple[OptUUID, OptUUID]
OptDoubleOptUUIDs = DoubleOptUUIDs | None
ListOfDoubleOptUUIDs = list[DoubleOptUUIDs]
OptListOfDoubleOptUUIDs = ListOfDoubleOptUUIDs | None
SeqOfDoubleOptUUIDs = Sequence[DoubleOptUUIDs]
OptSeqOfDoubleOptUUIDs = SeqOfDoubleOptUUIDs | None

TripleOptUUIDs = tuple[OptUUID, OptUUID, OptUUID]
OptTripleOptUUIDs = TripleOptUUIDs | None
ListOfTripleOptUUIDs = list[TripleOptUUIDs]
OptListOfTripleOptUUIDs = ListOfTripleOptUUIDs | None
SeqOfTripleOptUUIDs = Sequence[TripleOptUUIDs]
OptSeqOfTripleOptUUIDs = SeqOfTripleOptUUIDs | None

QuadrupleOptUUIDs = tuple[OptUUID, OptUUID, OptUUID, OptUUID]
OptQuadrupleOptUUIDs = QuadrupleOptUUIDs | None
ListOfQuadrupleOptUUIDs = list[QuadrupleOptUUIDs]
OptListOfQuadrupleOptUUIDs = ListOfQuadrupleOptUUIDs | None
SeqOfQuadrupleOptUUIDs = Sequence[QuadrupleOptUUIDs]
OptSeqOfQuadrupleOptUUIDs = SeqOfQuadrupleOptUUIDs | None

QuintupleOptUUIDs = tuple[OptUUID, OptUUID, OptUUID, OptUUID, OptUUID]
OptQuintupleOptUUIDs = QuintupleOptUUIDs | None
ListOfQuintupleOptUUIDs = list[QuintupleOptUUIDs]
OptListOfQuintupleOptUUIDs = ListOfQuintupleOptUUIDs | None
SeqOfQuintupleOptUUIDs = Sequence[QuintupleOptUUIDs]
OptSeqOfQuintupleOptUUIDs = SeqOfQuintupleOptUUIDs | None

ManyOptUUIDs = tuple[OptUUID, ...]
OptManyOptUUIDs = ManyOptUUIDs | None
ListOfManyOptUUIDs = list[ManyOptUUIDs]
OptListOfManyOptUUIDs = ListOfManyOptUUIDs | None
SeqOfManyOptUUIDs = Sequence[ManyOptUUIDs]
OptSeqOfManyOptUUIDs = SeqOfManyOptUUIDs | None
