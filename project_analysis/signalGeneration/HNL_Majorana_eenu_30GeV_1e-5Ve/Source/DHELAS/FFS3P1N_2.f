C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     ProjM(2,1)
C     
      SUBROUTINE FFS3P1N_2(F1, S3, COUP,F2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(6)
      COMPLEX*16 S3(*)
      F2(3)= COUP*(-CI )* F1(3)*S3(3)
      F2(4)= COUP*(-CI )* F1(4)*S3(3)
      F2(5)= COUP*0D0
      F2(6)= COUP*0D0
      END


