C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,-1)*ProjM(-1,1)
C     
      SUBROUTINE FFV5P1N_2(F1, V3, COUP,F2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(6)
      COMPLEX*16 V3(*)
      F2(3)= COUP*0D0
      F2(4)= COUP*0D0
      F2(5)= COUP*CI*(F1(3)*(-1D0)*(V3(3)+V3(6))+F1(4)*(-V3(4)+CI
     $ *(V3(5))))
      F2(6)= COUP*(-CI)*(F1(3)*(V3(4)+CI*(V3(5)))+F1(4)*(V3(3)-V3(6)))
      END


