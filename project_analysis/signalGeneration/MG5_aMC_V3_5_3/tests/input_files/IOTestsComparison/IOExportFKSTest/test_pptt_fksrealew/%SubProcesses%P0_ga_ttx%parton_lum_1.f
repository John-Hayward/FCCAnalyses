      SUBROUTINE DLUM_1(LUM)
C     ****************************************************            
C         
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     RETURNS PARTON LUMINOSITIES FOR MADFKS                          
C        
C     
C     Process: g a > t t~ g [ real = QCD QED ] QCD^2<=4 QED^2<=2
C     
C     ****************************************************            
C         
      IMPLICIT NONE
C     
C     CONSTANTS                                                       
C         
C     
      INCLUDE 'genps.inc'
      INCLUDE 'nexternal.inc'
      DOUBLE PRECISION       CONV
      PARAMETER (CONV=389379660D0)  !CONV TO PICOBARNS             
C     
C     ARGUMENTS                                                       
C         
C     
      DOUBLE PRECISION LUM
C     
C     LOCAL VARIABLES                                                 
C         
C     
      INTEGER I, ICROSS,LP
      DOUBLE PRECISION G1
      DOUBLE PRECISION A2
C     
C     EXTERNAL FUNCTIONS                                              
C         
C     
      DOUBLE PRECISION PDG2PDF
C     
C     GLOBAL VARIABLES                                                
C         
C     
      INTEGER              IPROC
      DOUBLE PRECISION PD(0:MAXPROC)
      COMMON /SUBPROC/ PD, IPROC
      INCLUDE 'coupl.inc'
      INCLUDE 'run.inc'
      INTEGER IMIRROR
      COMMON/CMIRROR/IMIRROR
C     
C     STUFF FOR DRESSED EE COLLISIONS
C     
      INCLUDE 'eepdf.inc'
      DOUBLE PRECISION EE_COMP_PROD
      DOUBLE PRECISION DUMMY_COMPONENTS(N_EE)
      DOUBLE PRECISION G1_COMPONENTS(N_EE)
      DOUBLE PRECISION A2_COMPONENTS(N_EE)

      INTEGER I_EE
      INCLUDE '../../Source/PDF/pdf.inc'
C     
C     DATA                                                            
C         
C     
      DATA G1/1*1D0/
      DATA A2/1*1D0/
      DATA ICROSS/1/
C     ----------                                                      
C         
C     BEGIN CODE                                                      
C         
C     ----------                                                      
C         
      LUM = 0D0
      IF (ABS(LPP(1)) .GE. 1) THEN
        G1=PDG2PDF(LPP(1),0,1,XBK(1),DSQRT(Q2FACT(1)))
        IF ((ABS(LPP(1)).EQ.4.OR.ABS(LPP(1)).EQ.3)
     $   .AND.PDLABEL.NE.'none') G1_COMPONENTS(1:N_EE) =
     $    EE_COMPONENTS(1:N_EE)
      ENDIF
      IF (ABS(LPP(2)) .GE. 1) THEN
        A2=PDG2PDF(LPP(2),7,2,XBK(2),DSQRT(Q2FACT(2)))
        IF ((ABS(LPP(2)).EQ.4.OR.ABS(LPP(2)).EQ.3)
     $   .AND.PDLABEL.NE.'none') A2_COMPONENTS(1:N_EE) =
     $    EE_COMPONENTS(1:N_EE)
      ENDIF
      PD(0) = 0D0
      IPROC = 0
      IPROC=IPROC+1  ! g a > t t~ g
      PD(IPROC) = G1*A2
      IF (ABS(LPP(1)).EQ.ABS(LPP(2)).AND. (ABS(LPP(1))
     $ .EQ.3.OR.ABS(LPP(1)).EQ.4).AND.PDLABEL.NE.'none')PD(IPROC)
     $ =EE_COMP_PROD(G1_COMPONENTS,A2_COMPONENTS)
      DO I=1,IPROC
        IF (NINCOMING.EQ.2) THEN
          LUM = LUM + PD(I) * CONV
        ELSE
          LUM = LUM + PD(I)
        ENDIF
      ENDDO
      RETURN
      END

