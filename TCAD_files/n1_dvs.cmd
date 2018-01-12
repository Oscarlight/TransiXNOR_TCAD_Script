;----------------------------------------------------------------------
; TransiXNOR with S/D Static Gate
; Definitions
;----------------------------------------------------------------------

(define  chLength     0.010) ; 10 nm
(define  sdLength     0.005) ; 5 nm
(define  chThickness  0.001) ; 1 nm 
(define  tOxThickness 0.0005) ; 0.5 nm
(define  bOxThickness 0.0005) ; 0.5 nm
(define  x_step       0.00025); 0.25 nm
(define  y_step       0.00025); 0.25 nm

;----------------------------------------------------------------------
; Derived Quantities
;---------------------------------------------------------------------- 

(define chLengthHalf (/ chLength 2))
(define chThicknessHalf (/ chThickness 2))
(define sdLengthHalf (/ sdLength 2))
 
(define s_x1  0.0)
(define s_y1  bOxThickness)
(define s_x2  sdLength)
(define s_y2  (+ s_y1 chThickness))

(define ch_x1 s_x2)
(define ch_y1 s_y1)
(define ch_x2 (+ s_x2 chLength))
(define ch_y2 s_y2)

(define d_x1  ch_x2)
(define d_y1  ch_y1)
(define d_x2  (+ ch_x2 sdLength))
(define d_y2  ch_y2)

(define box_x1 ch_x1)
(define box_y1 0.0)
(define box_x2 ch_x2)
(define box_y2 ch_y1)

(define tox_x1 ch_x1)
(define tox_y1 ch_y2)
(define tox_x2 ch_x2)
(define tox_y2 (+ ch_y2 tOxThickness))

(define stox_x1 0.0)
(define stox_y1 0.0)
(define stox_x2 (- ch_x1 0.001))
(define stox_y2 s_y1)

(define sbox_x1 0.0)
(define sbox_y1 s_y2)
(define sbox_x2 stox_x2)
(define sbox_y2 tox_y2)

(define dtox_x1 (+ ch_x2 0.001))
(define dtox_y1 0.0)
(define dtox_x2 d_x2)
(define dtox_y2 s_y1)

(define dbox_x1 dtox_x1)
(define dbox_y1 s_y2)
(define dbox_x2 dtox_x2)
(define dbox_y2 tox_y2)

(define source_x s_x1)
(define source_y (+ s_y1 chThicknessHalf))
(define drain_x  d_x2)
(define drain_y  (- d_y2 chThicknessHalf))

(define tGate_x  (- tox_x2 chLengthHalf))
(define tGate_y  tox_y2)
(define bGate_x  (+ box_x1 chLengthHalf))
(define bGate_y 0.0)

(define t_source_x 0.002)
(define t_source_y 0.0)
(define b_source_x t_source_x)
(define b_source_y tox_y2)
(define t_drain_x (- d_x2 0.002))
(define t_drain_y 0.0)
(define b_drain_x t_drain_x)
(define b_drain_y b_source_y)

(define max_x d_x2)
(define max_y (+ d_y2 tOxThickness))

;----------------------------------------------------------------------
; Layer System
;----------------------------------------------------------------------


(sdegeo:create-rectangle 
 (position ch_x1 ch_y1 0) 
 (position ch_x2 ch_y2 0) "InGaAs" "Channel")

(sdegeo:create-rectangle 
 (position d_x1 d_y1 0) 
 (position d_x2 d_y2 0) "InGaAs" "Drain")

(sdegeo:create-rectangle 
 (position box_x1 box_y1 0) 
 (position box_x2 box_y2 0) "SiO2" "TopOx")

(sdegeo:create-rectangle 
 (position tox_x1 tox_y1 0) 
 (position tox_x2 tox_y2 0) "SiO2" "BottomOx")

(sdegeo:create-rectangle 
 (position stox_x1 stox_y1 0) 
 (position stox_x2 stox_y2 0) "SiO2" "SourceTopOx")

(sdegeo:create-rectangle 
 (position sbox_x1 sbox_y1 0) 
 (position sbox_x2 sbox_y2 0) "SiO2" "SourceBottomOx")

(sdegeo:create-rectangle 
 (position dtox_x1 dtox_y1 0) 
 (position dtox_x2 dtox_y2 0) "SiO2" "DrainTopOx")

(sdegeo:create-rectangle 
 (position dbox_x1 dbox_y1 0) 
 (position dbox_x2 dbox_y2 0) "SiO2" "DrainBottomOx")

(sdegeo:create-rectangle 
 (position s_x1 s_y1 0) 
 (position s_x2 s_y2 0) "InGaAs" "Source")

; --------------------------------------------------------------------------------
; Doping
; --------------------------------------------------------------------------------
(sdedr:define-refinement-window "Pl.NSemi" "Rectangle" (position d_x1 d_y1 0)  (position d_x2 d_y2 0))
(sdedr:define-constant-profile "P.NSemi" "PhosphorusActiveConcentration" 1E19)
(sdedr:define-constant-profile-placement "P.NSemi" "P.NSemi" "Pl.NSemi")

(sdedr:define-refinement-window "Pl.PSemi" "Rectangle" (position s_x1 s_y1 0)  (position s_x2 s_y2 0))
(sdedr:define-constant-profile "P.PSemi" "BoronActiveConcentration" 1E19)
(sdedr:define-constant-profile-placement "P.PSemi" "P.PSemi" "Pl.PSemi")

; --------------------------------------------------------------------------------
; Create and place all electrodes
; --------------------------------------------------------------------------------

(sdegeo:define-contact-set "source"        4.0 (color:rgb 1.0 0.0 0.0 ) "##" )
(sdegeo:define-contact-set "drain"         4.0 (color:rgb 0.0 1.0 0.0 ) "##" )
(sdegeo:define-contact-set "topGate"       4.0 (color:rgb 0.0 0.0 1.0 ) "##" )
(sdegeo:define-contact-set "bottomGate"    4.0 (color:rgb 1.0 1.0 0.0 ) "##" )
(sdegeo:define-contact-set "topSource"     4.0 (color:rgb 0.0 1.0 1.0 ) "##" )
(sdegeo:define-contact-set "bottomSource"  4.0 (color:rgb 1.0 0.0 1.0 ) "##" )
(sdegeo:define-contact-set "topDrain"      4.0 (color:rgb 1.0 1.0 1.0 ) "##" )
(sdegeo:define-contact-set "bottomDrain"   4.0 (color:rgb 1.0 0.0 0.0 ) "##" )

(sdegeo:define-2d-contact (find-edge-id (position source_x source_y 0)) "source")
;(sdegeo:define-2d-contact (find-edge-id 
;   (position (+ source_x sdLengthHalf) (+ source_y chThicknessHalf) 0)) "source")
;(sdegeo:define-2d-contact (find-edge-id 
;   (position (+ source_x sdLengthHalf) (- source_y chThicknessHalf) 0)) "source")

(sdegeo:define-2d-contact (find-edge-id (position drain_x drain_y 0)) "drain")
;(sdegeo:define-2d-contact (find-edge-id 
;   (position (- drain_x sdLengthHalf) (+ drain_y chThicknessHalf) 0)) "drain")
;(sdegeo:define-2d-contact (find-edge-id 
;   (position (- drain_x sdLengthHalf) (- drain_y chThicknessHalf) 0)) "drain")

(sdegeo:define-2d-contact (find-edge-id (position tGate_x tGate_y 0)) "topGate")
(sdegeo:define-2d-contact (find-edge-id (position bGate_x bGate_y 0)) "bottomGate")

(sdegeo:define-2d-contact (find-edge-id (position t_source_x t_source_y 0)) "topSource")
(sdegeo:define-2d-contact (find-edge-id (position b_source_x b_source_y 0)) "bottomSource")
(sdegeo:define-2d-contact (find-edge-id (position t_drain_x t_drain_y 0)) "topDrain")
(sdegeo:define-2d-contact (find-edge-id (position b_drain_x b_drain_y 0)) "bottomDrain")

;----------------------------------------------------------------------
; Meshing
;----------------------------------------------------------------------

(sdedr:define-refinement-window "Pl.Semi" "Rectangle" 
  (position s_x1 s_y1 0) 
  (position d_x2 d_y2 0))
(sdedr:define-refinement-size "Ref.Semi" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.Semi" "Ref.Semi" "Pl.Semi" )

(sdedr:define-refinement-window "Pl.Box" "Rectangle" 
  (position box_x1 box_y1 0) 
  (position box_x2 box_y2 0))
(sdedr:define-refinement-size "Ref.Box" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.Box" "Ref.Box" "Pl.Box" )

(sdedr:define-refinement-window "Pl.Tox" "Rectangle" 
  (position tox_x1 tox_y1 0) 
  (position tox_x2 tox_y2 0))
(sdedr:define-refinement-size "Ref.Tox" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.Tox" "Ref.Tox" "Pl.Tox" )

(sdedr:define-refinement-window "Pl.SBox" "Rectangle" 
  (position sbox_x1 sbox_y1 0) 
  (position sbox_x2 sbox_y2 0))
(sdedr:define-refinement-size "Ref.SBox" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.SBox" "Ref.SBox" "Pl.SBox" )

(sdedr:define-refinement-window "Pl.STox" "Rectangle" 
  (position stox_x1 stox_y1 0) 
  (position stox_x2 stox_y2 0))
(sdedr:define-refinement-size "Ref.STox" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.STox" "Ref.STox" "Pl.STox" )

(sdedr:define-refinement-window "Pl.DBox" "Rectangle" 
  (position dbox_x1 dbox_y1 0) 
  (position dbox_x2 dbox_y2 0))
(sdedr:define-refinement-size "Ref.DBox" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.DBox" "Ref.DBox" "Pl.DBox" )

(sdedr:define-refinement-window "Pl.DTox" "Rectangle" 
  (position dtox_x1 dtox_y1 0) 
  (position dtox_x2 dtox_y2 0))
(sdedr:define-refinement-size "Ref.DTox" x_step y_step 99 x_step y_step 66 )
(sdedr:define-refinement-placement "Ref.DTox" "Ref.DTox" "Pl.DTox" )

;----------------------------------------------------------------------
; Build Mesh 
;----------------------------------------------------------------------
(sde:build-mesh "snmesh" "" "n1_msh")




