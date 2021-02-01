male(pPhillip).
male(pCharles).
male(captain_Mark).
male(timothy).
male(pAndrew).
male(pEdward).
male(pWilliam).
male(pHarry).
male(peter).
male(mike).
male(james).
male(pGeorge).
male(mia_Grace).

% female
female(qElizabethII).
female(pDiana).
female(camilla_Parker).
female(pAnne).
female(sarah).
female(sophie).
female(kate).
female(autumn).
female(zara).
female(pBeatrice).
female(pEugenie).
female(lady_Louise).
female(pCharlotte).
female(savannah).
female(isla).

% parent
% The he 1
parent(qElizabethII,pCharles).
parent(pPhillip,pCharles).
parent(qElizabethII,pAnne).
parent(pPhillip,pAnne).
parent(qElizabethII,pAndrew).
parent(pPhillip,pAndrew).
parent(qElizabethII,pEdward).
parent(pPhillip,pEdward).
% The he 2
parent(pDiana,pWilliam).
parent(pCharles,pWilliam).
parent(pDiana,pHarry).
parent(pCharles,pHarry).

parent(captain_Mark,peter).
parent(pAnne,peter).
parent(captain_Mark,zara).
parent(pAnne,zara).

parent(sarah,pBeatrice).
parent(pAndrew,pBeatrice).
parent(sarah,pEugenie).
parent(pAndrew,pEugenie).

parent(sophie,james).
parent(pEdward,james).
parent(sophie,lady_Louise).
parent(pEdward,lady_Louise).

% The he 3
parent(pWilliam,pGeorge).
parent(kate,pGeorge).
parent(pWilliam,pCharlotte).
parent(kate,pCharlotte).

parent(autumn,savannah).
parent(peter,savannah).
parent(autumn,isla).
parent(peter,isla).

parent(zara,mia_Grace).
parent(mike,mia_Grace).

% married
married(qElizabethII,pPhillip).
married(pPhillip,qElizabethII).

married(pCharles,camilla_Parker).
married(camilla_Parker,pCharles).

married(pAnne,timothy).
married(timothy,pAnne).

married(sophie,pEdward).
married(pEdward,sophie).

married(pWilliam,kate).
married(kate,pWilliam).

married(autumn,peter).
married(peter,autumn).

married(zara,mike).

married(mike,zara).

% divorced
divorced(pDiana,pCharles).
divorced(pCharles,pDiana).

divorced(captain_Mark,pAnne).
divorced(pAnne,captain_Mark).

divorced(sarah,pAndrew).
divorced(pAndrew,sarah).

husband(Person,Wife) :- married(Person,Wife),male(Person).
wife(Person,Husband) :- married(Person,Husband),female(Person).
father(Parent,Child) :- parent(Parent,Child),male(Parent).
mother(Parent,Child) :- parent(Parent,Child),female(Parent).
child(Child,Parent) :- parent(Parent,Child).
son(Child,Parent) :- child(Child,Parent),male(Child).
daughter(Child,Parent) :- child(Child,Parent),female(Child).

grandparent(GP,GC) :- parent(GP,P),parent(P,GC).
grandmother(GM,GC) :- parent(GM,P),parent(P,GC),female(GM).
grandfather(GF,GC):- parent(GP,P),parent(P,GC),male(GP).
grandchild(GC,GP) :- parent(GP,P),parent(P,GC).
grandson(GS,GP) :- parent(GP,P),parent(P,GS),male(GS).
granddaughter(GD,GP) :- parent(GP,P),parent(P,GD),female(GD).

sibling(Person1,Person2) :- father(P,Person1),father(P,Person2),Person1\=Person2.
brother(Person,Sibling) :- sibling(Person,Sibling),male(Person).
sister(Person,Sibling) :- sibling(Person,Sibling),female(Person).
aunt(Person,NieceNephew) :- parent(P,NieceNephew),sibling(P,Person),female(Person).
uncle(Person,NieceNephew) :- parent(P,NieceNephew),sibling(P,Person),male(Person).
niece(Person,AuntUncle) :- parent(P,Person),sibling(P,AuntUncle),female(Person).
nephew(Person,AuntUncle) :- parent(P,Person),sibling(P,AuntUncle),male(Person).

