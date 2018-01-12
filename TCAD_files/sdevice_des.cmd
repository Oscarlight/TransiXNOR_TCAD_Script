Device TransiXNOR {

Electrode{
   { Name="source"        Voltage=  0.0  }
   { Name="drain"         Voltage=  0.0  }
   { Name="topGate"       Voltage=  0.2  Schottky Barrier = 0.02 } ### prevent skip Vtg = 0
   { Name="bottomGate"    Voltage=  0.2  Schottky Barrier = 0.02 }
#   { Name="topSource"     Voltage=  -0.35  }
#   { Name="bottomSource"  Voltage=  -0.35  }
#   { Name="topDrain"      Voltage=  0.75  }
#   { Name="bottomDrain"   Voltage=  0.75  }
}

File{
   Grid= "@tdr@"    
   Current= "@plot@"       
   Plot= "@tdrdat@"        
   Parameter= "@parameter@"
}

Physics {
   Recombination(
     Band2Band(
       Model = NonLocalPath
     )
   )                           
   EffectiveIntrinsicDensity( NoBandGapNarrowing )
}

Physics( Material="InGaAs"){
   MoleFraction( xFraction= 0.2 Grading= 0)
}

Plot{
   eDensity hDensity
   TotalCurrent/Vector eCurrent/Vector hCurrent/Vector
   eMobility hMobility
   eVelocity hVelocity
   eQuasiFermi hQuasiFermi
   eBarrierTunneling
   hBarrierTunneling
   ElectricField/Vector Potential SpaceCharge
   Doping DonorConcentration AcceptorConcentration
   eGradQuasiFermi/Vector hGradQuasiFermi/Vector
   eEparallel hEparalllel
   BandGap 
   Affinity
   ConductionBand ValenceBand
   xMoleFraction
}

}

Math{
   Extrapolate
   Nonlocal "NLM" (Electrode="source" Length=25e-7) # up to 25 nm
   Digits= 5
   Notdamped= 50
   Iterations= 15
   RelErrControl
   ErrRef(Electron) = 1e7
   ErrRef(Hole)     = 1e7
   RelTermMinDensity= 1e4
   RelTermMinDensityZero= 1e7     
}

File {
   Output= "@log@"
   ACExtract= "@acplot@" 
}

System {
   TransiXNOR trans ("drain"=d "source"=s "topGate"=g "bottomGate"=b)
   Vsource_pset vd (d 0) {dc=0}
   Vsource_pset vs (s 0) {dc=0}
   Vsource_pset vg (g 0) {dc=0.2}
   Vsource_pset vb (b 0) {dc=0.2}
}

Solve{
*- Initial Solution:
   Coupled( Iterations= 100 ){ Poisson }
   Coupled{ Poisson Electron Hole }

#----------------------------------------------------------------------
#- Plots
#----------------------------------------------------------------------#

Quasistationary( InitialStep= 5e-2 Increment= 1.25 
 Minstep= 1e-5 MaxStep= 0.015 
 Goal{ Parameter=vg.dc Voltage = 0.20 }) 
 { Coupled{ Poisson Electron Hole } }

Quasistationary( InitialStep= 5e-2 Increment= 1.25 
 Minstep= 1e-5 MaxStep= 0.015 
 Goal{ Parameter=vb.dc Voltage = 0.20 }) 
 { Coupled{ Poisson Electron Hole } }

NewCurrentFile="IV_Vtg_0.20_Vbg_0.20_"

Quasistationary( InitialStep= 5e-2 Increment= 1.25 
 Minstep= 1e-5 MaxStep= 0.015
 Goal{ Parameter=vd.dc  Voltage= 0.40 }) 
 { ACCoupled ( 
 StartFrequency=1e7 EndFrequency=1e7 
 NumberOfPoints=1 Decade 
 Node (d s g b) Exclude (vd vs vg vb) 
 ) 
 { Poisson Electron Hole } }

}
