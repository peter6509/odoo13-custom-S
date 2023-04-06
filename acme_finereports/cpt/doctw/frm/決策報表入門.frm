<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="company"/>
<O>
<![CDATA[VINET]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT 產品名稱,庫存量,產品.成本價 ,產品.單價 FROM 訂單,訂單明細,產品 where 客戶ID='${company}'and 訂單.訂單ID=訂單明細.訂單ID and 訂單明細.產品ID=產品.產品ID]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="company"/>
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
<![CDATA[select * from 訂單 where 客戶ID='${company}']]></Query>
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
<NorthAttr size="59"/>
<North class="com.fr.form.ui.container.WParameterLayout">
<WidgetName name="para"/>
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
<Background name="ColorBackground"/>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.parameter.FormSubmitButton">
<WidgetName name="Search"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Text>
<![CDATA[查詢]]></Text>
<Hotkeys>
<![CDATA[enter]]></Hotkeys>
</InnerWidget>
<BoundsAttr x="567" y="25" width="119" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Labelcompany"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[公司]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="50" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="company"/>
<LabelName name="公司"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr kiName="客戶ID" viName="公司名稱"/>
<DBDictAttr tableName="客戶" schemaName="" ki="-1" vi="-1" kiName="客戶ID" viName="公司名稱"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
</Dictionary>
<widgetValue>
<O>
<![CDATA[VINET]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="130" y="25" width="80" height="21"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="company"/>
<Widget widgetName="Search"/>
</MobileWidgetList>
<Display display="true"/>
<DelayDisplayContent delay="true"/>
<UseParamsTemplate use="false"/>
<Position position="0"/>
<Design_Width design_width="960"/>
<NameTagModified/>
<WidgetNameTagMap>
<NameTag name="company" tag="公司"/>
</WidgetNameTagMap>
<ParamAttr class="com.fr.report.mobile.DefaultMobileParamStyle"/>
</North>
<Center class="com.fr.form.ui.container.WFitLayout">
<WidgetName name="body"/>
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
<LCAttr vgap="0" hgap="0" compInterval="0"/>
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
<border style="0" color="-16744448" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[订单明细]]></O>
<FRFont name="宋体" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
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
<![CDATA[1104900,838200,838200,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="6" s="0">
<O>
<![CDATA[訂單明細]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[訂單ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<O>
<![CDATA[僱員]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="1">
<O>
<![CDATA[訂購日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[貨主地區]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="1">
<O>
<![CDATA[貨主城市]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<O>
<![CDATA[是否已付]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="訂單ID"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="ID"/>
<O>
<![CDATA[A3]]></O>
</Parameter>
</Parameters>
<Content>
<![CDATA[location="/WebReport/ReportServer?reportlet=/Details_3.cpt&ID="+ID]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="僱員ID"/>
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
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="訂購日期"/>
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
<C c="3" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="貨主地區"/>
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
<C c="4" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="貨主城市"/>
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
<C c="5" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="是否已付"/>
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
<FRFont name="SimSun" style="1" size="108" foreground="-16737895"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1577999"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[mC[XB;qoke]AE8L]AUf`Y2/f$E:;%sRp!"i(*Bf;Ee-j%hKJcm5^@KSb#W(8QR&Q!0B,Y/B%8g
b>;KW(+8+Tr&^6H]A924e?[)h!^ghhY4bY)ri^O6Wnd'[J$-:I-,h=g=s4e9b#'jOSStX!3tS
)%\Eq*5r\iMCfr(&s33h)%tO`=a>eWNs6R-]A>.K.6DPs:8!k<I3^3q(]A45TdP8R3h4BUI<KS
YtnJ8\DT_k<&]ASQc(a#-u31XYM!m[i/_ZBUH_:eGdC9$dmGK^ccsNS*adc\YSf-g-rU$9G5)
:=Nb+WjA'6t1c*HR7ab'o]A_fkA_KphmOj^.&&H1&o;g+MYIa?a`,4,'OHJdD<31cO$!e,cB!
:8u;c\@e1oDaT#kJt/3oBLi5UDu+mp?2BDQ+fO2AQ*+(%m(-[0/iZ[2$,"RCQ^S/[_g0fdfp
Wan+l(cghCRX?1ik<D\1G,I/COtT&;>&W_kj)k^.s%.&'.'R(F'%-P*JOS1WRn'NfJdj0eO`
3j\Lf$\XQ5ViHg)/o3_&D:Qbtp&*_;9aO;!(,QTFf!9%K+L_MaJWD_j=NWiPP#G_-9T7YWnN
.&;+["GDqeiCRIQe2JVAA&-E,I2g?*%'/sQ[/Og$(?mmHFO\D483/q2>(RYZVZ1sOR1hEd<k
J,fMNA&?dOfM%'k8#@th\eG%KPfGK6)R[M?Y)<<4"YU2V8\Tf@E%nm1B3\m:b7cEX`Wir?DR
gT(5-&MU6Fc-H7m/^'(-V(r9aRk$^&iE,FVh'*X@fX.iurrW/+ZeU*Y*buj\?'<$R%.;`h"?
O]A<4?"?E6%qg#4V?Bu(Q&M87TCL8;c1CO*E'jegLnQZk"NB&E$m'+'b=?lc"AQl^2D1)e)Y[
T$:'IVG$Wj\$/:'r(ApE*A4&!Q']AVghdpp\lR]ApW&gAm[de@oI%$cO\)/R$M8^:4hcc.6;hJ
sB%Zi7+Y^n(-@@2&A?Hq-$Ss1UZ"kPCf8KGh"`qiGbH6I)%Jg]AFR@,JM?-Ol+?/3XZUbp9>(
K8bdo6c3>/uUbNsWJZ?,1qmON:8Cl%fQ>EZa<E\Ad:ga\ffZBq=5gF"\M:0&O2\X`l\%)4L@
B,s*GZ^ua^g.u/t-$bf#;`qmeI-4FMnN6OW^.2H.<JN'Dr2'3/@4[@Nc?)UFaT[*6bWR[@!L
%EPk+MPAmpK>_"LZ!Rd(C?mNLV/`k/4)_'bg:eEQ2&gAd/NI*?W+pQ(S:jSH.n)?fA[Xc#Qi
uUoOZ2j9qCVdQTt@;KAIOIK%h_4&8GoXA/DL]A)C[C[;2n04@%]A*2n3ql:/)1X>P/[N4iS.fD
rq"8X.#6^pFRNUnqZ[lp;3'/Tj<dFWiGnK:L<^[%WWu*%Qk)EjSe3]A"Ek`-jN*dtS,[FlB\h
J]A3t;5c(kPM&m;XEc]Ajg,oWYW0%VtN*/3srIgSo'P$LM$8rkE^RCR>HD>Rc/5Ir?.(.o(o^@
KOM-oN,"a8,Yt"5:G>8&F>f^66??;._\[IeIc".SC*6"Q(?Z8h*GM602dX9f:#(m:Y>(&l1h
f2CiNgRI'Y'a5lUQ+A^1>q&?<J@4>eUHt5*U^Eqdc.h".[P!h,k]ATWCqAX876Xg#.YD2"Z^.
$Urcod5XZ2s%L2cS:W#.lqX$`8fhA:`mBtdHJ$@>q.Mk2HTg9p?r;4>-]A5h@lVI,_XLCAha,
p1L&Fb.*HR?\;s?*,Pkhc%B8o/t.e&KtC.R`C4P@?K`up`12t*![>l7q&+OpDc<8RbQ&jP*Q
!9Ek9npl8)/]A>^t1&aERj/"AKKPDP@>tF=B-LC[]A_S6.rTkkU#*7=:^+Q*k#2L8#*h9bZSdq
&1*Z[P8H7gn`<Z4M+!pGN%iis6qETG$tdV6H1WNlHgfYm+Bkp-]A$*SP16+jBS/1=tdpj0.!T
rsrYH&T..J3j=CT,+[R<+'M=aqJC1,BbXf8bIS&WJt@HQUPIr>c8'iOCiig)fFgIJhV7QTGH
Qok>)uJ:DX1MhZ05)7(U1b39Nb>*-YS'hVrO$XiCrOc$',&\[oa?pqKEMO#T,W9g3#/q:DNk
qs&0d8"#Pn,]A"T2spQ5L=PF2iF_+Z51T@.>:QYj(WJ!>WqDfL')4P%J,egE*!1ZIY-,J9I6b
6U.K^,g;H[,ZJ:\Dp*LOj5fu\hj&k!TVV%DgnK72Cu2di;f&$0N:g<[gl'ujV3ng:T65Cp')
R:.nER(q"e49%1\N'uSJFsL)3h.'PJ334".D([*jHFAo7l;HSB!)_=\,i9ge*jUu=*lRCj,d
U-q^%s8_X?t2B#8d(.Pa+MRlc<=a2n>p`SLA<eh^mBrDq.dBnM<<jg?Mnt)]AqQ+b-gmaJk*1
Z">@.$d7GCpC<<6U%gn=+W@]A[h4]A;ICFH0k%>J#<!Z$eaQpgX'nE/`1NdDGX#_(eX.ZOI(JY
Gd<bYohi(^`eLc(;$e&):Fc`XP55EE^"R#NO')ACF]Aq;f[<DVLQFP124W6S$cX4qq@e[Cm5p
eU8%9gq)t</C<?E8BFM'#L,]AR%10:1[@RA=E5&EnET^Tk(%dr-#Hm0o"9J%&.fC<mf9!fV2L
H8[RWVb"g'Hg#IO)Den<gX<gg!C53040dL*(9I$NO60"%P-1;B@R>.d0R'ksr5f(5;E)1#&C
fq29bWh4C\*-);B-HU+[durYX\_)*:BQYi*.XSq1E4Q:E3u>"3WIn@CoFAFS2'(mNFF_NSdY
/qM2B>m=G-439P^7Kfd76?%jDfCm*PU.bNjSPCV/PrG88rdM*']AT;7B\WakIGXSsGh++3dYN
/O5[)"U*JZo'NL4"s#t)b'I`!\R@`ZY)U:YlpYm?rurCRF,h0q0J>Yf8#"bBK^f6cmmsP%U$
`/fiopu@cr>a78-Smq;Dl:UjQcb-uY;V^pGM;CZ`;pDY*J3qE=8(fs0\HGO*to`jFZ-.PGX0
X*;HFmrHeO`+kg[LonVKG52s<Sg=EYl8,<#JY(@C6ec1\c@0E>+t'>n-_\2X>mE%:?0aYZ8P
J@Ib]A(H'%tca5!`l7KMk(#5S>B<n=[!RgLr"rHCaS7?K7BZM>^nG+!o7E<^"\"l=F\Y]A$aBV
!`34M4I$DOrSq"F"T:pSO`I<jES-p?@a;=(:9M'%.S9n6kPQ<;41Pb+u3b@t4g2N?Pn2,]A/W
TJG3'4WuEkLic*]Ah#KjP/)Yr8El'8kW<(rVi"oYo.A6EN8$6m&EBF]Ajl&)#IFW,V<N1Lui/_
J)\B)Z(khYu/+j-E+)4e3N<[>\+DcArd&[shFDWOi,e)>-Ug=32?oies]A\fdWOWL+j`*)t;J
eVt!+mg%C]Akq]AkK^:E'<r<X48JmAnNC/q"Q=Uic<.rZ0J2LE\-q5*PRA-$bV<&l`7<R^C@.n
I6-&;GcKq#mAbSH+?:Y3fP"!`=EAW:7bb8a]A"Scs_6@?Si>]Am]A4Oro3l67Nf-1\b9dAW?Duu
"^+e]AO=/NF_;%l;8.!Z@oeE3"F*h$[dGKts,cBOjci:._I?/,SY4JiY,8oo\cj^F'AIq%e(`
bus1_e#5pjjcG>!uV!.#MJXV*a<Q$#lKim016h'i/UeKlY-:.i7J0hXbZ>t/n5^S-(W[UnWE
-D9Z=nJX)gm>`Z6&Gh;lq,X!tkdnT0]A)h/:rjN6:H^2hJ82agc,oO',f]AL=Xu4WdflCRj)fL
IkkJ'U9_D,2]AI546!_C1(Pp7!^c4(4DL/sd4BQAWV]A2trfSj["+D<qh]A]AsO7U%pk.KrUK%Uq
s&93G+6FM=!'G@UAi9#sTr*gQ;:>>c)FL_*G:NOkWMO0md_4^6Vjm56%HFqfS4RJM'24i`9&
%_KkmcpEIQbIRm)Aqni+6g4R7a5W8%K>k;"gHpb0@A48%,h)FsRUgVe<'KL`3A.`J&njhF5\
muIu80u+.0!3"J%Q@bV^f+f=jJ#3fP<ggP=[)Qf)J%E&o3!QPU4C@+g251>2$ur]AO,/7';o(
#gAX+HN-g)dQK'!)P:Q$JM(,kCl0QEn\Zi0Y[96iFbJ5)OROI'l$ll>9kH$&3]AB/f/U_\XbI
s#Yqc+"*g(4"#+ppN7sZ<V*qjIcj=!D#9Tl'sN0R%d/E%d9sW`)^g)55;P_$VJu2u[o4*0g$
^;9:o-e]AG6oNtC%Y@@PBUWD#)t8NHkLKal$))3$<M*]AXR,d5K,R=Ck'Gf)jHe0LkV3?jr2Y&
\ScD6MXF=GnZ&0:OCbuOd7=LM,5(:;+C6m1a7;NCnITc`U)7h6GZAP>@J7M1?Dl%A8nDU`,E
'J'a#Y??&dgjBDZZ3q0d\M<YS,FfcB\M4p+j9BsHJYfp4uKIgWS#ig"r()Uj41pqU-aL1?-J
HEOWS$FH=>b/M-:U]AR3L;2o!FL97JChc3FXg8(G*2&[YWj#<B'BS/%fT1<ND6/&'i6HTc(7M
-G^&n]A8BqZRB\`7$,PCAS%rgrT/?qD%$k&UHsCOOT(rjYbLR27ak(:Jc3@=2aV?%-C?$<+MR
o8qfjuX)62cGh?;SQO-T</]An5b3FE6p/P/81c"PF\`)e<u8M5TZH-g@2^gI)iP+d$2@scI2^
.XPCVX@WX]Ah%c4<*As-;=m\eXp6D`bY]A"qt\q.g4HR5msin/umg\fR'c7^tlOVGY-Q=,MVuE
/fF37)5V7*(jB#V+oj6kX^RPGf5@G-;l>Oe'4StJ[f6.,%UaK6-_P#6A#M=&S#t'=s?M'\\Y
Y=89oRNm_QA=%dI6Xq@^n2UN\IMMAXHD@:?Ps16T6GkUKT1Lt=ZlYCsd<,A*dELkrD6&=>5U
m)361d<^TA^8;P>*f$(J#\Dj1f2o1JS?SE+0rm$;Eh:%h5)u1)UqbdZ:FfEHN\cQUI/:tE_&
^--\0\OlLhg"/NWp5H);4%O9PpGI"]A9WsWP1MZ=M:EYOjuL6P;cil<q*sAkT<M1hN;_+YLY+
T)Y^S$R:aR)n!)&W-7ach\RitlYc9G8"YB-slQ(S>n',>o[6Cu&O[I%&Y/+QklEbq$Wh95:L
e^?uqAKuOgLc@D!j@PW;mmZ;,_-(k`^)^K3qjaA;#H)3<J8P.,lkuE&hn/KcK"K[bfuFK#(#
'ZJqSc;AM6ZLMm;$.dE)2@H]AhXOk:+6gjDH(BiEpM5@R'UFV'_G#mZIOhZqu'Z4`C+$;#LK!
"Q9^RSW[e1R9mb"c%QmnRWrN_GF$_.r2UJ,o4doCGN#i;6R.e(Ls%_mh<gUR[J0#Jq231qg&
o@eU5rU_eL")q2ZH?'<Jn?NWe:cg.6V8H0kcI&)oml)OsQ3'?K>=-Pk%U?,#S:Iqaa)Fkn`5
C_[LU<Jp0P"+5XD$D_OU(i>`Lh")2<3q:)s\GD#W0VPf3I11XNDcJ4B04&)_heXmD%K^-Bm^
Tt;a]AMM_LMr+F>V!n`K"h$O]A"ZC*;HW'1n$.PK6FjX\82dX7Ap2,62;;6%PGqqe:XeI4p`T7
.?X1RP$0gc,UT`(s@B.\D[o4j=!qa/OT,9WB>%iHHAHMr<>PCAKO8DOu=nfEl>?R)U4QZ`R3
8nVLSQ;r`K\s#ibH;VoUpZO>iU(Uh*273*-617%hJJ55#7sWLP#j*aU9IH[D(VPU[5KD<#*Z
[*)]AT_/-?CJ,<9U08'*ql':]AO2t;e,JdR'fagL*:k91['eT'Bdq0'.AXPP4hBfi>i`=W+l%C
W\_:4S=R_##h8bEJihr`F<$?HiVc*X<JUSOU?TfFN[d&:CqrNO*"u\6T.pU@['O*.R2ee(em
1Lue[""CVh@qY9rGl*gfX:*FEk>-.dGn-V\\sp:'8aPYrkS&b-bN+\!W7BB21[BLre7oA\MM
mK)+=tCD8JTFI$LU_'r"58mb5YWA-gY9>Hb*7T?ao^ZL-$6&LhCiVaQ&(:s_F*FebI#;YScj
#['bWdnnKreS"qCl3)0(*%FZ*I',?u5Gr]A"B=)0aMVd#:0r=j%+pY%,MFbZq5eqsi2X"Q&S(
J79=-S0b"I$iij9!^NK(2GiDD4?#+`M\k`k?1#9-X6(]Ao7t#<)l;%"m@p7(5(dVCNiPsG@i?
En6k*L(u7+e7;$+GR).rV,=aU']AGt]A2R['9;Ki]A23]AmuI"\oSuU?ae\k;[Z1/<_&2)>F+C3+
d"l7:L(g0n0rXHj7!;WXMhZ@pFmDfdWg^_L=,*X[Rio0cT;O.U3-kS[dInU'kIOW,`oEHM\1
P)5@L((r0`"$3]ACZZ$l3%dN^fL"rW!`Hn1/3G8dI^X-t,Z=`VhofaKZKa!`n9hR`9qa1OC2l
\Q^`,LDb&?i+M=&B?a??[QAVISu^J.QG4Vh*kYnjqX>fVl%5!KGYlaa*:EYaNN#Y?k0PPQl;
!b@SJfY0?.Qj5:nojId?gGl+u7WTpL+qulIb.7<@CTRJQq/iI8L1R3I'PbTN-bW`Tkj!',Jt
fjc:DuG\t+d,H?Utb0NXs9T[G#6/\.+U,'FV.Y*gADCYG^_'N;dUKj&0<Wno[O?liFnq:cmS
`22.N7Sei7=.ss70n#*_>&,Fo!8i8I;G\F)9;lRl+U!Kr?.@#\lr1p3KbB'UeXaXN,Rh6:Ap
JM<OaeDF&D^jED_$)V0(LugNCe-1\44d!*NF-<E,dKGc6_BPVWN&S5T77jUf6:cWSe?+F;cF
/UTL`D+bmNh9FX.n!a%h='d9L$q3?s5tprcoI.;)ISK+!.jf4US%PXuT^,Ckc[A%r>bFG5"Z
*29@&8lT]A8e/@ja5:-oDA`nV#3^*NRRSeq=SaLHn5%kE-g\2aJVN26CI0"l;KW8U`sKkB='9
MMruEBMd6FS:j)jU(<Wmc^L3+/m-kD(au:qJU8Y4kdCm;n2),WmB]A+H:Cd.HEG8#Vc>4^h.]A
!Q@f;eZJ4IKlZKhb,%;5,dM/E2tkJX!:ir2D"[Dl]A2ZG[BlcpUjdi<n'U*qNH"3f`j]AY>8,G
I]A4CKi#mhN.S'WRn%YOs68?e'6U>V`K_gm<g==g&MZ0V.;,ULWR3AS&cB_uN^X6;lg>bhl+\
AHUS\.GUVFfWT'cWd?,=mGs24qsMD1K*\dsd.B*%Q$m0jP)R7DPbZNBo&k:tE9?ZhP"'uL[\
'83nZ/Jtjff'aXB$jsr*:UCYr_QQcA`(((jB.j2dC5mWRI053\42o6Q#>$lrioic\+MiW5<B
cK<n+O123l2-A6>@lp-ibUIgV]A!;Bd\>J9Z`4k[Eo3383kJ5]A8"$4-t2JgMeRhc\lFJ?>iVp
7&0H+)"ZblApDTajT`=)@##ta%^gB0DkQ)F>7)2(V+Xa5C5j_C`hd_:X.T=6spkFbFVST$52
#]A.lNSj9Uq%h-XDbG\QTC?$D[p>lN<(7q-qdO@%`iU!JaGrak?9gTaD[S=gQbc@']ApH3qj\f
Oe+VIm;.aOUtStRCMdO"CUEa;EZT$TIO_LmAalhgEGu"rg3kGHC[LJ]AE=[#cbS%>$k0!Jn_g
'DtQ4S]A4Sa%Rp,+OngmfORKakkbaV.KCF@%:J25DNot#=VJbEW/PoI\Eq)<-rXs;K?[7c%h6
V-.p9a0BCm8Crr%/j-_E;7gK2@E7Z2\Y:##,#Zuf9G#jU<:Bq)nU!PsFG<?<KZ"hso5$C0OY
00lc4h<GN_0kj6/rP6#4icZ=c'^==.6Y\dV+g*1I8gr]A3gEu?F\WoP(5rHmApu/(dtD_\3Y+
G^D0(&KhD0uS7t_^"1HAT:Ym&]Ajo*DG42-?_Hh4a9<P%X4l1Xdbkg#G8o8_*XYeP_[h#Wm$$
6fnNOPnE%j,lVh'b=O%Y//U&Ji`D)-AC<?!CMr]A24LtNEQ`fZeo[?EZ,$jHHpGpH`"B^>+/%
5g@en\_?/!-bJV_3Th-]A:SXV;9qo!Mb3od(B)N.Si8Hca8JHpOR"&$tYX`Q\4=cU=59"d?F+
`AN^&nh3eO-!<`aL]A!VKq-=u!U;S\%Odnq[__2i[Y(H76J"gud:;Ni`T^'KI0_qK[0)*I$@+
B$O^Vtd7tgtsVI+l,7G0LVQa/#7=N$="bug8W3SH1>k.WtT(Nqaf<_2P%o7,RrjHcPt3QS!f
fI\Ki<OB[-5TBD+hYIVKHt5uR4G"R>q"5H!-J$T[.kE2tcq:AW6fNet#K2)L`A7RTaZA>=V-
\@h)2'Z_#?F5uUBP5+ac]A5JuJSOjXGloJDhj'M%iflg?TSR]A`aI\rMQ)qQWthuff4R@%YZU9
5Pl5*W++#l=+N/'q;b^ks3D^1#8M-YOh':%*V70)E$%o0'KH[$YdIUQY=]A[H;:TM"6sp8=.B
i%r6=aK9W(S:+L;Dn?so39lXsKf2_O'$/sD$H]AH:Yc6HRt:/mgXRj+4PNp`jg<We>f)c2e=\
`%/K2nJccfb1i*.iTXUXq>A'>@KNjDNqdGHh8SQnCYiWd-Auc%So*[Zoi",&.Of($T\V(?DX
jDLt\L?#/nWodgI]A&GloUQ;$'oQo(&GIHWF/(KESCeZuOsN31\W`!#F@aB+\3aDUEU$4`0T:
BKGBbmFU`1fGc?I[gkVp6@nb^#Jch[RTsI-)c3a9\9h^T\CR0dj2e>jUNj4<k#A6"3>\A%Zm
UAlkcd1LXM2Dp7ZQm?4.W#pls[_+CBE[go]Au2=,Org([i+&@JDeH)d^,'(G]A2#Wc^smC(Y_X
cPKn%t5_nUY(>5gnAG6T:dA`(@iehj=:SrmW8nf')#]A%)!"Zqm4e2(<=F#P_?8a57k8E>QT;
DKMj_g#`h.3U]Al1SHcW[Boi;3(oSrfrBM"mF-nKrIj43o#k.KXn,je0-dg4<r=4A_duO7S.N
>B!Q80onBIt@56Z1r=pVK7'ne@r]A]A&u5p9,"jQ\rUnF$FN9bP;.;*""d!mNlh2(Gj=-T!tI>
RDU>2ES:61".\/Rd-4/C@6>gYVQm\G]AU(Z<]Ai"@C"4'?-:6qr"BKmlUL^*gREL)l+]A)%rdqF
]A;ML3)p]A\-m+:bLaV.R=jFXlOCVJVAE'te,$%Uc%A35["L+tF:VG<`R,^tS?ll>n-qTeEa)5
lfq6mfS8HF;CLMC&:OA9>E_Yi1B<E\(=A'dN2Zl4.`U1\Id7H^/\hd!R*h:r>ff^o+5tpp/8
Sr%XV;rDUkRaN=HlAfpAX)?oZjWU%h']AkILS<5@fY&?h%AcDUUJ2_f@>-dT!RkZq%HV3j^PG
K2ls1"+*\\Y^]AY:H%@S2ie%@7cipRul!b#`nuYXDQ^hCK:la$&8p;(-hTK2a/&#9@23/_d4R
=6<'`BGOj$Kc]A0KG2,IqX:-tu'N4N$9!eZ5^)9-iRm"Cs2og1u@lb$ES8tR#_^=D3f@%WZNI
cbCi#9@8OLG;c3hD13GBFQ@T@"I_HK]A%OF8S)[R(L.6KQQ>.a_toY7W7sdQf@kMc`Y3AQjC(
gfgHo2F9YC1Z0,b&olsKuT@TXEGfLCG%DVEKM3;rcfJ>a%]Ao_]Aa/Zl^f<CVCB;>*0HZ+SfY3
-/Z-ihEGID+9T=0@[HA5h4)6H+ae<#p(o#B?UjdU!f<3OY;&0>`\M$bqk^b?qOm.Y$m`CB/0
>hd/'kue<<b_RYA?I*Xl8P.jAZ\WS*?;JlXf7ZeV%@iaQGLed'.8b*edeRpD0]ACP#u^*=$st
bSsEZ(R9pR)4pa;iNtHscl&@ja*<]AU8fsUber%lo*gDIA2-bXjd8gfUF8_Gnl/B8W`&DCAHb
`o48SQ=>ge:`lkbiQrn9M/MgC)o!.O)0e$4Baed@(7nG3;YX)R"`=+^$5;q<.QY,-r9#_V5-
b7ROK"^UIj;G%k%;79&l,gbT^ZR\i8)H_^mP4$ud\.#LFs(E.*afBl7<rLhHnOHi5Ff78WeA
ZK1\^TUY3Q2S6eG!DURf(\]A-AB4*S'I6Z&*]AY3aW2,qW\iu)>0Gh5M2,6cT,5&fqo%Da;jFW
L/!fd[UNLrs3q#8@X[XRDOe`Tq6]A5WLQ<#bcHSLX2"]AR.VJCI#jd@2L@BF"%@Ja4AX:`sh[3
f*Uc1\2uA'/gBDuY<R+tnu[U[`fFeS:Wi-23TM1<7d(XK1jXgR,9i13-b8aAHu))(nRTqh8U
R"o?]A7n8V_#Dp9`?&)<p365@'G13KV-FfP&Y!Rp354A+u3[%6&MS]AWjp6O>RlNc=Of9g>6!W
onTD+5OihC-[)pMunjbkibeE;O]A5(obdfR*4+i:Pe(8n3&H%acYdQ73FZeei')^J(#rkR3)9
7CU-]ArCjc\D1n<6:Z2C2Ys9]AM6Z(L^\/IXn2Kl1s)<Y_HQU;RdP]AEt+>MtjXm7:H#9$CGaHV
%]Aq"HZ\Skl9+=Q]A,UC>JTTH^0JU[$4VD6GGt1UM!Ma_$llNf</abOhFq@4WnD"an@)W5tXq-
7Q`SZpB%CDE*N0CIA5C=p;L,;**;@6PicY;M-ppA?e\]AaWrR(1h(N'/;KV\fR)n6#J(bLD1Q
lWQ:/1.n5IlQ8VEpAC/pl$E2KP*$WfM3LcoARTd3OphD@Vd9Q`N&I#RWZ`1M69^ae_$RTpoK
/Nk2jVGu&)Qm)Ih[R,h@;@=>IeXd<GIRuXV^O:>HkEMq(T.)[S!X$/d@q6eDEcf5\JEA$Y"$
-26Q(^9p\`PG%QC"jH=3lYs(7hAZo2V4#F*\M6qm7.`OAghXL]AT^0\WXR1J>#kHO)Ke"7+n$
8f)PXn/6'L1Yapnclk/]As7OMcY<XiU$q\s!Zm<tf<5Dqh'l9aq_5Id2s<&>-#6&3a0oF>!;S
fPWm]AN\t7+V=$$.RC3IUJ?O87nkuqtY?ZikT9's93S-u-1U`M70F1Bb8G=Gq^pdd3X*.AZYF
<F^S5BMZaIsW*Kjo1\Tdea&^)c(UES`pG8j=`N;[ps(mF-!r5#+&q&UUN^EV6^Jf.::8-V@V
NE)?JQGBE"ugL'YQXIPlS]AA^u'YU*W0[GS$3)Z?GSkj;6*!3_P\`tKr"2]ACO@o-A.I-VcGBC
9GED2)E\gL^EDlV\,7&CAm3D45Lj;W4'1en7tPKlSX,8Qc]A=$pn,__Eg,Ys`+e;#&b<9-:rF
ud[i2g/2=ejsjV`(8=f#-+IbRd):J9Ch*Q0I\Dbke"P]Al]A@!p-0+hqou(!ZYRg!?XuO>N+u`
iY_P(hqqdY;8qUEe)LBDrEsYI+c:NL+\M*PPBF6rF[q;!<(aMrHY1b5`8.&#6`rN!^AeJ;]A\
q3>]A>q7L+h#[r5g?*>hk""6Tb.(nQVZ!J\HSJ;mh@mh!f*j$K@Wn1hHWpR$CXsZF$Vr>'tc[
%IZmo0nSgTlN_Q5QCMF;A5,/tT&BkL=?*1e*cComA/kPqC$_;tM^5BHBG9uVR4!emIlCa.Q[
#p='[El<$Bk5MnAn7A[eC/cQh,8]AVE\SuqYM\7"SC!ujpO0Lr(ps^R+O.l@e.^4l7d^"J=Uh
KeO]A70Y`lMp5f\h9<\5<t[cDl*HW>:OW]Ar.6[*&':<^q]AUkQU/CW!Ej`8+*^_UoBBI0(eSD.
qLB/kNapfZfp<2=0:Nm9#r?9F-?>VP_X]A(>&hh!?1lu'Xr^a#U/'Mk;`V[s%bHYdj:$&8?(l
gDSU^e3+ZtCoO?@0G&R)b+6+*WT!KIsRdS8F7b\2lq7>NSH[84<,,'[<eo>sDsC8F%p!9t+P
V=/RE5@=co%?$&u&PF*C4*l\p&mC=-/Qb7:/JJ:f[eQ&GJo_SN(72WY+)"2`0YRpZ6N7+::4
?I6A=)s%H$G"/I+R9_k(@sR`4C,Eh@Y*B0i/)tr!NhJ^+Ce(H4^SptB?t,(FT)$T#X171'nH
i7cMn>qkYV=_]A-BccR_:<N^kF\Xf$q>)9$@WS\WZ+@2e)=$FG+"8YDF=,R-6QMeU#BMZ)J0"
*LY8uOj$#<8`7iC'bRr4,tan-;fFA1hq.j:@aIN4a(.IT\!4Z\F`p'Y-1kQ8I[m*q<fBb$66
aERaNmop`tRc7EVmN`6^Td4X'2^eA%#GM[8r_Ys1p]APW405Xl.pYjBn$h.\nCr/F.Oi,VY+s
=*B)O2W0A5hF&1HCCr,fm<OXm8)3r'bQ_tpYl9+CX1Wp3WRn8GnOO1[%5qXkQ`Ct7XMk7Z5C
KWA4(!5lV<^]At[^]AM26Shb*j!jdQ+Zrp^Zl"i,rCXg)Z5Sh3JKBERc2\G302dX8jZ+#2m?S"
+F/*HR/mo4#L#j1?(1Z,]Ak4m:LWSqo:m>:;,S!EM1^C!qpLLqSt0,#L(;PbHcJE"6(om(`)"
n0Fr!P\%k(6aOgar$s+n]A+#\Q]A`*#Jf%lo0mlZ]A=m3.$:U`rK-OF)ZG)j"j22]AU?WH^bs6[*
,92\5tOPN0q#B.OK(Tq\aer]Aco%F(<m5Ho)9cr@dGP-^(6]AZPuNNR9l9@nMKi2.;2/[7#)%i
^!*KRdI]ALNgVG9uIYjj$oX4C6U%'q.=_^k*ng7sD.?^EDNc<&3LPc\4\m/m+A<%DdMp=TgNk
&:#Y*A,XGBWpATT4CFNYSW3j8!@So^=%]AOPNFQ5kFj\\fo_s(d=EiENZKF*kRk%:>13'gT"9
ocD9j#(7&^T`1DRI1D;hh\!bkS:[,RK#iZW8l4A%umkc**.2>L8I\2ciTYC9)&_XA.`fZdA0
Po'DTAu?g4nEr>W\<Q<a,")1QCO?tI/DCgrm8&SQ,r=9%1iu,3i04aGRXsQ/.LCTP-#87")L
XCWWGk@CR[bm#%:GKbF_?WI_8efUg97#]AQ`r&>5n(XAp81=1VD^@@TO&U#'bTpI5'1U9VkY#
,XT1fJXu]A=`Eo&Y\-JQNaZ(-^\</G$`.7E9Wa%#>:N2"]Aam]A>YZ_<BaN6a\8\l[UO\QQBX=P
Mjb8JD#tQ?,I]AljtC#VVP2X>9U?l3']ARQG>X$n4p4C[5#-)5CI>NL:O!eC`NVNlO8N4qejs\
RDEoufB55^8s]A_=@:3t5%&bNDenEoZ8.*1_r<"6*UJna6GpEXPY@Mtbnqd^9EF$HA6>h06KE
r9Ko7SSQs0/aA4eq"-<m%u"BXV]AktaF1n1\&@7$Bea*`h%+fM`'@eP'LZ";mUPmVHS2M<.]A;
`kNHfei^lTb0+*J?t*T'p`D]A>R!>BnH)2_=a)MBA%p"Ar)PNMO:*@D+HOY:'$8@dt/B,Gu0:
4Q^KjO?TX9Pl4\PM^\eesXtHVa]A.6KM@PmK_`W+UjEEq[C$U80*d7+1<a[H0lD(iH5c7<li*
s;=8n'!9NTWJ0e5hu7pcd\1^<I1(YDct9B*'fcNV'o`JnYLThq/r$Gs("YPT.jo0.-"D-!3O
ZI&\>;%bWJ7IL5JpJ:f>Tpa"P$jb?!hQo\#5S-aUQhg#!J=`(j<Empbaiq%l0rLpCNg>2Q[C
hF@o;]ApNd22mJ//b?2)f8qqNtg;\hc1EgJq*trfJL%$Ni*[,Z";GKBVZ[BX!OX6tQiVNH[]A)
SuC*s'Ll>cbr&4IY^#Qe#0HN^gBQ^la(pW(\nI`&DSkP$scMD*0hH.aPdb61:3ASq-!:cs$p
'C)8PtCH1lr(t#(7hWR></.'%H(>[>nFRAUB[JMQ#UOS#CoRs_d#[2q?3c>DkG)DueZ?3-SP
R:_PRqrc>',1jrV^:(aI_P)>r42Olh8T[K#jZG,aQOk&*@/0cj3Q1cPH^N+]AjJUOkO<MU(h*
*%'XebI8&!"#^rarQn2WmP3mhTjTr*KheKS9h/ZIT;b[O)g@-XS"\Jp*5$5bo[nu=q=6m6(A
(2qQ#1MeUm*0;M^QE5ugRK<*R\r1U#6S)"'*7*;@5LFEPppn_+8CFTA.[/:M^T'd2"'g[^O=
N=Cs(gq;cfg8kr/N8.c^O$q@!``f0K5_>7:*l%D6Z;c4#AT^'L)?oMk<Vi&CPDW9?@j\?F0@
=nJ0l,*]A(JQF3W3%d-CoI26'FoWI)+Bp>Dg19)1";+HVd2l?TM0/K+"bdVI[K)D3HR,HG`-)
;7:udrSuf042Zr!fG\PhqL]Ar'^R<bElSp<n<AodeEmq+HO_6aE5(/'Ek%[QWi'A]A.mq=uCn!
o1)+BLJe/0Q'o[F24b:$:&"N;aal+N''R,ZfW4FP*_l?P!Vkun<%VsMGC7\gnO[%hcd%iC6b
JC#IlqCC;BH`$HQ'b<'ZV'R3Y7Od+%C<b7-^Y&D;3I=H(pu\uL9e_Yblo17SLrBbQ[*4crfJ
OO&Teu/-Zs"Xu]AW?)AVhO7jGNKa#oW$4'9sT9M:6(0&mR98IJWbc<E3m>5l^8(VpZPrQ04S5
N-u["j:Wo*o8Rigp)BsLG_r]A-P]A?D,Nnf_Y,VhC>"\3XPh*:<rJ':8I,@n$I/FA62?r-iQtq
:g6_r':F!^`0W!i*!WOoW\3QTOr,I&r]Ai62Rg_-p7_ZdaVecp=,><f;>G3UF@JL9@qql5Hgb
sFTQo99bcubJ;56<,<*j!el5'W_Z%WGi'?l3gZ#.qmkoBpgm$41.H=]A'Ag6f$,ZgPbR+F'ZG
p279RV6$W]A<L5l`nlX6?'[o0gg:-dlS\V"Ll1bID/si1aKh<maHM#q6SLb'[&H1UHNMVH9p$
gZ6KS.[c>*K_r?GU<,j7Ci$r-cAT(?E)K"]A!`Ib%PmS`dcK*oZNq)oqI%GDl@+4-8B`Z-WC2
XGROTWQJkh^q,dX%+->L6gVCTBJj63<SokW6[dW+bD.>d(p&(/'bY2*s;""^;<$gOLITV#Kb
hM$&Bs[phHHIg=i2YI#?%2b:1'*p23GJ_GVdRlAJ%e4i]A4:_Q"gq#ONG"*<hFD!UK,mdaVgI
-Z5c?6^WpSFu03S7H_d%Z7rZX45RtZAmY[;LTNT]AC8=L.UX&3^Q$86;s@eCk\')T1jX>:MrE
ADT/iCie)$FGfEdnZOe_g8/b[O7>`u&HZVtYN;TiR)WN1*P_ZI;R0^&;%LB@;VMP'&q$Fb,^
</UFNoG#^5+@a'EJuR&NicK9_Z3\"Wf9qG8ru?YfsB::kC*jgN:*S@3?V>^LeZcko6h4f&40
Z:."[qP55`f^XKF#[<[]A@W#jIq)`?K6]AR%HJO\BN0)\09Y)5kf*^C<)QlKO$<7=37Wh)19=H
CT't9P]AKY`k54(k3E9!q)*ADF\1,PNNO+2_af!YD*+H]A*g7JQ1$c$TnFKR3T8'$*nU^mHf+*
Fnj,"XlRPgmellYh6gKD5H#^pCE5/RpR=B*A(?l/!j#&Ziei3o-KSW2Q+Lb_9@n?&.F4qFh/
fU/XCYQ!q"qphWC8/D*?3oC2qZiqH3]A!*DnW:Vu$(IJk/^7!'ss$L\C_O."`k24m&odau:,4
6pdZ#s*2pW6.:L1_SM-(QT04SD]A*GN-Po\/*VX)6eb%s)9`o_.B?37OoTbel\]A>`#K9$@B(`
'WV.%t5(e)fIdSRfUlONULKC>tr#6X)2%DC7q#g.XYntCjPGb?a[np@?e:\sZ-8s/G%`;U=P
RU?5,>/Bh1srr;#Gb(a>S;O8d`X!5!8^PP_Ij<7?a22)";-E,FLaS^(91&I\Kk/54%#rT_@"
/N<a@t]An)ek$Gr-I3AFV2K4rIG571N2^C3".t9;6[Z="<rK#7/'Z'TB*JD@k:J-CmFH)EIYb
)nPNnV-B%?eTf<)T4D#bmS?6iG:jZXQ^W(S+r/;=MC6^.G:+e(Pj&LC!aC@#MS]AVHIm'ds<P
AR#XZXWWT<T`Zr;8!MTdZ3WlHhD;p9dU%=&qrogE#D2pgrTA=jY>B;.Aa!K'N1s=.+=u\lo5
nhhK\(mq`o\a&*/H/fGLf2LQ1^S6.V%rg&0#gFI6"%M+_W?e'kr6Dr=7[0fC#-57i(4q$qif
,$Eui?Yg*X$liV04WB4_X"q#QfHk==AD\aqq70s[R0;T,WE/32AU'B==Jf)S(B&_@Hgi\aQ`
R7lu,Tp$P:d?LL@&A]AIbmiESfHAR.Z#-<qgKC)o'ZOH>C@U/(^IKk.KmI&U.4OQVq+@qK_1%
H1/GYKa142"l5#sHG%:>*FTK(YE>R5$*eJJrUFTbkdJdWI+LPT8X>8Ss*,q;iSr*-[u>?jZI
[Kle<e&FHuDPnN+IZglQ&<Gl\@;*Y+!c&M&c0@Ng(L-di+6hN$fse04?jLZEXbW["PcE!nOj
?lIMb,SDogM$5.Oc(7mNrk*X)\!/JMChg&5+%4Iid?/tMK<)5kQN;M25LC$pOcSXf!Y^6MTF
gVM+4ZB.!,Ej3Mo3fSuAh,*/n5?_b>"f]AW4a)aDHCgN:hH(>`rD%]AG?L:h"*eei\)b>*4$!n
WHMeTl6G6><^"T)u,TY=rCIb4>[-lC&u\!4l2^i/8J]Anoe%jgV\8f+,Z9>nGD]Ab>5A9"lkV[
.sUIIU/QQK0ZhIWr;IYB+u%I;WJbe(XXViP]A64GOojMP,Ae*oh^VTc`6$?.CJ1B+&H!=a#;8
mAF)^G"R]ADL_22T?oe*Ua]A#EJulDA1bPLO\+eu5kAXGhh6W_;Ho]AS4[1R/8DXFf?:@dq%@It
(.mf5bg6--]A3`cJa8bY1<2=3'i/l+nM'#W"Yq"p-jMYAa%3BKcPDtL1)#Ug0sH1P#a%[Si!]A
8@]AF3=2n\/QS/9r6S9CQsOghi1_1.[Bk[X$52\IQR&i=Wql3f'JjX$bd0Bi85jBW0h1\S<&2
,no,R_BItV$/CKa-/e/<V)3gUtgg<"g"h2(:!SX`<H#?$0<`:ngHjY=1I([mDmSWnC`jU!Fm
D""p,diHi&E3htDm;hE&-I2f'?-)X#/;iu60#n7DSXWNGp5cXC5&ci-lEN:4\T7I=0tq@kgs
hm'Y+q8Zj!7b/IO1*t<.>O2o&^1Q_.&=`c;_N^0Oi[U_'jfSG]AZfNPM0pS4hi7?(O"#Ubkt@
0Ag)n4f,+1Rh'8R_A"E#5"D\7k<.\A'8D/u8nVi'i;<Bqd]At>k8E\(;PeaS9[n'*>O#IXm4.
C\GqH@\B,D5>KHeks\T;iLN@*E:d2ks-`I#lCQ\=R6]AS,N]AH(@J*ZklBW2QH!LVi[7]A*t#)I
H;4EMgm?Y@h?PNENm;fP=,MooB=j-pu(3VuYZ[kB7?h`P0]AV`r/*6]A;B4Y'D#mN2g4Opq3q3
52N%/P341k6QlH)</qsiF`hX;h+qYh);NQ)g@"Y@i8$YE7XGuEIYYC]A.S(o#^H%4d]A`"/<C,
g'A[#\k-ofkQ4$LhH\OIc+erID<)[XNrA;oJX"2^)b.^Z$_i"`CO@WXDeu:RICJHiS`C!`n;
!K>&OkWSUY^\95_k?(0bIWnU`5F*c-c"Y@YJO)2-!390.3jUpucog_a8%41,u>-XFW5DRZ[d
=#)r)nFub5fRbL'@/!iqZ*tKLJi]A]ACK[OCG["uIfG$1$K,&c*;X*5B'#XpAs"AT1De@J5j*p
#2>i9!aLb@(hZUKgdH,/K8q(c,:$MP91r7X\Pc!k[57VdQ+#+$>')+b.bM#-&'M-9(;HGJkF
i)&M5,:oocVSt+'r.ZML;J\]A=ZS7LY-j);LDu".Fo6+@?eW/KRj9F"/AA34Tp$;sRlRX"3ha
leKcQ'\u5PN#a;EQBgMDrn*j$Uq?Qe('sK6TlMn@m_GUk#]AdOo3l5N=5FSOdS*`Ct[_V's/j
`pU,)@>OL0olm'4nM=tKnRXXAR0Y:5[nH[fd@'R<]Am?DIO[ar^WU0K0=_J8,q"2>JpmnC(?T
TqY;LOSDF@cD_i;ZGX#Z&olnFO*:Rdd>/K7Xfdcp`GoFnYP?d2n9LkWgIu.^Fhit%!5#k^@_
*=)_I(&I^UG#\POOUc]A%Y:h7d46Vshr^7Q/^Y:*FE3LX"2\0)8SKrq>U&Jo@L0%BJ$/rr'$=
[0us/-:\h9&67,sln3^SMoeWj=!)URQ2fYVIts@4\f-!7gN1XuX03qXN\7^0[,k^^0@f$Z2a
_4>f7e/fIgH"nFdrHrII3I.(I+)]AK8m[X'mmRk7H$:W*TER7q#W8>U&lMBrNd0Vi2Z)H2k/'
L20]A!&??)GbYJ'SFHjKbmoc)`g+3juqW[%Q1%I)#nMF)ZRa/#@*aWKEo%uuYP(fa8<hU34QJ
2G@+c7QRJ(pt8g/W]A$&VJDKYp+<pY$&5s$?\dF_=:i&#rX\cQ<k-%#@uD&%AUGEm8quB^%qb
:fMjZV!#/XpN*%&9U<F2IP4_04OH)4^g9-2HLIj8AO(<A*'o#n1cG,%2H,>W(kgR?*q[)1*-
kM5#hRbDcmVRGaeP!cgtbP<MTXtlH1l3r&DB!:ba/chA!Qa?r=H,fl:B[D58$Jq+T!o@Q_ar
PL*_jBkmP<`rX%pu:H4Se=2IQ]AnV')Ks6.ra!,(\*JtXZJT!Djk,P:TA0:4-]A"*N'Zg`"+Q&
.KHA.g!TNkqck,C0rbZZAi3rD`@[C[)e"nK&9\Z.nQop./Q!#:"-NnoX`[E*jh50sqRF)f^&
*S%DT0K?fc_p!DpG`,;!VnIZk-&k5See[7o:/P[Xo(\Mr=^r?MO"2N!_[<l--3O&=RnU`\4#
3#h*aK:[GA-oX6!^Eo.mrShn.NV]AVjORFh$iEh"OUJ?_3ebO%pU-.r\p*@4qsVs&R8Edj4S9
1$sa^n<,0;_tr^T*rH<%a89qEJIpK1W"jS.p[8-!0j?#am=LBP<D;V5EV!Ng'*,,GY-lGhoA
<k]ArN2!S99JkVqo/@4h[u0ho<BoQp!-p:OUNYp>f&%$s5o4UH-"AfonClZAc."gosAho_QjI
.ZXeY@HL3J_7D_\&U((M:E>bqC'jPeR0u;kSOK=F7"I.?t#QMBikZUV`_7si>Bll#'I5rg&\
$]AuK4m`4;d9,gFT\t"qqi8/kDc;tkc<[uoT:>lL#oROokkaf-6cD()A\>1OA%-AVB>/rIm"W
3pAOK:3r=A(XS"BC'IH;M9/(pbrdNJq<AJ%PSqc&IPSOACF'lF"&KU7#)JBAM=4Rue;?7=JQ
d7BW*n/fbi/D@!WqY2i.pb1D#IpK]AY*%igK!8C*[dj7O;BB%CoDE$=V0^\)^LMJH,M0urINo
s_jBGj=A%[0H=R'ha`Y-EIl_;Gk):gk$[G;@(%@'cK[RYbNQe(RGfob9DkZ$Z_&reG':aib^
/&c-DlpHMm(h%o&bi1sc`.TgRKZi;Sgj/amKNeM?LHe%!?es8(M'4;LG+$^Nna0$Y'IJ82FY
e`(,F3iHs#5i,/CDl:7O@)>`3p'rRhoRM:#:GB.+EYjre-m$:6T6[AG)+kQg9VhOZJCgXfkr
+]A24(Zi1T75o]Ar^q)%`%fi_74s:(sf-lMZ':J(k;(YYpJupJA4=Z@G)n3i3S^kSHFVUb:L\a
9Yn^"m$BEWqs%/e[JqH?IgL[t]A9g^+2CAo)QhTs'cXIp'h_JP.KR,tj^n0oSb4%b#Jsu"H7,
^f8]AN66,@#b&uh?B72^@Ad_\\,[^i\:KI1fchpGjJce4Ii2_Jh-Y2GGu3OjeJIQ_]AWPcfsuT
aFlWMgf(Si>^c0&YmG14#Vi4"BPP+]Ac@9cnOXmttf3ELFF<F9sXgtnTOM\,YK'FoQGmVL7FZ
b/63StiY7=T[[;&<DtP$#.TU'npY1jUV$&iKbY9AV>H7io^EKSYE$Je+)ZOj9CZ,2Tr4K4.m
43j);'pDm/C_OgKQp8Y>+CA">7M=&_4`DfFGS&:=4;Ttg.9^usgE9BId8p>'F#[rN%>W8NFA
reU\ZY-A?UqRIBGOC*%VhU!i7HN/;)7fs[:rAJ-Js!JH>Y='eFoI6N'AK^bT,5bfK^b5f'?*
W1mr]A/ZTVU=TtV_kML<a0SnRm`Q`\/,LFlJ\'[]Ac8Z,qGIOUQgG+a!"&N_c#U>fJ,OA5V(+k
!MlcrMp@1hf<MaYI8X]AHM">??3/hq:C@0;Hl'sgt"BUN=`^RJp8s)qcKDn*$(WaYD+Cen`9J
((o:QXH07;LFW4i6@VKRLT=IM/KlZ6!UTYQg3>e7[JDo,$iF\'?dd<j$G6Vn^6ajA`HBQ_,K
b$(VQ0%bF!*95iqHZr-2\iIn'J6mG]AS8SDdjq$:WEOH%"\/Mr0%h+KDMi[ldtRW4Y&:Qe*TA
aHC@=/^S(6b\7krDJ;dW6aBP%!'YjGN/<fEeGe;:)'=7B(8(A)\UCIBl(g^KT7k*nTm%maIM
q]A`IJe$4a4XhmnNXis`l_!,lh(7lA?"!MXtj9!!SH$VPOP`r=oCM;h$rnqbY:(.>Rp-4lp-=
XYEc47&_CQ[7:Ut'h4[ELj\CVKprrZqDt3D54kkD^cTWp40]A,<U`U/'3s+ipCNnLfoSfSs<K
d6$'bGiSHel1""-,+__ntO=XNER0+0;a:(PP910QN=qW6jQdPbQ%DuHo^r46F+sK^d;uhN'f
^VnrR,IF[q4&)rIKJ**A$d]AY08eh3>SCMAf?tdUL['#C,J^IN.1`0@R[@#-!g/GAdC%Su.%2
n?F80(V%9RCk2P,r.sUrS3ucbrso~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="863" height="243"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-16744448" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[订单明细]]></O>
<FRFont name="宋体" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-3342388"/>
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
<![CDATA[1104900,838200,838200,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="6" s="0">
<O>
<![CDATA[订单明细]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[订单ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<O>
<![CDATA[产品ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="1">
<O>
<![CDATA[单价]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[数量]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="1">
<O>
<![CDATA[进价]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<O>
<![CDATA[折扣]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="订单ID"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="ID"/>
<O>
<![CDATA[A3]]></O>
</Parameter>
</Parameters>
<Content>
<![CDATA[location="/WebReport/ReportServer?reportlet=/Details_3.cpt&ID="+ID]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="产品ID"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="单价"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="数量"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="进价"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="折扣"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
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
<FRFont name="SimSun" style="1" size="108" foreground="-16737895"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1577999"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m94@/;cgEYTcI`9#MRIRg&bt0iq42b&uhueO>uJQZs&lX'au54U;dNDj[0=\8^UG:;Nf%/Yb
`>))*:kA$:=Lp&Q(7aSl,]AKJOCap,X<Uu#t[[.cNuWi\oXM;cKLnJ?[29QYJ&Q"f"9eH%Yt%
p52pc=YIMfG2t(s/8,hUgoB&'lkKWl=mPhmMSqtZHS`\0)X*XXrIssV_G[_dXA_W"4U;?/T0
*GVXCY3O>MdQ*madR^S4<F*'[^0&T#HQ-G?.n[d@QWW2mgm(Y3r79i5=u[0heh!cLeW-chNg
ro".L6*T2t)bD3>F=l;IfDYH/ZA8EjO*5rU><l,Hkn@Pu/=RdVC1i6JnfV3C%OJb`gS\E'16
p+/2$`-bcKpN,MCNaF2E#5O\@EBO-+Q's.CT4$t=\cfF(.S%mQgn5D3Z/"+$Xa7#6dmDOib8
VZiAM_Bj.6ce)58Yo'EaFb!-89%DBm]AgK/?>@R23$eG!_9;qn(XGk)lsr\(]AIn6$M;C2$pVB
^21X<0Q.f.'gk]Abc_\6_',un<gf@TfCPjPLI%Xr%"UBWl[\b3b^Wt89S9Ya]AF9tsW?)ne@7g
hKl'(7!e.8EDL4.@")N#?U\TD[?3t5h)i5K>D"cTC[Nqi5\DibP7_WKFsbMm\I!<h8m*7Z*q
2a=_7\^3S_!NO`cehqe5-0oEcBLNnBVh56]AM/$QGiuAFZQO!@i263nrU[:jjCeNkIbb_/mqZ
IQdC^@\WaX%87AKM,Q<j]A(KC]APtS^[*EB'jfB6HT[ot4W(U^L/io-p9E)^Oq;u_ls&@;X%^9
=MPkCpfmT9YRL#jeVQN,-KT4.h98_kO&CW>E(X]A*Q-!p\GS(QaYa/2fC--d,dUXbqI24,:Dd
/^)D%l4F1a<Sp\7VQ7p]A3AMJkpO5*E7b]A_<p^03.m4pA^M6C"40,6E_ddJ%=RQ`-(<Kk.IUn
pYgB`l5I"c"u$'.(RH9s3(qH1SVYLG(#D9m;c\[!G_GpNdm#A`VK[oSs850^:RAB%`,WW9Wj
M<p'J12_!7U]AK(#H)&HoGI%Ro9k>_2KokL1OC$B(\0jG>d9[(9#1nnh`+86*>pm6B5[9r_/W
#c0Y]Ak3GQ_;>'!5n&:+u\.K8>$<nq'P_EpmH]AC^3,+@@:$U`plT\1%DiUp%:(hP>nUK@OEil
Dun[M\un=M&>BaH-]A3!&[&QkABO4O:=.>RZH2)`tpUA#nmL%i?FD`_7DEekUN@a0HlN4+joX
qi73O<l\jJs#VFLpSl%E#EFiQf^>XK7I=<D>n$Q;ph0kGLe2;CCZnX*:B2Gh"6-(\jY&&usq
)WjqW%Ysp9)4L<G8^4Q^(:hC`+e\7)i(1l^\rI0&Vn*2[ifTn_\qXd<Hi8+Cl1W^(O_L'lUr
,=]Aj!CY_5KRcn9?rJ5A5i3d4L9Z-rR0G'IJtFY)2t"gS-U9XeT4uG,X_4m<R!ooK-KnBXKmb
KeX]A\8L6-GH$5/&<Rd!Rn%_Yq0(RNJR>_S8Ie]At_@1fY73q%$N8t^t:@TO1O1CBKXXSJ-i,K
F/@oY_tp_p1EQMPZYdQD\TCrR"_!OB0:3f-_3BlqRe0@)P[[<TN'AE-]AYH;UOR-2S,_>2PVT
fel,_RLR4!"fjDDl!iOGO3Z52!;`D@tI]AV/l?(Ut_$8K*-rl"?J/"b1+rr*NM+'DN>Rlk'b(
W"XbD7H76=!,0qHW-`C>tS(]A"SU["cmK:=q1c2qS@cLG,G,WF2rr.]A'?V#0;8-HZi12>.Y"q
^oZ^Xpn*KI%%?UuFj+%,+fi[)h'k$&P%-^QEmhYQFUVs'*<<r6o^jn*%9@h'LiV1qDa_CBW)
7)80Y8V-Fb1CDHLP2Fbqb_Tka&dI45&f5^84.<W:8eXUY@t"%/FQj:rp-\Ol@1EGmJ\s4/Ub
Yl\K[p>:Y,uE!n\U+Vg4t<l(cbP1CI0MG-G=Wcm*Z0RFJ5T#0pg.V$5qRB]AK0^dQ8_befadR
&itQe)ae05QpA[3ps.*]AY@:^Wk=JA7$Wgb;:B8@8oSZ!Yp43jiPR]AZUOCU\-%%iV_"DRjh87
5q?;<9rHrb<4#Fg/hdspe\47dI'kDiXjNX8oS!B>^??cgH,)AFrM_8mA'D>;W'Ch7Rh;[EcQ
2TkAP0j;YUMOi_r4F/u!0Wr7p^Hq;b))0%F^I5Y5lmAa7.^X3TsbkW'j\N_4PYrhr$2e@e4[
>ZI[D.Q?2E2l<%16>:eJIJYF@-AuQ(+("MUpp+hnTn94%]A;b0C[4Z[ig/^Y7gFO?@ij`EnB^
AWV,#Pp694o<(_:B6YMYD?;@`0V%QrH(C<F&!HWN^Qn;>25oAj.uF.(d:bUs8e#qY2YN<-Jc
m0?JM,8'R:-_,&s`1A<LMpIL#sPd$'(/u\='+2Wh\EpfNaYmN%.RBaTT\_bU\kug!7k`c#B0
?_WaHdZ<`%E<2RK1WK;"PiOpFHq-@gAU'Y(FEhu?S#4]A)j:LLh(3>fUP_U/>(,0[@a.86nla
g-Ab1/GF#fei&S>WlRTd+'5(@`4GL(_?W'=JBnjB$"XJ8pN;U'-;[Ps\u#ecEcEE49YgB=^Y
1:!(tmX68B[=`KTgJtnE;OON^1C\5s-g8[TrTsB@%?(uE'`Y)Pon;-FCQZD.g*@'g(X0SqeI
rf<ZC,q/O:QmpCF,rm+1e>(PQieE]AM;?@<cH%f=YafD^59BB%Sqp(N4eP*4a,@.>_lQXe^\@
?di0ZkWgjuZY$>o$\AmB0R\R>kj>G>S,&_!ZE8#.qRRG15faG8T@`>oZIb'A/dEDqm1&^o">
e&KK&r3:kXo.:G%gO''!52BXLK(7_c&a#bQ9'p2h>0:EP4hHj`$f^GNc;^1cIU%__HNm1bJ!
<Igk_A$(SAaBJEZ<[(D'ViRi!%;ZK9TL`%KL/B(Q?H-c1i*RDZa`\dCg8CY=7"kK,T"r+,a6
ikh[)cMs^&SCWtRFJMNDF4TU9H/$!)qKJgKq4.!!R;;B"r@At!*%Q^<(:r-.O>[%4?LM&<@F
_srOTiti#X4$K(TR%-^)2/48V4AY]A2%M\CueL<J%(`MXhI]A!<-GJgI]AF_5MNI81]A>Gg9LG;+
:FS;\!<PkCUs(<Z(W[=6cL$AtbWa0qE8pBBT2SR6:dSRd^DD*U)Ftd+k>8des_>q6iXHTTQS
Ijf0_]A/B@fa_/4K#I^e&hJZ;MqUSc&9TClA2$Y2-Uc[R6cXTE"3NnB[e2geqh;UFB@Ab:qkC
Z1!S;(KYtY$+Pt/J7A>YfqQlRJ.V0:BPl1XL@>hPKRq)Y(_*MosjI(L>PR9dbR"8soJkL<@'
UT_$A<"Z8tW$h`G3K#6Z9-hkR>A:*1\j_Pj</B#Wm4G@n@OYQ822iKNP]AV2T=\G*X\Sk@,DK
1Gb`*>>B#mUk'UdTRX/8=+f1;6!=r,K9rR"#OI@^BL>OmZr17\gNB_&l>f:lJ-\&?.`[)sLE
/8[C?N"<0K5=fT_]Ain%%M[FXjPrcjIRa56?%rK%R2m5N=#[,oSn(4KCd_.!6[$MVWs=Za9MG
$,CZ$en,e`Gc+gi#\UBdl^Bu>KpfWX9u;57u#PM:Yj:&K33+S:Tb/>")4q"a_s2IpG?YY>,H
X?rTV'/.9sg@WP6_j`?E-!qp*\##:h$ZFi>BuJN^Oh_Q=AaVCE5c`[#`BN-I0oJCe<g.n4)#
kS@sKg+Mfd(5.)PbBs5n/I<4K'RV#)qdg5#?g@QMdY")WkPag/3_!VZ>=:j\M[t"Qk]AflJ'I
c(;5DD78]A5n>UM$<i%SV>Tj&,V9\k&7Ac%==dQRQX!g2tm*i]AJrZNNMDnZVbPK=>rs_k`/+@
ll,qd5cU5NBX,fff-S-35b@X3KC!(K5oV*kc.>0QI/1B/G&KXS8J5BLX\>tG!m:4`=V&g]A5T
ne"POsf]Ad(fOb+)rYDW':)@G/=cKiSK\H^Lk?Smj@DW$[6as51E>gFRe1Chb2)tm9kUe(qRi
iNFORl;[_C:g,"=8.:$aufnP?f!2=Ab$H]ARG1;dcLU#ni0fmrc4ldTrJ,CIIJXGd1o;!7pJ1
Y+JVMGlgW#&MO.7K-Skf'GCVtK2'tB$F=GEpb#T\m=D-Vg[1AYS;eb3eIes0)00idf4DiE[o
tRDE$=m)-P/Q7]AuX>6(=PN[OgbmjrQ]A+:3+je+lBcXX;./)T]A"sOn+Yo9Q"P\.[6GEE?_g\J
tlel>rf,K=GQ)oqr2J"(3L%QW(Gj[-P/ul1@PmU4:Epm>P)9L1Uh&-CE:PFBLUpc]A+lLs08Q
9_?EmDG;;On$>^%rl-biYHDRXOMO`OBUqU:&_+$3eDl"D6B<nilITO8SEW#]AMrpeBr'DT6b4
Vs44ru$L-HgAlW\lN16Occ15'Vmi'3VRpeL\(]AR#"V\A$?14O]Ap'4bs[4*<5jW3Vk0$I8fA'
S8UK33i%r!Bh6fPV[]AEq@bScKj*/p5P*A>rV0Y\95NrjQ@uZ_QKW?2+<Qu_@Y^4ZN/8W?Or:
r*7(PetD'k'u15*V7H%D"fl3L]AHa!>rlKjJ@Eq58r#'<3LV62YU^k$tU*)``T%e\K!YgmsU"
M\e]A66iR[6AWt.XlePT@$HDV.#.-79MCb>Ktf6AX[W`/*0ba8F<@s^LOg`DqWZ.SoahNhD72
4@"a]AcrAXG`g"U^`\3,+'?a.]AkHPa*ko=5WY;+^a,^_T!>ZCdH$XrHH7bAYVs6nF[S\B.?4Y
2s:;e#V%i4Wj=23P@p]A'j6RZ633H2,A*\SH%O3i64C2U_KsJ469)JsT/p_2Ib+MlSLpe?sIS
rZtdPIf%20k2]A[_-^u<n(P$>@6qWSTRK`&ti0Aq4<(BGiFO28Y;%.'*56KS/2"U&,hKf`)J3
B"`r7q:5s+ec>PiY,ZNqO.^5nnYC'=.js2l)QL+2B+M%ea:&Ch,Yg`q\6!eX>">pu0n]A*^>l
uE_/.E<Le<sB1LSSN'#>lqk(p"!I\7ia`8+,!UNT&G\P"/lOiW+crLP4TE&F7Mb^n<\Gm9H4
TrVK?0r<3jWHRp8835:QA$0KD\7452j4eDNW:3$aLfYh%M&PbGeqRf9'q\tLq#0<=aoLdNQr
V/Mk67Dc?]A^s@Rt%1T>>cEj6GV+=Kc,N#!epW?f8klp0km^TJc,r3"KmW#S((RpAqG#i+`%.
G0Atpj<H>h6Z$Y)/>4>FJ&4[K=,Zk4'i2u<"!0qj5tLVt8R2HQi#7DQnMkMN/i[Pb=JAbqK)
k`Y>\tklr7K[Mi2M%iJ`:s(`>iiUM*4YY(:[8:bu@m&C_2anQbfuF2AKEiI(8X[CM?\_f`]Ak
n"1%<2i4qou,(5!:,m0m7BgQt-R=;CU3*Y[=jdSS!\/IU5lk=F!j$IMoC,l1K+;l+3#qh66N
ZVP0]A^hl+T;A"?9Rm0+Z9(k';\!?hgo&buR(ppH^@kn%QmZIgO[K':]AXHefQ2Z"olf5fc7E<
e6LK=1s@tdfY)Wf(;i\/Fc:J3sCMT9<VUuLY@!P_'.\EE+^R!Qh!i)/6Ws#HF!,=u]AYr6sbY
K-&gViA>BuZ'CQ>!*F/A^eJ"eg=,3#Q%6FMV9>Ppq&W@@2(st'q"]A/R-NFW^:Q?t3E3r+3S#
LK+AQ#?@+QUkASOG93R2f1+CA7^nAu[ML)>>^',sUGBrrC(LfJjYr'7Pcr+Q$Q-ann^4(i&P
b3GK?\*Yas8[[ud'Qd[0tYQ6q,>8.$9rE)!?A!n0?UiG(!UY:+5XW\MNdq/E?W8Qp4IKLgd!
bBR45Wg.;)R21efKi,f"5)<t_&3ZTi','[3E>.^-]Aku:#K>5tMcbRA,,ejJJ`SNl-s?7Pd^.
`9b>"^MQKa0+>R$M?\shHHjAg[(eiTOU%8+=,=]Ahp@D(@p:?C-<Q1%*#:/O."\*D8mN5QPUs
B,ZrF23D;Pjc.Si8Xm5GN==aQFn_=f0k)&/I68[Y_VZl/;Ssr4's)$U!cT2c1C2B#c4%0e".
k>"C"mAD*Z.+H/h*(?E?TnJ80;8]AqMm"T7q?-$CS1$*`@tkhZiuN#hm?h':fH38c@*94obL"
ZS7^u";^(^F]A`WP5BpJ2?Nhjs24fM?ZOU$(9%'/RR21Bel'-`gsbr$78=G.$Q%I.cgZkFJ0`
DH3k?q.I7DFUoc)-7UadOGtOn:qEq?sbI@-=ZsQ&E6==8pf-/51FS4.@C?b^q,0^T\a/^jZI
KPRbmB01.FCuo=nfqmPb>(LO:+5@p_>Xj_S=ZVd:.+_hl^.chm(^2QUd:V[;tU9cu:k&MuN$
aQbET/2JIE<1YTWAjg\dqnE=N7j6?2f9KeTkK.k>JR5c8U:-r7AR,XE$bQm_5'T]At?T=UQl>
9n:MNUl<^g[O_/^0QYFMmHTJ&$k]A5iVqiVq/[XSp1f\4j@>baT:_rm3)39FQ9/YE-;/QO(K\
VI/s7KMF=C,IGuJj`;CG&:p`^3#I)oTHK-1s!Q.uR0.H:`hk!,8ffsrj"hgc#r*aP]Abmb4YI
8<K$EUYDNnbpj>E3'-FeN`HCV=S$1M"`sGFTZ!dl,Q!:\S)0UfQ;#*Y0k(]A[_[TcZo/Pfj0C
qf"b1oiM@,YD/MO3)*4.@W55(uVQe7KpWhCl[lT#Hj/VX/LF$/,@qGB%!KH9<>2i^!>*hfa,
SGQKE'b33jnp59JD-*bMfq\Ve-fRp]AbeY2qDR'16*/o_,E5q5Cp&QdV$)k7hg1;;T`^OGFJ0
6=:.ldJs!k9CCMJc/--afbWP\7;s^?e:!0tU1^Y=D3&rrNEOpXGF>fE_"NSp]A!?kWh8@7]Ant
#Uu<11=`_e%#*'NsI#12r$^j84W4O5J3&H%Lr/4$[WT$Gaphu1a'jV&5QY+JHO*?Ltd-4E="
)sH5<\qZW"u*WACs+\c9$I_;kq\@W$9s`Lih_cg[3!S"UgJ:qY;r3R[/rnrs2ENt69&\Fpu1
n=fgHI5-JCK'0UU>W\,^TT^RC?;]AKo/bK*><0<JMKMV!bn%'c01>kHJV:;83_K3UFS!"b6;1
PH%4VDY_K0>RbI4ISk_[q,JXr&,GtnlLfY++Dog3^A~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="864" height="243"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.custom.VanChartCustomPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
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
<ConditionAttr name=""/>
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
<FRFont name="微软雅黑" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
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
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
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
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<VanChartCustomPlotAttr customStyle="column_line"/>
<CustomPlotList>
<VanChartPlot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="exponential" prePeriod="0" afterPeriod="0"/>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
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
<VanChartRectanglePlotAttr vanChartPlotType="custom" isDefaultIntervalBackground="true"/>
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
<newLineColor lineColor="-5197648"/>
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
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
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
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<ConditionAttrList>
<List index="0">
<ConditionAttr name="堆积和坐标轴1">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="0" stacked="false" percentStacked="false" stackID="堆积和坐标轴1"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition"/>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="true" columnWidth="40" filledWithImage="false" isBar="false"/>
</VanChartPlot>
<VanChartPlot class="com.fr.plugin.chart.line.VanChartLinePlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="exponential" prePeriod="0" afterPeriod="0"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrLine">
<VanAttrLine>
<Attr lineWidth="2" lineStyle="0" nullValueBreak="true"/>
</VanAttrLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="NullMarker" radius="4.5" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
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
<VanChartRectanglePlotAttr vanChartPlotType="custom" isDefaultIntervalBackground="true"/>
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
<newLineColor lineColor="-5197648"/>
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
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
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
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<ConditionAttrList>
<List index="0">
<ConditionAttr name="堆积和坐标轴1">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="1" stacked="false" percentStacked="false" stackID="堆积和坐标轴1"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition"/>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
</VanChartPlot>
</CustomPlotList>
</Plot>
<ChartDefinition>
<CustomDefinition>
<DefinitionMapList>
<DefinitionMap key="column">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="產品名稱"/>
<ChartSummaryColumn name="庫存量" function="com.fr.data.util.function.NoneFunction" customName="庫存量"/>
</MoreNameCDDefinition>
</DefinitionMap>
<DefinitionMap key="line">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="產品名稱"/>
<ChartSummaryColumn name="成本價" function="com.fr.data.util.function.NoneFunction" customName="成本價"/>
<ChartSummaryColumn name="單價" function="com.fr.data.util.function.NoneFunction" customName="單價"/>
</MoreNameCDDefinition>
</DefinitionMap>
</DefinitionMapList>
</CustomDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
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
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
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
<BoundsAttr x="0" y="0" width="863" height="242"/>
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
<Chart name="默认" chartClass="com.fr.chart.chartattr.Chart">
<Chart class="com.fr.chart.chartattr.Chart">
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
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.CustomPlot">
<CategoryPlot>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="-1" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${SERIES}${BR}${CATEGORY}${BR}${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name=""/>
<ctattr renderer="1"/>
</CustomAttr>
</DefaultAttr>
</ConditionCollection>
<Legend>
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
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Legend>
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
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<RectanglePlotAttr interactiveAxisTooltip="false"/>
<xAxis>
<CategoryAxis class="com.fr.chart.chartattr.CategoryAxis">
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</CategoryAxis>
</xAxis>
<yAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Century Gothic" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</yAxis>
<secondAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Century Gothic" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</secondAxis>
<CateAttr isStacked="false"/>
<CustomTypeConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBarSeries">
<AttrBarSeries>
<Attr seriesOverlapPercent="-0.25" categoryIntervalPercent="1.0" axisPosition="LEFT"/>
</AttrBarSeries>
</Attr>
</AttrList>
</ConditionAttr>
<ctattr renderer="1"/>
</CustomAttr>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<CustomAttr>
<ConditionAttr name="系列设置1">
<AttrList>
<Attr class="com.fr.chart.base.AttrLineSeries">
<AttrLineSeries>
<Attr isCurve="false" isNullValueBreak="true" lineStyle="5" markerType="NullMarker" axisPosition="RIGHT"/>
</AttrLineSeries>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="1">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="1">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[3]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
</ConditionAttr>
<ctattr renderer="2"/>
</CustomAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</CustomTypeConditionCollection>
</CategoryPlot>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="产品名称"/>
<ChartSummaryColumn name="库存量" function="com.fr.data.util.function.NoneFunction" customName="库存量"/>
<ChartSummaryColumn name="成本价" function="com.fr.data.util.function.NoneFunction" customName="成本价"/>
<ChartSummaryColumn name="单价" function="com.fr.data.util.function.NoneFunction" customName="单价"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="243" width="864" height="242"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="864" height="485"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="08031946-e406-4bcc-a65a-b3d2da9cdb5d"/>
</TemplateIdAttMark>
</Form>
