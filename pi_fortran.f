      program pi   !fortran
      implicit none
      integer d, a, i, j, N, C, MCS
      parameter(a=1, N=1000000, MCS=10000) !MCS - Monte Carlo steps
      real ran1, x, y, p, psr, start, finish, r
      psr=0
      d=-1
      call cpu_time(start) !start liczenia czasu
      do j=1,MCS  !p©tla MCS
         C=0
         do i=1, N   !p©tla N
          x=ran1(d)
          y=ran1(d)
            if(sqrt(x**2+y**2).le.a) then!le == less or equal
             !gt == greater
               C=C+1
            endif
            p = dble(C)/dble(N)*4.0
         enddo
         write (*,*) p, j
         psr = psr + p
      enddo
       call cpu_time(finish)
        print '("   PI = ",F11.9)' ,psr/MCS  !srednie pi
       print '("   Czas obliczeä = ",f8.3," sekund")' ,finish-start
       r = (psr/MCS) - 3.1415926536 !r¢¾nica od rzeczywistej liczby pi
       print '("   r¢¾nica = ",F11.9)' ,abs(r)
      read(*,*)
      
      END
      
      FUNCTION ran1(idum)     !generator liczb pseudolosowych
      INTEGER idum,IA,IM,IQ,IR,NTAB,NDIV
      REAL ran1,AM,EPS,RNMX
      PARAMETER (IA=16807,IM=2147483647,AM=1./IM,IQ=127773,IR=2836,
     *NTAB=32,NDIV=1+(IM-1)/NTAB,EPS=1.2e-7,RNMX=1.-EPS)
      INTEGER j,k,iv(NTAB),iy
      SAVE iv,iy
      DATA iv /NTAB*0/, iy /0/
      if (idum.le.0.or.iy.eq.0) then
        idum=max(-idum,1)
        do 11 j=NTAB+8,1,-1
          k=idum/IQ
          idum=IA*(idum-k*IQ)-IR*k
          if (idum.lt.0) idum=idum+IM
          if (j.le.NTAB) iv(j)=idum
11      continue
        iy=iv(1)
      endif
      k=idum/IQ
      idum=IA*(idum-k*IQ)-IR*k
      if (idum.lt.0) idum=idum+IM

      j=1+iy/NDIV
      iy=iv(j)
      iv(j)=idum
      ran1=min(AM*iy,RNMX)
      return
      END
