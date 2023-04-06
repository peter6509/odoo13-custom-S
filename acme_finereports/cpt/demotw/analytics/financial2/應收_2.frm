<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="Embedded1" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[ColName1,,.,,16-01,,.,,16-02,,.,,16-03,,.,,16-04,,.,,16-05,,.,,15平均,,.,,比年初增加,,.,,月均資金利息]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String">
<![CDATA[23"jN_E\MsBD6239<W<l=/cj#=ZXI?K#GmKhjiF""YiO/_+N_MeGFBXDYs3ZdukX_N@?Ch-_
f3Xj=hh,=X2:[aEI6^XRATR1-/?k*[sqM=B]AKj(N\onf;CfFTgO1rB/1e.O$+Do[A,G60)~
]]></RowData>
</TableData>
<TableData name="預設" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[日期,,.,,項目,,.,,應收款]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String,java.lang.String">
<![CDATA[D3MRAJj9l9C]A#!4*VKM]AT8B8G^kQ#S)A?los+Z&RiPH(GLIZ]A3k@>XGjNf/`rUW3Z+2:I8=^
t3kfW?/XmDO$R_u&3'RYc=NRX4>cXC+jQR0++j'a>O!QXkY5H-f]AnAB7'&,F;rJkUU3P?t(X
>_<-hh>F>a7D=bWK27kQpXHOXYGUaoN2CiTVU\tY!gj2l@pICV'G1+H>X,ou_\B%4Xg$%9bY
k@m\fuB=ugtP/=]Ad:,$l-.Z6OOJQ7`#dR4Z;nb"0-oZ3k*\2?/&9*cKY\FcA(soG%smj%Y:q
cb<%Zj6jW=~
]]></RowData>
</TableData>
<TableData name="化纖部" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[日期,,.,,項目,,.,,應收款]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String,java.lang.String">
<![CDATA[D9t!IK.m^fiAoZsa\GAL-`gLN)]A)mPN-+)<NPmCe7E2tQeka%sbNrF?Aq,6Cj0DI!dh=TD/3
TS=>gp?R.+UaEW1=r5_#ZkL74>iW`6p,%.>sR2AnH_E$$(H+[e`\+&-autbF6cj:5ip!Z62m
FKX)85=?=FeM_]AJ+M[H&P4jN]AMM[KGJo*5~
]]></RowData>
</TableData>
<TableData name="Multi1" class="com.fr.data.impl.ConditionTableData">
<TDName FC="len($kind)!=0">
<![CDATA[化纤部]]></TDName>
<TDName FC="len($kind)=0">
<![CDATA[默认]]></TDName>
<TDName FC="len($kind)!=0">
<![CDATA[化纖部]]></TDName>
<TDName FC="len($kind)!=0">
<![CDATA[預設]]></TDName>
<Parameters>
<Parameter>
<Attributes name="kind"/>
<O>
<![CDATA[111]]></O>
</Parameter>
</Parameters>
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
<Margin top="5" left="5" bottom="5" right="5"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-985610"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-985610"/>
<LCAttr vgap="0" hgap="0" compInterval="10"/>
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
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\"  \"+\"應收賬款統計表\"]]></O>
<FRFont name="微软雅黑" style="0" size="80" foreground="-13421773"/>
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
<![CDATA[1714500,1324800,1324800,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[3390900,2475360,2475360,2475360,2475360,2475360,2475360,2475360,2475360,2475360,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<O>
<![CDATA[部門]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="0">
<O>
<![CDATA[2016-01]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="1">
<O>
<![CDATA[2016-02]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" s="1">
<O>
<![CDATA[2016-03]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="0" s="1">
<O>
<![CDATA[2016-04]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="0" s="1">
<O>
<![CDATA[2016-05]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="0" s="0">
<O>
<![CDATA[2016平均]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="0" s="0">
<O>
<![CDATA[2015平均]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="0" s="1">
<O>
<![CDATA[比年初增加]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="0" s="1">
<O>
<![CDATA[月均資金利息]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="2">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="ColName1"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="1" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="16-01"/>
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
<C c="2" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="16-02"/>
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
<C c="3" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="16-03"/>
<Complex/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="16-04"/>
<Complex/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="16-05"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="6" r="1" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(B2:F2) / 5]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="15平均"/>
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
<C c="8" r="1" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(B2:F2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="9" r="1" s="3">
<O t="DSColumn">
<Attributes dsName="Embedded1" columnName="月均資金利息"/>
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
<C c="0" r="2" s="2">
<O>
<![CDATA[合計]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(B2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(C2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(D2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(E2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(F2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(G2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(H2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(I2)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(J2)]]></Attributes>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei UI" style="0" size="72" foreground="-1"/>
<Background name="ColorBackground" color="-8402710"/>
<Border>
<Top style="1" color="-1"/>
<Left style="1" color="-1"/>
<Right style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei UI" style="0" size="72" foreground="-1"/>
<Background name="ColorBackground" color="-8402710"/>
<Border>
<Bottom style="1" color="-1"/>
<Left style="1" color="-1"/>
<Right style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei UI" style="0" size="72"/>
<Background name="ColorBackground" color="-2560263"/>
<Border>
<Top style="1" color="-4144960"/>
<Bottom style="1" color="-4144960"/>
<Left style="1" color="-4144960"/>
<Right style="1" color="-4144960"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#,##0]]></Format>
<FRFont name="Microsoft YaHei UI" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-4144960"/>
<Bottom style="1" color="-4144960"/>
<Left style="1" color="-4144960"/>
<Right style="1" color="-4144960"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<a+\P@rIUX]A(ah#k-7Tg`Vk7ZpbaQA.(tD/Od_2fNK4++fJ6hZL<n"Q>&.D.a:eL)i;"<>#
Aa]A&@UX3&IBXLN=[=-=:?@7Kog_0ShJK+42"6u5,Vc&?LK1ArZIa.\X.AdkFCEipVX]ASlf7+
i^[V%:1M4j6]AB8JkB$?XaR5*aTJ3S?>s'hYcB?llqa]A\N7WXk"_W;;((q]A?Wq'm3$`ruR>mq
,Yq<\,&<66p7%9"`Hl[nnY5gG9kA8M)J^4p?S6R1[UG:%*t"/ApeUgjqf'HpEiFLI"?W+Cq/
`UG$bTL,OG*j5D36IbkM5u3U,k/-@u#RQ38Pfas%W19YMI^5b_k:Gg6gmc>"F(^bTSWn`lV9
Oc=4ZW`!8]Ajsg@+5UFr*?2#B)o4JpJh2:::H_6_j62+@MhVEdi?"4mC-dI<@Poa4V,JQ#`Z^
Rm>gWL_AY20G'3<F=h@jBnP>$kQu=kU))*R+"./K\1l%\1Wm4mF1tH?R,]A/g?a9?^01#f=0e
((jT4I%Ir%@]A>c@.YP9f5.>"@nI#pOT&bnrqK4u6+(^bWlhhC@0XE(H2RHf10:Ubh4kAti12
(a,)EbPN"!gg7H\^.ViM@[$hRocL<<`aAfR^sKc5+U28^03m<k%2j2,fGZ'_!AMt4HsP2$\)
#]A9YeJsQ[Eusc&FW"`_C9G+mMLR/@hno?AUn0^DS:,O3\PfH'C\4@?]AE]A5#q/u>A4@e(,_'l
>:Y#c__+Hg4a:op-a5;Y:JG6T;t<;VnW!?7TE4igZ`YEEOdr94rBmPKbZi=*jOa5#fkRiM6A
4'd)8(5T!"WqC?'lJjYY0\-FB847feDl&;Nn'9'F5*.<B!`"oaiSl`5@sb`ar<B,9IHU8"!Y
=m_OHhk/,A&%CYYhQh,?WNujfRLm+RYMsbor+n&#d(Jh<?(=r;8NJ/+e3>Goi@:D4a\CQS#D
!_1>Xm\2T:)-8tPph9Mp5DYdPk\CHGk16@a^s!oH!,&+Wu7$[e+D85RNoF_.eri@%mTQs^-+
<ketc[`akh.m(YWG\fgWNG]A/`":K]A8FkT(2k"SfnL<G0p)RplOqXI3`+Pmm]A3mS(du_5?ZB@
A@9&=IsGu(/#E$fEZYVf^R*)c!Ofmc-"Wa0$jsc>G-:9ukB*;mGF7RkrF!%,)F)(;j&m5O5q
[7>iBX*V<;K9;*qmA_-h"\smg(o+U&Ak<d(/>_7l-Sj".E@K4\Wp%M[b.08XF\VT,!9P%5)M
.NbMER859uPZog;uA)S9@c\L*E]A:Ikh\9Xl=l4AtoCa%i`g.;Cr$R"gta=a=i8?2go-OV(t+
4DQ0L\-JYRRAJ&[ZS[4j9[dZ<;#8<.\Y+C,Zl&L-8,9BmjF6JBHj/4LXhg$3Gi)+e"$9t`2/
t6R6LMHKC]AgF;e3/r+9BnU_;RI+aOb>&_Ma>9N3`(-3;/&lJD3rBHp>JGcD!kW!E6bXiB60$
`H@CdO3e"Lg"p1(^K0JA&d!)&%($FL+"nk.XXT4I^B7'2J1X"pGY]AA[7Ba9'G-moj,ei]ARZ_
qmH[Y<(I$.P<`g"/\&7]AMVUGn*`;@Bl72VF_&]A6a;`PXA'q(IqH4(h(`ogRPej6N5M7WU99W
Jn)R8n0?>".)/;&_MD=L"Ju5+30q^o!,JhfHB<IG>2;8\<r_.6Kd#\aCQ<kr.ku14X`H\9K3
+N'f60@Oe77h=sGe@6j'b-Q6,Wr94ntOVuqukh/k"h^->stu]ARp5'4NKdIH)>7RF`nKXQ!>R
h=%4P*<mGY#k\c@qa5']A49Qk[I1]AoKBoBX\XE!q6PE7Tm*.5_?<9asi6ONn\no4J(:@hETOa
B=t@6RO<ZK'E8+b4TOS_h?LBF!.8&aj$_X7\guZ<3B-g$[r!$eB7TPPX0C$3@1R_+^:*+MqQ
\3T>IQE)^)hUE,r=t9j;(u<!&J>UggDNF/'!,>(pfTu`oe%qY'o.WJXH6C=4CgTHB<;N-'Sa
2E3V\df,j--5L3ukRe&\hFJa3Y^::cB8l<uEbT^JZW_F<6(/:@_dgof$[5BS?1OD$T&Om1V!
]A?YW-o"9#oiu@sBkq4CWR,Zu:&ZAYXOou%RD1-O82&[9b?5(C.0p-9Y1DfKo`W-,Z5Y_84*&
NP[qoS*+4`k'<<8c_k1AXn.Q%\t.GoH)]A[9)YMmtf-[PQER>4p=<`B`$IaM2oMjF+\RC@eK+
iH6JYA`0D``8UZ`NCmHA81J=Y'U(jV,bbupJ)=ul(@oI3?VkD0CV)[^..SXA&^(b3KqYT+($
Ek%mcU/O"QU4:JA^)75a+B0k5,0W3Z%o8%6GYY-M+a.Ud)c(buYN]AG`bmKXfO3Jap86mek_^
G<5!b#>F8]A4BRDRd0l[2QS:imTC<P:[@"L%,Q*S^k*=K/,U`AdR.+StcgnWU>d5ks4>6=uCU
<hl1V/=c0+*7]Ao$0XZ@*M9p0>L@7#Jhi>ZG"\KIX!Kh+?3k"3<tl=_n3_5R.AAGIL,_*@5$Y
$/6$[rLkU\;j1#CbGOoU%,ci=0P[?5>"=qd*:2cK);J5@<o$X4mHO;bNZLUt!tQb\,(#oT"r
p#0E4`e8Bl\"g#*[\?o-KXa[*W2*kGT=Zb4'.4l,ndZ>@/?3D0MNI+:6`2]A$2o`#f"=<+]Alb
V(>*j)l,m_S4k]A?<@A=?.l;6DS`6WdH)e:=A3X>E2MP#3;0b+#+GYg(+M@+\aKP7Q!ema$d#
6k\Mk`&)3%5(;Db]A`DFTmc',B"bkppWFVY")>rkOaR[?L57#mEH<B2B+j[aIf_=:$ER3J"G)
.*Hc,1kN`,"5.FD,ID)raO;!`spLV7-i%%50OI,4]Am/PC9C_M7Uc/M:[]A9>[mf'i]A[qMLkik
m@*;,u2ZZlr('tXJ=[MkY&-jtC"Uc[/;dPJcA`tt'(@R<a8!uc\-3o2@O>YXmWZ<BSUOH2`Z
=Q:*:dVSME7dMX`Xc<,g*D<>F6nce,+mTS7LSjg+o/PTJi$W@2bdnI`<ua0A5PAT_5X4U(mo
ZqQC[u*'*k&l[D/r3l-=7=u1=BTeW*^$[<FZKKb>#"$(n9P2$ZfY,44&9$%%l1\JV]ATATFRO
sT/G%IcXNs#qL]A)GTc>eCY7V3(r+O>QVno?iQKGsdEEJKs5fmbHZ%-pPLa,pg7Pg7KlBt?]AK
^FuckS2%be*Z`PC6'&XYg%e%J00%ABC*a/WZB0SV=0hb:F%tL&jWHj!UU3;Yq`qeWs'Nt#PE
3Lp&NWs&Oku*6t3i;(B\5%6'?d*0Rl5$RL2SN]AIq)WO#I;#r^8d$W(P%akS*JGTKbL_f,4mt
7\ProJjTfYA`-+T/Xif,Dp=<CR9-tTfseT2UJ7?*8(Y"IC&b*-oe!t_F<.hiN'BY)8D*IMU_
qp'VqNP+o@%Bkr6b_HCS61HHE:!<W>S;bUpX*nE(GW`XgMa>?B0kK@SUEqp#Q;`<OoB9>R]A.
@JYoaA"TsEY97GRh:Vo40#>LZ%*,:*,e_eCcgZK?CkfU0FHU*VhR'0#mhram8$h#ieo(/;g_
maL@P=n'j1L?8fZNULE7ABi/I=YZS4u6jfQIM_7eR>oF\TZ$YCiA2l((.0nNiH?kTMJp.<-q
GR98?4>N6&1ZiaEJ,3u_USDJu]A)Vh,umf1J@@d3GAt@=md-!,:s`cg&!RS0:;u,l031bWS&*
H+$kbWo`t'4to0FbssP$0VhDmWmTIaEmuOKD;r>\KMD64CRZ,5TNC=2kp"8U??<ZJ0V_Tba5
9&8gtnnBgD?COgD,&0bQPutQ,`J)#Ht]A)Br288_kSb+ArFd\O-[N?aM#F0ie/IRXAG.,He[&
!V8=&2jXXJ"0#R=.%1JjWhJH7`0>uG]A4c8d?U3RCI$,%8N2S5plDS%nkCa_ZRd55%gYOGPu`
bi/86BWl!R5]A?r9*DQo.llADPI$\_YABY:U#3#X1*f.LP4CTi`Q38h_5PA<k`X=jLbotqBO7
juT2lB8BmCZuD?f#HlIE?3UJI-AZ'RR&RlhM4Y7%RO)gB2r)Ai>V,A)7pkN)0h0Ru3-1UqA6
8U.h'Hu65IV$(LlDq+,5WQX2sG-n;X/W23JRF7biirPP1r'&j;?B1E5%mU>?gp8IRQ[-Z\^>
o.$)kM)5d]A=1,&X>cTq,?_$m;:]A>Z\%S!>g/73q4lgHG>=5n#2,)t*'#MZrRfs&KhPBa;+LE
p^UELJD:p:1E)Y3E`X4grN'+&FVO4Sa)s!0WmR*!H#UFpPA@&`Z"EYr@f502O/gtgm*hG$Lq
I>l]A$SuC?hWFXBA]A19b>0^X!ki'ZSK*oqo\l=#X7;j3<^DSD`NU6:Y`GpmDdeCF*Jqso-[l5
05Co!^DNZ]AB=$;"FNBQ.]A7PA-M\2lRSg8fSRi'G,aW$=TRn<tEtl=@K.*ltB6T_FVU;+i1HB
'1Lc,q8Hq-5C/-+iC0H:!u2,%<km6a:-LG4a5sqE$k,n_S4a=u52"RQA>uF+$gRqg$>VR17?
Fq6&YU2`:%LEI3r*/-5d#0YB2*j21<\I@*rDE+>,lc0>7/%_g&F="aA\t+kY+c9ce_3Dq970
P'i^(Oa]A*n<[#-(&76qISX"q8#^IuHd;3`092nb[`TEC+ZO%rZ]Amg8*/!i665>^g<n]A$j<4m
(D#e,Sc`ta_-rp8c@(D@JV%g]ASo/iaH;R3kLlZP4ti]AS^ik]AA]A#R<]A60^K?Cj8A1k;"ioh'?
*``;r]A]Apge'N:l*)IY/8LfnYbN)Xmpd]A@:&Hil_gP9B6/t@WGcH@AlA?F0%Jki6CBSpl8>`<
<Fe>Hm,+A'rPGtq_F,B-]A,0gM@B)o-8NB%Rg2=/43.F?IIp,X&>7bB&oI*UI>:;UJ@2[X0=W
DgLbHof@*O;P))PX7*e5?om*qAri&rC-E0[RJ$m]AY;Ob&ieAXTR[2cDDX%0UR'Y@E\7h3rjN
=]AF%iJbQ[B0hE"mkiWAW72[O_c\2(%tUnHp3jVX(nJ1&$Ud.^)sp8juie2l>phU-.a(4;,#K
ntkCAD2aX5^'1'euWpj8#Q(63ipjk>7&H>Y^\PtUjJ-Y-o6*Da9EarH_"3[9K3@2UF>F`%ps
80WB3R>RF2+9!<.G(3UBEIr9k-14.n.-Yfk&2c&rb5(XIukT!3cG,YRQO@,,'&Qe0n&b#=!@
lIIS.\_PbR`Rd*W0lq&rfIG&tPCca.Qcd)_V8_)FJd/udpF`KNO2Vl.E+`(t&h1)`Es^mSk"
Aot*C1Z#\Wb7U_e/uR=n>=NKVZRR`4P/'EE07i=)(.-"^p13\c*+h$,eG]AR)2V,?lMUI<;&&
^4?h6)qWIIZMSSD/mG"s.&(U'PYNL[9F_hQ+r3M:]ANR01K-N_P.1M14B;RBnP&Qp_R5Dm(iV
HDkqdj>"$!*^P3pR1U\jrej.@&hciQB(lfLU0Oo/YuGCIo$b,;J0^%%Ql[rj\Qu@RnKtI\Zr
QR96FD1@SJs[;tM`,^?R4_UV&q%A;@X>#:#**d%$dCM$^o#/PROWi693c3#!jgRPeI\k"lC\
@Zc.t,Xlll>K@sMj[=$>q<"[E%WA>/5+jD:G:Jo/.h/fH0=))C(IE:j71;J[\A;Gheno^<)7
);B?_dUM`0m=o;@P3"IeTjW&E,.=qRMd4JE76m!Ch76Z&mtI6Wf4!bsIEX.c_<>ULMGVY/N=
2o,]A6Cgtk\=M)F-Igo_K`LWt!mPM9OJ$bo+ROKW"kh`iMF&"ruP-YtqqImZf4TbbYp3g-%/4
$PSQ0htnd^->]AF`i)HD:bcRLhrG'-RL8_b*38+@1j^r%iEXoj,K4W.@8hpW)lZmCkV&>[i:>
bq<'l85jX9.XpO0$,kT<9^=j&"3%N8P<#qHocg-HtK#0[7mqfZ5WhR5Z&(&+blE8Eip$;Hfc
e#1ocI7o$%XMan'8#CsF)$_*7rp)pUE+lgBiG^pPI&ukTETD`pRJc/o_MMB)E:qamRq4Zjr>
mg\]AHU,2_hm=%]ArPD5/dboj\%$MnntS8WW/o4L.+t.#Lk\+>':opo>u>55b8rh[geUtofRh:
?g`F]A0OdL;rmJEJ(F\S,pHgbpL7j[-l[h%20B*7Z5q>4n0>B&#/*i91o0eBTLa`dnAZm?eDS
!WTL@a"rrLGB&RB>X1;eN6Xj@cJFs><0%7\-d]Anp%!a5(6-(4W[;K_;1Y(..;1CYR'X&kGTU
8IH_m=E"$`#*7Nr^<YYAIr+ao6<iG(259MWf(?\q>*5ZOOflk\_m^4SipQ%H-+YQDU`]A_jSa
TP6,VGqZT+P(Uat+U$X\OJ!<V7[0a%!q9C%+,_N4I%a+Hi/G7,ha!uofPm),?t2.!V&Xra**
tqYTfsA7mKL?aD]A>Sa%$qcVG[<>nbVf"@=pI.Y#5qdQYN(qn?s]AlePA7,7mK&WM]AAtEmH_[[
Q9ZrH@Qg$AXl1cmP5YU0KdX<BMc%4*cd'4K2$+E+n6gF*8g<DUcI6j'XUu;mfX1,GlOrX@a;
FoB%8TL=XYlIaN\2R^?e29WhBod6V!,tSjEYDHp"P#GKQ^#H-.q<e>)6[`77sE[%HmPV*!ki
O\(991U^4=&pCc1W#f5ZNC/2/-DnXP)X5hIhVX^eR;DR.KW@c?d_^WWF&jTt2f-i.!5a'(_&
ni?M<dciKdNs+n/@B.F@HbFgA.??@[D)Vu%PmRC\8[k\5&oLWe;\k?Poi]ArTN3#.M[d"I$;)
\ePM(b'tTgeVT(3;=@l=q&*p`<G7!UQ7Z;e@me3F^/e5+aaKS;jM`VU-;C.4=&=f#h%)q@Zu
3+.DsYdj?RbA"2321Hd3^\hK3*.jBnET%PkWo39kuSMheGrgkn^l-C&QE>jIde>`B&ArX7<)
COYRErh7&fj)tQgX/kB$*YH4Ib#htFI'jYHB3e#8R?,t9,@^V4>&flM)[?h;UX,fYGuf0C6B
Gh9(U]A7lZ+'RjNq8+<%rC"C@pZ<XFUD\7]AM#J6-E"SHQe9u:h&Th2!u_*d"9SF!DA67[g/2!
:O6G")ak.q6SW]A4!od02^urPHeDFjL"l8FiQd.Y/mN7b-TaALcI5MLUf>"?^20LquG-![:Al
T4H8k:+4>>:A`75XP'/fJ%E'_YkTAII!uW@7E7G[0B@_Ph>d*:=Xj8RdQucH63)45VFHj;X>
sE.3>n@`pN\_QC?o,#;Bn]AO[F0WVj#T^h#Bm6"25ho=\Q5"E;-4U=mSn^V!.ns.pP3(_8['@
:li(`TY@Ll_DQb1<hU5[@&0s#E:O9"6gY-7cO@MY0M(uRf+&@;<[`=f6q;h%E<2nFV)$>G*\
^GCJp>jA/jA)XV0[R-FALTi4#^sB=c^fnM4a4gAN=cCf=k;R1r*.rrh>=)?D)A?5J`ok59pH
)7i^F9QM'>UZ:5E2H>E.eb-2UXJfOR2Y`#A-n94p0U+p0d)L-bDV#+Vj'1WqQcCkK5Ac%F)\
0HDK$$OspU?!Sm&=/+H5@Nr>i".^``1>*;bHGsguT3"d<ZL0HZ<kH/Y`]A+nuNr5HBf=$<G/U
t3+aMcLdmYGhAc*u7]AB1HomA89oQp<O7ok]A7-Qjj[`d?)N9j`+6.#:>?#ubR:&0mH0CjL`,s
2,$l=k/uTT<pCo.0i5%WfD"o&MLpQ:moF`8Zd`nfiOU7\IF8sIStqWG'J?XJZkO&_X$X4>4:
e><Dr'':'@E8)*G(UJl*!hBLJ,$B>>*Lku(8i4g4)j-`]A_jC,^6t/c1fE;T;V"G'3p&[+Tjj
IZf/#9e!ndc66KM1.3=h$qi@E#l("Mg"sPQm@,7_P*R4K`S23>q9:\p:C/$BpsFNQ_!s`J>s
sslA38roAaR4B7t#*bs$._EFG!T'KhKY&;co?"pOfSdhqL91lqBUoHmWCgX-H!6A0#IoniG6
l'\s=g(q_>*N4Mt9PhOup-N?6[(sAb6't"_t5aQqW^o:jAQ/Ig&auZ@IY`'eDf^^GgpCV+qV
WUSd6a^dJ/VK$0r'A>Ib)IYe%\;UoT:e\nAte;*#U"dLC^@iFlH'e3mCSkjXXdAH\uA<1*-j
A1[sB#g?@:iCHNVF\L\p3u"_Kaj<21mP3*3ph:#,[7_5=@^Ed-Fi#-ju)IBKHH]ABmL9Mhs9b
KPdIrgJtOH>=,V')hZK6LQ`$%`eM!o-\*^oI_nJNWQLK*2'.'Fr/pmWl(BfJkTpqmZ"4I:@.
N/S%`^jf1<+X;VV\MU>DfVC2+F]Ai6uat.6g6s>Uf)M8,M%(;o!#eiFRKMDie$@1*h0OmnK;K
4=NVfASHN[ck%-0EM_%QN`>XN+UiVMi%:'K"EGbP_P@b,p0tQ7X?p`n`[,-GS'DmMC"D=4hK
(E$%I3^0Fq@1'6C0A^DP5QqgHiEW%/lhI)B(VkhdP#*i.ID*V^\m)<=IcjjWSAV[Y'iPN)OW
"oeE#T(e^4Ul,+TfM@97En`i_*5NMCGPZ>5'>O)g%QW$YY/lt^KbKD$HiGq`HTBmHs;pLBAY
r.hhQE#l0Ri[1=I^1]Ab1kTtdW#aA-"Xb_meWoKmDnZ>#t'Ncr.'TDdR-l9esiFj>3GR+$8;`
cErV>8E3Wt\"Rl@p"8*;rFh>\+RWr)%ecYAQp]AojbSmg-G6Ka9P+EZ]AehtKTQ/:2g<t\Q@*[
:H5b5ngA'g]Aa&hEh.>r'gIUm;uNLq;AGiM"(CWqHd\_`>E9SC+VN7_SA#j+kk3-q>%*-0Jnd
q5>8UbM``fA5C9&[#%fmBRKV#WdB&,8#-)Z1_'l&>#n,B2_V`rWQ3@Ck3_86bSHeO-D[P-Ug
BgcEGJ5!8]AiVU1=<DBC/t[<K"Ft=54d#k:0ZUZHSh!$Y-aj;2_ojU<fT"MR"%$(PV>WZDsQM
)q;Xkq17NLFQDHYV(C9colJ]A:LpTb<'nm>WZ!]A@YetJd,?T[+I_,F;=,bu#B!CpWhUoUS44O
E#5\Bu)N*09oD00Rgrk>kj\hphrBMclEQ!5D0D[OX2N*8qj\0,O@7W>NtpP1!a,mpUTaNk>S
5]Aulk()>HV-#=XYZG$"N$9N*/^k=\Q.hm0.&Z\cTWY:@5MA+!4Y=PhfHXNJ*ND6ou(;rR(LK
q2,4l.k5i1)/n.`Z20)btC`ok!e;-;A"2W@Q2Ob3K*PA6+M^MI,.NVh:QZTG"'SOb%u+r/oQ
&[p[U-ZYI<nB)#9DiLdir;+!)q#&]Ag0l@UW\c+M3sGk+teprhaM.3I.$:Al]A=^#a9X4HA*!:
"qu+\Wp$[Cikj7PF74S7XNR+_*OnFe\:Z$Nfp+H]A\X5VL<6f8#/03Ekasu^++Uj?VWdhh?,M
k'[Tdm;WFiOmJEKiml*d#5q;sfOi1Tf,FFXc0XCSMBd9W]Ar!!!7Z2]A8F^tpm9C4gBH09<u%+
2gq]Am$HI/:[<N#e)oQ%&@j[`Bb/+g`#lb?je+\t)#X2\Qi^e:T<XG/b03ltQ";dF@2[NMX2L
"o_@GWoOp"V\=+_Y2Z7V")Q*Sr@Cbs%6KEhk(g&]AM>%E?C5p<l9.E<e!i>ApE(k^GFme]A^)C
e2(Of[:8@%6`'aNl^g?olIqdPH[8%=)5)LR1ch,pdc5;5?VQLME/_,M_0IZl@3n60Wo-+B,E
6Fs*@j*5&DW.1T3NB)n7KGU:,%hlHu;D]A!lV?!$;(79:^q%LqtO7#1ma`0lCOt_P&@>D%;ks
h+5k@^:,9jr7P*kHdua0^;04lJ$4#L[5\K6h*_Ch/a^OjcSp<a/?qGG]AKHOE*KKTVN6b5`R0
Bnc`kh0RmU+X_![d%GRP$K=On/PeN;"$;pG$*gdM!-=q4Jqai7H6%Xe(iH<%f]A-"+aM<d)MA
<VD%7&3V;j!pb+X`VPK4#Tu1,XJFR^arVHTN&Z7jfcVF'Yjb(K!^=UnD>'jRg;PMY1>MoPZV
i6Ij6g^qagGUL[,C"!R`=l@$b]A+qK.u[<N"B?85h':#':lH.M[dP.qCpRouEaVJQ79F\hp?n
6YI7EMgV1c?3lNY2V"r3,b`/QOX(tWk.MgP&q`V3`?P`LrER]Afl^jU!@&?EKHmA7CYc((>cY
6-Us3-fTD2ZH^*@5`3b6[+Y8DmjBR]AlWH7Jo=U_R)L,lTe<$\;igq,W$f">,/kdEoL^=N2K9
p#Q*V5rd8LS'OGG:?1kl2\HC?"nU;d$.*K4Z"?,!B[>\hN%d$dM#r.Q2]AnO*S_WX@X`.1_LT
&GSL!rcA^7)]A$tJ">Rt(6=+D*s>IMK@Tj&fQTk5LIl/TSS4.]Ai0qm.%<8<h[<Af"L)3]AdE8;
3L$(h4\WKS_*3aYj>rh#abB$QS2,:4cbSD+T.YG8R#8_`/2qID[VDjda_[f1R"PkO0=S49\&
m);<srR&nY^B3tA3noV^JlKU#nFVgr,N6GU0O%8WG?q*@E5ujc0)'ph,LsZa-Sd#IF_&o1R-
6uqrY?#.9\J\7]A6bE?c@^i7h=2+m[3:i/3AA5:FlX'5n>TGj+cSGAfaqQ_mm[Hu)aY+t,B64
MmmRp2E!D*e250j'P5a/N[qncP[X$(!$kA1p7JRmU`uUX4KKMY+qk3uhdL>pN/)`!#^6cn0<
(&o\5L'd$^EAa7]A%m0`Dn,+%UL-4K?[i<TLepiVIl_PGji`>$J)Os')D'q*hl<kt_:_ja1Bf
,sN:"0IJ6o\MQ*"EEhT9J"or14fhYqO8bD>s?K/8Qi$2bZf-Go3F*<5+40]AA=p:X1RZs,tLc
n^R.r*8\&DqaqLVc0PSfZ!UH%o,AIs7p^6jLpLdh1n%eJq[bcu6XaJSH#C4NkC"YN"0>jM+=
H'OogO5Y)lBlobPe:qPBS_\N7[>'hD?W0mQ'm$oVLEes*K,.pQu(fE;8[[H^Z$XRlS`UFEZ5
.I#a\E\QS^L6kY8\6)S[3(>O@lO1+DNM7VqOfCo(Qai@m!\@k9ipWb\5Ko"uXSUQ=A;&NSrS
IRrs!;mm^#SRA$P946PDft_ljiF;[2fXdb\@J0!`dWN'QUrKA4pB&X$^,Q`O<C:94mkQJb)q
>'b5D&q'CS@DI^.2coFA#=)#$^rX>1HuDknrC%_1@Js(-@oo=#A*nW+/rr[mm8b?SR.Xa`D0
meD3dSEZfR=2h@6(nWu81Fm6ZMe%R[4)<Y3\XPDkF/`j81nZ>qeWV\\CjI/L>C/HN?)7DK8`
%eJF3[S5*^@kekQjs2g<+L8k=;EIYT%$p5BfDc=3TEE<:t$*3G&W'm!NV$B"H'55/e7m;Psm
j%0:]A2`--cG(lFP5*?^'dr`]AZoggn<0h#j]Ap(/_#SB(>H@,EG2^;bsj.VOGeCINKbB%]As*Wi
;\e$:B&=/g-F9Y@jHGTJV[OcK]A>6_m$#sS^Ug@m4J"#2As;TIRFC(XKt!+mnL<r%pS*muB+U
28A[g>dGK`DiIVbpUmn/F'/F7O9XQh_I_8!ekRbk@\+B>tg5eWUB5(!3AM>Qa1LT/E)PCD!1
*aA:t2sfQ#Hhop$K2j.:Q]AO[h3'It<]A>3:V@<BP/X*l:@%c;EL&;2;=b?\2&kt<X-So]AYq-[
r_m@b4gpEKbZcp6&1k0]A.B&@/klW\J82uaC>/_gWSC5-?!hHpf`-V]A:8.F(:c'"4$);;0IEK
bVtcWCSd)&fVCcE]A51.Z[:>7<cm*XD-\kN7dFNa@t+.N59U%TQtRmP;qF**[/+3p;/q/sg"n
J@>qgm*sU'Dn&fGUWmf"St4J.qsR)*-SoA15N3TaUd3\Wj7lIJSF)m?0qaL5>$&#itUKV_e8
D7s4,5c>)ierRUkem5)q3"F^*S^rB>PtDF>KUH7'JfBVRY0,4d8*GX!pmMWHb.<!`amE!*$c
o;U;5\+qW,fL%<>,-)$L5[7(b*h'O'9*qc\UC/ujj64Lt>SV_bA0$1J',@1]A<nU;'qX_A?]A_
@(=qKG7/h2(&X30!k\9KQH)F@QL@O1:J00g8!#^u;3),f7uS]A8@3`h)/8ZY.&tMe)/(lK=sY
&mMH>sdbX/MiO5qW'$Ss'DO8)eqos5!8+l^CT!Fa`R)S]Aa6V)lW&p$\5e(k'O"b6QC]A8K%*!
+,?U;Vb\CPWn"[B=\1k=js&j@hE_2e(2_2WV*"!3BXE,X8X46?MJNJkiiL6n2BuS>Q6W7MO[
8:B)6ir2u,PWNc5cp[V:Z%/\'$a@Wr78[Qi"je`+"BSJ$l<&\ihLY5@ZVX9TW!S(l%s<k?C)
+YLila2Ob.:R4'r`%pEc-^CPA:Lj'o^67pC<#Uf[*OH+m<]A<)]AVia_uH/V#-kbS4B3K<X+BO
O(&K%he/L/RQadgG>(&BPu"+QeD:SorZZW]AS!%3CeXV+4h_kmX0Ho%:PFJh;:]A9miALtT+4'
?>O,m&`_N-mSFDY".G]A]A2H7L&'8[S!CEHbcH-s++2D7S6EEA$lt^%<D&SBC3E0WDMG-KOU]A:
-CdA0<;>reifF*$9(O`_LEPD\2in?/ZkI7Ck(ER)k3^,E+lE1>49c'iu2*q_g9>I&6Jcq)^a
?l]AJkM'r8q_IqJF\^6n"s2%):_4ROYAQ,e)g(RhkMPj(#(Yq6<D.3fm(D1Ce&(%`"Rh!/RPF
E'p.+!Vhg1?CJK<buOoV*W"U@i:EQGT+[(:CR_n`N0*Mh?uNif]AoM*DJ49h8OncPJ5Mt!bht
;+YB-h.kjhHX:F;!!jp'09d#sguP7%V$5:f(0Be1gi0lGqWs8KU's[/RaPUT<(GmYs!h@>2S
S0q5:nDkVUJ365nXZ02MOf0+?:;TWgY4.O<'HsO:hgE[U9VAk&MLo0<N`b>XKPWd3`=d8jMs
*.Cg<BS1pZSm"*gJr/<J,4Wp~
]]></IM>
<ReportFitAttr fitStateInPC="2" fitFont="false"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="36" width="946" height="213"/>
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
<![CDATA[="  "+"應收賬款統計表"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-13421773"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="946" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[利润明细表]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="88"/>
<border style="1" color="-723724"/>
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
<BoundsAttr x="0" y="51" width="946" height="249"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[報表日期：2016年5月      當前層級/總層級：第二級/共二級]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="4" autoline="true"/>
<FRFont name="Microsoft YaHei UI" style="0" size="80"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="472" y="0" width="474" height="51"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  "+$dept+"應收賬款分析"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Microsoft YaHei UI" style="0" size="112" foreground="-13421773"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="472" height="51"/>
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
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\"  \"+if($kind=0,\"各事業部近12個月應收款變化趨勢\",$kind+\"近12個月應收款變化趨勢\")]]></O>
<FRFont name="微软雅黑" style="0" size="80" foreground="-13421773"/>
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
<Plot class="com.fr.plugin.chart.line.VanChartLinePlot">
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="1" isCustom="false"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrLine">
<VanAttrLine>
<Attr lineWidth="2" lineStyle="0" nullValueBreak="true"/>
</VanAttrLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundFilledMarker" radius="4.5" width="30.0" height="30.0"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-11420997"/>
<OColor colvalue="-8598298"/>
<OColor colvalue="-5860413"/>
<OColor colvalue="-82082"/>
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
<newLineColor lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
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
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-10066330"/>
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
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="項目" valueName="應收款" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Multi1]]></Name>
</TableData>
<CategoryName value="日期"/>
</OneValueCDDefinition>
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
<BoundsAttr x="0" y="36" width="946" height="210"/>
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
<![CDATA[="  "+if($kind=0,"各事業部近12個月應收款變化趨勢",$kind+"近12個月應收款變化趨勢")]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-13421773"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="946" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($bb=0,"各事业部近12个月应收款变化趋势",$bb+"近12个月应收款变化趋势")]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="96"/>
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
<Plot class="com.fr.plugin.chart.line.VanChartLinePlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-855317"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-8355712"/>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="1" isCustom="false"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrLine">
<VanAttrLine>
<Attr lineWidth="5" lineStyle="0" nullValueBreak="true"/>
</VanAttrLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundFilledMarker" radius="4.5" width="30.0" height="30.0"/>
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
<Attr position="1" visible="true"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="项目" valueName="应收款" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Multi1]]></Name>
</TableData>
<CategoryName value="日期"/>
</OneValueCDDefinition>
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
</body>
</InnerWidget>
<BoundsAttr x="0" y="300" width="946" height="246"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="label0"/>
<Widget widgetName="label1"/>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="946" height="546"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="938b9d2d-c49c-4c68-88a5-754af02ede33"/>
</TemplateIdAttMark>
</Form>
