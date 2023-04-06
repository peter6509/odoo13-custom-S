<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM MAPDemo5]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="PDp"/>
<O>
<![CDATA[店鋪一]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM MAPDemo5 where dianpu ='${PDp}']]></Query>
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
<![CDATA[SELECT dianpu,index8 as a,index21 FROM MAPDemo5]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<ReportFitAttr fitStateInPC="2" fitFont="false"/>
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
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="Al Bayan" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="5"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'店鋪資訊\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
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
<![CDATA[1584000,1008000,1008000,1008000,1008000,1008000,1008000,1008000,1008000,1008000,1008000,1008000,392762,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[392762,3600000,3600000,3600000,3600000,14744700,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" cs="4" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="dianpu"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="0" rs="13" s="1">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="pic"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[toimage($$$)]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[鋪位編號：]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index9"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="4">
<O>
<![CDATA[業態：]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index4"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" cs="2" s="5">
<O>
<![CDATA[合同狀態]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="2" cs="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index5"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="3" cs="2" s="6">
<O>
<![CDATA[商戶名稱/聯絡方式]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="3" cs="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index2"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="4" cs="2" s="5">
<O>
<![CDATA[是否主力店]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="4" cs="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index3"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="5" cs="2" s="6">
<O>
<![CDATA[合同編碼]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="5" cs="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index1"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="6" cs="2" s="5">
<O>
<![CDATA[合同生效日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="6" cs="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index6"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="7" cs="2" s="6">
<O>
<![CDATA[合同結束日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="7" cs="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index7"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="8" cs="2" s="5">
<O>
<![CDATA[簽約面積㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="8" cs="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index8"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="9" cs="2" s="6">
<O>
<![CDATA[免租期(天)]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="9" cs="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index10"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="10" cs="2" s="5">
<O>
<![CDATA[合同到期預警（天）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="10" cs="2" s="5">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=DATESUBDATE(todate(E7, "yyyy-MM-dd"), todate(C7, "yyyy-MM-dd"), "d")]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="11" cs="2" s="6">
<O>
<![CDATA[租金單價（元/㎡/天）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="11" cs="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index12"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="12" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="12" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="12" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="12" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="12" s="7">
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="112" foreground="-10642722"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="4">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="4" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style horizontal_alignment="4" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border>
<Left style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10726059"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10726059"/>
<Background name="ColorBackground" color="-1838849"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(?t5'4'*?lsg2uE$tc[O\ppjJd=mpO-6FU!C8uM;?RqlhB<XkTa3,?LBrL[Uai'.,uPG5TL
]AA#.2&F%e-$%K:9ZiLID9jKFe-#>q#2TrZhIdQm<,UZh.n@S`9?tsSfKq/eu[Q)G62BfB$GX
@c'l'1>T5]A<Ufsa;rWpftK,lrmO?-P1<[N7G.NQ]Am6bZk&\D/8:J#7CF,'m3Rkm$4fnJe_N)
`M]AjVNPpp;+F]AQ#F0AK@YPus5p+fnaHc!=Zu:HGr>Y1fJp)ND-ZS1\:/Wck5gH[^Qi&`mE44
HO(9fX^l9Q]ACcaqQkk]ATO_JP5%;^@'A0Z/Hpe"+8+/Q#WK6mo@!IE9o5'.F@VH8*YgjW"A'Q
7l0lGNsE7qTi=FL$liV(m9cl4dL4ejYe9BH#kj9cb]ANhoksEkh@9L]ACoW/";s'hLLR=uhqXl
gttM'.o.l66pd,7&Vf.@-J@EGa\(rF?mkZKk7sA"Qn"E%;,tCS8=*^Kc*u*A;ms;ikQ@IoCY
]A^pQ!L3rV>#0SGN)]AbcW!(#(LoeZk4=fg@l?9Q>eRJg^>"TXWhT]AFMY>SoRUr5F5Z).n&'`q
2(#9jg4okQlQ^k?h:Z`Kr0qp]Ao(iOLD>`JG-,n`0$lg3dLROZ.^;.fa>M#0'd&Om/%$tf'Pt
PIg7Ha^O@sr:>A$[l%iDs)io1,d(((*&2kDlb?_a7^8GC+6Cb2D=Ju997;s6;Flitb`1N//i
?OQA]A(<De"g1;:Sa*9+,@S9jiNE,n)j/m:5-tHg?S!HM3e"4nr0#DI_X[E<s\(6#9>3='2oU
f;%i=VsI/"6s1:<Q:=G$)P/gt_29gM-epSl8QPBBk*EC[V1T^rC:K^U&+NbU7iWrL&cUH3/#
\8'H&U`KkjW(XJQ8W'jbjGF)%$4M>'3[HRCP@c+'W22<'s5"]A,b%V2[OH9[!g^hrDc?\<olk
PudY$3CgKmWhf\gjka]AB12-<ChH)/]Ab/M,mKr^ns6#YaB\N[O;cXo:U'D*q+Dp<7e.9W0ZGf
%sQ/)s*AbT8iZAXl=*]ALjhZ01#Y;&(/"EDK2IldCL^4,!%f\%k[uk-R^4\3@AW/8Is:)I4ua
OSR,2l+!nA%c\iKR%XA<UTljgT\[Ie5^N&%dD*hC]AK5X5C&%`;L*+Gf^NkE#UP#2%'"53W[8
pHEQJi;-#,hb"b8lk1_J@^BI'pU^!<hKn`g$BLVt[;74?iQ:2/@$FVsDGn+VUmO`iNb,/o^"
`o*2nN'Que.jIQIc,]A>mRfkq:H[K3gg>I3H*jtq$Fl5I5X9GVF]A^'J'+*!37gAN=/\@sLYH5
Lu@R`l$D$Y6Q)u9juHBmpR5PBA3OFTYRsNf#Y%KF+3R4Kl-Y_^'ZRc(B<)Gk<_=@\6uNloXf
Y7'39Uc/o?(eHHhnZ$UEA(1Y+1=bmngWP:1D?gMu:XZ_i=I&4!!d!#Z89=]A2;Agrg"MT0O(B
/eE\khbq543?RLl)64:)q@gAn7LK8Z7U\CX4WEm?s3Pg[26;\s?ml-*fk!YZ?6g`ZjaeoaLb
R<3[$CS,F8O3!V^HnRNHK8a/4n>4f6Uq#GGAM&PYS?5#$t&<Quhr.6fdk'PRR$tLP'@C5Sd=
:M,=1hr;E#=Om&IGI;)F.S$*_lkI:hBjk&,;LJG>4S1:[aoD)9>$T`T*'^P2k[fL]AhU\1T6^
2ElJEch&@[Z]AoOpF>.sqVce+4kc]A"DUp(B2PhpD\mi-[BZ3!u;<L[Y(OtLAL,FOqQrRMG'07
Qg+M\YUq"R;;lkGU%%TD%4Hq*>snn43U5.eC@^SK>_.u/=<EiI/T3Ga%gP5A!P<[0Uu6p!a+
/F3`;r/-`kVK*AkKI=@%OXLJ)K1bjc%qCpK(KE@r7aBaO_W^hZDiuK-Y`*F1fB-H?^AN)@He
\#-2ON_kMF(Bu5=AkL/($c`WN>:62Da0HX_mc$nuk_?\dm=tjF`BpqN:6'G\8o^:-&XSlGuA
eKC2=BR2'W"MFt&GcGE2-e?ZTlM0#$GZ,'b^b<]A"8me=sa(=:h6F^m"200k`IIkoe]AKB9`<Y
EqNF;nZL-Tr72<1!!ZAMda?&VCN=&BJa!%Mf8ddCA<<8M.bfB(RKY.W^#5_"+>=05nEb8Jae
c_#7=N+"B^7=@&E=j4#jJQb?A._FN(er5/0WBPJ(XSG;g\>S\tkgj!fO3%o.Kbs34<?'fe)F
0'/,ngT)Wr6K9Q#d2X=&H:l$oB%Z"n6D-mh^<2/IC2U5%I6=<B9-dR_cZc;cqdc:PI?93N01
Z_8S&^<=#]A5FI8)Lm)Zt8a29`^\uF(4[.'2\PE-oC>%/9jqQkN-r[K"^Ab2N7>OM_hkc'=N:
&bBj>u@SmJh19V2!9KLjCEONNI>)kKaql-jWD.s)I*W!`B69:l_cf5a;/ga*Wlh[%;/6H[Se
o*TP7?68;IB*gK+Z%FQ9ra%milkh,*+U.9n%;t=<oO4(bLX?gI^Y'+'qffa%JXH.`5uSl^cX
.EJ0ZG;-N$""TSWPD["4L#]APYucPR:L8onGVhqI7Qs(+V,bHo)JL=P;HZ2!IUZ^SL8e-J7tu
l<jMCfqJt,%q3ZBcjMVr6S$rWEgBF>)Dmj@H0FZoS=n%O7SqC#JKa9&W-`X:I5PVkkYrqb$h
C;n@(XpQGGMB>#FTP]AoHF',(bChcX#IP2214WiIsCHtL!;%X!7/&fq]A?">F@o88CJm*a/5^0
=^roAU^U[L]Ae?\Yh?J#/6/7^m@hQI`sZ#0r_YYgMNs"%.JVo6@MWe^;tKIg):4Rj.PG@MSDG
&C6??%(3Sl@t@!"7ub;V?Le4(;gh_0'<)2J%r1t:0DbjfKqiDM>%\4n'<S'-N37;nE=4U_[-
\u=W`JIR3P2.CqZHN6mUBL=mWpUri]AJ]AYNPO_*0-6(m9Km)dr3]AQp]An1&X?=I6^qN/5cV>hn
FH7PZ[n>sbSF)Mi%42+_Zf\Zs$Mn")D.+KRTMq4qa[).>agkHP"Tl9r^/-i06J0o>2B>7pVg
Jc9:>/3KgJu=r8mr>]A[XB#`8+,G*+pO0O(6'DMm>R8(H.?L-^eFRpV`5Cbq["`XL;mm:F*.>
AFN-7FcMgpH<+OP3M$H.2$oLB6nq+@H&2!Wd'B=^1_eH*[(8^Fc5i@XA>Mb0*AU5uWN\-kn[
?M*i*j(><Lm@PN8SW1.+]AE\EU>.q]A!C?<[nZ[8K6fl4X(J.M"@<Fsrq]Ab`CDrQt!5(3<"7+R
*rRJn&e=Oo9BCB/T+IaU!a.\SYZ4HR9-HkN`Q3'23aE@e7uE,,>m1DcED!d\VBEj[gf1;l$O
*6OKJO.CCW[E7Jfn8g.1.oiLlMQ]AT<:Y>mREMW\'6L8FniSeh'KDni-53asY;^mZVMnXY"GL
5oGU$t)0[U!ecV[+TY*LUJF883khr-=L$pOP]A<%f2nGh&pD(AR!eJU=%hEEQmM`9RQQ<I;gd
uNZE"ZJkEl$;FnfZ5\i>]AJ(L@VEnd95+SN+bQ/*3^WK&!Mo3kk1O/mQ'(:W/!e9k$+c/*UmK
Z`oO+Mgau1O;X"Hs#]A69Q\%mc[uU/_`iHs5n)-3od_?AhQ"CCP%.bmhF=6lmZ<Y+_7%?g`sU
4!aDRa`IW:3]A0LKh9kUc6k15/P)`*Vt6:?(t*(!*kpW3gA(0Xd2#2I*DfKA8X?$73Fm_dbX!
et0$5ODg5&90&uL2ba/P+nVX*_k1oS6sl7VLe8XaL9s[[`2*VNf$[*:d$o"+.K*mDN["NMO*
-^?BuV`SJd%i%`sqO$3o*W4pu?O.gN9)'00s_5jl>oQc.l-#&8Ps("iWYE=#utYakT%'Z&It
2DD.ldZY\HETeaj>FLr.!lKuqFg?q#hhP+`D"ES2N,tsnQX"LsDFDV@0=j44a,Fq;BLUt>>#
D22.g,5C2_hr+pLeg^%F2MsLf$>He,6XAOTV[>Ck3$/:acDo8d8Q1:VMcZ_g`)[5>LWtHR@s
bL'Bk4pp18ud%Q*XFi*01EO9:L-%(0(TG`_"q^S!<HcR#n0?"4T;7B7Q[O3K^Cluun0m`*76
kr<dq"'^s*krQ.`^TGVEk364BI@k-55T8(Mg70)_<M*+n7HT2*)Y:B)_=87t`]AjVCN#jA,YW
BA1'$US_2]A.BPDTDIsTOt)n[0HPX7I-jcK=YLF(IK'd-C<:N(>]AfRF():aBhrKIs1*1@Jeu0
u:"Z;;3QBk]A.8;$B=#k=p'&,sDm#CB?gp.o$"2Kn3dKG-_<1-?`ILF\_?*,cON),,P,t`LPm
90@012"_m1N9!Te%abco_j@6<H2`2lhjMq@+`K/XQb$hYm]ATHCDG_;G*(*]AL2V5PH1P)`:Ti
SN0,r"oNt:-?fXF;c6.51@HHQ3@bC4*ZT3)-]Ac]AN''3]AQKtZhcHh%)(#LjUI-^YD=>Z]AMp.e
Ln`8tiW#E53uh;:!&H./^MY;,I9LSab9hq7"onsC5L,6c7ZahnY3t)Pd&E6NMNsH!O4%#Hda
PDH@X@BX6@5>@dBM*IflY_);G9Po#+Id>!;6[L]Ab[R9o+EA.P`g37&(S'u?+BsK7h/E9&Z%n
g'tFI2djg5Q(dY,eS^C,oOm>kaG/&:5FlBHD/Jr#VGH!b7VKMO'&S`T:]A[-hB02u7?pSrLGI
:K^G#=QBofWMS4mG*rC@$3CoSsK$MqjdFf!LtGc0mM9H+W_8o.-]A4K`j6_1\+unU#5.cCAF9
c;=-K?0o8[kpO2ns4n6faHk\Y.4rPn1J*^u0n;FSqF.8!M)ff;/`I3M:(467=nB7=N9+]A5Ns
@.KYoC&ASR>Pt7nf=oPb#>cBT=[Y!3I+<Q4d)pQ2&c7B&WOM!)AB\#)4t<]A:JE'F1DLiLH3<
ghrR`H"@8<67QQs?'kLIiH9.Ds7HL_"&Um/hV1J2fW,:JjB8fh\"/U`7NGSo'11.7+:3a)@N
$C`oka(LP[s/S_Cr=*j^CB:c]A=&)DQ2;\3V7.nbbh5%*Y)Ym+3BhpGJ=*^gK.Z]A'i-Fd1QTr
47h"pj.dKP5fj(I3F65E8,`^$c;,KqIr]Apm-=)'2*s7]ASn:cMbg3QUY_%:?@G=6@N?IV&ahU
BYJc=qk)@X?g^u,HE.lmG%)X3TFW/e('Rg&/q@S"e*,U`FnMseP+Bat1:,>EL#eY%&7j7dQm
?XNe)Rbmig5CYeT(`^[0.AGs5EuY(q=HA*eb>gjpPG=`TqTPqeQq`1[JU=kT2uiN5anKnbif
X.n_E9l5P'>]Aedd*ShkakSa5nMbqld0]AC%P08BNp-\coO"c'XWATfYj'"'#TB2cQ89g+Q.`C
YS8(qQ(3ce44&IJF^T?'+3f`II5"hZ2hIe6_VA'dA+VgkFoY.FcLVIbgm.fAoQLF(),p*%0o
Pq7,,llk.<]A!V]A?Pt@F4j@t`\Y.+/nWTR^Eeng8hB>B^.m18@8>pM)V)P@Pb6kfD-Aj+'g'd
lTOdn+XG:Di4!$%$/Hem/\ib5ks3UZEpK4lfi/-lZuF\ZQ[Q4P)HAYbgZ]AFiaOh$_!2<%/A4
;t2iJ8L!!R;jMMa4;'5rR(N>\.mJ:d_rpm"9]A698WKhhE:R4d!Ti)A*5(?iC$X:%OD"U^RBq
_3\GL;8]AYtL>L!2#f05Lo?E4Q'ORRL7Eqj`Y8,5FnkE]A6R#.AsT"E*P4l>oIe<O./tVI6fU#
)@%g'XqdRk!an<PY\(a>6R5:<.3$P^a9W?Xj4ZUC#"?+SIc(e7:.-*\t;MV[I%P=N<U0=t/-
Q3+nC7THg#Y-`+$"=O=a95X3r"B%7,"$IiKhO>T>8/Anf/a+$P*iPVE83#u&bOb]A./GK?;"V
f4<-%s7Dffe;W2<h7q%Sq<7R-Ybh>KU'amBWDa4I#s6g'g=$Q9>nP4b.[6h9qi+j5'Jl_;Cg
k&g@M4fUp$XG(=RnLRR&R&M?<cet9R:8Rc2cA]Am>hI<n[.D2hEOhKesGNX*oNo;d#^RD:U7r
eo+=,=C22UjqnO4jb$<*pi[ANkI]A$%4093-\Er;%]AQ\\L[X3-Bq.=cb@bQDtG?>gZ>ejJ9K=
nQV8*1[suk@>doM5/M?qdM((9AjD))S8uD3-591]AoO[I,0CfTJ1mC%4caI"K5"b`_NbIUBf1
%i*2!6(g.N@XJiYM[166AranFZ`,5G1NEn7O$6XjM2AB(gGp9O?@IIT.mp]A50$JujEcA%X+p
0neJAu_$d3h-SlZ2b_&&>iBEb1d<Vr0.B!t1J4#.+.N@TJ2L@gU5b;AW%#;)RWCBC?-/"U$k
>I_aH>O0Ya]APk<<b@!u"A1_e1$G)CDMp]ApZ[$W>d,S)q#5bfh\32(5A)%s16lZ&%7IC[(]A\(
(TsQW?=!i!-PuEaGNd4C_<]AL3MCA58rH;Z:K$&FK-hn+4oAa6JiG\/"kmrTUOb]A!781H=boa
hM_Kbh!P5=,+LEd\s7.tc%W-L'*`'23af=h/hO;J>gR;-K\UMc\\44=`=pSMN5(Qt.;11It=
`YF"^-9DG\uJ!PGu&]ALM^i7:&9CPX.5g2J0N0Z,*51C!i:<eKJ$s7>H>Q0%/I'd3i9eU$ebA
NM.O*F36.0WD%.sqMrS[#c3Zl)VoJOZ!Nb0^>T[dT/+2ms0H7'$t)ulb$V^)u0=d#EI3YhQ5
nF=u8kMBnN!H`bPnC%rgH_(i^dCD&?iMVNB_X:%&h![V(Nu]A,jq&LotYfB>pGA-^MlitceKl
e8,W_L6^Z)\B#95A2=Yl?s1fm^HGHMln<CVWj@jl)7ghml=+dEJ8cYI5)&M/$,T0V<iX4K.b
V9/0JlnlM2:/2l5pm0OL:975\jH(WT>>^Qqh%.dtRi25(0]A+N5qESE:8*KFT"jj)K7eU4aJ9
CZZAEFH2K%da&X&$>NB7=?nLP7*<IK2^:!\'\U'!O.o\KC&t[frH.,'\=#s<,mPY[[ejFGMT
LqP(/(>fu\CP2m"uICaGj>\^]A"tZ2&O=MXO\Mb,)L%#;9QK[Y?8[Bg7*;^2R?gWBJm<l_;<l
9\;n+RM5r1Bq'p;iiT<cM0/#V=acj,]A0QRZ2HDc%GACS^af0`WR\aNUn!]Aq*[;VSGK6GN\=2
2,.V!rJT4MK]AUVlhrEkql\?Yk0IT:je#foaJb\Q9Xt6*D7G9S8sdVZHXI.*TN`_#;^3amkS1
?V/KR/0@P<J/uI#;cfaM=P^E]AV#'fRl.NuX"U_NQ8f%MnrqfSj'n;rN2HWS<44ibP'it=iKp
:!\tKLRU$W;EbuOQ]AlY*PFDbW(LRL=Upso$Tcb>FSqI3liY<(YChj[eH`M,I]ARb@VZY]A(WA)
Ad!R0)1SpSX:$POW8RPk'Bj@OP``R*Q,B^seM*PnFH(Mc5W?L*M32eaa#&H84nP$T)6Y:"S&
74O9Y[1JpFhAZ-9TC`2M+8UPgIC@!t^u@&l#rbp_r30?lcqVr%(!Tu\-/GsSMM`3[#F3LR=X
gKQ1C)l8!:)jD?p5,jU0cb6R$KaKbK50W=9pamkN'Epg_AikAOZR5d%O`g4R"oLO3Z%`1V,A
[3cqf/>C!\h5Y-+X_^8lu"c"*igfJmiY!-R#K@:N)aWcn/58_WqToNng^Q%+:=n-t-!OnPsE
6N))Bj,S4A4R*]Ag:j#61PFb?QYR_S9UidOmiRs,U=RM\6nth+e3CWG#Mn]AFZlOZ09G?;^O`'
1h50I%cZ"1YKY"G@=[7="D\O7)<X5tG'>.R-e*(\L@gL:!OXrL6:6$jJ`$Ud3[THLE^9;c30
Mja4"`A/@^q:n<4()/[&;YAaidAdO:(0s)JdUfdeCYRS8Bsh/Of;"Mlj(a26r)+u)6l1V@6s
kI\b,mmI#\=ba!%BsQf/ciCe2_,[chKpbhT<ic..Rj!#l;i\Bupp7=nhjebD\ZrhF-$$:+nf
NnMoNe,BOAe/S@MR@;=A1'W2^VeYO^jejVc\ngpB&QNkES\k59A.!`&>Z7s/Zffn,-3k\&Bn
8,O!(j,GPH)COuE^*!6AY[ZC+Xjn'VJpolkE_IZ&h2V<eQoLC=`+&=O/c#i7(No[dD5npo83
epH5Gth3!>#qk&]Al(]AY+RgHC&.T"s^4(6Iot=QO/LT''4PQL[1bpLJ7td-8ha`?ar0M"9_$@
Q.H%%Qg?pC6,&8Nf0CUMnlZ9nk)j`G%."=.rKn22;(VMWkm932Z9l/O-Asp5)mSVhi@hfJmn
Jd6?odR_HC[]ASUuCYS!W`2?6.D`"OZDlDjHD%@RmH=W*M4]AQC^pD!)ljS-Zf?XB:.?"n\79.
kdEE9OrD-DiEDMQD7BV_:#sl&TA[XetH)&M+\L_.7ipM&SL'Vo*c4kYJ`;*3KQuL52OdYX1H
Z<['"q'0\+HIkgP=qqCC\aNQZ_M6$`:M>"(&)#sWQa-2E.o4@!S-PP.XCoo0bJJhm#a_hjnH
f0d<P?@`16LCO-n6dRF\?cT_g,ES\[]A=@X0#BkZ$e(LTa&_[`U*+bPtH\&I-Hq&O<t.Q<"4M
ku;+0"-QgrK$Qg!X;s%SND?&RLVo"WB.d[;3EPS1MN@0p?8siY4ZK\/JH+#lS@AZ$:JG<RS6
$]A<r1o.]A+]AHG_GH5'_+gm(L[&;0N%R$,(VFYlI3U%Qf]A6-XQqAaBDi-`)*FOaS&MRR_HfCP@
Ukr]A,Cjdt(h$5U7&Sgt&(D`bEfrJpc_T4lT/Qhdi"i<KC"3:diqB=FGrO)&W12jfSFUFYD*,
t$iYI>oS,7I.Q'0/#rnCGlW<oYQ(%+3jp*KAM_t$f#AZA;L5;.RnGq`UKjSkFYh,hpSbe,6+
'tn%Y^Qalp%se?jT\;*F=_9P7I_P%)!`)2O<IAK%BpLeJ2'jYpQb>KC6(hK20+jek1i91?>U
C7c[UDsU/s*j7.b2t\9-c`96YBW/ANKWhCH@]AN]AX7K'a#oZ_U]A%``ms[aXR_r+9;N8UQ&^2e
JJZ`'3m^g:47JN5FFR%[CSRa#8F>WSkXVa2W$j^cNlDJ0:U+V.ZfM<o:,D=g,F_IrBrn&3CS
l0i3,E!%#^3p*kR30N%\(+2/p7&_hP2M;hlAHNtNoEi[j(YjYG/8.I_G"4eY\5G!tC>*>K'6
E@)1>JS1%cr4(DXXdf8akFVM1FH`KXuB"jnH]A*VLE_W?O.S$OiNsOuW!4!G+oS/TNdO4(j@g
T9[]A_A/C'uNrL\_F]AJTeq46)<S^D5;eJm^K?MRJui(.<).^VA'M]A`;,oQ[JQmcMC$MFOcA#e
of?QOo*f]A=$!)Rcd!=Hre%QGs-8E;+Ou8NLHAq$;(Y.u%E5dY6k_t"#Dh91U;>l9G4M_@2d/
%?*fM'IpO?Y@AEMq&rHc:N0,_l4ND9S8([K?2(OCotpqiR]A`m'Fqi>gNcp'A;NW!G*U;%1Yh
;rh*o3*.#&228`=\Gdet3rVk.[HqYI<:,T$0nW]A/;\X[Jpg,8'6L(D[gD*PP'AtSAml0*%Vk
G/u9^_Z&G)=nZmBiRTe9=Z;fa*NQASUN*dK6I75VHPh%8s@X;l^_QO>tBpAGAc_83H2Xama>
99FpOR`m;6rmd$\CG<fJ8=,!-<]AOfne7l1GK+^%9p)X^_ke<ak[_-dH+DjgHmM2b^8LESJ6k
6*l')5t='[M_34kU4<<Qc5F-mBnqV*6D*;)[Q(S5nt[E-s-j>K!2i$Pp4)0($[ViEr:0H!]AK
05)&6g[gXFk>X[#[57=E"VUk:AL<fJ[>":[&cTh?%i`:HS"#ncsL&Wpk,q5@J0*h[[ID7*,'
J:r6N`Z+jk#R!(Jdm5SGN,-J\HYH7e.MG=S96-inu>qEGjdj-\_jk^rbo!UHAN[p8B-R\0q`
uhC@R(M\>(o`(?"ar98^pG[2aS_5&3n%&1RcpK@A_XuKTsAY>$M$pMot@RANgK^=TI?cSGb1
5LR7N0&[mT_pfKl`r3WfhTqRdRtB3G6Mqnri21KkGqq]AFYj/_*`Y5)YJ[Ju(4B2uFIn`W!%n
GFb5jS/>'#kR]A?<E0&)1ac9@+'r_j)9S2ULWj;F3M+/ViUpfak6,PZ:?<#C'T?r'D:@/4%K'
`AOCsAr-I1sQ=7>gKLWt=?]AqhhYnP<8a/E[>\@k-iXZI.tLpr'nfK'Jj.tg\Lgp3N0go1ear
.QUB,SQ4!4]A>l,I[!FG_F.d7Dhc-_^J<LcnLMWJn?f94c&6^<@t]Ad2/?H]A_dW?E(+Lf3nB#^
L<!.]AA%*6M6,&njGf!X^N.lA4sO!4JRsS0W+$W*#BGrX4>(UFe@lH52)N`(;DkV)12lLX9.d
Ej0=mY\2:EompY-e5P*n0tp8NGBV`YbRKdef!*&-qMG-S?&0/."5M[uhfIk`";_-oqP:!Xp#
U'$"iK%#?ErOhCD2.*jF[3N]AOV,3,)]A!R%H4N-&.Vc-?!PkB3'Kh3l$H`P.$"&">+6>V49i4
9\q(mVtZLHc<6"+pCrpO_sl0JCkk6-l>>E6.#%L\T-6M"*r0HiQJN/Wo7b_Vc2ZJsht7^r]AC
FpC(utD1RDD]AXa;k1SIf^lQ@%NE&nf@.YO?)rNOG4L-j-&fN3,rPFm$SeI-Vi+e#&:g32dbl
c>9cZ1XVubsY$Tqj%$G"^bgO&Xu"\9LbapoTs/"(g4YKrP+[!N=LBu6[sggm,*Ts%q0fCUO4
B9O8P_X_:PGe!YkB[6'1pL@:3hP!a81\YH&uF\sUCZ/10[D$ea(=qJE8`okSiIIsp%Yg?Zo6
8G;Dm[YV)k<<%of<LtE`50-.>*r-%B<E'+l]ABQJO1l!!,H[W@&7>@'47ouVIa`H5a7VSLQ@p
oAfGfAV'Pdu*KME+MXco+RH<LTTp5!8\o*k"L8j8/AjicE?Mp97l-a+\#iCrYI0>:dOI[el4
"Kf5+RmmCE3H9'O0?U8nk>kQ"ZEW7F)Hil2-9oh2s?-bh!]A4_^Rhb\72F@]AJKpdlW:iNi1E8
2QN7U#)o_P$3,1771_3;T=@^)%dJ(kIB9sBZ7FcFd9Vtp`(Hm9/H;.l5"@`[F)a;?!aQGh..
4l.0NI3b)'!d)L[gH-OXL^gc>0Q`\4#,@<q-1dDqCPdc6^D<H<+KV5R[qII`'d*)T8-5OOB!
YKSi'jP>B0,7b7oF^uQW0nil'9PnkgF+,fa3F)D]AGO3,p<.l9EEN``ca<C\F^8^i;3]Af<j-E
f<!DTd=5*c?\'*r-M5r@@=:3,C3X8mU`=CG%S_19WFN<SC"8E>9a<dT0q'E91/]Ad:rK8i?Nh
N4Vo]AubMi(.%h3>kGOLm7F5-7OdVW>fB>]A3/9WgR0U1GV(/-$cK:B.&4NrCYO]A(B#<g;He,>
&M<?IR\ESplN/XG,bc(gRRWfBJ=mgWTf&N-(`13TO#0L]Au4e9QBqu7.B*46R)8'Ed/pJ24fF
.(@jN8hQZpb1O%pVkMq%d+I.(8Z1naNjlalggkqrE&`6&A6SuITUGV/,GQfgE'N*<[@@L[$c
QrFn\.LGKPNsb&AZ6S#%Sf"mFP@be<)l2]A-'00_KC"WB[X0]A2K@DV[8UBeI)qh]AaDA.CkB_"
$de!F0%Mob#`;ZntpMDolT>B_AVbj5cI[lV9Y)BC!hk.$HVc^s,%,7',$OSd8FRl`A*?fN`*
XdDRWO*g^-"-2"i=M4F>Of&WHU?CW/mor"e!TF/-E)[;c5?$9ItO3G&)o@IEc*`$H"2o]Ajm'
mD*4c>i=Ad6t^dP*?b@s44n\#K]AfhK]AB$Wk50/?cp<:ZkfR1)!Gc;)h1=q1Yp#[(m&,$Oe(H
/?:(?<Yc$]A.0)?iX4f;7D;i]A,Q(Ea*e7VGV("[h9UcXuJ4L9.]Ata_@6o+2f/$h1s2A+bSRlZ
SQ%YYjkgJef8f"3`f;VB$gAf1_+JmR-.7a_KW,tNSB&lLP9a4A8>f$PDlFKZXC>tQPpI+f&'
6"><>PHc`qQre-CG,A#U0mQ<Ce:mQ6bcIR7kIJOeqD?Fi_)k@+Z/#GG]Akdc2P(\-oJN@98EM
\I7b'Ld/)p.rO]ArD;=Yd$+SuW+'?6-nJq"3GfEudqpB?1O[bel69Fu+;!E:Z$FV)^TYau`t@
j?sS\uH8=of0JlbFlH[]AhMO(KIZiH'T*KsZq,DnW=up8/b5U2liY0!maYQS9qWD+OolZM)2#
aYmg$!!$fAB6QOL8nHbTu-3(OGKY\NId/]AD&^RsN.1aRZ&-a<h=s+?SslTX]A0_H.$4?lgkcX
*eN4)b[h6k,'6jdSg7f\")1AuYp?D-Sn*DBS\RD,Y[`eAb:bT.[H!hO3a)Xp)tQL"N\q9fo4
N8.]AS;2NfMdiM:N_7)TZ>1RMdbJ\j6ab*08$G$N+o4NEi'URaSKG,l`$E&A<06'o!.&5^:;!
oM@2C3;B>b='m9H1QE0boj\_ZFR;LHXZK2ST3ZI4'(UD,/$r7.5E0UiAAWQR!3,\3cab$l4_
@ETr3)3"B0]AWQ;Q-U[rln;=O5-(rEL$dr2Ft6\!8)I5gPWAch+uZ$#c>KG>=u/R?992--MaN
QFGHt?m\@rAkbXst"^ccMp\-.NaI!d;>:l!1O%p`iW97,th2"Z-0gp6"O+GX0@GciVV*7`/C
edcbQ7LIG$RB[GQ7Eb\t4Wdo[[<E@WpeRR@M;Is[<E4;HQ*joMfU:j<TTmg1<DpP'_J^GA+"
fQ-?F%1JTskU!hpqOY0g10VS>/7!N"n"FNSu/<]A",T@^\<A`,L($&rTOPU/HqO?0\]A_@>Qm1
(gThTQS887^Y*#uT7o%kHUpLfI6E`*?^:Y@&<2Uia9/!5iXO)R)Eth4?%@nDLBF%+tb49BEn
ln5AUH/d9'O8TEL<_NNaF\ItJ!'(9,2;l$q8JPi`DOpL9%#hL/2q1_S=#4$#B`<1*&.]A.`lX
E?:NKZb(s7Dr5"'E[U)tAd[$JX*;]AS&4I;DeGC699>DLA>G^ghJ1r3e8^V!..SXGl$BYD6%O
)FpNmRSG?%`_lVAg?'@+lVtjGXL*^hDNPR8O39?%3!Da\%]AL5;:UmSq\J-=e-0f[K4Hr)rX;
sDY6,s@$j/U\T5PgN$TfT11npr:_$)T0ln$<umr=#OSPUZgs,-4Y-,*N=%W-f>pRglIA+S)(
EE4cX8[9'-A[An,f9KRXDH5""4Q7E)#Z9/O7cC(a&91>OlA4?K#+uqGZD;2s#6d^aua3'9_>
A2:Qi-`:`:+#i^FgNF.6Kd^8_D_-W@UI,DR6qBGK8K^^%Q3<bFa/UK*B$,Bq7\R&Mn5u0=#B
/9coc[3*R:@G44&t!h\BJJM`1!d8q,raT"Zkk=stGUi&Oc\)7r&uB"eDO[(WZsl)_1uHd/`0
+BH^8@J.1p7'!(0Yghu!kV:!FqW98e%-J1bEn\281S/6!T]A[0'2p?k@?`+Nr+06P0ptb:bFR
@JiOX2IUU3:C*hVq?,?%>^;mk'FrSU$gJL"j]A;/mgl5)iXP%O7I-0K[qYBThEJj'<.U9dtgE
(b'+#a'm3!#>Dt.Bo9T4V#]AP.T7n(i=%4@_GCfC<TVK*=@HMcbi0,uL2Ig:`lfu?a;5*N(L0
3E[OCg<e=F]AFB@I+>//pGp1b,6@JuqDX53:g5=*msD"t0$;-n4eUiA-6oZW+B-r$WBh6(9if
cj)K$)3%k5$^/[(B7Rb*gXIVPlII#G29M6ilkYUuqWC!Q#>WmU/o[3$^Y^EmZ$^sb)O5?KCc
GqTF7^!6D66)qD1%M'[G.7/7EfJ=1(5S8Yp4PYB60"X7G.^-W37?rklY,FpHfi[Y#ouuqNOL
/N`hu+i$8&W*h_.g(m#\WX*/SfYgr@_u?jMPC##Q"I"k"T5AWN-Bq(*f;Q&6aRi.ANnhC9)=
hUi=Aj)X,BNK&0,-?(!_V&&53.n)#XgjC^U0?%(rSNW8g!+9*/K_h4X$A=]AOFYUreo6\8+sA
?h)r*s)P(U<]ASlg*D1#q4f:C5ctpu-7IDMg'G`cLm<LY8Ff;rU#o!Fs)^*WUmfp\L)]A4l-Wr
'/i1jV_498qSH\DaWI3Uf)JH,O^kUbCQ<9=#+#3RajoFE%Vrr;;us2hjU"!uIKgXj*hgUd_7
3F(t/)>0ss+l*?S_6TA1b=[S>f%T+p9EFLuo^^2K>1L).Jo.nun!<4p3cE"#cK+pRN#c/*'l
<K^Q^dm<S[DG38=47aUi[nWP9gn9Ja!9aq_bM>)]AIV]AI'I^.%6hYQ,Y]Aa\ouLQ-+MU<&W?HS
4M?GHJlh:[rB.in@T!4MWrgaFS)nJ"j&em,tHJ)Ik@g`^P+B]AWlIP"VL@0L*gDm"OkJ'ebqg
q0mt@!TW(nNN#C?*G'jhHrH),7%!<ITTstejMpg?P+lP4"s'mki-=K1"2Pt$g*2]A."QK[>m>
X-q_tmYUur*0'IJ"V4nEQ3#ZYJaaSNf=C@98a[R7$4=j"@Z37]A:YF#$+)>u>reBO)`#L/<HG
/p+(N?9W>-Kol!PW_l2'?4PFX>i&Vg(j:Ln^WVFc0)'giiDkOVRN=89q+M[@6HLq<>Jbc4O\
P_t#XX'EZnCo1LH/@`XVZeCWu#mA4lB(^YkHdX\70=oTQVN?99;NslZRF`EHBT;eQjQ"/lt%
#?Kjc-S(@L@ks96r&mk$[qlH'/iD=!DW^(sNZO7>>R;ete+2Of)O6'j\8D5\FJE$'ij<Pm6&
@d+LFURrO=rcIeYbW9s-QR&j[-dQ0$io;_qK7j8r78=Bn[a8t-5>ENaC`3HD"c2o&O)H&rdc
']AM$I7#5t>_IE&(Tb-):$0L1gVabfjERo'V)%G8L?5I?R%?s,]AV@$3Eu4)in\i6@\-HB/i3O
8`?g?4.('fp&R*FnLKoE)cE;eKpg0e`%#ur^&e4O+K>49LfpE;3B31=q,<\`&H(*9P\?*CDG
$"o1mhP@NZkIiJ+4/@^2"=s79:-#0/Q)eOaJhiJLuH,4aL2dL6Xq5Fplf/h$:bGAZ+#@^-4Y
NVJ(+n?:F(aHb5LW:J'u@\mD*NdbQUJ+^,15E`/OP1gN-2eH:G/i^[#"Dn7egA&"`E`E[,IU
$ZG80e"nS3$np@[?n+9*U`g7\@?dM&]AZUk5X,KVK_Yb%Y^WA,C5C,6qW<om99f39B(\ST0=L
=#da[(A.P]A5]ATa6GjEJ+O)]A84NsCG*3jF8PJG+LQ`lK4OlYaTT:;$XJIN>65,67"NhKOSC=W
XH'Th+RfPs@9-?#A/Uq<4HCIs-;dZ3O;[Ch6(i1s@,Ra\FD$2*]A=CfgH1*2&r/%.GDX)TAQf
D5=/.4L,Hur?AfD"tUeR_luBAN#kFbPE4amfH)=Ao"-.Dj8;\NMd$jqfa[GId0tcmh%pSD+B
2.ob0<7D!f.`.a(M)SLRI<l2KI5>WL2g04-PbEC7+U7)^7WNuiWE7q\HP-t<1nb<(SL9e"d9
,gSFCq.EJ&tQT-iu5lJKu??uJ)Yl,Qc:)ck'L=kRRA%upl%+4&s(BLhl.Ck%Q[fKB&?pkcK&
hJZ^:Q=8hh=i3dTB<%cHXC,l7J%?Y)YUV)>ojcSDqjRYQk.L>lr.r+?7dj]AgVr.iaYPZA()7
Z=!Qj7H$<XE$khhnF,.L^9+7fJ"XB=W_Mumk4,@R30C.B'ZueL3IY>fiK$p(6r/5%6o6I)/V
Hg<&5CuRnV>CoS^9E6p9dS"_m6F=[S&eUMNu=pp-HeWZ5Lh]Aq\KPl"+<Y#hYG7ShJ"muTsRL
E4'D#/P(.qW4RL@63Ir?e[[.$JY6TIp%1Bl547.RlpoV(If>,Tfa%h(m%-O._NB=B!Dcge_?
`5r(1Y[?TC<]ArGMN^8haHfepKl?/NDSX?T&@HZ\6D@FYd%O>@T&/VY8tHrU<lkW^H9I1DfaK
5#"&D>>*!p)"B$Z_#C_[r0g(m>4*KZUKZaGHRgn:_(6,LX:hHQT"e2qBl&C8&Po/4;7-d?)p
ch7#C>mDBmdL^_He.j(HOgIL=<+RopmVm/5TFMhdCorf-l14[9RA#YWg51Z%r57!_Pos1]AN%
!UleD%k#X+I2!HG-MAX`E@)U+9o8ZT]A"-XHVU`kTR7aC+iD5i>"ObDCRR>2Nr7AbcEILL`in
\e<-@P&B@SLji$EZ[0a=7mB'*NT<p;Ca.:okEV9P'aoRn3FtUF37?9W$mnHuA=^'>/1aV_dh
n?/)&:Hj[@Hl'$Y0qe8[a2X8j_[.VpItIDSuE*^m-7jaL.Z8k<m9m)4?sBC%gi=e`/+0%$[1
CnQ,((o`KF";aqp\n]AshdRLZ7hP_c*/BG;nHgq_d?DG^3+QqTf.b#'6k1?!^j3?^dmi5P!*?
SX\,7"l?D)htP`SYqupeef3$A*!&0_"^/9W)k@AZht%1`2%2[UQ#/`I&3:\c?H*_Vkk,+g3_
uQ(6RP'4N1,l2FIB+pC;s$OhEc/ijtfD@4*61-[%hstf^H]ANY\?Hu]Am+g3^%ubHMVR(kIU$3
J55f?6_UZ*R@i>[P=p5Zhd[Ro#UDh+V?tR!2Fqk'EeEI<XN\F`F&HpT81e1CYr8E!5`c"E.C
"IP"&Ogf+G?_qYXT0fO;Af`EU<RM54>(IJ/u)a)8u?ZXFkVjU2S]A'\-QLIl&ZoBO)d1JYE)[
a!Ic.uVk'`\@U'Q0IH*s$A\)8B0%e7q%r59sJE>RG2'FlC)D\kI\X!"tO?g=OWC;+e.![VYK
Z:hN%qD[3MA#\jmWNj^p;(;NHeY?O]AF8dG<WIR7MYWPJfnD'Wh1$>G./d>mbIV3S3OL38W#i
CRCmh\c^JL>&H-hi2$<YLjKVbJbT\2M6:<8Uar;YC'BSl`5(C.VE2rW&RL&i$,G[^'HulTB1
r?@<*,khk1LVHU[F8F=\'YWVjTM;X\b%rlLW4AMuQ/N(4=ikJP\%5O9m<RS(r-[7t:rVV4Jh
QWNZ]AJ8[\Os4rR]A*!hWiSZ1hrK!U7s2!fH_\A.<s,WW"(=M?c/HXZhD<3FenQ>#(D,GM,W/_
&FGL:,n%s\*.;)aA5=&iC'."P?-.K7j/S'kuJ^#D9))G7/2-+rNcPGD!<#k!`l5F5$fmEkGP
g^a<Lli'V4c4hDl)QAc@$XLaS5*Y=7P!_W0IYp?I:O(7`j+dCsF?n2jSf9)4Gl!VT(jDXd`b
qV+pr:_;A]A?O5K^l^p&2T[-ZC">3FE,JuoeYjK/Rd%8!LC16qr^GH)FaQAaZYW#U_/p<`,\J
i01lNlS2+^("Wj1dlWsYMT,l]A%M7.^?K%;Ve!DO:t1H6qQ!=70_<K8Rr0<HNlP$:?\nN]Au?L
iT2dPE-Ct<or*n7<aO8):-`NU-GPP>IFV_XYNO\(6N::'RT8[3]A:@o42l>%&j7uu0_?uD=`K
b[o.nc,mk$M`f=98L>nbRt!d"TgbkQ>e!S-6;+Wqt-C0B$N/SWDSBtH0?GMg\MXHS0IW\Hh,
AreZ2C"c?P+]Ah3b32bbGWR_,6%L[m+ke;*dJ*/?UeQD&2W^9.;3'pW1K/EJ1Vj$PEk#_sm*6
tjWp+`L@EHMO\?tm?K*"QISW+6G5GRmMt7WL0-\HcMW(QBPTrUL`!-&e&5^Bhmi>bR_n!5nX
'\:e8u=B6+sUL$.Q/nnCLC[R?pTkd:G=n)Q(3N7IOHN3dpqG7ILWc[O%HjUYg=a0cRHLb8ZB
jl3aqJg4BfH*[Kr9I&MYJrDMm;F)f!63nbqsjR9g3/Tl3YrHW0S>nfQFH]AWS(UL*<`Lg#^h#
6_m)ij-bWbGr(mSNteC.27OARB?NqpSPIP.e&X_`-R3LpB.$O=2o;s[kXaDl=Pk<)Z,pTGF,
)Q0%u8]Ai#j<<leTP2#A8'hcqZnZgHp;`A'!aI"ne`W%&MT<3Q8N#o8&mri1r3mMq[L^p]AtLO
V8:Ao.=]A:4Y7rMoB8lo6l$d`(jk+(>kl=`:6\B<kNoTL1i[J,1c,he#MrbS<If*U84(2[cG@
H^A)QSSc4<uhP64se'/nRb`=Q[]A"c\G%E+?N42ni;j?UK3YMMXDp4ZjIT_98"N]A.oV*JqW:[
UKSU5PZnH&bikhCX_@oB*Lt/2\O1);e^;T9@Ch03b\/2<C1i(;b+?ABp(VJ1sV\"g#3Jc7GF
rs<rW.\=Q`AE1NW)[@ar;d2^"B755(_bS^F@%?@:<LHuWLD."2RYSfbtBPQQ^5H71ke+>^6,
c&rCB7ec%KRn/C_\=MCK93::*P2b(hiG1#jp[Iae8`'qPZNg@YHRXmL(_a*CDq\rdM4X+7[d
(iQ4iB_"\Fhd*gAmfKK#%7Tqi)Z"?6(,]AJbHqD>?^EdX8P*pqQo&6n@K!*<of*p3&bs3>qa]A
%:"Hn<J'P,E&K8.5-u]A%N_FglNYAGPHPZm1bLI5hC[HCaJKI&"<MhMhZgZ&7I'%VPO_s__/!
2uf&Q^q=kZUotY!rhs6SXf^Y\;ja*+u1_%]A[j]A9Tse-IBi?,<0KmcQOu7Z.J`Y&b/0D)=-t,
u+pAUFj`I>+TgO!E&`-C!NUSZkn=6-]A)FadH4H=^P]AJ!ZR)[p9<7]A"lg6:8#ZaR'[LdKbO5&
8e+0Kr^,Yp;D]A:)7cY$hE[:@`K/>5"IT;F9#H1hhlO:Cb-T)5&Be]Ah?=:T_t:gj?-7Ei?(W[
)ZNL*HYEVN+.I`ME_IU1Q,(GA7B#C*E4b;tlpaqVK.N]AQt8QGpN<5gAPN$?f]AHSjBP/jn>$?
j:iA&Rh!GR+LA/0JJb`^Po`<$%cRN\/T*:8Sr#H'`6OS-Q(/<>C+[U"".@o0i@B?N3W+MDZc
F8CgI_RR&OZ?AkrUJ<![2:[-R[f"1l1S3SP1U?&f2`L/]AU)f]AmZ,De;!Vq?84JBk)m$cWGA2
oa#A2t5dhodBSWi(1pn+^+NpWMC+FSD?!UX^E1L`DNG&3$,GQ33MkNi".7Xm8#5eY")h]Ams6
1W^di?M28LWEk&ip6;+rA*Kq(Q@nF-%>uq(?mY6LN&S"==eI<Y,X?sp^PZa]Ae!4IcIg,-l3T
>'*I]AB"OSBB%j'q<qugI"fI)8#]A*-!ZAa)AM>!cEO-'>*M5#*"iA-kBa(nObP\d2)7\Z^[K;
,KS'E5s3!FtYQd7H6(YT9BSONb5s9gX4":SehrMaEJY"+Dn02%jAYF\j$Om25+f@mm8E=Dh)
qZqpi@4VV&0OuRG>((pcfi89RCeb<ocl4U&"1D8`mQO.5p9P]A&:,m9ppdkl1&V/M:!7r5:uH
ZOKJ;"tM.FEch,Co-WU7(6CX,i4YLnp5R:jBn3\*KLC%QHGO\#*Z]A>bqGln]AgEb#]A\B(kljM
;>NVNfFN:>lX%/X9@8V`P[R-"r1hU@lST<eo0I>peV3QH\j't`flm0I?UPCb,dXO5.'`"DI@
*UM:n$<8421#l62$t7>pJ&g1AS(1r&o)+%g57#3hsAGZg8`5*uJR&A>2j6eZ!8ncI.Z7mT;W
eUB$=9``g/$S!t&JcX"1AU_L3T#k,W=[YM26:jn#"1U%I^Ogboq,=92o>OHN_K_J8&a29Mr(
RF7CHYcQS>#&fr*N+0TT1XBtg-*<Nd]A>?Do>Jp2N41D2_D-A45gl1V*m7eCCY7l)Nk8m[-eo
Rii/eaBK9P@UE@cs+4U^&Q]Am*mSfr=(-]AOJ`glAolP`+qW>GeU%aEo;7"R:dqd[MsUqjuAQa
NUF&dL4`DdD.+Y)Yk]A\h+1?]A`cReti@Add<&%-"j^SAsI@YoYQRhS]A%W<bJBS[r]AQ^KFg2B`
@j%;D?X5='>pFH^rC;TkSQoq3n$_F-G=\$-^$PC.TVSqXaNObhQS`IE7V<$"&DE*JK3(I\gu
BCc:YU_>N<C+BJEtPJlU>8G&^g_BCn_`RMXp#]ANU&77%3o@?J+(?bMpj056.QnM.Uul3s?L_
faHLIWW-5"QC#1Hq2Fk/Uei7ES<<h=[k'ie8W&rjOD?U/Od/.f[]AU)nYnE3aD<.N.K@OQf)H
CHa$M`Xe%QheoHHWeR+D"^FX+Jl^tJCPiZkg%!]A;7nK&H`L=\aVlNXr78Rqi,oWZjC-o\cr8
rI`&f]A7Lg&(H9n1cQ=:BaXsEo7p>m9)2U>&9'****Gj/(3qa9DKJCZ7?RrAm;f2FHbuO2h&;
e[iZp"PE)VDVBE`d\"2ac(>YUshaQ+G[b>5Ae7i"st>fQ7oNXqB(5"G.AGVtPNe'!ek7aU'q
h<oZ%QNm:jV-RZl;X[sad@*MO)9AhScbh!VHq+8A_Y.A`!7Um^FD?+bubn,lA);J8Wfd+rQ`
:H\tkk+ZW@udbsjZq8tg"T+\HH?0#a&X*h4M=E/\Q.</4#*55`pT`K(ZA:<g<'%JT]AjX?Nje
ol)l?S9dbZIsaL"%-QTu-Q0>/8P]AS!XKfIh[u6Z&neqO/9W:XM2o;?EtHl]A3,!VqU#k2gK]AK
mE[M<=6G$[TgqWDde=;t>qIqlcp#"5%9Miuabi*!42b<,hM,545C1L\THV8Nb\`?80oF6D5p
:kX/Jhu(e.<%H-1e+jR%FoOl?HT6lntf$2GG%?&rV8-M^,%B]AcS[s<gpHh1]A3pZcHqlSrs$/
eSTCpYF&j-=B6Dr!i+!cDAUu6dNPDu1DsgbW6'f_-KLBgc/!BRP735"c;`SFAPlEp.[+4tli
:e66SsgVBrX6-3&!(2[>-$iVTrNTqq%2oo`<F4N8S;HRihiUiL6-HGFtc&=&9FXL^bWe&;!S
W+6"'I%rl3%D7$;EST&^RQO=*lJd,>T'(N'B9WW+r?l3H`"*@<9@qN31.'Q7?2^iBWVBjUdM
$AmRs\='U5parbE8A3Z!n8mLs?#[5C=I[77'X^ZT"qJl<C\,QGP8ncGoWb4,^H^(':PQ.cp8
iou"L-''7<R&aQW@E)0OG<V*/K:mc'ceM0GETh:%h@c@FQ0n8UoC$4u0]A(MtsT7H#5U$Lm4\
qNVS!GYeCi!aWAT[RafWbj'2tAAkNSAOfR_<`O<%]A*Er1.e]AkK(XJKGHU0A4XG;j5d)VFG6M
cs;L7N<63cEYkX"0MTU]A:]A\b"aJ_OHM^l]A1Zpc_5>M;1*9aLIJI@L@+_Y9gCs5lcD)H-]A4+i
YN^"f.KaR2W5\gO&Q,'!&r:6hNO4OVWM2,sBeK-KY\GmG>:_^Fs</'e`sL^5JP?CWXLWloa9
?+"b+h`G^aat9aKHYu>""r1?JkjDc5JdfsFL<p_F"_`sdh@[]A8D_$g]A6SM:I&>2&ArG4QkUR
0-Q2'sr_n3n";Vl@i2`,Db9N>(>...TX),))ml)-\Q`JK;AtS%P0$3hNlI(s$P(A_JgUm[J,
M7rm&P:IUs?3Ws54XK_]A,5536\Rbf-C:g./[8`S=W;CQ[H&J!XIlc+RF9^srplo/A[b+lt@*
:=B?!Ipn3:J"G^;^4'kjAL!ee4i6%2=,]Ai>_^n@B,Frfs,$cS>4?Mt&;]AQ2C41.2JE,I>@",
:o1d;D;\@:)jm<',c_Pm6<cV_B>C>=63$/6M(lL%6YgbH4-!Bn:r6lmQlI<n'3O_mUg\t[Ti
F5<oG;q--\Z(g0:cpRPW??>A2Uo;J6=i6iA'B&?)!`El#$%(1f;[q&P`XYtdLI?';4a#3,j_
,=WK95.M1`bb)S(qVr68TJ_o)-:r[r:*%oFfoH3I(j.CoS\b$CAU<^dZ=<&!Bcd"M=jQg?!M
KkMN/U&m8Efm-OjFV]A-%p`7ht(btSpbfCDY!9R%dC9dG0bZ8cPh^&iPMgPg:\Fffr.O8mT)J
P.LN1Cb@F\N;;Qi=Feg%(78/RDahc$$q'FMA(1`QZ;h.8/;Q)Vk[Th00QnkQZ;Q!P!dWY8SU
>)@Z7nmCWV.A%=N*d9g>*%r\bZTkJU?[\VrUg*7X'OA+'?e![;Q`M"T/GrF#JPNFg]ACp9AW+
H+*$f:o45@Tl#F[\#0&IX,1>@<TD,#%SZj.geA)hPm'ea.Kf#`_MhL>/600`=RsA,%4gh,=.
?`<!YsbV]A3i_nFMt>cDt5`0r)N@NAWuQU_udhB/V/8UIX02I#EDU@Iq9.T*"\IP`\!kUFM22
2f<X()I'-tQp$*$+r-LtW4]AL8R(,"Nh(A@+^!!@RG!LtHXp6><,l-q%[m(3`;A]AYcO$L!R":
tEB5org#4=FM!'l2CblL[j3[HbikX<VeVLnP9C,d5h)L7o=<=h).]A[\PcG_XnRN_[(WL<hQ_
H06ZqK\rmtp8cs.-'a"JqfTVI9UfJ>m3H,F-U_JhWHpjZ8BR&^c"1cBdZ%)bAE]A)&]ALE-WOm
Cq^5)-4:<')kD^PCWM:hZhG@SK9#PiY'pqF2-kX^nqk@.=^d#%fA9Sa^=p'<a<L-%0M0U%<*
X$]A7`_S'J$jLfiD?XlI'n+E"gbc[apcPCNh'GoPpi%W1T@KQ:V++p'fp\P*9GVm*/[j`NI=c
Zb\eqGB@fUWWDLf9U8HA`<j".k`ZUHgEu#\]AdsT>[6p9^YG+[sfcb%bPH%3U'rSI:T^/mRni
E!d/7[*X,s&Brr@&iAbr;%':$\!:`/iV4iL8ag:NIQ1@nJbOe^nc-_6Gan1]All#h5rUA4HO(
AUoUSJp%XZhZR.>=idlE`&gs0Vnf$[\^qQ^MOp=Sg!C!mr[)t,C1[%>j;glXHdoR5OmQ%O@e
BcCO5LlU;3FHs0-GJ?dQaUn([1ck-^bEp[]A`![OpP'>#lS"9-Y=1S_XA;Gn'nqJS4[DFQ&Ot
CM7FVgskSHUN,dhZu17kQb_eOcZt]A)0I/W)M$TJ(TpdbM)+$3B$ouQ3T.i8'a@S5OW:Gmumf
4HO[$q,(NVkV/*,5^TP_+iub#Q(hA%^ha8;Eai15&e$rnrqu5>)<;s>t=/oq?]A-`41+'g54H
f=poUIR).ERiZ&hE?L.\8uj>"JW+!5qtbMaQ7^9$&'NX^Z`W6p[rl'.S^A!qZA4%%4ad%B.F
^Z)g%Xu?Xm!K^W%Op\PH(hFsrp4NlLYi&"Y=/iTe#,e#1aMr:ssThJnD<hN0:4cE6bA_1NSH
JT9'Opbg)/3@:bSVJH0'e#_\K`Pop!V!Xa'RAF-FP-n]A-Yp`7TWMW+)Im%\g2;:52Xf(=PEK
4qp*3P91!XEC55*8u_06W=(;1Xb+0a)R$D>=!`Y6HkCJ-)QSWHG_#XFu'*@AXj*1S-g;#,ea
@?YiO$5Yso#;G9A>MmbAY]AB=X=U%Uhanmo6aUdqNBoAg_o.N=H5]A<B#rYGcf`Ek##VB*=:[f
O-`OjC`Qf1?)U9@mC/iN]AYU?j[j-lL>m9)m2?OX:"0&HJ`n:*)#iVEFJDEg-;'V68m)3]Abt^
Lr<i7jZag7Up-.BXI/U(Gr*Fn;F8,lU/4RuIL#OE?'.l'BZHN"c'q^AtX0kVF8C]AD:&krh*W
mds6,O"a3@4LT(H9SKf+Up&d+":JPZaKq'ABXl!#H[H+t#%.CBZ?p"j"6>gf)#706[T$jkgN
b4<1E.kWeToX2k\ie,BgFhScW!&\meF,F6/k`KlS"j9O.q4ZrkLFI-rCrfX2'-8p"5L;m=0@
,5n&<[EK9_HoZ%%6GAAPYhIIau?KD;gP.7M>ENOQD<OCalfUeqt8Yfjt$?[;L<tc(CQ@in0V
*UASM=A_Lf,*_h$6n8bj"#=C?]AQ)@&>Tc-q]A3I,h^R?"iLKZ):b3mZD&Wk<[Js%,NKgemPKr
.!C:u48lg>Ft3G3ri%"PuT6h%I)1Hr@,jrjIi#R`h_gW$m[T)BipHAW'T*qEhgnI$X^.8aH$
\pMmV!^9fBUEY'aU.uV7'5?_,5%fp&fG>*/f9kPc#/e'A2&ktb33!Roa!BVg%sHHh?iiQ[8.
(0=\c#.<GM59a?M4b"9BJ;:f9l=:L55m$GSJd`f[2(IK-`ol\16oi+A>(g[i5PXCG2?(QU1q
5+gHFfTg/?.=0uX%Gh/-9.p(Z@1]A1s:N.g;W^";dBnY-?^^*_LFITZIh?HK>+3X;J3f#d^`:
W$k^[A+'\59^SZHYA/pVX6a<N]A>\'^m'!(plXQLg\#/qoC/`3KpaUnB`hGr0q(C@^!%<9:'t
44WJ6"#/c:jt@jLOC42JQ&Hce&90+["9?C[BCNP9PL=<96Ci\8X1J/6[#BDC6lQu-6"Uu<nN
5'aG(r55"7VUlQ^Hhg6.6p($_e8^E,(+#k0eD\<a=]AV*YcT)f^>b?)<Xe;e(k%cVl@slag5C
De>&skjIQ:\MV[O,X(c0;=XFu'WcZ'+&,WSCG9P@+tS:JTFdl*m/1T>`7%+M=K[F/ZZVkiIN
NB]A=AA<ZJ&Hs!n!t5&2b-qT6gK=G^sE=X#L5HW.mPF1VkXM3>h>9aXs'=,-m0PWPs"S<_Q,+
t"R/X/.k:Mg(*JlTeOL([Dn'a#t-E/4QpV*FhE5Nq*5^L8(E*cA"$A+A6uJLX+.i)Sd(Ucid
A$+PASfZk:'42s)"LdT5ppaPW.89oq&oBEU@cejn7\XaXDI82XCRARj!N`jZ=EE1YXh0M6f?
Y?FOV%!YZ/'`GN3bY79Yg*eOpQuLlC+9j'SB:W6R+YTNi!Ds)^PM$_3->j33^(Y"WN(_p?R\
TKX5sWu@B;`*R$Dh/,eG.JPnYRHQ8BgB]A?m+)BIlu-(^-SnO)[^[p5ZgJl4N0<m&R,#/J4<(
Yph\<.q,g'tQ=^CY>IY81*>=tj[YJYV.]A\8.eKF&)!js"R#,h='Ra4\3)WTG7%8SL]AiH-cTD
7XO_$Z)^!$&e%:8P1s9dX[&9dZUTFH"OL]Ah<)%0KH7A_PSUt_mI\&l(ICul>-s9ipF21BK]Ah
hlT4Tp+LKdTU_9Ou#=JV9b-<,b)Q.O<07?C'_JKfl_<eC3aElgu_jWTPaF,tW"T:l`fQ*KkF
V;4l\\J_5d<IgK8%SND:DZYp$$=d2.7Q*s!/!K1=[!d-POL@M6TFrWMo!/76*D0EuX?+ncT+
+%>.g7aqL'KqKg<btr"KZ6#L7cFiDAUpFc`_L'%X>J]AMO[ePI%^IUN5iHb*%aWi!7of2j(P_
\O="oO6L*+pN6F*ZOjeEUDQke-Mkp9>F6=gNnr!Hql@[H47eDm;ddhX`#n#RZ+*7%unkXhc+
NPoRUjA8_*;m.ZjB"8YbIJK?&co,>X,c+\!$%2-RFT(lT6nD^920]AQjQPMi.?2F7/ct)#]A\^
E:#RF\/(dkH_5`#S3"m3ZW2`G\lomOVWe_3:9:q&8iH]A+u=40B=Sg2Emk>32C&,(W;NlQ@&d
Safj#6@L.SOCXa5]A!&DC,YAbE`SX`ik2GZ<iM]Ak6X97$r>:b+[RuP/0"sVfA6J*m,Fhs,l<+
%82TmMZ#>YgG4XAc"MeX9]AoIl/&/?.5JL`5_/tN!>I5K2t..HNrrhemc!67Z%Dj8D42_l\bi
l1Vs8N:a"iT6%Z4l,fFi0M9OgN27?j)R3<n4nd%*(q`G8eN6E!nCR-VCL`g6PGaiI5W>,P./
2382nnN1"0(J>=&8HKGDquQ*'N.`uE`8HJG/=gA<\eLTkEiaGrso~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="568" y="36" width="622" height="346"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'店鋪資訊']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="622" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'店铺信息']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Al Bayan" style="0" size="128" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</title>
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
<CellElementList>
<C c="0" r="0" s="0">
<O>
<![CDATA[店铺号]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="guitaiming"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="0">
<O>
<![CDATA[店铺名]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="dianming"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="0">
<O>
<![CDATA[铺位编号]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="puweibianhao"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="0">
<O>
<![CDATA[合同编号]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="3" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="hetongbianhao"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="4" s="0">
<O>
<![CDATA[店主姓名]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="4" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="dianzhuxingming"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="5" s="0">
<O>
<![CDATA[联系方式]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="5" s="0">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="lianxifangshi"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
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
<Style imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80"/>
<Background name="NullBackground"/>
<Border>
<Top style="1"/>
<Bottom style="1"/>
<Left style="1"/>
<Right style="1"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="568" y="0" width="622" height="382"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'商場分佈平面圖（聯動）\']]></O>
<FRFont name="Agency FB" style="1" size="112" foreground="-14898964"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
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
<newColor borderColor="-3355444"/>
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
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.map.VanChartMapPlot">
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
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.38"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapLabel">
<AttrMapLabel>
<areaLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
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
</labelDetail>
</AttrLabel>
</areaLabel>
<pointLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
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
</labelDetail>
</AttrLabel>
</pointLabel>
</AttrMapLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapTooltip">
<AttrMapTooltip>
<areaTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
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
</areaTooltip>
<pointTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
</pointTooltip>
<lineTooltip class="com.fr.plugin.chart.base.AttrTooltip">
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
<category class="com.fr.plugin.chart.base.format.AttrTooltipStartAndEndNameFormat">
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
</lineTooltip>
</AttrMapTooltip>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-13312"/>
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="false"/>
<FRFont name="Al Bayan" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
<Attr4VanChartScatter>
<Type rangeLegendType="0"/>
</Attr4VanChartScatter>
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
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-10642707"/>
<OColor colvalue="-10237754"/>
<OColor colvalue="-19351"/>
<OColor colvalue="-9111"/>
<OColor colvalue="-15033779"/>
<OColor colvalue="-7239179"/>
<OColor colvalue="-7881222"/>
<OColor colvalue="-97670"/>
<OColor colvalue="-6812999"/>
<OColor colvalue="-4520142"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-7881222"/>
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
<VanChartMapPlotAttr mapType="area" geourl="assets/map/image/廣場一期一樓平面圖.json" zoomlevel="19" mapmarkertype="0" nullvaluecolor="-3355444"/>
<areaHotHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="PDp"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report0" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="PDp"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
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
<NameJavaScript name="当前表单对象4">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="PDp"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
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
</areaHotHyperLink>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="null" layerName="无"/>
</GisLayer>
<ViewCenter auto="true" longitude="280.0" latitude="290.0"/>
<pointConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</pointConditionCollection>
<lineConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</lineConditionCollection>
</Plot>
<ChartDefinition>
<VanMapDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<areaDefinition class="com.fr.plugin.chart.map.data.VanMapOneValueCDDefinition">
<OneValueCDDefinition seriesName="dianpu" valueName="a" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds3]]></Name>
</TableData>
<CategoryName value="dianpu"/>
</OneValueCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</areaDefinition>
</VanMapDefinition>
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
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<BoundsAttr x="0" y="36" width="568" height="626"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'商場分佈平面圖（聯動）']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="1" size="112" foreground="-14898964"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="568" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[哥伦布广场一期一楼平面图]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="112"/>
<Background name="ColorBackground" color="-1381654"/>
<border style="1" color="-723724"/>
</title>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
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
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.map.VanChartMapPlot">
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
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapLabel">
<AttrMapLabel>
<areaLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
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
</labelDetail>
</AttrLabel>
</areaLabel>
<pointLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
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
</labelDetail>
</AttrLabel>
</pointLabel>
</AttrMapLabel>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapTooltip">
<AttrMapTooltip>
<areaTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
</areaTooltip>
<pointTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
</pointTooltip>
<lineTooltip class="com.fr.plugin.chart.base.AttrTooltip">
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
<category class="com.fr.plugin.chart.base.format.AttrTooltipStartAndEndNameFormat">
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
</lineTooltip>
</AttrMapTooltip>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
<Attr4VanChartScatter>
<Type rangeLegendType="1"/>
<GradualLegend>
<GradualIntervalConfig>
<IntervalConfigAttr subColor="-14374913" divStage="2.0"/>
<ValueRange IsCustomMin="false" IsCustomMax="false"/>
<ColorDistList>
<ColorDist color="-4791553" dist="0.0"/>
<ColorDist color="-9583361" dist="0.5"/>
<ColorDist color="-14374913" dist="1.0"/>
</ColorDistList>
</GradualIntervalConfig>
<LegendLabelFormat>
<IsCommon commonValueFormat="true"/>
</LegendLabelFormat>
</GradualLegend>
</Attr4VanChartScatter>
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
<VanChartMapPlotAttr mapType="area" geourl="assets/map/image/2Fmarket.json" zoomlevel="19" mapmarkertype="0" nullvaluecolor="-3355444"/>
<areaHotHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pgt"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart0" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
</areaHotHyperLink>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="predefined_layer" layerName="高德地图"/>
</GisLayer>
<ViewCenter auto="true" longitude="0.0" latitude="0.0"/>
<pointConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</pointConditionCollection>
<lineConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</lineConditionCollection>
</Plot>
<ChartDefinition>
<VanMapDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<areaDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="guitaiming"/>
<ChartSummaryColumn name="dianming" function="com.fr.data.util.function.NoneFunction" customName="店铺名称"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</areaDefinition>
</VanMapDefinition>
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
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<BoundsAttr x="0" y="0" width="568" height="662"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'累計欠款明細\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="240" foreground="-1"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
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
<![CDATA[#.##]]></Format>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="1" size="72" foreground="-1"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
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
</labelDetail>
</AttrLabel>
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
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
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
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-7881222"/>
<OColor colvalue="-7239179"/>
<OColor colvalue="-10237754"/>
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
<VanChartRadius radiusType="auto" radius="90"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index18" function="com.fr.data.util.function.NoneFunction" customName="租金"/>
<ChartSummaryColumn name="index19" function="com.fr.data.util.function.NoneFunction" customName="物業費"/>
<ChartSummaryColumn name="index20" function="com.fr.data.util.function.NoneFunction" customName="其他費用"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="891" y="36" width="299" height="244"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'累計欠款明細']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="299" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[累计欠款明细]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="112"/>
<Background name="ColorBackground" color="-1118482"/>
<border style="1" color="-723724"/>
</title>
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
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
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
<![CDATA[#.##]]></Format>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
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
<BoundsAttr x="891" y="382" width="299" height="280"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'當季實收現金流\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="3"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="1" size="72" foreground="-1"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
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
</labelDetail>
</AttrLabel>
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
<FRFont name="宋体" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
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
<Attr position="4" visible="true"/>
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
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
<OColor colvalue="-7881222"/>
<OColor colvalue="-7239179"/>
<OColor colvalue="-10237754"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-11385531"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X轴" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-11385531"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y轴" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="45" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index13" function="com.fr.data.util.function.NoneFunction" customName="前期欠款"/>
<ChartSummaryColumn name="index14" function="com.fr.data.util.function.NoneFunction" customName="當月實收"/>
<ChartSummaryColumn name="index15" function="com.fr.data.util.function.NoneFunction" customName="預收金額"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="568" y="36" width="323" height="244"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'當季實收現金流']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="323" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[当季实收现金流]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="112"/>
<Background name="ColorBackground" color="-1381654"/>
<border style="1" color="-723724"/>
</title>
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
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
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
<![CDATA[#.##]]></Format>
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
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X轴" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y轴" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<BoundsAttr x="568" y="382" width="323" height="280"/>
</Widget>
<Sorted sorted="true"/>
<MobileWidgetList>
<Widget widgetName="chart1"/>
<Widget widgetName="chart2"/>
<Widget widgetName="chart0"/>
<Widget widgetName="report0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="1190" height="662"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="950bf13f-adc7-40e2-9d22-3f2a81644ca6"/>
</TemplateIdAttMark>
</Form>
