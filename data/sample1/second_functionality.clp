(defglobal ?*propozitiiNeparsate* = 0)
(defglobal ?*propozitiiParsate* = 0)
(defglobal ?*totalPropozitii* = 0)
(defglobal ?*propozitiaCurenta* = "")

(deffacts facts
		(waiting_input)
		(answer)
		(rule G1 S PRP A1)
		(rule G2 A1 VBP B1)
		(rule G3 B1 JJ C1)
		(rule G4 C1 . S)
		(rule G5 S PRP A2)
		(rule G6 A2 VBP B2)
		(rule G7 B2 NN C2)
		(rule G8 C2 . S)
		(rule G9 S PRP A3)
		(rule G10 A3 VBP B3)
		(rule G11 B3 TO C3)
		(rule G12 C3 VB D3)
		(rule G13 D3 . EPS)
)
(defrule read_input
        ?a <- (waiting_input)
        =>
        (close fisierPropozitiiNeparsate)
        (open "D:/School/learn-a-language/data/input.dat" data "r")
        (assert (text S (explode$ (readline data))))
        (close data)
        (open "D:/School/learn-a-language/data/second_output.dat" fisierPropozitiiNeparsate "w")
        (retract ?a)
)

(defrule apply_rule
        (rule ?g ?nonterminal ?first ?next)
        ?a <- (text ?nonterminal ?first $?rest)
        ?b <- (answer $?steps)
        =>
        (if (eq ?next S)
        then
                (bind ?*propozitiiParsate* (+ ?*propozitiiParsate* 1))
                (bind ?*propozitiaCurenta* (str-cat ?*propozitiaCurenta* ?first))
                (printout fisierPropozitiiNeparsate "Propozitie parsata in intregime: " ?*propozitiaCurenta* crlf )
                (bind ?*propozitiaCurenta* "")

        )

        (if (eq (length $?rest) 0)
                then
                (bind ?*totalPropozitii* (+ ?*propozitiiNeparsate* ?*propozitiiParsate*))
        (printout fisierPropozitiiNeparsate "Totalul propozitiilor: " ?*totalPropozitii* crlf )
        (printout fisierPropozitiiNeparsate "Totalul propozitiilor parsate: " ?*propozitiiParsate* crlf)
        (close fisierPropozitiiNeparsate)
        )
        (bind ?*propozitiaCurenta* (str-cat ?*propozitiaCurenta* ?first " "))
        (assert (text ?next $?rest))
        (assert (answer $?steps ?g))
        (retract ?a)
        (retract ?b)
)


(defrule success
        ?a <- (text EPS)
        (answer $?steps)
        =>
        (retract ?a)
)

(defrule failure
        ?a <- (text ?simb $?cevaPropozitieNeparsata . $?restulPropozitiilor)
        =>
        (bind ?*propozitiiNeparsate* (+ ?*propozitiiNeparsate* 1))
        (if (eq (length $?restulPropozitiilor) 0)
        then
        (bind ?*totalPropozitii* (+ ?*propozitiiNeparsate* ?*propozitiiParsate*))
        (printout fisierPropozitiiNeparsate "Propozitie neparsata : " ?*propozitiaCurenta* $?cevaPropozitieNeparsata crlf )
        (printout fisierPropozitiiNeparsate "Totalul propozitiilor: " ?*totalPropozitii* crlf )
        (printout fisierPropozitiiNeparsate "Totalul propozitiilor parsate: " ?*propozitiiParsate* crlf)
        (close fisierPropozitiiNeparsate)
        else
        (printout fisierPropozitiiNeparsate "Propozitie neparsata : " ?*propozitiaCurenta* $?cevaPropozitieNeparsata crlf )
        (bind ?*propozitiaCurenta* "")
        )
        (assert (text S $?restulPropozitiilor))
        (retract ?a)
)