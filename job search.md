### Applications active
- [[Software architect - embedded Devces]]
	- BOSCH
	- zaproszenie na rozmowe kwalifikacyjna 27.10.2022 Teams 10:00

Google Tech Lead:
[[description]]
resources:
[what team lead does](https://dev.to/ksaaskil/how-to-lead-an-engineering-team-at-google-32jg)


online practice: [leetcode](https://leetcode.com/)

obecnie aktywne:
- Bosch
- Google
- linkedin 2x
- xing schweitz


odbyte rozmowy;
- medima.pl:
- emmerson
- bosch


inne:
- dell R&D
https://jobs.dell.com/job/poland/software-r-and-d-center-poland-remote-apply/375/36233242784
https://pl.indeed.com/jobs?q=Dell+Technologies&sc=0fcckey%3Aeff15de8be318fdf%2Cq%3A%3B&cjsFrom=similar-companies&vjk=170785d17fda3733
sii
inne linkedin

zrobic liste code przyklady

psycholog
treningi - mockup rozmow
alumni google
k.wilczynski

wieksze teamy
wieksze zespoly
agencja pr

pytania do rtos
https://climbtheladder.com/embedded-rtos-interview-questions/

analizowac kod stm32
np:
``` c
void Paint_DrawFloatNum(UWORD Xpoint, UWORD Ypoint, double Nummber,  UBYTE Decimal_Point, 
                        sFONT* Font,  UWORD Color_Background, UWORD Color_Foreground)
{
    char Str[ARRAY_LEN];
    sprintf(Str,"%.*lf",Decimal_Point+2,Nummber);
    char * pStr= (char *)malloc((strlen(Str))*sizeof(char));
    memcpy(pStr,Str,(strlen(Str)-2));
    * (pStr+strlen(Str)-1)='\0';
    if((*(pStr+strlen(Str)-3))=='.')
    {
      *(pStr+strlen(Str)-3)='\0';
    }
    //show
    Paint_DrawString_EN(Xpoint, Ypoint, (const char*)pStr, Font, Color_Foreground, Color_Background);
    free(pStr);
    pStr=NULL;
}
```