MODULE nielsen_generalized_polylog
  IMPLICIT NONE
  ! this is from the cernlib 2006/src/mathlib/gen/c/cgplg64.F
  ! It is same as CGPLG and WGPLG
CONTAINS
  ! the Nielsen generalised polylogarithms function Sn,m(x)
  ! Sn-1,1(x)=Lin(x)
  FUNCTION Nielsen_PolyLog(N,M,X)
    ! limitation:
    ! 1<=N<=4 & 1<=M<=4 & N+M<=5
    IMPLICIT NONE
    INTEGER,INTENT(IN)::N,M
    REAL(KIND(1d0)),INTENT(IN)::X
    COMPLEX(KIND(1d0))::Nielsen_PolyLog
    COMPLEX(KIND(1d0))::Z,SK,SJ
    COMPLEX(KIND(1d0)),PARAMETER::I=(0,1)
    COMPLEX(KIND(1d0)),DIMENSION(0:5)::V
!    CHARACTER(len=*)::NAME
!    CHARACTER(len=80)::ERRTXT
    REAL(KIND(1d0)),DIMENSION(0:4)::FCT,SGN,U
    REAL(KIND(1d0)),DIMENSION(4,4)::S1,C
    REAL(KIND(1d0)),DIMENSION(0:30,10)::A
    INTEGER,DIMENSION(10)::NC
    INTEGER,DIMENSION(31)::INDEX
    REAL(KIND(1d0)),PARAMETER::Z0=0,Z1=1,HF=0.5d0,C1=4d0/3d0,C2=1d0/3d0
    INTEGER::IT,L,K,M1,J,N1
    REAL(KIND(1d0))::X1,H,ALFA,R,B0,B1,B2,Q

    DATA FCT /1,1,2,6,24/, SGN /1,-1,1,-1,1/
    
    DATA S1(1,1) /1.6449340668482D0/
    DATA S1(1,2) /1.2020569031596D0/
    DATA S1(1,3) /1.0823232337111D0/
    DATA S1(1,4) /1.0369277551434D0/
    DATA S1(2,1) /1.2020569031596D0/
    DATA S1(2,2) /2.7058080842778D-1/
    DATA S1(2,3) /9.6551159989444D-2/
    DATA S1(3,1) /1.0823232337111D0/
    DATA S1(3,2) /9.6551159989444D-2/
    DATA S1(4,1) /1.0369277551434D0/
    
    DATA C(1,1) / 1.6449340668482D0/
    DATA C(1,2) / 1.2020569031596D0/
    DATA C(1,3) / 1.0823232337111D0/
    DATA C(1,4) / 1.0369277551434D0/
    DATA C(2,1) / 0.0000000000000D0/
    DATA C(2,2) /-1.8940656589945D0/
    DATA C(2,3) /-3.0142321054407D0/
    DATA C(3,1) / 1.8940656589945D0/
    DATA C(3,2) / 3.0142321054407D0/
    DATA C(4,1) / 0.0000000000000D0/

    DATA INDEX /1,2,3,4,6*0,5,6,7,7*0,8,9,8*0,10/

    DATA NC /24,26,28,30,22,24,26,19,22,17/
    
    DATA A( 0,1) / .96753215043498D0/
    DATA A( 1,1) / .16607303292785D0/
    DATA A( 2,1) / .02487932292423D0/
    DATA A( 3,1) / .00468636195945D0/
    DATA A( 4,1) / .00100162749616D0/
    DATA A( 5,1) / .00023200219609D0/
    DATA A( 6,1) / .00005681782272D0/
    DATA A( 7,1) / .00001449630056D0/
    DATA A( 8,1) / .00000381632946D0/
    DATA A( 9,1) / .00000102990426D0/
    DATA A(10,1) / .00000028357538D0/
    DATA A(11,1) / .00000007938705D0/
    DATA A(12,1) / .00000002253670D0/
    DATA A(13,1) / .00000000647434D0/
    DATA A(14,1) / .00000000187912D0/
    DATA A(15,1) / .00000000055029D0/
    DATA A(16,1) / .00000000016242D0/
    DATA A(17,1) / .00000000004827D0/
    DATA A(18,1) / .00000000001444D0/
    DATA A(19,1) / .00000000000434D0/
    DATA A(20,1) / .00000000000131D0/
    DATA A(21,1) / .00000000000040D0/
    DATA A(22,1) / .00000000000012D0/
    DATA A(23,1) / .00000000000004D0/
    DATA A(24,1) / .00000000000001D0/
    
    DATA A( 0,2) / .95180889127832D0/
    DATA A( 1,2) / .43131131846532D0/
    DATA A( 2,2) / .10002250714905D0/
    DATA A( 3,2) / .02442415595220D0/
    DATA A( 4,2) / .00622512463724D0/
    DATA A( 5,2) / .00164078831235D0/
    DATA A( 6,2) / .00044407920265D0/
    DATA A( 7,2) / .00012277494168D0/
    DATA A( 8,2) / .00003453981284D0/
    DATA A( 9,2) / .00000985869565D0/
    DATA A(10,2) / .00000284856995D0/
    DATA A(11,2) / .00000083170847D0/
    DATA A(12,2) / .00000024503950D0/
    DATA A(13,2) / .00000007276496D0/
    DATA A(14,2) / .00000002175802D0/
    DATA A(15,2) / .00000000654616D0/
    DATA A(16,2) / .00000000198033D0/
    DATA A(17,2) / .00000000060204D0/
    DATA A(18,2) / .00000000018385D0/
    DATA A(19,2) / .00000000005637D0/
    DATA A(20,2) / .00000000001735D0/
    DATA A(21,2) / .00000000000536D0/
    DATA A(22,2) / .00000000000166D0/
    DATA A(23,2) / .00000000000052D0/
    DATA A(24,2) / .00000000000016D0/
    DATA A(25,2) / .00000000000005D0/
    DATA A(26,2) / .00000000000002D0/
    
    DATA A( 0,3) / .98161027991365D0/
    DATA A( 1,3) / .72926806320726D0/
    DATA A( 2,3) / .22774714909321D0/
    DATA A( 3,3) / .06809083296197D0/
    DATA A( 4,3) / .02013701183064D0/
    DATA A( 5,3) / .00595478480197D0/
    DATA A( 6,3) / .00176769013959D0/
    DATA A( 7,3) / .00052748218502D0/
    DATA A( 8,3) / .00015827461460D0/
    DATA A( 9,3) / .00004774922076D0/
    DATA A(10,3) / .00001447920408D0/
    DATA A(11,3) / .00000441154886D0/
    DATA A(12,3) / .00000135003870D0/
    DATA A(13,3) / .00000041481779D0/
    DATA A(14,3) / .00000012793307D0/
    DATA A(15,3) / .00000003959070D0/
    DATA A(16,3) / .00000001229055D0/
    DATA A(17,3) / .00000000382658D0/
    DATA A(18,3) / .00000000119459D0/
    DATA A(19,3) / .00000000037386D0/
    DATA A(20,3) / .00000000011727D0/
    DATA A(21,3) / .00000000003687D0/
    DATA A(22,3) / .00000000001161D0/
    DATA A(23,3) / .00000000000366D0/
    DATA A(24,3) / .00000000000116D0/
    DATA A(25,3) / .00000000000037D0/
    DATA A(26,3) / .00000000000012D0/
    DATA A(27,3) / .00000000000004D0/
    DATA A(28,3) / .00000000000001D0/
    
    DATA A( 0,4) /1.0640521184614D0/
    DATA A( 1,4) /1.0691720744981D0/
    DATA A( 2,4) / .41527193251768D0/
    DATA A( 3,4) / .14610332936222D0/
    DATA A( 4,4) / .04904732648784D0/
    DATA A( 5,4) / .01606340860396D0/
    DATA A( 6,4) / .00518889350790D0/
    DATA A( 7,4) / .00166298717324D0/
    DATA A( 8,4) / .00053058279969D0/
    DATA A( 9,4) / .00016887029251D0/
    DATA A(10,4) / .00005368328059D0/
    DATA A(11,4) / .00001705923313D0/
    DATA A(12,4) / .00000542174374D0/
    DATA A(13,4) / .00000172394082D0/
    DATA A(14,4) / .00000054853275D0/
    DATA A(15,4) / .00000017467795D0/
    DATA A(16,4) / .00000005567550D0/
    DATA A(17,4) / .00000001776234D0/
    DATA A(18,4) / .00000000567224D0/
    DATA A(19,4) / .00000000181313D0/
    DATA A(20,4) / .00000000058012D0/
    DATA A(21,4) / .00000000018579D0/
    DATA A(22,4) / .00000000005955D0/
    DATA A(23,4) / .00000000001911D0/
    DATA A(24,4) / .00000000000614D0/
    DATA A(25,4) / .00000000000197D0/
    DATA A(26,4) / .00000000000063D0/
    DATA A(27,4) / .00000000000020D0/
    DATA A(28,4) / .00000000000007D0/
    DATA A(29,4) / .00000000000002D0/
    DATA A(30,4) / .00000000000001D0/

    DATA A( 0,5) / .97920860669175D0/
    DATA A( 1,5) / .08518813148683D0/
    DATA A( 2,5) / .00855985222013D0/
    DATA A( 3,5) / .00121177214413D0/
    DATA A( 4,5) / .00020722768531D0/
    DATA A( 5,5) / .00003996958691D0/
    DATA A( 6,5) / .00000838064065D0/
    DATA A( 7,5) / .00000186848945D0/
    DATA A( 8,5) / .00000043666087D0/
    DATA A( 9,5) / .00000010591733D0/
    DATA A(10,5) / .00000002647892D0/
    DATA A(11,5) / .00000000678700D0/
    DATA A(12,5) / .00000000177654D0/
    DATA A(13,5) / .00000000047342D0/
    DATA A(14,5) / .00000000012812D0/
    DATA A(15,5) / .00000000003514D0/
    DATA A(16,5) / .00000000000975D0/
    DATA A(17,5) / .00000000000274D0/
    DATA A(18,5) / .00000000000077D0/
    DATA A(19,5) / .00000000000022D0/
    DATA A(20,5) / .00000000000006D0/
    DATA A(21,5) / .00000000000002D0/
    DATA A(22,5) / .00000000000001D0/

    DATA A( 0,6) / .95021851963952D0/
    DATA A( 1,6) / .29052529161433D0/
    DATA A( 2,6) / .05081774061716D0/
    DATA A( 3,6) / .00995543767280D0/
    DATA A( 4,6) / .00211733895031D0/
    DATA A( 5,6) / .00047859470550D0/
    DATA A( 6,6) / .00011334321308D0/
    DATA A( 7,6) / .00002784733104D0/
    DATA A( 8,6) / .00000704788108D0/
    DATA A( 9,6) / .00000182788740D0/
    DATA A(10,6) / .00000048387492D0/
    DATA A(11,6) / .00000013033842D0/
    DATA A(12,6) / .00000003563769D0/
    DATA A(13,6) / .00000000987174D0/
    DATA A(14,6) / .00000000276586D0/
    DATA A(15,6) / .00000000078279D0/
    DATA A(16,6) / .00000000022354D0/
    DATA A(17,6) / .00000000006435D0/
    DATA A(18,6) / .00000000001866D0/
    DATA A(19,6) / .00000000000545D0/
    DATA A(20,6) / .00000000000160D0/
    DATA A(21,6) / .00000000000047D0/
    DATA A(22,6) / .00000000000014D0/
    DATA A(23,6) / .00000000000004D0/
    DATA A(24,6) / .00000000000001D0/

    DATA A( 0,7) / .95064032186777D0/
    DATA A( 1,7) / .54138285465171D0/
    DATA A( 2,7) / .13649979590321D0/
    DATA A( 3,7) / .03417942328207D0/
    DATA A( 4,7) / .00869027883583D0/
    DATA A( 5,7) / .00225284084155D0/
    DATA A( 6,7) / .00059516089806D0/
    DATA A( 7,7) / .00015995617766D0/
    DATA A( 8,7) / .00004365213096D0/
    DATA A( 9,7) / .00001207474688D0/
    DATA A(10,7) / .00000338018176D0/
    DATA A(11,7) / .00000095632476D0/
    DATA A(12,7) / .00000027313129D0/
    DATA A(13,7) / .00000007866968D0/
    DATA A(14,7) / .00000002283195D0/
    DATA A(15,7) / .00000000667205D0/
    DATA A(16,7) / .00000000196191D0/
    DATA A(17,7) / .00000000058018D0/
    DATA A(18,7) / .00000000017246D0/
    DATA A(19,7) / .00000000005151D0/
    DATA A(20,7) / .00000000001545D0/
    DATA A(21,7) / .00000000000465D0/
    DATA A(22,7) / .00000000000141D0/
    DATA A(23,7) / .00000000000043D0/
    DATA A(24,7) / .00000000000013D0/
    DATA A(25,7) / .00000000000004D0/
    DATA A(26,7) / .00000000000001D0/
    
    DATA A( 0,8) / .98800011672229D0/
    DATA A( 1,8) / .04364067609601D0/
    DATA A( 2,8) / .00295091178278D0/
    DATA A( 3,8) / .00031477809720D0/
    DATA A( 4,8) / .00004314846029D0/
    DATA A( 5,8) / .00000693818230D0/
    DATA A( 6,8) / .00000124640350D0/
    DATA A( 7,8) / .00000024293628D0/
    DATA A( 8,8) / .00000005040827D0/
    DATA A( 9,8) / .00000001099075D0/
    DATA A(10,8) / .00000000249467D0/
    DATA A(11,8) / .00000000058540D0/
    DATA A(12,8) / .00000000014127D0/
    DATA A(13,8) / .00000000003492D0/
    DATA A(14,8) / .00000000000881D0/
    DATA A(15,8) / .00000000000226D0/
    DATA A(16,8) / .00000000000059D0/
    DATA A(17,8) / .00000000000016D0/
    DATA A(18,8) / .00000000000004D0/
    DATA A(19,8) / .00000000000001D0/

    DATA A( 0,9) / .95768506546350D0/
    DATA A( 1,9) / .19725249679534D0/
    DATA A( 2,9) / .02603370313918D0/
    DATA A( 3,9) / .00409382168261D0/
    DATA A( 4,9) / .00072681707110D0/
    DATA A( 5,9) / .00014091879261D0/
    DATA A( 6,9) / .00002920458914D0/
    DATA A( 7,9) / .00000637631144D0/
    DATA A( 8,9) / .00000145167850D0/
    DATA A( 9,9) / .00000034205281D0/
    DATA A(10,9) / .00000008294302D0/
    DATA A(11,9) / .00000002060784D0/
    DATA A(12,9) / .00000000522823D0/
    DATA A(13,9) / .00000000135066D0/
    DATA A(14,9) / .00000000035451D0/
    DATA A(15,9) / .00000000009436D0/
    DATA A(16,9) / .00000000002543D0/
    DATA A(17,9) / .00000000000693D0/
    DATA A(18,9) / .00000000000191D0/
    DATA A(19,9) / .00000000000053D0/
    DATA A(20,9) / .00000000000015D0/
    DATA A(21,9) / .00000000000004D0/
    DATA A(22,9) / .00000000000001D0/

    DATA A( 0,10) / .99343651671347D0/
    DATA A( 1,10) / .02225770126826D0/
    DATA A( 2,10) / .00101475574703D0/
    DATA A( 3,10) / .00008175156250D0/
    DATA A( 4,10) / .00000899973547D0/
    DATA A( 5,10) / .00000120823987D0/
    DATA A( 6,10) / .00000018616913D0/
    DATA A( 7,10) / .00000003174723D0/
    DATA A( 8,10) / .00000000585215D0/
    DATA A( 9,10) / .00000000114739D0/
    DATA A(10,10) / .00000000023652D0/
    DATA A(11,10) / .00000000005082D0/
    DATA A(12,10) / .00000000001131D0/
    DATA A(13,10) / .00000000000259D0/
    DATA A(14,10) / .00000000000061D0/
    DATA A(15,10) / .00000000000015D0/
    DATA A(16,10) / .00000000000004D0/
    DATA A(17,10) / .00000000000001D0/

    IF(N .LT. 1 .OR. N .GT. 4 .OR. M .LT. 1 .OR. M .GT. 4 .OR.&
         N+M .GT. 5) THEN
       Z=0
       WRITE(*,*)"Error: Only 1<=N,M<=4 and N+M<=5 is allowed !"
       WRITE(*,101) N,M
       STOP
    ELSEIF(X .EQ. 1) THEN
       Z=S1(N,M)
    ELSEIF(X .GT. 2 .OR. X .LT. -1) THEN
       X1=1/X
       H=C1*X1+C2
       ALFA=H+H
       V(0)=1
       V(1)=LOG(-X+I*Z0)
       DO L=2,N+M
          V(L)=V(1)*V(L-1)/L
       ENDDO
       SK=0
       DO K = 0,M-1
          M1=M-K
          R=X1**M1/(FCT(M1)*FCT(N-1))
          SJ=0
          DO J = 0,K
             N1=N+K-J
             L=INDEX(10*N1+M1-10)
             B1=0
             B2=0
             DO IT = NC(L),0,-1
                B0=A(IT,L)+ALFA*B1-B2
                B2=B1
                B1=B0
             ENDDO
             Q=(FCT(N1-1)/FCT(K-J))*(B0-H*B2)*R/M1**N1
             SJ=SJ+V(J)*Q
          ENDDO
          SK=SK+SGN(K)*SJ
       ENDDO
       SJ=0
       DO J = 0,N-1
          SJ=SJ+V(J)*C(N-J,M)
       ENDDO
       Z=SGN(N)*SK+SGN(M)*(SJ+V(N+M))
    ELSEIF(X .GT. HF) THEN
       X1=1-X
       H=C1*X1+C2
       ALFA=H+H
       V(0)=1
       U(0)=1
       V(1)=LOG(X1+I*Z0)
       U(1)=LOG(X)
       DO L = 2,M
          V(L)=V(1)*V(L-1)/L
       ENDDO
       DO L = 2,N
          U(L)=U(1)*U(L-1)/L
       ENDDO
       SK=0
       DO K = 0,N-1
          M1=N-K
          R=X1**M1/FCT(M1)
          SJ=0
          DO J = 0,M-1
             N1=M-J
             L=INDEX(10*N1+M1-10)
             B1=0
             B2=0
             DO IT = NC(L),0,-1
                B0=A(IT,L)+ALFA*B1-B2
                B2=B1
                B1=B0
             ENDDO
             Q=SGN(J)*(B0-H*B2)*R/M1**N1
             SJ=SJ+V(J)*Q
          ENDDO
          SK=SK+U(K)*(S1(M1,M)-SJ)
       ENDDO
       Z=SK+SGN(M)*U(N)*V(M)
    ELSE
       L=INDEX(10*N+M-10)
       H=C1*X+C2
       ALFA=H+H
       B1=0
       B2=0
       DO IT = NC(L),0,-1
          B0=A(IT,L)+ALFA*B1-B2
          B2=B1
          B1=B0
       ENDDO
       Z=(B0-H*B2)*X**M/(FCT(M)*M**N)
    ENDIF
    Nielsen_PolyLog=Z
    RETURN
101 FORMAT('ILLEGAL VALUES   N = ',I3,'   M = ',I3)
  END FUNCTION Nielsen_PolyLog
END MODULE nielsen_generalized_polylog
