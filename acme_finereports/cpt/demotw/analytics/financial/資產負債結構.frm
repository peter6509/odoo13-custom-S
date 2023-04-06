<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="資產負債結構" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="aaa"/>
<O>
<![CDATA[資產]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 資產負債結構 where
資產大類 = '${aaa}']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="資產負債比" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT 資產大類, sum(專案金額) as 總金額 FROM 資產負債結構 group by 資產大類]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="aaa"/>
<O>
<![CDATA[]]></O>
</Parameter>
<Parameter>
<Attributes name="pj"/>
<O>
<![CDATA[]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 資產負債結構 where 1=1
 ${if(len(aaa) == 0,"","and 資產大類 = '" + aaa + "'")}
 ${if(len(pj) == 0,"","and 資產小類 = '" + pj + "'")}]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[select * from 資產變動]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds3" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 負債變動]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<FormMobileAttr>
<FormMobileAttr refresh="false" isUseHTML="false" isMobileOnly="false" isAdaptivePropertyAutoMatch="false" appearRefresh="false" promptWhenLeaveWithoutSubmit="false"/>
</FormMobileAttr>
<Parameters/>
<Layout class="com.fr.form.ui.container.WBorderLayout">
<WidgetName name="form"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Center class="com.fr.form.ui.container.WFitLayout">
<WidgetName name="body"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="10" left="10" bottom="10" right="10"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-985610"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-985610"/>
<LCAttr vgap="0" hgap="0" compInterval="13"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-1513240" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[1371600,723900,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="9" s="0">
<O>
<![CDATA[資產負債結構分析]]></O>
<PrivilegeControl/>
<Expand/>
</C>
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="Microsoft YaHei UI" style="0" size="128" foreground="-8355712"/>
<Background name="NullBackground"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m94j=;cgE*j$i7+0[lGE>'Wf4C8Wj!6kBV1UfL^c?tH4Ze4+^c&YeA!1dVfW7'S?(TOP;TL6
0dI+JVpJ,7-(X,AO7>iN!/R8-4op'FY9N'(S0Z?lsGOSDMFO^:*e5`fE@^:A3@fmBqE?[si,
[Zi>78f.?^eZTep*#[">)[FK0u"O*PD"T0\=agpo)LDS6.!WlCS>e>=D+/k0brh-j),D:+_r
X:LQ#^P+*@u^#N4o_j@f/G?Dd/J>ehYUND]At.k5q=bAsD-,2:D5n&>XH""bk8s&q&H2*rFGb
-KQgrQ(]A0,KF5:2Ljl2JN)-;=Z*]A.W%PF96J;eg4;k4\_$MOEu!X_e6W3.i1gP:#rV5o;5b2
85k<R.E/$#_$2gC4T[4;o=JSc:WWH;*"'a`[m".&!WZ&ea[cm6\_:T___u2%f=?SNkiYsk>V
ag7gtd--cl-Olq]AN@ind*p)nMAP^PM1ki1"6t_mKaNTH5=YNLN1\=M:guDgjR\3DpBjbpA+W
n<4C8k04YfX5SqT\2liKSV\gE%:E#3o!j+,%GHtqt%Q8F%C"b!t@i4iVKIH>*Tih5>`g,8)d
*sjSSub&QA_6kEq;(uXQ&e>bFXT<u)>t@1fcj]AKBh/de^Qg.dqSC%g6B@&pA%Z)uLF0F;_u>
Ug@p,9DZGNs\I+C)jd-JD(QW'=JJ3f`5o(=i6eb0M?7m!Bu+s>7dV_Ja!DW/8^h_c@[ID1H>
hN^cX3:U^(X8KMNGop!;:n(>lHW-bj3:4Ht\br]AGWuN@$js/?UTBh+JTI+Tt,_!,kCk%ocb"
S5(]AaJB`I7@;0$'[;]A57n'&IiA/3dhVPAj?@IJ*1Pt*DB!kLUTJYOo\J%OHn0/cJMJrQ@5$j
)3q!BYq(j'UPEcH:A]A.X$>LWU443=E`F;=+KdCIuF,@ict0HNqWM/3#qD/OQ=Q%,THi&P/nN
Ar*=%j$mXW)kqq^K$X>gm`-J>L4W'2B\T+]At(F(,/g_nBF#9\Pd5fLT/XoB-H\!e[=;V9Deq
r,22AX's,)KgPC:'hL0ifpW8>=7SMXSGZ(t`ZJ,4;;>6gCLSI85$Hff4KJpe/Ud5NNWquV^d
,LGV>Q1S]A2hd-dV$SS-Fp"C9!85ndKFp)P$*=C:q421tRC&C79[%ct1I'2]AD[$G]Akm^'ppf:
L)G&9mLZEfKQfP#>@(I17NR&u'bK5QGqH1s?7,)=Ica"pC=eT//VB&:jX,$5X8XkCq+05lh"
peSj.!!Sf&T,6J!"rTrqOq9kPSd8\2ILWD%mgD\)MRU!$J'XH7-r>)/MX5GBbQ0oK:Tka(NS
-k?U"kM7)9q2KA]AM[%?,$-miD;@?UBlmCq<^BIb1t]AaN-c(;;<IU%gLINCeJ">a4hKL=Uml0
;*K1(HH)!.Sn%fWPd3bE>'SQCfbIUg,cj1RqQ?L*p1pI0@%&q=[dj`"gJQ+Mb/*qCct?:AcQ
gBl[Ep"esme>.A92:;hmdKoZ-`Y#9D;hg4PTT+5&p)qH<>,[c;Sqd/Da?NFI'^Hj"X\XRT@Q
j<sQ7ZtOK0&PPkr/9MB!'dkAQeDsYf^0YP"$7dE7@0PFg9@bh9ne\7]A42gObEQ&]AZ(;D[R0Y
d'n#q[gD0!PC:q]A,RCQPamES.UKAO=#?XJ#JB=Q2N*!BjEU/g.$+M;A)1m%h+C;JXPF.p]AX8
6O%sLA,lM.mCF#6*;P/Q+d<<O-@-,1)F;Z;/=S;GE'.XGRok'm]AM@C!*49l#g!U=Wc!EN20c
`S9EocQZ-\=X)P:=\R<"B37p,3SP2,SInsPB&J,ljfFf4$4[CWje6FRLjE=_1-LLR0Ad/rg2
on#6uci\APd<%pu3o/l1hB]Ag6@F8+Y5(,(K9j8Tk:VU3%pV?B-'iaH$&pFg.GLlS9lM=FimS
@E+X\jSBI4U::1(?JB\6\@Sq$t0!kc*"/XSu'If.-pb%kt%*18S;=H(B*QG-E.$OF1mmRns7
M!UCd9keM=Q#M@JlE8Y"lnNsk=(1S>FBhMB`Yq?Ymq+f5T!:(alOHaAM^hD@cHkE0$:QjK\_
fEehc5kr7Kdq(R4e2%G]ADdV`k!a_7M(Y>'N,SL(#btVOIJm-l)1a9eHRZ<gDHp%cHW?Lm)d"
@)>=;)39h/miW,Yd>)h)NDSiR05Hs29nC7Y+*\nFPRLi2oEkIR-A7$3te2o\H`&a3;`DAFRK
G6t#E*KcXYHrBH+U&'$!Q/Z2h]AhuJ+naS=ad=:/%<Z3k5*tY)&^CqrSA$/is`J]ARko'!o[Zs
WL,O/nN+%UeHWQ6d&H3U5P/BT]At4eknaP+'bN1hTbQGm>fL<4!(8&BproD^&f3OZG^UOMf&)
XMXiN06E4rtXW\_gP^Ur#l+HB%.Idh%Pg;EW7MTscI,`LO.RH*Z5O[8rp8`BYh$rOZV`<^?l
>Mc:%>lu4]A-*j8m!s<)5-qfKk9<k2"NDT$a"G),9Om79kfS?r*Cnc<gRh!X[K4>6(H'C"Le$
sC]AqP97g0kgcgt(<P7D)tV(!<4"ZM>`g)+4&YRaAr[-2GMD0o<O$!f&XUrrp&NpkW%jh=(1g
fCb7KqfjlkWa8!$=!6*F610ib[a(E9%ZSU-,NN`pguFdrCV'E90BHmPp3Ac'j.3:H-Co3HYd
+7O<Hu>L%>eAS3pC;)V"]Adg8,*=:e%"cd.RK+uhFcV34r^ma22L>^l5F>JdIDGIA]A;m>eAl:
73./7pO>M&2))bZUQC@[CHLZi"6WQ@Ip1Escag?W#NJYT#<E<at[5]AXm\1o7F&#M#j=R#L)]A
WMZtq[Ont.<rr!<EmGP_X`Rj>t&O1d"JRr@o:s7_YT]AR%E>?'?HM[B)"_iV>ZQel#7d7=(j>
4-7%-Y(5e[r\6s3B&>nqP6]AO\Vj#*no2-%Kk.mHk^!%bUIPgo:$gP;0Yl\6?AGXqu5te^n8P
ABDDX`Z&b&N4*/qJQkM-m#8fbZ'Pq;!'^)s[='euj6[*:r"&(5._X\X$YM$rqWk]A7=AZ#*=U
JJgH$iDGAMJSBb%g;/A#SIr]A`X0S@Y2]A=rICW@[S)HM,&MX-C;rlj6NfS]A5&mq`P,_Z0RWd=
B8s+B?*Jl/X$fm#_>0-roV21DsDo<<m30Xg?Hl9mDhN5Lc,_:p'h8TV*3T\aI?Ao,`8\-7pL
s/*#,^F:YUeM76Ed1jcW'+D@[:m4XJT*CJ&$@BI4Wjk!hR&IB1W$WOg#4rJ3/rO7N(G(r*Do
IU;$8l->e3kj&Su-.3sBh;H$=c6d>oh/`.6W%d/9Sc2jJat^_,Itlgu:cbdkD)-.XdJG#<V&
9"$'!ZniC7m>>8n92I9%81qAH#q<H>/50Y"Z0.3`+(Q8(`9P2Pdi?ni<;]Ajtgf)+XWaXIb')
&%b_L-!"$0n8H8.PnT9FWLQ+'0+T(f,/b]A,0!Y*E8SJUQoIiOe[cf\X5mS,W/4kbcFt9_=3V
5SECg&,6S(5P&SmEd56(4F;dj(D.)Ni;=kRW[2ZpJ'ZAAbAOT(`o%jklB$lShh$BoY0#'=-\
-icTn)K4o6]A&3sgb60'G2>k(`led5U[iHYK<?W;/M-3f9G=sc%fs.'L<^0.c`t!+#]AB\]Aa;!
nuFU&\ThBN\j^riY??e-JW0S31;ToH:Xi!EFF`33qX5?-=V8$V-#%q.dCbC3b/8<T"1`uNRq
go7p!Hh`CX02tgW%%NYp+2TL44t?``'l81&Ho8?eKGUtMUL1(,@`9k$lb/rc3T-0Ud`0:4Td
Y9;I(grA>;ngeeZ$R:]AZ."MfI+QG4b/"FCs1Ua4X6e7n7q3dE-*/i-cMdU`3o$tbdr@]A<jSr
le2\+TbL.^Beb3?H$u*qDWoJqtpMd>9&FJLW-nSQMDCO!lY10<D5A@1[F'_EMQrM'GhIj=^W
fr6OJ>2p6$;(qS:/)LdWL2YLmM$sM$Xa;V]A`+N:V(J+d-FP@n]Ar3aB0@B/\B(kA'g"VQ/j"q
(RfYbiP#1:'V7/LKtRRY"\X$UAg.c^]AfbDIb[C#2XTGiK=>b^b5lLt32!HW-PKNgK6>5X#eY
R\9\qbiniK#3,W:mU'V&7TjT3/n?jQU>ZsD!0>(`9Sa4F)lb@:PM86n))S<p[j922a[n'E-O
8Q4hj2/sp.Qq)rpffV4")C/f]A2usSm,/nX03eC,?"?:<bj/BC#GO0(P,$RV_I+9'7,A\l[i&
a[gXhDho(8692:Tc%c:(mM//::2)J+b*TGZ"RKdZiN95^d[e5e6=74J:$4[rO2-jk9#(c$3n
A#P1*]Ag^\Hp_TiF;+ltE&X97<sr-S/]AZ9e6B$ck`+QpJ;O:Ko`AS&VfGhF(8S'RemG<$0c?l
^R@)u\Y:gu6SYbA/Vm2fTKHl#UnV&MW.qkLFWr:4`8eo.NWb[b('$[Mh$O#B&pi)#sl41BSF
l9+%MQD*AsaSo1-p$P2Mcqnbnm;Dbnb+W;s;OL0Y'73n4Z/!lSU/0O?RDa/B9UdOh7J*:lKU
2_M]A9;B_:ZiU;@gt-lHLu76*4MsGg,;g>GuZhmb$1b24mPs,SdGPLn4EO4E?6Vo5lgL[@UX\
CY(4]Ak_@Y+reY*fOk<,[S>q,Gfdi3Q#\#>3a&>u"t^kIgI7Q15bfk1"e/8[-"PPR#q;pWlre
>N0m+\d[?d<0jI4,nRY,KqWGN(mr7^h;RQ(Cs<jk_O:1CuQN:(Y-X4SA.l69dMlYl,ut]Ak)e
rcEr$Y5l@l@ZZ2(6#"ejenkqRm^=A"a_fm=g!>ur"KHdbl9+&;DC(c/uC<n<Fs1iOS0:Yu,%
s%$;&1f?BdPk?8pC1%'j]Aqf]A@dRBo1Q^9't)_lC:Q"iuEc0I%F#MSuJ.cH4S'red,TTUXJ\F
d\>!sE>8k4K3d\nB.9crfb6UNaU.HkYQGh9t[H&tW/]AY/O@25K@>Ok8H"P*2\V7>u=KAeU\@
K5p,L1BOXB\,3JiQa7=Lf:?QAt[&&\iOnT76:n8dGgWnL"&H@KKVB3NU/N<J3l7l=c\3PZop
&[a%@VV*B21/?-JjLN,8k!M!Z;KUT!$>L2Xqb[TMf]A?WREWY`!%\j:H;nmgL9`jl9[j\MJf_
#gQ?!GkI4KIjl`kL[\)OB0ERTK:]AaEm9d7LS0E*RPH;uFE_FD9'?G`rLsdA)h6bF.T$/U*(t
S2b>?a\nudna>Vrf'e"*8F4;@-jhmr6Y*%0VfK.Na#[-MB3WDmQm931/P7_)_Ge/j>_Nf70n
8#sUL8f`YQaRX[D5me&ccf"\ZhU66/Y`,%M<)TDD`I]AfRPb:%CO/LC_7SoK+6''78<Ufgon4
\#,o=D8B`LXo8[7OY&X3VP%b[kE,-S@K<^C8b5J6rCl@78hk.toa4Y"`LU!:YH)UZE,q,RNb
I9!)bnscBAF!ejN8Jp=:oIPTYaFmJejnc>Fq!l[F`X5Kk.m,a-d..>g3pr!EiW)F+jh__AFG
uq8riDH[tm%_j#TlQr9c=7G%/kkM6G&MODj.Bi4U_B/n,Nn6TCfq=$(@eesk;4qgkgn;]AjLh
g`P6qT#F>M^GldqD4`@NWa)L'(/Rh]A7Ed\7iKYf@m5!uO$G>d%KAiP6^5/T9oFC'fmu9tm%H
Xs*n^$<p_A4)UjIZ_3b!qXQ[C<#fn0]AD1Jdt]AeA"n&gY2Cg'f_HbmU>.[R`00X2n7cRbnl*#
;GpQu88\Ig*U^A)i*i!0-cr_8=6?>]AeDQB>]A`l[RLc!Wbi&'iAO,%pL2YY0q3FQU#p-;o7B+
mWZ?oFCFi;Mk%Y`8hBE:I2:D.lZD%'ohEa+m\a]AF<tUX8.-p'PbMSh)4hnk,.2X+T$iUiVnl
n]AV9iSa@W<Df9\6CMlZN!lc8-B-%takN\P4+B3[qE:4;ku4Kc"_>\odWBZka(8LJqb3Ok>ih
"GHq*U-5T_=S4)6jiD;mWV>+"RNbWj9Ifp&5Z<=Hib_`>83BJ?h[2FR>'<Y=Bbc)aQQt/A+n
Uh5',(2"E^tq1:G35ZQ"e0)&1+2nj;(CQVan#+$9]Atb-L&^+%E"67-EDW@GFsS43%aq%WF"'
qMed)9_!c^iUqOb5N79]AH2oPa)`?:9736-.!q9(g=B'_-!VjSPr8"FXNK_rQ1AarA.*d]Af&0
#q!tYPs=m38@&'abil6=C@DfJBe>36;Oo&e3C=C'e]A;VmVEuh=2,2UT![j4'YRBVr40`"69@
m88gW:d5dN^CgVBV>(tr[:Scsr/?)\ei2pl&"qck4X5AdbTqP8Z5@`g=U`U&V(l,;\(MP<`T
;/S39edf)`94eh1kQFOW!IQNK*./DR_Sj9pk/C6c]A?+U-IK&\7m9GAS"rg_4`'RJ+p54eIkb
j&WK24n?Y?'%ts5ZaM=RT9<jVkI&^OPStOZSZ#<$h%=YEj:Ra$r6QfX9suk3OcMGN`!'R8*+
]A]Ap_Qn[`a@F*I\)SLl5\)j"WUkG3D3KPo%lgpiW+"EB?p/k,$gh)3T')m;NMVm$2F$#qkO<=
Ier!b,.e/aQVCS6#t"6GZnc8MUe:]A=#e;V-eI5&+3<>M"0<ICLMcQPXjmK31L*U+TnaIM4QK
s0Og1C/^3*]A.Mjf6\1g\C.4IsoU)ktL.D0_j9O5L)qk^;fV?!N&>[kkQqKj1l(FTGu9+&f%8
/h\5OG?&!J'tH1op/d"^pEZ+"P!,rpZl6:mF)$;p)D\3u]AC<t+ar5<>S2rtlOk#P3St`RG.T
&(afYa\^%q'h&,O/_b6CE8/[<oA]ADnt.o[$&r[0*o1,J7[a6ZHd)n:5QB!dTo`acR>+uML0J
ZB4G4s&b._tDN$3nE(1aTpuM$3;SCBkcKcoN^SCfLciZq-Ymn]A7""[;NHn0L>K4k@4BfW1(A
&^3m""u%R>4ki;m801[X1OZCHG6:<.%o&pCFEK6)@I:IYBDbh!`@!=Ob8mc]AEAEmF[h:q)2\
Q&:%=)&3;>%h1*5)n$k*Os-]AT:+mFK<6Mpug\?14&R4s`.UWH)fTQ'n8@cE@J<j/M;>Z1A$R
ZE'L9X/e==G`(f4&LTnQBcI"+SJ'_=3j$K/nX8^+)_ju#+j;asbD4,t?/8.0<7/=KR(S;bCF
&]Ac>=\u-4,e)@-Ml%uW-ONoC)27hHRX[D(I4?6aEI03W6;P@WPiE,$!.mLaD0#$YI2%-Z+'>
AF*7WFMEG2DT6VNZ,+dJ\SE$<^N=i2>]AE=j%^/!97+\#U0GhBO%;CaLrmX1M[CmP4hmWj.b3
IGm16rD:nMN4.[$&Jg&T`tCWDW-jS-;XcjO"Dfp(tnNa-iY3>^c<H\-P)4"Y^!9nCJ>a=fr"
174b_G!Ls&lGeSnit,J>0p@e0`pfRr@Cof]AIb&EoH^bN%9eF^5M.LP85#!jZQ)c'iP(9t`[4
7c)bQ^E*%kHTnf"kNEQ[HUOF3O^<B:RpB/kCcKC]Af$7t!':(e!-#2J'U3mm#5$5gI/`(q8rL
cflWls*qmuR!UEXO3b%qX@m'a3$;H@MrRZ17>tj)%pToPAIlOg&YsgZeBLJ,Ft^%b:FaUT'7
KnnensG#-9t:St%(CH(XZ%m87`d*,tYL>!JZ;GpDoU>!0DXdKQic^Tg(qZku`[5Q:"&_I_43
0g\HVY!AC'B>ih5o78*'n1?q(aF\QBRP,Co7[LObBN-M).S%t>[KA`P\Pk2dr=8uC(NbWW's
g'OE*uV_+BG:*Vu'Dn*_OE$P?VXButis^NIU\C[VS-Z4jO)]A9'\qYIj\(La*2Jrq9#>Odd^W
7gJ4-k9P=3a1c9_=/^Hi;:W0r\^IPk3[Q`]Aihh8so787ub=M06cQCqjMj=Z]Ad1*I$`X@K!T+
9m,Q)Qi1%d;.3`e&J0s+4XrLg7jmqo<&\pM[C&s(u!?gVC$f[ZZf:*7Y\GV8)ol1$T6<TIJ*
TnShDid[MCV0+?G;J%lP?$oAQ4>h"`.,)7jOPdk9>oZc'dUETK+"!>.;Fs0!l[c9Q7?.%.lh
ct1?I()S+DjSqFSMAGm$I\.S?pca0Q=V.K+.K$tnH'+DoW7ESpC@CWZU@Nj=</L5o>N:PT$h
)>O5R9d;g\AB>l3=cCoBcu;d(.0"ql<F&5$hirDBPUB1e0YVH[H6b1c\JCsH]AN25=b1&@65/
+P0O_Mfc:P:@TaVXRTFt0W(,!pB,W"1VUC?`kfI%m$U=Ca@-D$S^"JZr0FJJq\lCL:HigLC2
#rKU+ZLg5Zl_70@@eSIpa+%RY[c/d8uqgR2M;pJ_%?l=Ydh$,n71CD<S"dTk5Y>?]A#t^M#:@
)'*o/njKuq22UO1,=GThR2JKZV.Yej]A0(+X5emgb[_XA'BfjA9ck%)DhZp+UtrbWN%f+qgHT
,1C_84@ZA"CUc<+)s]AY3t'"Z.qchBYVMqtq<=`&2U*i[bdEpQk6gc3D'JWQ'6.WS\lP;Kpch
@7hij;!Vj#O:i)?sX$0_aNYS`rd\;kLMr\Hl?JE*lBckmN@*-9Z\`-0+(U[QMeQ>!6H]A)cW&
_:YNZgQ@$C:"gM?`&p8k0X(`9<5r$t-@GEO)(A<W(]AU$K(YR1P+((m'VXHo4Ip#tlktiS1n@
t&/qF[-B$qW)sE!tZFTNqi1,3g=/,$=A$RVM#>)%,-2oJa,3(bQ(c[u?V/A'oCk`/K3\iM/f
]API!Clhbd/Dnrl0gk0fS<!p,\8&\gOnPuT(G$&,`$bkjs1q^f"b;kLc#3Z/5r]AB!'IQl\U^3
kIa6O7'_UPg`QCc8i:/S;E1[q_jER<m1q`Qg7G'+*Rg)c6/?'`,D^=b[j<Y>n%IF,Ae!9K5<
n^8$Ff<qpV$Fq`Pu;RfftY'Re(\J7HXT+-o<UNePppLqbDd=acM8,jBR&d1K:YU,pQE[V/)(
XF]A[[]A]A2#JURSF2i,7&JO4f4"O*hb,&k7XZ+K>Ufm`Y[b@Q8Fg*oL_nU8jVVi5e?N7q9r2/g
R+i2;#-Deht6eP;Z#A]A,fb/,<57cK3rA+I@C$0bHupB=?8P5=,X2dK1N"NV+qt8>XLD1NA\%
B+SGXj*@a)%0R;jYb08nhk:(0=n<QD'dVn$\%a(@bQ8JSjK9Z%f5LV_]AB7C@7<YkAt`LKYTL
Q&P1&!/h`Oi;A-A:#^;<tR(!5E;mX#?ie+4N3(bW1cRLr,t"q6ajB\+j0.'_F99>8$J[KoS>
j26nGb,r6BbEm+hPeG\eg,(U@JTn5iJgs'Y*KU@3j=XT1'&E_JaX+f^ih/L.)KCr`@X)'^5#
.H1-]A9"Q)U.YN^[j61AkG\miNVC+4FSQu[D+^/a_,b7$OO@SHVZ"7@I#91g',Gm?g-!CEaY+
"CM7/XqfPR*D9Iub3e<ZU(7pIBeaFaKQj47G,E2RJrkh>3]AS?QUV,ZPEF'NBkiKTmc3X;qOQ
:KmqQgmg9CC\o1,o/?S06@O/?\GMX#G90n_5WY9%q4c6lQZ,IDMD,D7t,&4H&\_pkfd=Z]AS`
',!-odE-bJ@MG%[7Tqq+'=6js$1e/`iCP!HRJMHZ8Cj+/up/]A4<*Qm6Hgfj.as'h7=CMtW>P
tEl_6t\g?tQ'o3f@RgrF0VZ\As1B1oo*o%9##05bFZOYCK(qofqipKg9>q.UoT>*&TZjSu+X
7J:@D4abteO?g-*Z*!>ljmIB(fDj52%8n*l&8W3173Z;6hQHfBn[DI[BW:6SY4]AkCAn=)B\6
@hG5oH,&?a*sujSGLt'A@&m3fM()QV;c@:"<k"lo^0kjhctV^#.8U*j2BaqcD_SY7:Ep:*.N
HXb65U?f-6]A^II0[IaA4oWRPQ.rr\*Q'O:d<ZBI'[_t$O$+!M&T0_+<gj:ZhZ%*3bB^oVO?C
O6`d/_NkGX`%5b2p'ls*M<9X^&@P=j=i:)O;(;`ENX2`]AOW\($G(3s7'=A-H5U15!(PC?U5b
X#,F4)X5jKf(DJ65qIb\P2E+Z79&P03r7k`2sFnh>]AJiTJQ)il8+qVBc@X<1p`jkW@(G4g?&
e,K0/6/lh"&TtT?KIOtNerRWc$MQ+j8eL1\#nf(a7pa8m.;;)E"</["5Lqh@fOSc/,0"Yb7\
-sJL5!o#;&$rQ]A3B#K"QMb?2.bo9s+%X<R?IAfgHLL5VHZsl;&i)I2Ri"68/X#t7F-I5p\eH
Ipjj-_%6N]Ae^'5PPl/9X=mgK'a@"V(Jl6c:d+oCaqAT=hi5S*^]ALlHCY2.]ACT8CnBng<dq8.
Ni!BPmUtMS4EuXfMbN7>#>Q4!&QM;P"7.BbEZc$.qIu$h^D%f-]AsKSSt070:IE(kQIqrZF@4
&F,Uh+c`$6j)P>UhP_4=0t#ak]Ai?pM,uIFlr+Pl^Bh[BHZ=h>6^)lMh%~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="962" height="44"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[723900,723900,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList/>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList/>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="962" height="44"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[公司資產負債佔比(聯動)]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="SimSun" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="3" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="aaa"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart1" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10895413"/>
<OColor colvalue="-9792814"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="資產大類" valueName="總金額" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[資產負債比]]></Name>
</TableData>
<CategoryName value="無"/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="274" height="228"/>
</Widget>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[公司资产负债占比(联动)]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="aaa"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart1" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="aaa"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart2" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10895413"/>
<OColor colvalue="-9792814"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="资产大类" valueName="总金额" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[资产负债比]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="44" width="274" height="228"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=$aaa + "結構(聯動)"]]></Attributes>
</O>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="SimSun" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="3" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="pj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart2" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10895413"/>
<OColor colvalue="-9792814"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="資產小類" valueName="專案金額" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[資產負債結構]]></Name>
</TableData>
<CategoryName value="無"/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="274" y="0" width="270" height="228"/>
</Widget>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=$aaa + "结构(联动)"]]></Attributes>
</O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="j"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart2" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10895413"/>
<OColor colvalue="-9792814"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="资产小类" valueName="项目金额" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[资产负债结构]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="274" y="44" width="270" height="228"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[結構]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="linear" prePeriod="0" afterPeriod="0"/>
<LineStyleInfo>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
<AttrColor>
<Attr/>
</AttrColor>
<AttrLineStyle>
<newAttr lineStyle="0"/>
</AttrLineStyle>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
</LineStyleInfo>
</TrendLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="SimSun" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="false"/>
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10903341"/>
<OColor colvalue="-11184811"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-4144960"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-1052689" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="專案名稱"/>
<ChartSummaryColumn name="專案金額" function="com.fr.data.util.function.NoneFunction" customName="專案金額"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="544" y="0" width="418" height="228"/>
</Widget>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=$pj + "结构"]]></Attributes>
</O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName="新特性"/>
<isCustomFillStyle isCustomFillStyle="false"/>
<ColorList>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="项目名称"/>
<ChartSummaryColumn name="项目金额" function="com.fr.data.util.function.NoneFunction" customName="项目金额"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="544" y="44" width="418" height="228"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[1143000,1143000,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2095200,2095200,2095200,2095200,2095200,2095200,2095200,2095200,2095200,2095200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<O>
<![CDATA[列次]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="0">
<O>
<![CDATA[資產專案]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="0">
<O>
<![CDATA[2011年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" s="0">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="0" s="1">
<O>
<![CDATA[變動趨勢]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="0" s="0">
<O>
<![CDATA[列次]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="0" s="0">
<O>
<![CDATA[負債專案]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="0" s="0">
<O>
<![CDATA[2011年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="0" s="0">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="0" s="0">
<O>
<![CDATA[變動趨勢]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="行"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row() % 2 != 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-2166027"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="專案"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="2011年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="2012年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="1" s="5">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D2 - C2 <= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↓]]></O>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="160" foreground="-539827"/>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D2 - C2 > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↑]]></O>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="160" foreground="-9579341"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="1" s="2">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="行"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0" leftParentDefault="false"/>
</C>
<C c="6" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="專案"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="7" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="2011年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="8" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="2012年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="9" r="1" s="2">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[I2 - h2 <= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="160" foreground="-539827"/>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↑]]></O>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[I2 - h2 > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="160" foreground="-9579341"/>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↑]]></O>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-10895413"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-10895413"/>
<Border>
<Right style="2" color="-4144960"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72" foreground="-13290187"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1" paddingLeft="0" paddingRight="0">
<FRFont name="微软雅黑" style="0" size="72" foreground="-13290187"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1" paddingLeft="0" paddingRight="0">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[¤#0.00]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-13290187"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72" foreground="-13290187"/>
<Background name="NullBackground"/>
<Border>
<Right style="2" color="-4144960"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[mC[^,eGIub?4%k?PbkIZ;p#_J7:R-s,$VMBV]A=B!m)GW5Pu-/>2e7uk3g_Wi'!dR/RDh2qAo
(s2`r&;smIU2rmbar"rOj<9rdJbrJ'IYXpZqL`Y35JjT%EXao2o@$PF[u*Fl0o]Alo2(S]AsVe
9!RSQ/%"a8%kb$("QIPBXkHK*hWi?XZID5\8<8,j'3b1;oj&)cBr`J_`P,s<u2bt6jLt[]Ad:
Cj[eKrM#BA-i*QbVo%T^oP46H$CP(ki#GfciEj/?QY#03Hch!iPfu,PoM*sQt/Mn,0Q\FI=5
r:c1RAY$$_("@%k?!$B0r;G+5),24IegJ=s*:5K#d08/(&0l5"hPENC9a,dt't0)2U7a5]A_F
`,1ObH^O3.qG*p.id-mqA)5#n\J[58RuYOXZa)'d_He3:`4`hZT4rPb-7^`"HfF;leZm`!3:
n3j6?WjJkH3rAo>CK)YtdFX--V>!<[*H2)UUYV_;drc'23/pRH?]AS-fY%V%JdmUA84l&;UtQ
;'a`bh_%D%=P.Hha793J&7:MgDXcf3IQ77%ooJ)pLXheM$eC\$"IjAI9ro%k%:XA^g?+oQ8_
j&KH3Frb>r[N;(Ps^Hq8#EgYdR2WcjZ"K22JD"S/"A)p\@HUO&)::bnu]AI*AX.,[*UA5,Et9
OFWW,Bs,2WN'2.)aGmAk-G5//T@bY_TeI"=#f<jRZXKG?[iM:BsQIB1)%V"I]A%8arPW4j0i-
R^H;9PeNl1hk)M8#*d1h%2lIjRX:@,B?DQHfMmuMgC4o8ShL.9o31SFMKhCN20Q?C$8`',mO
#U_T!K$q7+CRZSb@,nIHf6qW9n?fM(I!9k3lO]Ac$'l]AfC%9>WY[GGE?Zd/3/RaXb6f&7@3#6
U5-)]A&e`_e9-hM2TVI++P#3hE&3=d!bpHI:#-.W+a2t3Oc8TAQY'&gdQLu.7sNEApo9.d;,5
+9dBKUEglm@n<1C(%*e(NX;VaO)5f0e=Z=Y9C;'`s_8+,\45#/\6t_l4Su&oW\U&QNI>+n=W
LQ\5VQP@+g=Hpg\u7l[^@&]AG.8f#0!"md3ed5#BFNNi*Mm$)IPAJV@0RG8#Qh-)UUu_=_*Zh
\rhZ)]AX'r)8)KLe(H:E=im.Z.BIQB:/@tG-.D8/18Y3E01IW(%M)u(tBSI#Fr:m#FoUm_@pP
q^$p9)LtQ2E=tSRZ\*:Nfi-;e#S\[o1`_flhorI3^8^7hs1dLmD!Le\$0.EX/@oCn[d&a&k/
E1nkki([f9u5a4YP+18f6_!YaYWS]AJO!SfXIq5U]AeND]A139$L+7kt17"r#C2$-RX`<Zc7/HG
g_6SNF]ArtnAdn'IinW6`/._ue"aP2e6o8%oKABV'$Ye?Q=FW#8*f8h3'PmiP-Po84agom"]AI
l[6.Ma4VjrPJb##+3aio7>Z78'9naj$P2<CSX!h:At2oH6qV]AW'4O:QZPC-8WAV70#K^'CWE
e&EhR_h9FX6a\V$%-:+g1^d+(,.0GgZ`0^%<.lYn;++#b.qo_<kg`(Kf:)3ZKqL(NT]AIV$Dq
ol&j[N9dSCQnZB>ki&@DB8;N0+"D<hAHB<f^>H*[2j-[b@2ed([aN'kGLLQ)+d1`,'Fsg_PG
&^+_c9[R$pWZ;^jAog=@`Ho=T5'UFPYTujEsh9]AV?NMfQ:'VQ4k[P(Wa$CDu7;]Aj>>`eNa^P
@BS38CaRt8Eb@B((:M&J;<^lfH9[VLi^KnL.-f43B+I3kD-A.VUq1,!iKK6YA,E2`(pZJQ\l
lNC7@FmV$/0(DGNufS=R`sD.a=.dl_?.Sm$=W2LEF'0XuugU&rI*#t5-\k(E7OUf"R@UKG[>
]A<,0E!ebqRGS*CIB[hoMJ]ApdX3-68mfq.=:P!%f2'Su\fq6W;N3d6WU>:um_((>:hlgb1'$O
BOj]A&i?aNijr:f\<>Q!f.++@L,T$K\RfQXT(W\VipkskWtW;Pmcpq\Gb,HZO9BNG)M:D=YTX
OG,2a9<^Yud[BPp64q+`*Ke)G7,(`jZU11HBnt.Biag,53CWZG<`p%N9EogRc_7&rkAm:n0F
dfUKo?pk_lM]Ah1)dUg`G#Zgi5`?X6=jY_t9't4s"@95!qr[7UXL7,sY!CAb2Q-m3`mjAgrUJ
.s+IWp68GKKL,c<k[63tE1j4k0qCMmsYbc9?$%l/0]Ajnh?R?+DaVg%##<^IQ2+\'@W^c"r2<
>7r\)7L+nSLX_:\[.bSM<7d*<FWhL0I`P2(UhcI*Lln^TIp/QLN\>:+]A2JQT:C[.8YDgNS"(
+r=o2Sc@'aLr.6Qg/'Z;)S+-u2^oBaQJJkt0J6ACQh<,@\oPlna6\SPNQ7C=@0CUDlJ#pU[>
gi(FakO6$Ju^9<UXKl!X6-E78u>CTX=hT30*$Jl]A1%b2hpXVOW/_Q6?(P*JuMk_Y`F*dL<;!
h>ton7<)Vd:"FpS"FWIZg-`EeWT'shAFH3eROmcqC)]A5ej*E#r';mQP#S8c:R&Pl`aeD=6QR
<-&2FA$6@u1i>);DDp$T>[<JEIVgAK19e[mU/FDNRhn-?8L/N.DTHWnAhBcmQ8)=oUsW>+PP
P(:!`:mb.dp)jgDT!mQ[G+YFlfYH=p)E@NEn]AqVoA_U8=R%18Zo_)49e#JeSi`"cNO8P24BR
COR'aU=AA@*+7-\q5t/9ks?5Aqa8Q7bBLX_?PeN;$a;>-n$Q!Y-WVBY@R]AR7q)e=hnVN\6'*
9K;bB:2XO/cmBs_AkU>^T((fF&WDN!Eluf-kTmG-*iBg?L/[>+F%TBlJO-V=ol281LN<G^]A5
`DU5q68L7NBC//_qUTZ@:lb@'_T-g0+52<kc,<@8R]A!fBGL?gi4*`l_MArJHb[[U7<?4cPaY
L@YU$?!Y\mlLVln_b=N8P"'=_%n$J9qi2]At2_`5#%WH24GAH!U)X+X1psem=aRUcL[V%f(:P
4#JKHW#&O2=U3On@=D0XCHh9gZ,8J274/2YX(A.m@As0Sdt%1DfP%n!TghZJi?b;S-0ge&<6
/<`-M?ttql<RnaF);'Q*?=JpXS`U#GFF(J#!*I&BrbaVrt[q^s0*_&)cVmG\4V`i+p/6RO;+
PlDIjpW_,an[\X6+6_m7#P0mt*fZ;1&+R*32gYMs5DX2$un!Oo.CXJN%_X^s"_NcUMa1m;_N
&e_t1<6]A<',"L6RiRrbLGN:h7`I=jKM:si.M2$]AT(4e9Z;*kFnFOR<-;]ARoY,<1+<+Sf618^
RVke3^D+[iW^@X&K_o+42jWNG(nI8APc2/RN?()6ifDIgOLn.#UIa^L87r>37C@/^$NOZhN:
<-I^h:GLSJoPO8//6a3@"KJgNm9H+$3m%&:de0c^h4_@k`"W5lY2B;TT_iu[R6/8UKjWZI?P
l3Abo'.gqkVa_YL\m0j9fUa<Ocq9,+9^%a74VLM,"t-;,5GS2t6^W/;j5)`5sf)r'fd`_BTd
aDNKPJEP9tBl[@$,n0p<laFQ[=:'"]ADG5KR9orCuk'jXGuh7[_"!]A[*q`P%RN9jA"n-sf<K)
7KsSce>h-2VbJXM(5kkK9H\7^LEnu/qo8VNZP?Y"Ih5PH-.A8pMT%uMk4h,o+*=sQ>O6brTN
@F[2`g6)e%Hh`d/D(+'Vsj!9&=,<biW&(`[>1.=Z2uW'O4$iI=F@_h_e)0SGd$1;Db[^gR_p
6c-eY\)B/ZngIXJ$?BtXiW\Z)6Kr!V[1fC5f^f=HTp.O$^N=^3FfX'OYG(U"++g[sW/Ef._A
Abh7@QC/q'R5q0,`Q,T!D7u1+i:E0D\Q"+a;mNVD?g_)]APAL^iJ:!Ro%s9lEuD!K?)?.cn86
NE.V&Oe1W'^%VC$u>nU\dr)@#d#G)ZUG'7@7r^'!F/"8iJT=&=0>Bs%[)?[QB*:-%%bt[SLc
YZSL0.f0NA9$r$B75i%*::fM;NbFPbZ@:o61;520Qi)rlg[4]ANKg2q,XJ]ASG#)GPfAS7,X<7
b2#ePchZMtr<9VER'E?eeW01p^6Y@:rrnR_gCUQ.`4=g;,?<P8i3[$ViCJdWsYXCX6;MTM_X
Ic0E^?C&h?a`cMc!!8oeNYQ*/`<mEmD.RbRr(*QShPTb`p7-qlp(dKsPO;=:iS`LkT>+sECB
DifdEac.+4id<=-kg.GtnZUKIpHOMlkG.:H2Ne*QOOVhLf!Xb7%Jf4(\8S?HHmuJrLXORkJc
0KBe=%`krU6*#Zm!;,a8*8U2aJPCGMp*O7TXmG#kH4]AYgKM&u-.!N0ZQMH9U"Z+*N%EIkLPr
)GddL?btfn<8H:EQ9EQB4=gEg\&cDhjt[In^VD=L,@,4I-P((E)YnlC7@d';c$Q(YnC1@q$#
n(m=dcGb)%HJU0rFQ)K$>N,/[Ao=abI0NiArT#AVS=dV(B^Q5eEHF.1-udt6cZg^8H[\bRSs
@9TR/4mrk?Lp/ncjMAhllFFDc-3Mo@HKVpP:9GnUB:ZmIm*4)@g9Z'-K+q'bf0sp:RWkIh*_
G9-O<[!!E4%YKIkNJ'_<G6'+bQAY1$7'3#i<3#L:GX(\q7lqC'c8ghgq:I\Tm2VO]A8;KY<0g
]AHe&L>g&Ci9T$jKShO#6.AX]AQ-[5H9-eu9ZKee'!SP=5n+nc%C=est-DGPt^*>1^0`a%NPp$
rWbomUObj1GK*PL8]A33!n"bdd/8ek99+/bA:]AHQW97p"f"GLbb`CM2a2HML_&K)\*oKuPh=\
tR0^9sLNEXpGgs]Au?0")CVe5D(?qZ1Q[<J6_9[g@71pa%CLMS1M.(I3tRHj1eA7r\U]ATRjT'
S.i?8:Dq0MYOJVE'DqR]A\4AhA:[mCs-j@ToUMi.(>Y^kJjW6U#pTVIu.hUq*Bu@?.Z[l114&
DV:jKf_I_471Q%<WI1cN<\_9XlrTSs:N,)DYoBInkt*E4*/L0L0YK;/3]A)pI<Bg$5rN:4NQW
ohoJRKP;2Z#?#ZVt[Lci>&ZNq\p=iAkN6TW!3+k#dE>!4!H,/3X?gqmJ"oTedY?Pf1'f9['L
b25k[7jsbW`0,L2D,%X1tWumn985:#h4F1J6?(@+[mhkpW>)GO@d,a`u,1)X`h@(YhLY/f\i
Lu&%DD2U0.s4YW4jc_L*3:>K[M3O@Bo@^VL%5W?_q@\?GN+E`(r);=&pJ5"(I7*Y4Wr9gV8d
/'-V8=]AZNH(q18?NRR*?*\8^^DlLC;XdW=D28`?VUn\n/W:r(H#B"V^)_0.=R5<[C"q\kAe*
XY^#f\iYJ]A'SskM;B*:mYu^9<DQD-sV#q*88@3*;"b2@&@-JH-?\7Ee2^Cr!eu2BDCC3*klH
2N^GF(BjEYC5XcPE]AtXj;&eX3pe'k,9&l*'PNmlR".%<$-SrX8Q(?FX;,S4MXr8RbY=r4U'L
`s<5i5!<bQf7pNUsE^4mnX5@/mpS[BQC"&!D&N_9l@V/^N:.ncM7)q1Lg+.mmCOq>=S\SZ]A`
EnY8tI2&mS3ME(fg7MoW?,/fjVFaEVH0Dp'ftQB2dsR6YnQJjISAmbiaQkX6rQe5$ko^KC83
c7?XImO\YO%P93TXuA1&+1eZZ-1U70-Nc+[&>r.3"tj)FI_po>3#g%CXcha'\a/5+R]A!>M?5
6UK8F1V&]A<)o3DA']A!JbYqRR^H)U\[p#I-kZ1J<%@5<%(1(Xap?aik1n8pPZ*PEJ>."D@T*V
0KS0eL&R8,&PCU3^Ua$uD&(_$`5uHQD#,((:MfrbtqJ8W\]AI5*&8]A'O&0+0;^Q)S.kr2C-o8
jIMa"tp5+*HZj>1F5%7+T9P)=_j`EK;DHSio5UXWJUt6;ZAY7'K=5%OFBu'??)q6GXH9mg#9
(qbrroYntT8+@elil[Ws&%Pq(%N9=ld%=/1?BB!Z0&oDf/HY00b-ANf>tk-2`jc]AlO1d>9N)
Qh6rjh3jFr>1<8167NPT/i^?jqUc;/L8)=lbqFF'%4nC3\mD$JK^%;R,P);@4@/,;fo"j4IG
D2,@bP)7;X%RUej*_PKVa=lF[)GN[M%G^WNrIul!S>P.2.ciGc?Fl&V,fknl`/jF@OcWM0:Z
iGuQjBUVdE7c'@\\QXpd6Xs5[Q<Q*W.%Oq:XY-^rb#'cgBT]Ad77:rsu6gS=5saQN88#Yb4j`
AT`6^EBPY'A*-<h'HD(R+B/=0j?5bgo0#Y\s`*5D)Ak(ifArn>*XQ!),H3#\P_5ljla4UFjp
nl+kY,0,1]AaCd_9&4`%%i^RdLTWrVC222W<hM9=\+W'A*b\O*?P+gMsb;H_2=f>&Can"W0.U
D2o_c*"WW)msGI?l.<[V4n+EJYAZjEc>)6KfjhHtfOC`pRd9`)/pe2#^YGp(cEk[-DPWjO<#
7KIYmRM&>PP:._9U9]A\^>LHB0/i:ZZJ"cN6EJ;FK-m[`(QPN&(4"!hXXNn4jo\XXk_J.b+#A
"MGd[N>neMeEf(F#$/>s)")SV!)3-[*EJeEDrl[s55J!_s^FVUF\1q[eA$Y2)s/jN+m_0A8=
32."W-r1Zmtb#IoEc-`S#_5T=n#KZTatr$o:l/$Y"Bi4N_!GcbrDdNQJ3nOE[F(:/me;4Lqg
Nmf=4aFfQKi.RdTt!:T)YO$X8a<$NZ_+Z,b#<%-jP9T*Tj*I$g_<-*>>OQ->bKncW_.8[/g,
6n>s`G<AV?RA0`r)Q5%oWZ.GL_f,+&g^jW*hoTLtk69G?c<*_Xc>PMa3GS\@"jZ@q?7.A`l>
^:GXEK3ArOHJnYA!9_O-sJanX"jd>O4?.2&B&&T[;jNLS=C/Ym<uDCRHQ+@':PsYcScQ/8rm
A.tZhDn*Ala+=-Oo)6`7=FD.\amj$0@GnN/PC5J1dh/c=\D"T)-]A6p-riRMUMV>Ml]AaJtCM3
,@GK^Y`i]A`g[299@s92Fb"R5@G777M9U?=7mV/+o]A_UJfk.qL]AFkddDh/-=5MZoNkquZ6Y%Y
eq1VcNn?cF'%CW=o3da^Wrb(]AK1=a5?dk4F8:pn&Q0gbA;8&&q[3"Ip4@)Im%L8j(5WbY7fi
_3&S8/MbF4AQ@o):XQT0m>N<VKt(X==R5p%5>]A/2:#pk7F>emSCA\F^D'_?CI5?9A>i?^^(3
\D(9:L^9(@6g/Wjc4r#hf2um;Lml2j\P/%$cR$B4I^B'5hTahq94RTJ]A=&@dIL1RRgt`"X1i
T36GK8\JL^rq'Gg+gh,&.Jd`f@\qHu1O@e.G.3tD'\<LYA"/D!<U6ng`<E@VQk."OMrV3Z!<
o?qW*S1Dn0G74!j:teBY&HS7fp_i-TBoo9dUtc\=h"46I$1"uWIC@j&>!J]AcaCp%_6#apFT#
p&bUQ(P+KI)`,ur$B47At;54H'=X1It=!<*A]AiSE6-S[F38T6n.,ZHO#1U!M^OB0`-mrHXua
(?YdYB[QT`(X77nI#Pm1rL`qpfR%H<'jT#uHo1'4ebqc!T2Y$enKsVV@t)m#.8PEQnch1Rqm
)#;^(B4s=F!&!(!JMEm[^Bb6u)tO3JhRS,Y,!7FSS7J/u*%Ng)Yas7kJ;K$p^DT-2GQ$,(9p
[jU@O3\)A1ZnELJN.?!fUCLN>3"hd'F(EH;PFrV&05hqV_JVV2BW$;TTl8rT9e$L$UA+tAd6
FlBo=)BGlGmdR4rt++ts8G*4EfN/hX64!+\NmBcYl9oT`SS?Z&HL+.^k2$[$j@bqR`*kD]Aqm
`S"/S6HKC>>MaJE>J-@4XEa)7DJ]AqNWTOHbrc%\@Z`#CgE0&\%,L\d_>@R?eYZVK7J3/!Wbm
M`:;;_.(A=2AfT'Y8Sps_rO%%\&q3$&9\a#TLk>RdSjD@Vd=Ep%^`"ZJ[JkX%pIg*e_q^t1<
TZ+gSj'331`_"X2/^j:[ek/niN*tYmAb,`dZ2Acs.C7Nc9.q8^Y2lAKU4kUa",HBPhe<!\%T
XTrtEP+V!$W+IKmGAXL%?_0rrY$t7mkGa!P*plUJ=_E=A/Iu(Nr%_\Q#Y=?n+qRRKjTkYZTV
g!ldUR`>qN6![W?j-7EKpqdnQn2$ZdsNW71J>o(.PflYcE5-ug3RgQP>\Sf:aW;l*U]A6.n0g
MC72t%5DWb<'d1IjgX:SZk&oBh@[hRVFS,(!)R^;QfBOpRW<iVtEQECi#W!7<.):WZMGp(WW
&4>q&a\&spCdsE1!bl,%5,Wd:.k^d30t"6AoE86R9BW=ZKg#XkYs;s4573F:Eg@pK?%!l\F$
[5dd=V1kbV<[Q04:)-dFE1$1V-)ThULmJH/gkE@H>=P7IuqL]AF$nb:[Xm0P+uH0KBV^VMJE]A
=[c$@?J%!q)VI&O',#F`g3eZA.!ISffbQ&@]AIBkS>9$'lOOl[p4IGI;?iDmL)/'b[=9mmOnm
)XAT@\"]A*Sjc80<goq-X,3d:q(.lU5<X!;Nr;FWW/^)j0AhGcc\P%nkr0miqn,cXnJhN*[eD
?IUj`nG?FfJW0!fBq?Z9ZcRbdu]AY@knREuhNJ)3qQd0M,Iud`;Aqd[d?&2AfK>DSUVW*-_pd
Vbu3\V"gXo;&XnKV(O$NO0hAlH,!n.qqA:4Jp3gp:Q)mH!sr+O+!Hi%!YYeS>%t1l$'0\(,O
O<0`"_'8S-%G9^9OiXYAR.TeAgCS%u!'rNar-\.=;O"hmCj!p2/8!3%U"\3:Z0j]A_JUUbs.^
AMcY$K-i+G.TjBGa7UgL)DJQf@'5p/B.KU6R,p1"L$I0YKQ5Y8mK;B)bb:8VfU]AuA<gEp0Pk
`8><jl67.3jZYj:c#Re(7`1;\e&C^2e-^7H1i&PQEo#s5"<"lrW-&_gK^1d"Mled@F!Gn*dE
'>7qo(MJ=k>YS/)/?qpo;B-F1%Q-=7"[)U5CZP("@2.G-Z1]AQ<M"WTK@q9h1sr]A=+Z=RiiD2
f$3(=ZCWhQ?FLIY[r5,M1c%Qm-HYJ3)Fk!QORa<5Ar8_J1iD*sJkqX8cWK(VlFo")I%r55U4
u54M^bUFPUI5cR0o\FRQEW<ngL%<ljK%)XZ>4_mSQ;r+Wak8;(LTe.$+1[>53&^lF"fmd9PV
Nn!cA/H:[0(nre-=:WRss4*t404n65;ULD<1FJ6:;O=bJ0:BVLdeFc]A5'K"HR9aDZ#j"+(.=
FZL?+_BgQJq=6scq-@R*62-Mp8,14*T?S0#e`%2Iiu!.&PVi!PEYXRWALSccF[6$L:L#Ts*"
E[b,;8j@V'?Tjq?2-$(2^2qQZh>Dr9I[$^@f,+03&9p1[Mb-hs7:BNooO<,^7*28\$(@Ae5*
8A]A9G^Zl,#bX*f?^<a2&Q/S$@^)#q]AoqLtk^s;P0$N_KYg:=f9LMF>`l0!n+12qZMB+B`^Se
\jNcZm!Tf@lCa&E(O%LC@(#gg'mj5adkQ^\XeU[Wf8*Pp[q<fR![H;6K&oGUZSD2RTQQl$Ya
WiX_R_/Psbg7hsNp]A_?Gkrf"n?4--Qoa4a#FTGNBb9U!]A5ArN&ZpN#QEBTfG]AEQ+V.d3N6:)
12fR7:5;dmr?L,W\15CgM^$/m)M9c&,Qk0FD;6.'ot(b=Ut"pQ"3su=a]A46`tZhBU%QUb']AG
S&SWR7q*$+/<E4Z!>XOG"R>"X=THIDYFHF!99Y^]AdIAc:F#d#UO06^.f.<BtE2Xs7]A8-]A7Bb
KZm4$#.h!$Dl0_Se%IVq.jD"'#Ob(EAudn.`=a:MOZR4_\D;$i1JtVZC7#j.Yr50@aN6,>$W
_]AK>MR!im1G9_,JIg!Nj0@:qW=<9]A9!#T)"eWsE.hMS^U8<GMhd2Ric9T/i]A6@Fcr5#@8G2%
^j2BfTE4efP2`Y"LSAs\r'DK?hjm%+m"E(":)SG_$?$-HG3Y<WXFWoth4EX?+6e=2\pA.2<M
%_A9BCS6:Y,eXC7AgRPV!D<[SA2:rVDQoMS@F.QZT9d>*u2\dF""P8^`F78*a6<6We3>jb,`
"bef9jC`cg-Ka1k]AdH*V2Rpu'0iEg\hI3d"RK?5&Wq`P[nU#'Aa#^A=/%WZ-8cAGXW3'A*N$
9;s"0W'poTe82L1OQW'H<c)tEWV!Gq+GkG?=_]Ap7eR[k-ec7^'<b:G*do"Tg*?qMZ:t1Y+pK
'4Vi\kMG-CFKo10oFa3)5PWE[PY[,?edAAD\K9RI4]A7EeE_j1=N8uF3C^+4fGs`gMq)hXs7<
!)Wn$#'u-U>+LNCb>sV4oSKPI+hn;1fNj60iM48e?og:c]AXJ0OCll*06@kuZE]Ad:.m9U\-<i
o9%2kP7;QPqi0bnj=\/Oqo;YYpWknQo,'CmEV>2I)$kI;"GrG)>ireLulYh:N0f`#FZ$bqj)
.n-s"V`3\>tXZ^M47g;;-Jd5J9W(<F2&j]AE+!f2-(1gr>3*k+<4U5P[VKq>I2$5sISAJ4Km3
@M?(@%iuKt%eoU!W#G"8,hKDHB%",,;Ugm1PZRlIMAT$Y\(R@Y\`Z'>hV&3K+JT&*ZaM4,fd
C!M[*@>4;8+lLHgI_2$n[9/*3:N4=+kCtL+#Xt'6(dad=jPqg?)cY3O:Cegh$0?K:JiV$llO
Y+^pi'bjLCo]A)KjYQL!k=.`qdo$Kql%q=9P'H!arSErrh+mp,!X2FUaY<d:0!p>#i8g5tPl=
XcXh^-RDC*8=SUEH:OO+%DPOPXQT2+pW:T]Acb=!+60f4-bhn6$<sGMMVtb*V/-fZgCo5!#R[
XV?u8A3AJ:Xqap3Td;;`90'giDdhOqJqJk8s2E-j=^pAuf"g@LUWbK.n]ArL,*R>WZ8TZ9>14
:+cpf<XnFa&1ImXS)i.H*"=agpYr;rD#g1n*jQ/2Jt7TOE1Ga@Lc%-TiO(#sfl]Apb)+)51>!
n1q(lR7oHKkQnW/Q@FiurQK.I&C`l4oo#/r@At"Xlj.17P[79=U5]Ae:pq5g52\DPIo5CGlVd
*L7nsrYemkuc73XLX&k,24!2g7%^8a;$/Sdi"U;0+flmZ54IO%5Xa44?p!Ur>eJWQE4ZTPJE
XlcS$tJ5Z$BkR_m#[KNg[LZV:%$_AjIj2_R,#VJc39*aU29'<\m#)F5m@bomWaCC;^T4@KMh
7:)/l\pn!.'!>O;tT@ZE<>"25Tq2.%B.2'IVrouJS#p;Zp4DlRWlX.3/Era`5!\b<=/0eWMJ
cHDrfAufqiFE>B/7+B/9hkaG=3VMIQ)pp$Y5X0I!N&C-+VG?Dns%6>S79;^ZqLfd'rsWc_7A
ZSc9g5X<&Ac/uoZ>QtWJ.6SORf6u8',M0VR"aRP+Gn\X;QqdYeK=a5B[_HC?FOd7e^Pu<>'o
1S"HC;UP,S-odJIEo%"Y5Aj\*)Q!$9q=\8]AYM`$Z%EM3'(lc)[*$Z:@AoP#Xj`m(Z6m_/UR/
+*\Xh6V?Dp!Dd*O1f[Ak@Ekj94d@VP5(h5SD2NE3E*leih@"qX5\u.VlmKpT8!gS3h*<>SSa
o7VEC`sFo1Ed^DLQ8-Od7_00UZ2C;`)phMTmA[n5OWqQIK[6i<J`.n_'6@X988e7BrlB!Nf8
;mJ;Z>\,d,(Td7':tNGfs1*gkh7Z85q#Q0&I#An#@Lc5fRYj%h)MM:A7):4""t,G*b5ZS29t
<FsA+kag#\%kgbSROIJJ0Ap(UQ^u7umg"=Vm:XRSQSK[2Et3ACZA(`Ln!@c47nf7aRNTZ-7>
V'&]AjQ7HP/j`@oJfCMsmN)K`8D2!;)5hd)A`Mpl_/;]ADe!an9SB*KmU'[&o[U_/*N*@(pK%e
C\MEhKk]AT-UC1;N.Qg\.+Ajok0CtB,JS'KX&+OI[_2TIQ9K\0=qpGpnCg5fakJZjT^Df%^C-
mJ@C%r-4*`<L$8Ppe>`,]Ap)*a\r6<E2s5ZUh8Vs*1cg"q_?0cD.H8efhKi*T%R%5m(`NgCfP
pm'P3XDKUtb5P/^5(J(9BWaue$9%i=3+<S%pSV)a$3\VP$fPH#j"jbD^RHp)Cse3D[$pZb7+
eS2&@*%Kj(Rau3C#s_5tfPL-8<a[[=.u6eD6BHHA[G/GY.#b]AW"2]A<,5TsDYQOZKE!Ajd"\>
uFRD%]AM?8WP7ufchkLYA]AmdS*SlP=oMh+]Ap$ed\AqW),R#fS"VrXgK';Yk!%lVaZ]AKS9`m8H
pH!sgc0=_<6R&)lu^@ggbZ7efq;[Lm8WGAkd!lc$t_ZbSYocJKY>g(RJ&tQ,h>1Inr2sk`tg
I_ZKB<6\0TVNYDK-4j[:WY.md^:h("/2-?goB^Z4P3?GLBDbZQ),eTemO%9laGq9#L">S-a$
Cl[':%`np']ATI[kM\Y)58J'E'<mLOq@rc1k$h^9ERO;69m\]A"nh`/[%D]A.I,CT+G+>E;5^KA
LTd+ZfRKa+l$Xn2R)4)NnBA-XmgRJuSERoEa\_.uuSs/%pLM3o.ipB7,6S0nJY&*0!B&3oK>
FI-#qUCJ$V"7gr-@oZ?s7q\cL+rO@5Hb+0o)<AUF+_!9uJ0]A1>'HXh3?<ERiUS'AO5YNd5WH
SINk,8l2VPjPJ2-(S.*![L/eb:ON6?f<`ceUbrD>UIN?[b[kn(Gp5,.$JE1\7(]ATW8L5AN%$
cGWM>f<lANB&4/eF)Yac*$'T0-[5f(Ir:-.>>U?3t-a'OG]Af1FGLgj#epgA+0C%h(D]ACsq?U
]A.]AjLXsRST<0^p<X?h%7du:AF,#]AJY<+JZNUS*G\qM&n31m%uZ0J:>Bc>/itQ.aXO5Ch2aSh
s86)A\K6,lntL*_+og4iC?lO<kquTZ,8#i`o1(i$e1$BIVYIFFaXi%RU@uD#EIl$dIs0W9YN
_Ps+&+.@3S$m1h#"0*jY']A(#,6ICV;N&-FVN\mJ+A"jR^C&Z`GjgUai1T$EK/1$>O.IUo;c%
!"8--oCS>E72j$XUk1&>c/k2juWYl7eGL^d7)k-0TrWe!D!tJ$"/'/Yt'_6M/tAj`UeO:^L`
DoP&q7='f8]AQ?lIEEU\/FnP4-W@]AOg%Se,)URa_0;bKm+\=%!p1BR>^%e]A[X-eT&f"XH_!7[
lg8ThSmIu7--F5i!'&gPJq"@W\NFGOJ`o<(@tGOSo`p6-8gnL5X\\$&FIPlZond`0Xo%V!Rg
g*\XT59:@]A!]A'A9h,Aeh%3D@hXu$`0:C$Y.GcH>6>5'o9)[NXmlA+B#d\)>/b2'"S=o9<AU/
Tc4da*aVGJYeBAM\4jZ6A-O1c8":&Cl6KBb`s',j;UCH0,^Fn@RAo%B;f=u5f[8d;Z'#jpa0
IOD5\X^4dANm;D>,qNQH:bk<e@ZejSLEeVlH8:hT@(GcB^uYr!Vn29G6qrNW7Z?4&7tE:VE1
#$VNG/c3uHA8_S)aqke%rkK42Vp>Y*cqhgEaeo(J8OVO$Wg^'9<.$4dnK9b5mJPg3@,]AV9d7
n+$6^Bt$NUUfkO^$V?hLA*rsnY<LESljKJO1s@Au3]A6?B[5Q5)Vfdb%RB;_O2UdQ"\P2rdkm
$e)^M*<;A++\+6-*&;='\Jd=prPKWOlF-#WAT@9Qiiu?E1`t975-gO^?]Ah4s0KXo'F:tiSI(
NiToOOp2NCi[P5&ge`M*nCWo*'[(b#.$e";6S0CRjo`BmFlc<[E.sBi4beq$4@ukCk')dGE[
Ypcmg(:8g/:<A'/'o_]A&@\+1Y@jjrJL(b03P47j)]ATL:PFC.*%O/+N@E_uebFE('V70cmD?$
?0fC?;BdDD,U&t0?'G7aGlnktH=3ouirBfu4FNXbFIX4as;Tj>Kj5!+ap<O;MZjEts0cJbf;
O;1A]A3)1&5LU,J%CH&mR"a\3iLZ@N;`HN6$X0Fn:W,KW#MQ*5\<E\<'aG/S*hL%cS>RkBjhD
c0f[3T#J.:Z%b(:8+i3er<5o-29O$tn#:,<FYC&hZKh/\DB:6j0PYIGFCoCR<=Z=,iNQqY]A8
;Ss=BE*KFUU4$W7>XNMP71u/2P=@^?q-Z?bcd0h8p0"[]AH?o7-Ns'f&9"sYKiLH*)83`U1Xg
69Do')WQKXf/><$;R.Xc;GI.6rM@R&Q'^@qY/20/4B+#^3pl@s3,aH\q$u3l,SSqo7V/AeMf
11P+N/T'_Z5ps+J7L"g6'2LI)N$F,_Ol]A']AmK4k/!36On*)YB-FNO[CSdNcOF6"p[SYg!D:`
JA.TLJ6Bu>H]A:"1kDQeCTnZ:XJnJA&n'<Gp^U5gYd3tb?SRNoeUB<t=]AG=r:ARU^<DsY6.`s
OcF\Y>UsGRd=.lTthg]A&V6rUMKZ>dt*pCdp0U#qcK%B'aJbl)1WUPD]AIt(^_8m2^3HN0pI;&
\eKq8tC6(Eb#d`Pd)A4N+E8NAL_56nhXJI$IXl__\'2*K:eX+fPlchc4j4Df)K$A",/Nq]A%Y
p'GFU/SuG5<jq.D<@+rBp;+UR:gMd!^O%.77.L7@$D\uf%+MJ[8u,9s5[LW88N=QFlfm8Zi.
u[k?1*M+>(;&MG2Hfgt.Qb;Y@UU8J_d9e&^Vt.LX@'j3?eR@JmRjn9'k*XX\a!(MTNCi33aa
AO26MbV?:P&HS/+T9u.H<m-au^7Lm7Tl)$NRSTqd-*M%t`@smII+srnfh$CtU-[&-fL!\T0$
rD&D5h!TPGuU=1K*2b//6]A&QP/o&_8J(i\s/@KOoqXE4.oD\aIsB_h'oO%/5GaNPkoWEi&YO
n6?!L4E"DE:gOEKN;W[p`B!pRfEmBGhHD'1.,GOVOTRf53l.<Tc,Cn'P]AIVP$P$u1/d>,?qB
.BflB.Ups?-/j$AZ3HNHGS/O,)`!X6f/btf$8Q2n]A?2\/%K_QBnC#M/P.sHrE'BOPq,VhXa"
]A5bt@Y%;li_3Uc.TjKSN#6oF`qP;!1Qo!s[Sa[JT>1T"jjVY&g5t_lS>)MRM1V07DO2DAU]AE
kmbgNl:Pu">i=]A-erdl[^M_DR9<gg<fmQ(tQ2d(tG,p027%E:Kg)P6"XkL%2^OXc,rH*[Q"c
qrt0GFKM;YSJ\Ut4OAj_.B7_k51Ji1n^C__\Q(D\<ljgOn["qr-cUGZjV^m>";(H(:K>#'2-
6mh`I'be"AP^GmBdcfiQB"WPdPT[dOmP(:JCm@770s02I/7!X(*BZZ&%ji8E\Q:kMeQBHSKE
19X'RBW^Ql+A0cTd'=:[.bKL6]A&RMG`G(NB@0(pq-qpb"OO?i0BSpmV=oSBdb@L&p_c!%Xq+
"&5QuR&fPBO8c'cdk:>l]A"<SPfp$Bo-q,I=Zp]AS%uJ>+hioPbrkk^u?#KO=T'>-@C)0ll#kX
9fOafhtP@ATr+4O:7[IYbrqe),3C"^;S9H*3N*aU?[UH'2;<oHo_Rd?WO%_<X?j:ZW*!B&"i
!8RfLoL8ShPc/Nc^lsnTApG\`ZJsQ9WA@Z`e;@?!gcc4H'Q4b]AK"S'/D[7;/`?mM^of&^cQ/
)Qsr_,HlHZSUu\B=kJ$EeY#oe@>\.R0^O/2WK"FmpU%k6mLV3K1`+<[d[[>kMQ@Uma)QG+,1
3G#H^.Ruq5DeaQI8=$AD?sKPV^HJ*;F5rAiq:>En9n(WDi1J?SWZQcFi4+A2jrm[WKFObl,s
#^=6EOcY_**.JZ!NE_m5#+;Xu#<?AuQN(p]A-pU+kGDokRP=V;Rh8>Q-RNiL?T(Q'Z*hoYgD"
rI&<Jg0g>Q`?r%]A!((_qD">91,/_)GfbH1WqkDgPH<N0?qGID<cVs`R,mI.Q[R0:.kElfQh>
%ko$0ZcH`((O<S+]AehL#tGGk_3\T"uACb0Fhcro-@"MC/q0HpYi\t>MUuKCu::@Q)B?/8b6E
YDWaQYM652;K=JeL'#i%sr/TAdrDe`6h/6rX(!QHu@N<VW'ChcKJGhct=(2`8I;E$\6@6:0M
59KgHA^guQCisXisoamCX_l.\`oAL/46*cDbg0>\lDAQ#%T;es6-NSrhnXX*&Mk7J9]A25P*9
/.e_.[sq:=,mG3;7Rp5tr&/+J<Qn0qA>)>ihqe42phqr^Pr+fdUi.'*/<[YkV*D75$H03>.Y
ds5_)fUQVpjC:&[[>s^Ad8X,$Bh]A:sqi=GTDUfkAB.?)CWb#,N[:sMkHmI"&Ufs<rHsbt!X.
otoLQNm5C`[-[o?6#Jm*5aP4B>X*@Q[hO&EtCE+ne[D(/H_ns2?,IqT@W.$1#&jFN4d7Zh=a
^bJfjf`?Y]AXn92Lb<A&cHfmfE2F2h[]A<HseC#"rTd4u%S2+[Rq;Lt`HXXgt/7mB5J^U%a%#<
K.bL1'.h)">k3J7N>t]AIub66J]AeGQfu%upZ!`aBmrj@`=pWJTIjoe@K?RoFO`@J`7JX3r!E0
p`:`KucbD9>QKM^h3jkUsJ@cE;HDXSF[C?8?S,Lt;[+[F048+)a=#$LG>;FZr9`:pC]A.i<=E
oHYq_]A;Q?o+)1Z+I(sgR1d@a=DsqdIjLM\uCbG!i%#.Z@8Y^_=;Eli1R-S)sE>5Q]A]A#uiDCd
bu,H1':JRT%&3=8YinKi^r8Sr0O\IV?H=<Lc3=K?gjM.AKVp%SL_`SRdMR7dD4H(=-ATGG"o
g8DYG;54'aR'W8)TKKQA-8l%KA1lQOh8Ra.Y6U":dq]A&jc/jKu/14kU'`c@r<16oU<TmKnql
WQfRpnVg+r02UtP-=,$'&)`ngHR'"TIkO=Q$n_6*gC`Y^^3%N_nY+t5i_j`_(u[$JRe9_g*S
(??/.oV&>/oY@PWl#?1,a<"8oNf@oka"=O=LIp7o6^a`:b7CCN%K+7Z'J;taVIL:CZ<2>EHm
-u&Y"h*>/E+54RZ+cp[:01Yu`.f\t4,!B7bQ0Kt9nhN9I;I"OL2a?]Ai@-42JGO"7^PqU8jdb
h$&FdTh:ggV%ha0.!&eG\Cbg0Tn1SQDA=>\75Sn:qBgI+7MGXIX`)\G!@K[`J,L0q5G0;LWL
f7sWEUWN"&bXd>).Jd100OLb.fXiWJ+]A-T9$02/khr)nec%l+3qnD6E#Y@Q)SYH`o5:o'H#K
uhf4T,(?1iHYHCl!s0jBN"'t=>7,tN,DT;_CG\0ae=+re4G>Z0hjbfD,>SMhQYd\>8$a>#'"
4sO59)sbuR6n<Lrt;DL'nnT9\`k,-jTC"nQG(>T'U)_t;(bXRN.#Ys*9#*J!:DF=$qC^PD2P
o6S[P)3=&IZ%5iID1i(OYO\qd5T?X0.)dE35?=)?,s'Y*fI?hT$Pg.G:9t%;l!8!D`Y&11Qa
A*?IE.2MmBJ_0_JjeZd4"\OjQi^E4.W?#Tlaq1nte*3*!5lE3+h4$X+A^HaqkWp3_#Ve<P!!
1/=UF'I^X&FZ=W,YHpU6[Z7i68nS>9i)F\YpmpcdKDHp<Z(b7Ya$2XIa1k(:m:kJVl=j=K!Q
XY$u^Pr$S*MK+K`UbP[X[p5)ID=0mg0lm"<qtgHb!lQ\[F$p3+u,%krH69Mb<(2leZ,QN7<<
n72Xu]A2mW`K-DUVn#a`l(!^Q"f%EXjVr\P3iC?)\HAiI?'tCo[2@..dMqE15hAo_S:i:NJ3n
#Dk#2Z7f6UG'QS"$M+))-%qlMfU7*8Q/I/'.J<VaCQu*4M/I81rmr1>S)m=kT4R5Z'Z%_&dX
Cj_ILR<n!>s5YG-$;nG1a6Q3S@KmNb'#4]AR48aD4J[*j5Bt)LAu;A<u0]A&Mb2V2/'p!D,[0`
ZAWH4=^%c'.8akub&UrD_4je27n+8`N8$%u!4183=e4K@libi*UD6u:CIp_^&5Li!:oEX)sU
pPVu<-(lY*Qn[(fVeNuSrE[bog6d[<P?-PG0Y$MoFEY;%P\O"=KJS1,BFdp0'Ao!_JVlni<E
0"@i9e3]AA7r!*QV([X:+c?OL;mDd-=d.^eI[9g?+i>U5%V#D3,-YX$<F5%63o!#pHim_Z!iA
rprkD&rU&[8cWM7eW+.SKDDJ:3YRUcnaBV]A6]A>c9?.cVZP]Ahr>5MJTh*sGeM=fK)bhT64qHP
"c=F7?qlrgP.H.`hpFDb@aaVASReH2kW$LJBHu(r4SuH0`*,?-:,]AI;f%m:%TVSkdcM!\BB?
mf\jco]A.UWmU#a7C=nu]A/f,c9N>Xig-"n%sM<3Y'EIlD_QM&EW]AJB`+%=EeEKs2rQ]AK92Lh\
[>+IcWWBMj&7M>]AZ2=@NH6T"HgtinUBU8WoiTobgW>f8"otJ?poYi8[$p@]A?G]A1.rHu">m/'
[C\3ae,13D+fVC*kK]ACA*GfD[9p*Em:K9D724k!uB3J+.V@#NFR\r`sVK\JC/<V!q`gTtaNO
Msi(_ZaO,N/+9#5GBZmo!3*<A@s3cVM9+\+_#)+*CV"D18U>(:\F0*.mQ]A:AK2CH\]A0gb1(%
0oMh\`[!(SY&A#L.D#L%jM,;f#p,.t@)A4fQS"-&ZL3?B2bD3YUSq0#/BO_>lFL*O4^2N.Mn
JbE:V'3JjUH$C0?deH"$T,PHIP!kmcQP66+!Y$B=HBdFlkSTh[RPR=ue_>_meMB-^"Ir,%c5
$Hil;^=QI\9Ek@nL!B)E:K8&s)98ir`)P1)E7%0+KZSt/A1_=[Ib#6dkJaMbBp^I@P]A3dQe?
OT!3sL(!4]A;$FnZ%7I"<O1]A+dE!F]AZor%)AAr3a8M!!Cl_RDE*Yh'I:FDB)]AO,Ep!I5q"JV&
+(@kAj3?.L]A0H:;bordrY[%JXG)=tJMa%/o8Io,($LiNP@8hd'C`M6$IZ&G9\Sc,YNA4Qc3d
Uk?j"i&r_F9MopK.s1_'aL"3*ct2l#?4n#Ln%dIR`t@]A1K3&atB)bBT:P.iEYo#$A:+sa^%N
WXnp%NbZ7&'`pQ63kKF8lrZ=0"cP&!AF90;8&.sHLUBZo!oJA*uP(J9]AmS;_fPS#s2"<,!n\
oE>MpA_I3Ab>n*E]ANt>,!B>;UXIKKEpUCBn,Id!M)dI]A0#7.da%Wf.U#4NcE02/hjM@us-GO
QP*8%#jqG0'C)27purCl>H%n(bf2"$'0#UaTQ8^5[U^?FkM;;P1#:*]A:UhMA\uU,mHL'H4V'
"XGjtDiF'PMMfkb(T(K<ds[3Pk``]A+dD!CmB[L-&PT)Cc7_a3n[*&M?;N$k<2++'L]ACYm?RK
(Q.ErOC4aHKiL5fEZ-.Bs5+gqPenD;[H[DA+um_`]A&Mdb@,GBI(=V5Jm6E?9"jlR-N*"k's"
AWj<Z?J=_0RIA_1"K,5G!M_9HjhHdZ0P&&N?OVaC9eD8pE+)6l,@Z7PFA!feoaLLJaeB:'S]A
mR7JmBJ1QknI`C0GsO7/H38upC7"9:S<u.]A_:DpJ0[EknagYcCNWsY7AUL[mYuc-*N'`r7c)
1Bmi&OV1(_cjSDRh^LhB+_`:OmS9D0b;QWa;L56:`C1$9Sm*<ob2oOiqo@=WcMpE,Iqs0!!s
+E'8(\[&gsh16^/m^8Q+s&bb[Tn<Soo3Eh5go8fldI3WJBTJrjINPli!kj(35c1s=VNFX@(&
pYgs"15K/%DJr+u7-nDsc4rOk?=\j"=PXM!slR;ftstS;PXt4`@^VLk>>h`TOMBrL,BV0EHg
?@gq_J$J--:rSE<"K-BK+Ut>[:U1rX/n(5oBGT:,_DIJUtdutXDIF$aK+f=fo#3)O(c\a"@L
@`/IrSUcpE;+)+Rm%S,?$k1QaojS_'cn,[qYY#&H8\*QR[$j&Y_1gjH(YQ(<iI=F!*2'nf12
b%(NoJ6-l.QiN3s7Oh8_o(-M5Lp+WUD4'k(O0c/@H"!_^%NW-EBe8%8Nc]A@B,LdQPUK7)Z^d
J'MWnCP4H5^\aqD`oU=PW$(u#`pN6K]A>Cj$`jNf=6QY`rKVYX8h@Cs"Lb;G$iJ7F8/b98KdW
t>Q82nF=Z(j5sGG"G)6O^4G]A=kY"h`)>8n/nPW%9ajH'B9dj/X!\>epga1HMgH@=6-3&h@%D
5gIA'*[m.m9fRn6jAR[:8bJ^2_j3(!,VNV[gCG-e5+pf_1hbhUCs8'9$:1!Csr/+SdpdU1a\
s.j<b1ds.T;F`'IYXGB1YS`r(c-q9It8hBH?]AWCmDS>Mjn*\\$p1OPfRRk<ln/-n;8/fF67q
Bd[gi@HoL]AI-NO\\K>CSHSSj*e,p35gX$1e#MILdr$8j!!TLI?DtWTtLEjO9J2Nk'8X/id1J
B5)Q*2X%s6h1RJ8Br!H]Ah0i%M/04_9`c&l"Mi0GUs1]ATD=e-S)T0FO-['c#i3V<%uoa\pk$N
d"qUEbk^?RPfdV#H@ohLs\%el0s*@s=GeM'srd-"bBA\`Y4d9D`Wd_?%-e!\>fKmrEX%6kDn
n3q(rc=u-DrJVp[.]AW\Z"eUlFmBi-nYmhVEQ!81u/UG3FQ*WO.Po#cm6)T892X[.I*N$oh\H
1LDeYmXV3GK+kDOM?>eJIAH1:kL+t[dRaSK4c!7j#A$'jmW,D7,\5V*rKqLQ@I3]AUn\0NZa7
!o6)t#^U.TS8O`fa+>X8$+VRcNohlWjL^+k.!#<bd([0d68rB7OMef/&e`jG]AA@Dr"JE27pc
%Mdt*fkCAudqHsQC?VS(PI)##kW_!_FK_"1rUTIX!<~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="962" height="270"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[723900,723900,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="1">
<O>
<![CDATA[行次]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="1">
<O>
<![CDATA[资产项目]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" cs="2" s="1">
<O>
<![CDATA[2011年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="0" s="1">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="0" s="1">
<O>
<![CDATA[变动趋势]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="0" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="0" cs="2" s="1">
<O>
<![CDATA[行次]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="0" s="1">
<O>
<![CDATA[负债项目]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="0" s="1">
<O>
<![CDATA[2011年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="0" s="1">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="13" r="0" s="1">
<O>
<![CDATA[变动趋势]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="2">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="行"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row() % 2 == 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-855310"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="2" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="项目"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="1" cs="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="2011年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="1" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="2012年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="6" r="1" s="3">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[F7 - D7 <= 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2!=0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!>P\$rJ=?G7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us!Sg775u`*!]Ap8%Z'6,#4rJ
Q7Kp*?RX7Aq>+6m5FW'7CFSfdM>MZfPl^*[ltd@'NkGAMbi'VP?J<5t+1prQmNJDXME!DMQq
fHZe4m(-t%:jVqOqiUd"q?[VZia1$X"P_NHYWseAfp9c(RGu3@pW)g@_&W:J*):B>p1NRjQ;
f)c$V3gV+7C6,NP\UMdY9%0Hls;l7%D!dePW+a%)Cb;;Tm7T>g@qlEHE)G!Lj]A4XH#F@3[p)
]A+RsF%.VHU+3+ARSlosLFt:=ss[3_WuP;uP_;fl;$7a3]AI@2ClM:aRd_`3:U74>i6=8iH$of
^e'"!9t2<@`E<YATbqON&[gj$PB^ejRP2cB?S+H3"t5/Y0u=`D6nN^o:!ADra5W%79rd4Z;X
\T@m[g=9g55@H@j>a9'5M&H8^B@4Me&FadD?ogU>:<,7(Q2b/s/j:n*DMl[an)"@I&SV]ApKJ
ihp<T2A4F2arjf:TZ&#scO_je"7bibZl*iBV\#`m`lcSt:D6<b:jAV,d*oFn0$sMFRNF#+J^
SnQB[^`VC7N(rq:YoOIM4^&G6WjA1rF1nKr%cEI*gGjtb,4T;Mt7a\n1I;S\oXe&h5AASquV
@6*[H$"@gE&7!!#SZ:.26O@"J~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[F7 - D7 > 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2!=0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!=8i$rJ=?G7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us!ROD+5u`*!`RO?L'6,#-EW
<$%=Z4D?5re"3JWV.a@18uE8@$rGgK=:0Ln9nU4t@If`tkbpl@BV3V7$2/Vjf9?Z$]Aq5aN2'
LpV7"G[]AQ%k3Ss8eF3!U__-J!M1i<75T$BO^A`6X)@K!7PZ)>WVIq#0X.CTN<qmhJ,erBWF-
`>jDE*;m2X^.7OaQk5pMfuZg8$+C=/tCq[nfqr>@PPcWU^a6QNGHdMk#@nYa)0m0\UT6U^[H
1qk2<muJR5,G\(li[B<6m2O%T$5B_j(DXIK4^r]Af[(qJ\%\E,.Yi*1YAd3`B\%\9`u4D1F-k
#OdE!9Us'sgp>1:8F!1oiUk-2P/UD&BA>Eei6f75niejL(-?M34Hn(*B^Sk?9RL,X:q_a9dr
-SY@TRL5_K0L4L=BYO5)u$?.Dt;N"`OOX5!na;d-R3ISb^-SFa.M@Q@KPi]AG3?r^E;FPNaWr
g0&>P_+jAI0'TpWGTp9Vt<K!KVpeT\dN$<+386Z_9eI\.p96JXnYcK+<cmFm4&g:hV\U:+po
WRbND^>UO4slLcU@7N5/[%!i*X\qoNBeu7N&jUL7q'0Dh\:Abgkn*Ip_Q"L"["a'a@?41!!#
SZ:.26O@"J~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性3]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[F7 - D7 <= 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2==0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!B(#$rJ=?G7h#eD$31&+%7s)Y;?-[s,QIfE('k*E!!&t'5!ArH!W>SX5u`*!c'I6[;dgN`rK
"PTWggSW/eYjr80fl;_?clldSdtV_prcC<o+7T6_-SbCM#P/asp":]AN?<<Z8S78\ukRF4*R=
j^<f;jQ"TN,nUZJiH$K.(T'tX.#$ojVT4i1J^p-^Jm/maPXX&<R8ACWa;cS$q/Bbn.19=_D9
)ST1U@$"rni#Lqb"U9[OITaWk;Z[/-V.K)bj*hJG;Edo)VKI3PTDY[*,+?lPp<BN_sRg;[eq
-[##Cq=cVjD*-J@(2VE)ha,G@g'"hU?^W5IdDl+8=bVH2LdqQUlHf@u2Vm"-M_W.g5-=ndT`
`MZO[D.o]A2--B%')[hi^$8##Z2f]A5\In_,%EE6/7ou&D\f+X=n_*L]Amlfd@L&lFRnhgI5+i'
NpT(sBB,q:+09='n%8n.*H+[m\a*9_=Wh2Y-hFr4rb@.M_O%&PD)m0uNbc_O0bd)!FAU)jRa
Pa\YG+8T(U;/_lE_ddm]AYW/p=R0=G$(:`G.?Z'dob<*'f_N"m:t(_JFs5SrR+>0bVl80C+%H
V5N>dfYtY:THUO0NDE1arB$gn%F`fHb4+!1ZLoNj[5"9OcMZG[f8KL2%u-K9$*6sAgTIi:IQ
ir\uR/Ei`Dq_QB7NgDf0;>,ZeX5PfmXYpXDm8QM^f'q1KSG6,![+!!!!j78?7R6=>B~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性4]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[F7 - D7 > 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2==0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!Ajl$rJ=?G7h#eD$31&+%7s)Y;?-[s,QIfE('k*E!!&t'5!ArH!W,GV5u`*!c.)bd)K?b;nc
#TADh4r4NZa"+>#:2-[#1+fQ>K#fY,tpC*4=EpZ*Bpe=tAj5Xg)5F&7&FaT'*9BgUYFj85[b
B?L9r7%q@icWRhYVq!e8&a+Fnp]A;BC&Mq_3phLN1f(;fOUE1u"e@S_0p]AQ=B1T+$fZa81D9(
MS!dbV2IZ0^]AeJnFIl0AhWfZH+m&4hNec9\=%I5HRn6./Ed2iN.6J2BnJjY_Y2GJZG\=KXL2
MAg28H4:<R>FGG(/g6FYVG:Y(mBB)_t/19&9EShVkMp:B0AEr;80[):%0@P%/G0qb@K+&#?i
H4G70O#t]A95"<<::K#g09\hK/mirBHY!6T*@)/:f8FthF$mZ&94E6P6[5tATY7!;h2r,<M-k
oK/(.g$5<BT5qi'):Ie?q?<m&SGjj:52\E</&pV\hW?-OoZB1=Peh9d"q-)/`jk?J.tlnKZ[
WI*iJ3aM,]AJkQ-sE0_;c9_bigcS:7-_@1(L5"o:0;fs=gTm_;.BQdZ2(^<"))*X/+16-D)3@
NL2d>FI775X%)VC#Kfhj>fp)?E?c8WkPL%JAbebkR.m9b=uL/i!oDZ6r5@u1h3Nem78e`_<:
S)qhSp?K6!g<jCG7pjn!aGMLolZ>Z6I@4&iDd!?g!0g_=%g^An66!(fUS7'8jaJc~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="1" s="3">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="1" cs="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="行"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0" leftParentDefault="false"/>
</C>
<C c="10" r="1" s="4">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="项目"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="11" r="1" s="5">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="2011年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="12" r="1" s="5">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="2012年"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="13" r="1" s="3">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[M7 - H7 <= 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2!=0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(M7)!=0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!>P\$rJ=?G7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us!Sg775u`*!]Ap8%Z'6,#4rJ
Q7Kp*?RX7Aq>+6m5FW'7CFSfdM>MZfPl^*[ltd@'NkGAMbi'VP?J<5t+1prQmNJDXME!DMQq
fHZe4m(-t%:jVqOqiUd"q?[VZia1$X"P_NHYWseAfp9c(RGu3@pW)g@_&W:J*):B>p1NRjQ;
f)c$V3gV+7C6,NP\UMdY9%0Hls;l7%D!dePW+a%)Cb;;Tm7T>g@qlEHE)G!Lj]A4XH#F@3[p)
]A+RsF%.VHU+3+ARSlosLFt:=ss[3_WuP;uP_;fl;$7a3]AI@2ClM:aRd_`3:U74>i6=8iH$of
^e'"!9t2<@`E<YATbqON&[gj$PB^ejRP2cB?S+H3"t5/Y0u=`D6nN^o:!ADra5W%79rd4Z;X
\T@m[g=9g55@H@j>a9'5M&H8^B@4Me&FadD?ogU>:<,7(Q2b/s/j:n*DMl[an)"@I&SV]ApKJ
ihp<T2A4F2arjf:TZ&#scO_je"7bibZl*iBV\#`m`lcSt:D6<b:jAV,d*oFn0$sMFRNF#+J^
SnQB[^`VC7N(rq:YoOIM4^&G6WjA1rF1nKr%cEI*gGjtb,4T;Mt7a\n1I;S\oXe&h5AASquV
@6*[H$"@gE&7!!#SZ:.26O@"J~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[M7 - H7  > 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2!=0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!=8i$rJ=?G7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us!ROD+5u`*!`RO?L'6,#-EW
<$%=Z4D?5re"3JWV.a@18uE8@$rGgK=:0Ln9nU4t@If`tkbpl@BV3V7$2/Vjf9?Z$]Aq5aN2'
LpV7"G[]AQ%k3Ss8eF3!U__-J!M1i<75T$BO^A`6X)@K!7PZ)>WVIq#0X.CTN<qmhJ,erBWF-
`>jDE*;m2X^.7OaQk5pMfuZg8$+C=/tCq[nfqr>@PPcWU^a6QNGHdMk#@nYa)0m0\UT6U^[H
1qk2<muJR5,G\(li[B<6m2O%T$5B_j(DXIK4^r]Af[(qJ\%\E,.Yi*1YAd3`B\%\9`u4D1F-k
#OdE!9Us'sgp>1:8F!1oiUk-2P/UD&BA>Eei6f75niejL(-?M34Hn(*B^Sk?9RL,X:q_a9dr
-SY@TRL5_K0L4L=BYO5)u$?.Dt;N"`OOX5!na;d-R3ISb^-SFa.M@Q@KPi]AG3?r^E;FPNaWr
g0&>P_+jAI0'TpWGTp9Vt<K!KVpeT\dN$<+386Z_9eI\.p96JXnYcK+<cmFm4&g:hV\U:+po
WRbND^>UO4slLcU@7N5/[%!i*X\qoNBeu7N&jUL7q'0Dh\:Abgkn*Ip_Q"L"["a'a@?41!!#
SZ:.26O@"J~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性3]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[M7 - H7 <= 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2==0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(M7)!=0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!B(#$rJ=?G7h#eD$31&+%7s)Y;?-[s,QIfE('k*E!!&t'5!ArH!W>SX5u`*!c'I6[;dgN`rK
"PTWggSW/eYjr80fl;_?clldSdtV_prcC<o+7T6_-SbCM#P/asp":]AN?<<Z8S78\ukRF4*R=
j^<f;jQ"TN,nUZJiH$K.(T'tX.#$ojVT4i1J^p-^Jm/maPXX&<R8ACWa;cS$q/Bbn.19=_D9
)ST1U@$"rni#Lqb"U9[OITaWk;Z[/-V.K)bj*hJG;Edo)VKI3PTDY[*,+?lPp<BN_sRg;[eq
-[##Cq=cVjD*-J@(2VE)ha,G@g'"hU?^W5IdDl+8=bVH2LdqQUlHf@u2Vm"-M_W.g5-=ndT`
`MZO[D.o]A2--B%')[hi^$8##Z2f]A5\In_,%EE6/7ou&D\f+X=n_*L]Amlfd@L&lFRnhgI5+i'
NpT(sBB,q:+09='n%8n.*H+[m\a*9_=Wh2Y-hFr4rb@.M_O%&PD)m0uNbc_O0bd)!FAU)jRa
Pa\YG+8T(U;/_lE_ddm]AYW/p=R0=G$(:`G.?Z'dob<*'f_N"m:t(_JFs5SrR+>0bVl80C+%H
V5N>dfYtY:THUO0NDE1arB$gn%F`fHb4+!1ZLoNj[5"9OcMZG[f8KL2%u-K9$*6sAgTIi:IQ
ir\uR/Ei`Dq_QB7NgDf0;>,ZeX5PfmXYpXDm8QM^f'q1KSG6,![+!!!!j78?7R6=>B~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性4]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[M7 - H7  > 0]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row()%2==0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!Ajl$rJ=?G7h#eD$31&+%7s)Y;?-[s,QIfE('k*E!!&t'5!ArH!W,GV5u`*!c.)bd)K?b;nc
#TADh4r4NZa"+>#:2-[#1+fQ>K#fY,tpC*4=EpZ*Bpe=tAj5Xg)5F&7&FaT'*9BgUYFj85[b
B?L9r7%q@icWRhYVq!e8&a+Fnp]A;BC&Mq_3phLN1f(;fOUE1u"e@S_0p]AQ=B1T+$fZa81D9(
MS!dbV2IZ0^]AeJnFIl0AhWfZH+m&4hNec9\=%I5HRn6./Ed2iN.6J2BnJjY_Y2GJZG\=KXL2
MAg28H4:<R>FGG(/g6FYVG:Y(mBB)_t/19&9EShVkMp:B0AEr;80[):%0@P%/G0qb@K+&#?i
H4G70O#t]A95"<<::K#g09\hK/mirBHY!6T*@)/:f8FthF$mZ&94E6P6[5tATY7!;h2r,<M-k
oK/(.g$5<BT5qi'):Ie?q?<m&SGjj:52\E</&pV\hW?-OoZB1=Peh9d"q-)/`jk?J.tlnKZ[
WI*iJ3aM,]AJkQ-sE0_;c9_bigcS:7-_@1(L5"o:0;fs=gTm_;.BQdZ2(^<"))*X/+16-D)3@
NL2d>FI775X%)VC#Kfhj>fp)?E?c8WkPL%JAbebkR.m9b=uL/i!oDZ6r5@u1h3Nem78e`_<:
S)qhSp?K6!g<jCG7pjn!aGMLolZ>Z6I@4&iDd!?g!0g_=%g^An66!(fUS7'8jaJc~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-2624775"/>
<Border>
<Top style="1" color="-2236963"/>
<Bottom style="1" color="-2236963"/>
</Border>
</Style>
<Style imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-2236963"/>
<Bottom style="1" color="-2236963"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="0" paddingRight="0">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-2236963"/>
<Bottom style="1" color="-2236963"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="0" paddingRight="0">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[¤#0.00]]></Format>
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-2236963"/>
<Bottom style="1" color="-2236963"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="272" width="962" height="270"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
<Widget widgetName="chart1"/>
<Widget widgetName="chart2"/>
<Widget widgetName="report1"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="962" height="542"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="c99f3615-7a94-4103-9376-a5fef736f5c6"/>
</TemplateIdAttMark>
</Form>
