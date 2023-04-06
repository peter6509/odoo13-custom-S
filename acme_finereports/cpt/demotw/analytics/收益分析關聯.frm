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
<![CDATA[SELECT * FROM `get`]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[select type,ROUND((金額/純收入)*100,2) as 百分比 from
(SELECT type,sum(sum) as 金額 FROM `get`
where type='${type}' 
AND country='China' and year1='2004' and cate='現實' group by type) a,
(select sum(sum) as 純收入 from `get` where type='純收入' and year1='2004'
AND cate='現實'  and country='China') b]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds3" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `get`
where type='${type}'
AND country='China'and cate='現實']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds4" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `get`
where type='${type}'
AND country='China' and cate='目標']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<ReportFitAttr fitStateInPC="0" fitFont="false"/>
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
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-526085"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-526085"/>
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
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
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
<![CDATA[1333500,1409700,1368000,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[5295900,3200400,2438400,2057400,1028700,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="5" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  "+"標準收益綜述"]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[ABC公司（單位 千$）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="2">
<O>
<![CDATA[2014年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" cs="2" s="3">
<O>
<![CDATA[變化率]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="type"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="动态参数1">
<JavaScript class="com.fr.js.ParameterJavaScript">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=$$$]]></Attributes>
</O>
</Parameter>
</Parameters>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
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
<Background name="ColorBackground" color="-1049860"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2004]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q1]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[現實]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2005]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q1]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[現實]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="3" r="2" s="6">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=(C3 - B3) / B3]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="4" r="2" s="7">
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
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
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
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
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 >= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↑]]></O>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-8994464"/>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 < 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-23707"/>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↓]]></O>
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
<FRFont name="微软雅黑" style="0" size="80" foreground="-12961222"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="13">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="13">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-13722160" underline="1"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-10066330"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.0%]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-10066330"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.0%]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<a+\;ePqb*G1sS"*?TQ)F-hTrTm3H,m=lK8D7hG-u,WUMBX=C(+:Arllf$(2/-hXD(Qri8Z
Q<"KNK!mZ5h%b;%THiLb)++#U)H(+=l-j0/tbi,+Q1r^1h6Zd,Q3QOS?EBrSGkK5L5hFrkA&
B[maV]AS=H,)2Z@Rl]A1u,HTTdiCI%PS%r.]A>lP2YI9q>A8*DnME@VNUG`r8:&L+qaTfkc]AHqe
c)0D'TV>EN]A;$Wd,=?bf"6EK4BL/riH"Y/SK=u<J,d@:Qf#Qlo:2-di[j(qWUJHQ_l+?,)V,
cai)ZWB]AXoXI+Q1T+;9.OuGGer#R+=rg%+6l3>t`r*h,Ur8%iV6HC"q<,q8.?7co77sb0$!D
^HD.mHcFsP$DH^1mL&Gm?1sCWhG*XBD)%q8AEXj7VYHkJ#k@>gRLMIUG\"q%WcsE$aJsBabm
uthd/+/oSoXQ96u7-TI+Aph&:]Aa&o?afKH)^JR4,b@ZqO,Znmb#2:A%*KsaD6T;ESY9D2T32
JX$NM(2_]A%.W:K+AKVVZR,i+U'dD%n)i0=Jnje97)%m>b&0]AY&HRmu+o6q^#/J^pUa'f<C:;
+'n6UJR5q2i&]AB5<OF><,/+,;Q;!OV:\niq4S[.?=\<DX[AJ'oCB<2n"+m(*7H'igZH1d,bo
QHCJS$Pc0mSg[R/!O1`s<A.$cK(X-c6F:b.U[F1V!MiAg6A@0iO<\06ktYirQaMM=0Vkf?,O
e_4/^=^0N8^2:5(ZLXPQN1Ckg=L.#c/[c-PT%Ic4AYIrAfWs@lU!(F3,nmaXlACB,PV#4+mk
S\5IYEMqXRNocaN>IZ0;<!4m/X0C/`L]ACA=jAnhq;I<>_k#l0;<:R!36[:";PE*W0nhm")="
'H6[lEUi6EkY:f*qFs6+cnBL?\+`6UUQYcQNgQl9NB!F;":2GeF/CX?`lTVq;[?nmQr-[r!R
j_,)8K567ltB!6C%BPtYOju0chF6UH4&pR;3'TuG*P/O[^HN/LcX.B0?:0]Ao%Kr\Zt+!VCr7
@3YS5Z5*_^H!)p0qf!R/5oBIdef.,9`!#XHaQiqMMe@r$KOa(4q9H+1XF'Efi@2Hh,D::R]AL
__s<sn7'DW3_YlMhBZWTS-_!;k-Q&Cncq$^DHi&Al?Z5K^cg,t/&(hLZE15#0,:#am"\V1`j
mcq]A6N:8$Tb@:Pj^InWgQ$mL1&uPBIXMHGUnuarFIicf5]An!2Yp\#,)Tg^lLVJ![1VM)$dJ-
Co=(%o4/&\C2R/Qf/7I9_EHT'gD<Bq<fjZ?dCeO6ml=D#EC3mKKj,OSY06$8SFT?"8WEqtQm
tPF*e"-@nn/mAbNA6M<'oLmo/FK/1bI`P+;(lIdIeuujMc%05ep0Ygrj*"=U]A`gPG_'P+_do
_+dA)<oSX*()er"(!a8+`fs1Ob"fSC<.&?o:\N_uLI2;4qn?"jB^1?u5q@ZQLb8N,tu@P'VK
btb[R&ZC43_`ELFNBa2h1/_ffgQ:qCTZ35#Ea5Y=,1rZ3:s_DaEp;j!UY>;&Fu1NiV>F<jY=
>Hr.h3Y[;.+H]A_YTVINVPD@%P9&6ja%RJ9rG["?Lj5nX]AXXEQ%kNLPX_3_X%s_?CCM&2I6Ue
'oQR>d&pt#:Zg9gpS)Plg03!Akd0X[a!4d$8Q87O0_X"%WZO2%h"c]AP[>WMTlGnlX%35]A&]Ac
ssm!7&&l53JN-"RC^oO2'ep$Z&Eg8EWlrlVF\3mRB>Z$QZN<6QE+W$[4U=a-%@d:/f2.6;Qu
)_Z??EBHiucIiOr4+QJH\/)VmVD+(@M2e)rSTj#TO`\r;*9-@?d`PN._7-m]AXoCVTm1$Yh2?
:unZbrIs/s1VYKJ.A#[U4uSO#G;)O2iQ#rt7;K\o^3kR\e>hbLZ"o?)'EGH5-,b%+aX,Z_8C
le#%]A\\mPYA35es^_2AIem``DAH1od\%/J(`nY@eE95mP67k[Jgc"$kG)RfGMGMo=IISWPcQ
g0;;\U/i#hDQZ+K?C[p@33ZrFS-"A(u(8DCfb)l<UiEDF&rC]AU=QCMkkpsL:#db9FjEd"-j1
93k+!6:1.fB(Fh_Qi)j_H_Fi'HN.VkBP'N%"Zc.-Al>'iDctM5Wb?1L%+9%2H4?k0JUJ&JpP
kCiTC+@0SA\&B.sVHdT'YE\nP-9HurYK4m=$dj>`@s/$mAH6V1T+lV,Im?tGNX7;%7INqstc
#%o]A7a[o8-3V1=j[TP/S[;5';Hg6G7dk\%GX?qlnH_%8Y0WI&pqVi2TWNOZpnnHlV4'9g?09
V_Ykd]A,e^$46ZCr]A[_1!AI9Mu4FMlY8U4ik/Utiu4Ad^p97/%^@4&BaH".-<5s&i^[DPUW9O
5ZjM@Yf_,J;Mmh>;S<BFul;.epgdMueYl4DIL4&RKKWp94]A05gUhB88W`_\?]A1F\n3=nI.J;
g3[ZDA/aLUmF93!IhL"6"0;4,aBgYW3EqAT2q:7SY5N7mZ0/<_@*:_C&+NfT]Adn&\/$0B:c$
$JLlr.Eq]A]AhQ$KYZ0<ZV'cD_f^gO:2FXAhesNYH.7+-n7-X;uQJg^<Wr>fH$489l#2'\;290
"R@^h.MRBJ*nG8]Ap9`Ff'i]AbNNMs'(F8A><?q`LUQu[,'\&)UMbSD*oI3,$blD$9KMC4hCO]A
1rIn*0`0GO@(^bD`c!h.??4C0C'XV1ed1/HIH>r4tbH.QYuAKk^DjjfH1fg2Z#5F67u;V554
]ACpLY"4pKZoWgC2W:*geV2p_D$IGk]AG#m[0th/'-Y=W)4aYoTGm%>6!lfD_?J_TA1uiGNqX>
<!"g%KR?Wrp_]Al=n[6Q$Kqsb,ku8+F@u+VqAKF"DWtY:lD*$K('XdXYfSNjTkHP%Fj+$)lf,
tc/"UJiWsZ)>/Bd")6<aU#S#W]Ad!;iF-9'SF1RRZRCj@(=&Xgl`Ah]A[O>DN-RcIeF&<CdESV
q;)8@BagVsrmt7Z%*GEm3<JPI3_bBs_J.&-4WIY?II)#+A?%]Ala9M"F!^T4(NM_%3B5E*=`@
bF>j")raUp!%?!Hk<H>"mIS4%o@+EJqEoX1#7mf,m2XdOT!Hg07ah[\>Y]AP^qt6%CNuSR@V&
:Ce5A%ZNs!f8AK/#%7FS9k/Ht./KA>:T?KL(4+u`bpQ,_5@>o>0Odajb?_%sFCs:3mNogmVM
Yt89r(F)9]A%@p2)$T#Hm@Uf1>Gd6(jlgs\[bc&!.IfjM'U9,&Q=lU#]Ao'F>#EgrToC45oTKD
N5Q'Cf)),49_?aUhg@=__^>3Pap`6P%DnaHZ!NC/aErc.nSHQ,OF8qE3HAZJF[-CZ^n#B`C%
X`?*B%oBbP7Cc`k[."1C@Ujc!FQYbVoDB@Ho-64Ye.-)7N2IA!\:SEb*.F^(.'%Tl-kH:L_p
JA5QbGHP_^n1;]Aq[bTR((<1\nb0e1Y0(J@GE2M^hGn[2Uu]Ar3]A.D^H<5YZJ?^2/j3"@P?5gp
*a9I1R%$j.d/hs#*m_+s=UtXtsjc1u7a7Q*fIV0W3SHc176(g^CpZ!lM_3a_+Odr8XW&%9VO
Ni%UPE[t--n!Y@6cpHOB:Z?A[Te'%bW<2MQk3QWLLJ9IeamXf6_5+Q9CpE9,MG*+kohdI<D&
CXEVTHN3Vt``pBCq0md5fWp0nX."&:Jj0Ha*qdC^a,7]A<1Gp^V5FRKp<7`mHp,cQpEd\*j#G
;AKm0IHhKCIGE)@CW0uDBOYTgoGZSMNcQ'J>%a9:VtZn,@g-KH?pGnZR[PJE4;dgFEfO%a>e
cL7od7tl3J(0Im^'P+&B#kLjS?(<a-oY[#E@h'Z:[D#(GhH\92*aOXV8FZJDhWHcrDsBX7Oh
!CtZ0-lO0+</lXG(C<0qQ%scnTqZFA8@=pp=O7h<m9$FF%$*,UDdR=?*8PMd?SSkhg\;k6^C
\[uV;c@TR[W>u'/j?u1rg<;*]AjFEO?ISf$]AR/TOS&Xf0pL@lSm;$oHRtSoS6(af`lg5]AE3F[
PgcsO(]A<I(9O,0uk;iHhJ:4AS[./QU?E;u=>FVU2V>U.-;[C)J"u$`Rd948I2\bJ_$0N!Ulb
O!22K0,!=:;6&fWIeXRNp5^u+hlrEN?bj[1-KS!.L:ZL@cM2t]A;>nm/kHPHX/%.37WChMhE"
5N\S!%hpo\+r<&hi\$:)6-Bg8]AA%ZL,tt/^7q":^U?8]A$[2W,>V`Y8n;*D-25X6U+-.Yc\D]A
4Yi.LH:>N"9:"L(*`8htT9pZ0jDheMP&+Fi*dJ0&OTWm]Ak<qt-#&D+t;<-=oHA9X[LX0#!h5
Aro\9)'H^ZIdr)456EX[B`7t2?uEu)knaK7]ASA`MRp4$5O+h@9!qc[\>ZT-dd2$Y-10I!Z9#
#@BE7_r^[lR3q2]AZ%;G%5%^5G(!Bm<\_^#!oD3[F]Aje#;UR/YL4jTnm)Ec?N[`>?YgcGC6^C
K&'nuGZaNW]A<>G!qLL2dNT1@B8JKE17@QXrCm2,8=N[$I4%jT>pcQ%RZ#eX6$6]Ae*g7)EZCO
<!%4#g]A9f6'AA&n<_#fN1*/&jon'c*JZ==E0;eYeN5>UEA-?4%qNrDu33n%CRlHPcIqE3CG^
SbMW<Q8%MJJ[p^F;7?fHEmmEGdmOQbsEgJ9g]AU76X.:HmpcT;R/9u`>u;Si6$JM-G-iC#*VH
D+R^Ng"$)^MNH/dFpUPp.;gl-m0[X8j+Xd35s7?Hu#WMn85LKE9o99d1%e'(laO719a44bHW
gR.a'tT:.+5/AB-70@-UBsH7m9:?<HW=^51=aeI;FRK`I$9j>Q[neHk2'T'G#>L2DPj]AruCl
+.VODPY:kOegZb%KsDXXe:)hU?qn,oq;KP*V>iTo^_+0mb1'Q@?EmMVlH3NpfPTi#HFtI`G(
/&-3Ae8nQlNdBOkMKIH1YV0W?bc.3LA3k>q.P"Y#%M+<%921'\-T-VEOfjn>k@Coh&r8VmG&
/7<%1P+5"j,<pjeJ/lJ8":,$rGL9tu@K@Cms<pu-bdVrW.AZeY=M]AZ??4*"]A5Q]APf;bHJ31Z
<#d-r.-mPoMYEG*]A7l1H+I![P:gD11=H-g?eitNl)4qt,"QPUY8![red`,b=4W-NA6d+NliR
YVkgtd2MCk7:A"1aOp*2:Sc^lRSG$Mq'AjJE/&SK!7o0fjGQ"!([I-5EHZ]AJ0]AdSVj)U#9>D
KmH.0)t%8[Ctsq4VV1q2LK/.s,cE0d2Xf:>TcVJ=QTO2"rWG'lCjMaNm[U;p%X?D(BD3-o:n
p3/#kjeG[\k.`;^Oh:a+tnm=g-'M0=!MOE"W)F?<UpqA+5TR44M0k07oXrg,(212K:QZ4tA0
H83YB:c`O-D;il`6b4HnRghNq(e=/(94fLXupU8/7ZiWpj`IZ`!F<WV(E?+E8\?C>P4n6*e.
(\fNPJo%!RcN(D3oh8gY,c5"[1YSa,9#`IX$FV+62uXP`d]AJhCl^A.,.5->)euN]A5,25ndeS
njWu?_5G<i#,aJ8o70.b3Sn]AM?28VkegiVItc_2S$@Zdl+B"JX'rQarWXr%FP4_k;aF=hK"Q
]AWO>$kf3jMs.;N#Q"XX4%Nh:MIJE>59o>.aJ&f?U*(!W=!(sN'F&A9;NT.pGks<*/f=h^%H1
^4>aRp7_]A!Y<cR#\Y_#HKLd1[T*u#fe5N]A#R"c4d,dokc>OV\UuH$;%;4/os,=Bg;VE5Y3hG
NWCHb!aCQ(H=C6]A\D/r3%/encI>-Q$?<r\A@]AMODcYg-uZip$#F1"HCR@?,tSMh.Y0OjV102
[(6jJ*&5WkWS/Yf/os09"f(.$h7:QI,4,-NW@^>a_1]A4P8]AXUHViA9D'jmhj!b>3::nro35G
M*b4X\5BI]A"7>Ah*;YK[B@%K0`[EdQM`o;G#![<uoXM5'lGmWd4BVgciQKNBQr=q"^ZCWl"0
T,[<m2I;O%GRXA:4ZbP6']AB4s?;"IqTfKDLaHG[aOI5rWP:=h4=[NHp([]A4TE"&`Y[%J"Gqo
rZ3+$P=f1A5n63pR4Y5J9?LZ&.iQ039@5XPCkJGc,S`5r&=c4+jZ'E964'X^L5VaGJ(L?@F>
t1&3"2q#uf+,N??SlRCqrP<".CK=M_l/g6[t*t#.UY*#$%Bg/jD%^FP=j3Z2n<EFSCWnuAAW
T4\_kX@!]AfFj*i;+<@==<onApSo`cU?S-A)0P'[gbYJ>!e%+]AaGAs6mP\-;l132(+@C\:atM
taqTq@b&:J0mf[EJM[JcYghf9'(WG<Sp@iID!e0QAl]AiChOYV&p*iM>Tn)(O1D'>t+Lfua@:
(ZIq&@W,5HT9D6V%<t8-iurXo2'9BDmlR;A7"1C!-Qi__7R*rNg$IK0j"?dAAKR\4ME?^#o*
R$We'[Tdcr"[#pHWr?Cbk<G>M7Y>RXkjBd)M&pGkJFI;S\HVC`4q0pe&cc)Ukujk`:XuP+j<
d>/G=j.]A*TXMm*uWDBthJcCJRhBcQNcX_BV;>(I5DPj1ZnK*@%"a=gV9&s-,OUYps[UNo$"R
,+T03YkQ@/FBfmO;oX6:-.0qFi">d-G"n1)dB//1el+4MP19ZlH2)`Gf\gHXp7WiJ:CjErlg
`S#hA:%Z50e.Wr!YtmNG/\H5gYDQ4[I,kd3``SP/M"p*,p0h,Yk`MLU!b?"e8WP:YWp^l#RT
o\7E-BYARc!I6K^/:3TJ.L.>"Y_BH@HPtjAKi20+ZC!k^"_G"E$i4DHS)^cC=N"H8-W=B8*>
1<h8X1NkX\f*7[o@srqR4G,OR)jDW5YP=W8)jeRb-T(@-UfBHU3Xum`-m#DD(\>5,i!??*5*
a&4SQh/u>dYTaXO#!4"Hgqa\OYU8aWaVq-EtUtVL-?Sp.OLMj=8kRXdnZ7\G30uKW<)=5sO%
Nish-W!Cg_B8FqT<";6U(Ria@uuQOa]A+@]AH^)4$k1P_'Vb@M.1U;LC^1[?VdrCtC*2Z7T[uD
*..r#kVS&k<[Rq&+gVb=g5*Qm!0$Y"EulGZG@gB>Db6t1[j\L'I<J=.Gj'2kVeqgCoB0+Y7Q
9`??6l+(cVMh)Dejg38#T*,2GOQF4E?Z@T2EM*Mp//&Y,I5)4M`!N*u[H]A)_o.=;:fTmI.@F
IctZDf&A?Bi,n@e$;eKBtO"e4MVLa*i9.jY,8T+R/i%\PIFN-\b]A3f%$Q`;fQIZIq*]A#:N;W
tYMVb[e6PJkDBV:g?uq:eH[KNJ4g)a78n>94E+Zt<V/Jk!eVCcG@4h=rYuhor^ofu+(KT?qk
uPo^qU4RihPn<Op(`kTT;]AoXb3]AbPaUB'O*(ecS2>0M@>;LGZa*2I&VuB7"f,YP[Y&@VtO9S
/$U&Ck?3]ARA6%78:o]A9efZ>uh_=g.++:mc2LL$]AM[EEHtn*hG]A<JCs*@'i[[Y\S'bdMM^)Wo
M7Mn0\!dg'5TQdPH7@&4jkJF$jaA:pRVtinUDQmaIjLIR>^*CZJbhl"DAMj[5p)DNI\MqPUG
?]Am)+1qeM>Y*6abmgVFM#Bodn$1dU4VVd`Mg]AGnUB@YW!KdhY]A3HIO]A2hQGN@#tM4GFMqKhj
)-uCHKje02qc^hXf@aJKE")KZ*>bVNW"#c0l0hp.Pa4paAim"8bETSC4*3`qe71bVSFGD0GO
53`@nQ7^SY^d0PV%HeZb/F3qR]A$O6KXiDAmCCC7m4C=g;hA#C[SZ68?03PP=u>;75!bL+HE'
b]A)WfHJf2;@@;3."kqEksnM(ps[+rid-pV_OHm7g$V%ZOA,\d4B-H7/57@@:4jX2[rHL%L#7
O'<!C1j=+^S7ThZ(S%e^>-Khcoc!:XXcWe[$7:4L9Ldk.V>KXN:JaU/jNQNoNqj3T1BdJX79
rEa*)0<WG#:=XAg,[YM'e#5nV(3U#&.]Aa5^c6*2e.>H)V(u%>+-;EONl5D=Q&[Q!r/4e$q-D
cYR$Ob[h^F-:_mf6glbU,femn0T,CR$9ho0=9u7KJenBa\Qh3@I:a,G)qb96mb?mW`%bX7X6
AC`R(_F^_>1f8XU71Mg.SOuMhK8.ImLK-;?qL,ckt%Xame2e8RSNB7_C3m%(65E8iNLsQBP:
F)B4=b?2aG1\`.mI;N)V;Q-S.o)*Ks(,*&<-)f-l]A@C&pg4_s-"aqIqHc^1l/g>MVSgc9Z&K
Ha?(**Qo8k$eJ4=.i_L[P4]A\2L4]A[9`b@B9E#,3rlU*<@JiflEX#[UJ`8FdPT=&K3Cq/C.El
6)%G:QGaeYF!Tl[`.HmB/G(A3]AUo@N/"b%=C&]A]AiSG;@'hg^,aE"<DV1`T+@l`A]Ag&?8.6K.
UXth-hnTca,96D-1(okK;q"S)PA7Y77b1C*6#NlNQAIgseoh@DSn$B[9eEZP9K'@r$N#t/O8
M^G50N`Y:e.]A#l1MZQQ;m%s1n@#F0XC('#c%$E%Qn@SHRnS\7_Rb-e9N@85?>!Dgk!=F$qpV
g,U//*u^[61MSeAcsXG(hMEhrHh@`f[[pn5D`7p5Hb.)s0^Q8l>1rBJc8Um*$@+23F,oBN,/
o<iL1XHp@Rdtn`>G:JdbbW0Q/[#a(b`r=PYhRGP=r.4j>@2neX;X_HG+"IWKm&^b)nrXmDIs
Cs$3k2StmRmD7GrqC<A]Ap&3XYDGrj%9G1#f-t[)*[L%2<H%cKm,0Y?-kaE+#:m%Nm711r#^O
^5MRr!.j&<&_Sn#Y`VicthA0Dio2\0i'1mE3r7MgS)4<\_-646N%k&qBb^b&C4!b8NGeo:Z>
h\$J*O2eps1J5%6;gnaYd814*JBCuG1Jl^=pOYMD`D2oL<"n3H$C^WF#@4_mC53)i(a3`LEk
-:HnstIR,S#?>I"c,[at!a]AiQjME;gBj<L_\LIm/D_,Lk0GC>s%"U1$"T6HMD%fA.S'3&'e2
%MMRkhlf$u5BY>0\>-scq7H-mZRkPk_Vhc6LA=FsEnGSE>D9(^%ms$tdZHjU>(bk[4ifF8s*
V_6V3$..nLsMcYNXa`pG:_5q['0$O2(AF-HN>-9A@i7%Cc'ALil&ZFYMU8TbX,QO$'W<m;eK
h/<mktOlP?%&ugmR6-V_mo?ThG$FnWeGbn4.Pj-hO*AG!S>mr'M(5_SZ-.X.[#dY^(V>FA5/
9EY^#aT3Hgs9OY/af\=.7c$p&bRsBTr#c%]Acd;UJ-9]A+m2fYLqf&:j9fRFYOKT0eUK;r%'.G
37?R-]A=T=;*!!dCD,H+VB!K&Ba,]ANHT\Zor`l=^"$pg'Z:0H_]ArPs$cR=d3-4WW_SE5!oNru
'@[k_!sD_Q%i4F>02T[U*t.g+\?*7bq<m333HTN.DRb>)nG*m$V:(P24i$G0F,\"d2.GD=aG
Ek`C?F:crYu!H[G-b<bUn<.-8kkq]AK+,C^#Eg$QYZ[.dD>WCQB&n1j`51NkaNG\\u!p=/X\D
R'bVN:C%j89:c`S0)IX&_"?4SRI""kXgZ+t:_/kI6VG^]Ate+h[H[u\BW":%4k"l-^\s$_Yr'
1`EgkDccm=cB:H-]A4ko[/QtjNqUV#SciTQ4T5)=IkfLk4t/jiBW5LCW%^&>DD73_^qE#%/BG
Sgo8^<=jQntSpoN,pQc]A/N-CBF[?QJhA23aU(SCIS7"E+]A;UonT6moQOAE%s$EUr86/YteS2
n,EV04l-b>CI`2cHBrA%B573&_brH/QrT@QI/Lq=0;)a4O2KdhF*dW'5SY7iXs@U,hW#Qp,%
6HJ#6C;<R`S'daSPlAkOnG/pqWfXE3Y?nENXsh'G5.-ng%?52t75$`!I_\DD-N_pAN[`7aEG
3Hm)XZ;25K3"55)b/QkSO%d#9GCEf;!FTg9:YkanlbmM6.-@qRtR/&e'DKt#`'J=L@K0@#7n
#l6E-/Y7r_92>HmO$>HmIPWaIA4RH1DiCWqQ.7HKq\341K<i3qFO\(0-=s-3QTF@Vu@&V\;Q
_YdqE$d1`BaH>D^:X>N@!YjYPgY->X%Id7T89R0ss,4/e9_gd']AoGqn1i7JDUibHn)O-c/F2
d?IBm`nR_3.X_GdYjmRp><p(UpDKGZ/nY!s7_+N3M0JcrXiu8f8+?%]APnH"S3(Tn&/m,&Y&X
\293g#X:#:*jr#jV^o\3[^A:S2US!]Aas(X[plQ)"W>>X'<a+*L$[>]A]AmQXo5dM<?&Z9%cW\'
Tn1>s7q9bR_'F^PuKTfseC.U#I3.>;b4jVqT+J#\N,=G&bm@Z,Oc%^`d_1/0Nd*=%I>r'E=n
,<HeA(qV8+7_=2HamFP4u9KV^3Z1I?t)?Q<Ct^Qi.RW<EGJnXDtH!/`XdhVF>2cA#;olfl<_
Tkj%,#q+G?\8IM;HG<Re?Nl>-h.HNg@)c`jV6euQ_TE;0]AQ?g5QD;^n2Db9[\i9_2<FY),ok
XJXl.;[APV/ooXinN7IImi`@NHT;$97XG"W$P2"]A?T1C`-ia)jp;1;M/J.Q6`N,$_s5/!a1J
,_tCM\0/+"%A$A]AN),.F$beE6%IP*sd(M"ST3bogs7\^7N(L]AG(4P2R$#\ZS;B<p#kX-M:h%
<jq"FGXE`Zm-eY:!1q`C?0=_7_&n%m^c1'(kV5e4&!]A7VAM=0>[LV5MuMC'^?*:[Y?\o1%,X
X:r#&.N.;D'eb/e6oeQKHOAsjYH6.\E_J?9/L)5'A'[CL'.ISj`[XS?\68GD5KC]A!=2`>#b0
Ok87fG:&"?,Hp;]Af!7dY9g;o=G&rS@5YpQ[IOr7&>H$`Egd?nX*N49^&+&XI9rR+MZe#;139
0,]Apl?@3CW(=4a`7WmaSgA>8,B]AVp.16#gI\km1K;t&WTB+B85N-D95NJeD<Z@7P,L/\bh@>
tgh<l#I7!1M]Amf`ujhT&dL"g@1@4l(u>@4Nhebmd"UsG,!I:<+%kj!(W5Q[]AOKTj6cd>gr+R
9<J`CdPZ>S-X_A-plp#tl9`"V<W%/c0q@&[gFP1UVnhX+;N&L:db:P1#l%>SCC>lCS2;;LTG
VQg#oL=j=m"e=3kJ-(Db_6&,r:Q#Knoq\MpC[_2@P\LJ^i;mRs$1dR4b;A?c%M!\%^"'_?sq
5/K#%?0GUkh&c2=sck=X#m:BKIk"/%E;%Fi:Y;>N6155U=ii8<V6iDYOk<ekTJ_^.t1]A+PRd
QcF^9gu#&7D&(S-7%a8SPNr>ajWa&&nm=",DPsUnI.^>(#CdCK3W<lCC[:hs2g9cLIf~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="484" height="542"/>
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
<CellElementList>
<C c="0" r="0" cs="5" s="0">
<O>
<![CDATA[标准收益综述]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[ABC公司（单位 千$）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[Q2/04]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="2">
<O>
<![CDATA[Q2/05]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" cs="2" s="3">
<O>
<![CDATA[变化率]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="type"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<JSImport>
<![CDATA[null]]></JSImport>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[$type = A3]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-4144960"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2004]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[4]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[5]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[现实]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
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
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0"/>
</C>
<C c="2" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2005]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[5]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[现实]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[4]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
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
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0" leftParentDefault="false" left="A3"/>
</C>
<C c="3" r="2" s="4">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=(C3 - B3) / B3]]></Attributes>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="4" r="2" s="5">
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
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
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
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
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 >= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!T4,'qMA$D7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us"fFp[5u`*!Fd7/M;g/qrms
>A0<8#IG(;tp:(")#S$P#S*i';+\#E"BML0K`h"LXmFJceirWi2k(77e1J8/Y;qXiCGW'1D@
EUE-)LC2Nb>pOWi`:]AL4N]A\MDXTA84G?UBfqQft-GP\OMTl/CMGFQ[d!e`on.$h@"2E5^r%T
@$fAQ:83,%m;#t4W=3n5W_8;p2ol^)p\S5Y@q!@'Kt5:(%mu:n9PqBW_B.mRWDH*3D9"Q(b!
s6O5jTIlCodRniRJJm=M9gM28o'$h9Qr,I6r?";VD2\B5k,[te$8*sBZf1`d27FoNt05e1UZ
X8SH%Nm3)iZ40jkYX$bI#NW]A-V_M"D*X:TmX1h]A:mXZf7Xfto9K0;.VPm=LJp,lWGnufK]Al>
YV>f$b%ma4=\':(gu8@ojp>kHX81K)A2Q@Xf\?D<2=8-\Z'=.Ae-SNcc.mgc/5t@TRQaONKH
D"E=Uq[oMpA?g^#B&O-C49:5MgLX9cW9C<()#cWt0[rDS[f=E-(dRYGnc@d0u1*4kc,>:>l*
`ep1V"b1;^8+/f:Xl>T_J[k+s&D(NTQ!6dj'm8"Lu;FS@<rO%]A@[DN9o%,nCLcRIVCiIQ?Yh
rr<lAKK$',T-Ej4EV"`o\A@uXscl93`W&X-NT.rO-=@hpNps"0#bffWM[3B3WRN6W$oeG[m?
Bq#+pnf9Yj@+5K+LVp&q_Q]Adt.#,Y7/7WoFYclqc]A%`[BE7B)Wc32K,6FSod*&9MGg;>u/b@
1"'iHgV/e1nL/f-(Ya2cZIt+OkLuo<=(8_"1BHCf3Y(OBRuq`$ND='Ze45%]A5'cP6Ab<oUZ8
$8&lVaesq<Q2A+.G=\TMp'#T>4'4F?G]A:#W3:=>u:9:DtL\q0thi[>kB=:V&B_C,4dgVo-/?
YJ1YJA(m9:hGLohW4mf"qG*##&t=^qO5=O9QQ0Lf"6d'9cdJp+.LXZ!k3mh-R>c,'#b]ASr\5
r_RR?tRaWOVaT1/3^#7Qn/KIE5</L?L;!uJo@Ao_idZ%A1p<(dSc(p2;S-$ZX]AQH1`B^oqF,
QBNA,CPV[OV%R#UV]AXa0#k'd'jqpm5htR5BU+EZNqV84#HANIqO`g!1&si*ZM?L:^h\'!>=m
R/K&?GJ:0mCLaKO,K1dBAsU]AUYV]AZA$QUS%o99IjKLJ!^WXF5@PDoN%eU^O*jB`P;WDNQ]AKE
:orD3p^p@Vqeh+Y$K@)G4hf&TOnFe80GEn`EoIOMC`<<ek/2:Y('B[IS"B#,)$JWdO_s?^@)
sK:KZBg,"OqGO5hpBg*?k=,TT/"9<*$JC^&NZNVSMN_>p1n!B1[9Db!u`Y&#["J_h]A,O^&Ob
So2q^BaYSApB_i@B0D]A\.$puT^X`/UPF%`bl%'#O?kZTYt1N564]AjHu1%*CQ@Z79&*Cm$;t`
ZZ<6:VN;"?+^lm6T"p.p`,Y"'fEEc5(1Z=F)6hpHAoVR@j`H>)Hk^.EYP(]A/&>+MT1VQX@8^
#pbUjdKYeB]Ae066kq>WH,)3IFo5s+si>V#K8fZ@$s]Am8eU%j==1@1(7/h]A$qdaZhu61a2K-D
0[%,WpA[dT^r)JFn/u35/=))1nmc*k&@>YY`^GoX3[r`;Uh'HXI>!1#Q'$PO(%c:Zbc='P(2
8$5"0K3E&qKqtI2CWUNA$&d+%j'>!X]AEmocI^"us-=."hI%=p4#LVVQ:%uS[Pd4/=hprN$F:
(V)><F.5C@O,_/$Xj>\/PWa"A>ZQYd3i&S`i^DN^m-RdN'4dTIQ6d?F9*XJ=:N23_@YhTd]Aa
KZlU4=Z%t;kMr8`<\6Z`D-Matkkj!i`*(X2f.gh'c?4;=$"4O\=[l>A-Zp(%"#L9'')8bmn,
NFg!(fUS7'8jaJc~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 < 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!FH&(q2%pC7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us"suo05u`*!Fd!,.P=H>-(C
5eL_ZQ/s0jJH)<!_c>Js%<%ZrI@NH3$@K$Unp_.b'K9JO)`0:.L)%U*?F7JZ),Q:TU:bS18c
6&."@#0F8mGI/e(Te_6F?1V_U]Ap?hkAmG!$l!7B1I<t\5M/OB1WU:l&Ki(b0+XYPCVl+FCk]A
kOm;`'d2kngK?07FV]AFI/Mt&*Qa69;?]AF7dLHi]AR0(gI5)F@f"@Q+W:ZR4TA5K:k.u9q&SnP
.(#qDP3i3aQN/M)rhU&Aau,\k*ON5gebLsjc"T!SOXY[Fh6pP(6sX.&e;P1OBmSh]AY,g@VpX
gT)Mj.[<r"QOTbbrkj`)ia]AT<qf:&l.05mdH%8`dM=X&I$hC"F\dk:F:(VbHKJY0UP\0:/Q(
ItHXEsbu-n:i$mIPWJ]A2P#<JNjP8m\[en3$;-"AoBGleEpXeDpso]A",pV8R*7Bp>:^INCP^f
e5W!8"7<_5@(r_3dojVLW;kg:k+KD^PRtU]A)1lS-Yq)0)B&dr<h'$=*+lQX,\UuR2J^a)D7s
-%,49-!f'plK_<ULbVSU@9gS]AK_`q/h]A=]A`O1t!>?;heG?'7'CcF_!O<^,05+#n;JS"gGKFd
RqDD7(C?lEeD8Rd3@hI(/=9lpqWJ[T7QR\S!\"g-0&[jk,f&>H>/,4-cL0,?QMT\e3!RX#kq
g]AboL8uOO"B/FS6(_")h*B92j"HM!P.0t-O3lD=^D?R.+*V%^uX0jbLLb6I'a4&4u/^]Aeb'/
Xs$!!1YYAm4Hh[fka9!`OFAUR90U!+q*#NTo"r%Y=[2e4jK4J\)*B\rK.!@aZ0h'adkmESXG
bbL#Ul!iF@>4JKlO_PLKsnO^AP*m@#u&(:pf?UHN]A#';]A=4"^n-HUBpY3oc3,?nkM!3rG^k'
H=g?&;WJlMs3PX*5n>@PPe&^5s,A8Yr,jBd!3pc9erB>18<+?&:)dqE"WDZgr>7Dn)j)7q,Y
MVVAW#R)gs?iiB\p7eP#-Shm<a8/:p>)()g=FBVMjD@H"&j&[KUeY'R[PC=MGWU/$N.jO.GI
0eJ*;0pnq0)"=4hoH_fK1)ia(U(d=k8_:,a)qqNUPU7.R9r96K)4R@hAVrWmY*dDO>mItO19
bXjrE1ptm%fg[k%o,LA#%<&KYC/>a?o#SA7P[/:<lA7/:Jm5es>M.SVL7Xd1ER<5\t"_8i@X
#WT0_6%k_oNL^CEdLLYOFm0:P=/_H/D(lhWa"8&Cb%#Xna?%r.&6bSanTIMOEVRfBlI;fbOb
`!^AHgXaNWhCT=cOR`.5Q='E3LRSQh;g$+U>d@Q1W\p!d6;q+3^"g_^S*s^UC9u`^]A<s\F&g
UJ[#_LYqoBB5[^Ut;_ur*/p*^4U5Z)>k!mqbt%95kc]AXhupKmY?dg"SgTjG8h)erU%=J<<G/
769Z<Z0'/<8=Z6t1"li[Z&TAUfR``7mY9$-;6S)YQa\?s&UDY.,6.22Ffh7,\3VdCg<($kZo
)DI:6=*:KfgslN*?2M<G5U*d5>tLUf8gb)2FgR/uUZe_ikC3S>G58n--q!a%m8pIIRrHe5R>
,F/@!HK/tKKd-c0DK81N:.Hks:5aAlUDscqG+taeiDU.J9R0*0m+*;NCd-NS)&#*)ii'"KL4
?M<Wc.O9j/h&)0=0<.g^&qk5I""eZM_em%2Gd/@$>%j+:]Aq"i3QDZq_["PTZ5(Mbe"@-.6P1
4>(!d89oG*TD?]AK!Kc7cK`<cXe&3_:4srqK"]Ak7o2qT1Qu%'02etoBs"]A(_<IT)mnRFToP"`
C=sg'IQ\LIKd#Ya\e+fj,(\j6+^Z4G9+)OYeXLc$QS6ZBB6=9$ReuE#`#8Gp@NrqjRJf$QEQ
W(cWGQ+I#C;!t:b>r]Ap$+N8'3F5mqDDrHO2^Lj0P#16/\AYX;i1`mCr*3@jEQ(-s+h?>&kV4
Od^!LE&KNsopgQ-GZ&\-q^1Nm6>D91ra%^pX%\]AA->Mc/IKh$Q:X,_qY[6HW8PR,ada^0J3c
bt;8A':64"s4emz8OZBBY!QNJ~
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="1" size="152" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Top style="1" color="-398635"/>
<Left style="1" color="-398635"/>
<Right style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Left style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Right style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="SimSun" style="0" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72" foreground="-16776961" underline="1"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Right style="1" color="-398635"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m94d?;ch\MV&`c=_:epV,5Itt3$SHYC/ks7)llAAeQN,d=KI<mb9fWmR"`pG:b*kA,N+0L/Z
mUH;MYl.,h/R,']AkW1UbRse"G/sr&@.F8DQo%R_tULpVuALC&,4q%caiLiT6GS;pZ0,EFlCf
HcC*t[ju.&crlpF?DXM0s\#9(oq[<=4In`>FS(j)pCYjGKe"1#C=&;M2iis`aT/M(=?pPS%?
bC]Ao"Wi#_O8V@%[&oe$n&D`tAj*Q)iEr]A?XA.B&'>KcOqtn^C,iY;:c;ZD\Fo-,n,o]A1tl=N
Tb$@Uh-f$SPb?D(37TEHXrTuJ>D*)@iGeiIQsE?.X'=]Ah-W:,dGP\om@9nFTKBoO@[?OhU>&
&?0tp`MnGokK>3E(#JbeEpq9]A[^:M1gYLr''=4&fg74Mb7J'UmGq0&)W[SaaMFS8%4"o-"\N
Fa!pi=Yu,]A1NT:#[igQC'8p)BE)1<<-9%jg`a.*c,$n]Atu3lClG)g`[AI>/N=GiLX<bV1UeJ
[ZEC1@O).AD96Fb^P3_sf)j1L?[87L@g<XRjRItifG:9HT+1$$PC^6@ic<Q3.k@\N`hRL.c`
pea0\g(*F@P#DP=O^unmEq&kKXUWg\>9[i!&kPS0HC%RQR]AGRT9o)[l`\e\\Y4JL10)kk&@J
m<+]A:glo[Q=7XNXYGb3(d$/KrC7Xg@iOL"J25Z@:YsD%!W-%ZC#2bkqOgB1U/bD1Hg^41S?J
c-OhBFK6\W(%,Z=irko`['<NCcAcKK3gO!9PjPP9#%a'GL#k]A4RoA84Clsi\Q#<J(lr<p8A9
@rGf#Kl'2APOJ.I5S7hLDB-SJG@F*[2OuF;\.:n/X4iO`pp4lR/0[iVtu`)`33uUt:L:k`Le
4?5.bJ0CX6>dYd:K^e,J$6eMoT^A(X.p/'hkei(t."H>od%H4s'GU4OHf$_uaZMaY&Jn4fN)
"dZdl".Jnh;F.B$Ym&,DX%kZ`H5"DC2R)lmn5&QP/`m_LB??b\Rrn[`7+-T`d&/6/X/Y2r<-
[]ASYCU1?@@dWk0gM`ZcdRSnujul'[#bUoTp:C:=*'1l6tBOr2]A>1p/'a;olYH-Oj,]AdUXNj8
B_4-_`8=;-,LpKP:_MAqAk`<.A:"Z@5R&(Y(;0BHk@O/5s1A6p/@b=aCTc+B4=gF%I\#'HVe
i^YjJd^`@op3d6-Vnp6+pjVpF#18M0VC8@grJ&b.*hh;Q<Q;9g!gH[$u7,2"jlkg<m7`nR5b
NcHiLMSLM&Bh=q0q=cVn'KL?f1f0I?N"C9X7cbK)+%.>)(GsPl`\FfXH;tcR7]A]AsnD/ffS!K
j`sr<LN<%4qiD8<"Jp)jB/=Ae"@fpnF5]A`>OX(7ormi<"KstTS+8-FK9-Mc/RYT#=/=NH>U6
l+ion]ArgIj#4F2G%*7XH@[_17^7e]A)\Z3I%3pa_-`[^ARBFkrrEYep?kcj0sB4*fu'e4bnjY
l]AkI>Rr[jQUU<MKE3S`]Aq3MPJP&Q,K9g3Sh:>EW5T=?a]A#S`7oREOO>/@/Ypma1AtKD&qa9;
[Y_[),1Y<mZLU(pn`caEN"Yhp!M%[YDg4f;YI8N_2(&$/U,W;-4S<bs/r:J!M[>2oo1;ZsAX
FSj!j9_0;8$,acbN;3n`X8uJ'&fo/rnd\^Yo_%.,O$B]AImS\Rl&9P&>(dPZ-+?lJrK[\BP0<
?&ugVYMR?W72E"q3WZ`T(IX*nA6%K8S&Gl%2F8[*g2>B=W#.>Ud"!*PW;+t!Z3Ng9cf#9r5D
3`]A;@reTuC#iDo2!dBY4/ZU(EJRTZ3:G*(NHg)-uA%`"mX^3B'\%[T(*rK6;@Y^j"I.Ab)rJ
Xrt]AYJrZJq.#,a)bba(sQ+c^LjVrIL]A?@gK)WNnaYBP(kL>N*mZe.?hJ3T]Ag2sQTdeoU2_/i
']A?J]AeGE]AHREjbmsMa\-QiAR31jj2?s(2g_?c`(YaZXCY:<u)(hT;7adbF'Xqo7T%TEloo@E
hfNBo3<]AU:#"43#cK3Xm7F1N%rN_-;$qJEk&5R70k&2ZHUT46TV50`Nkh<GNVgg<?Vqsmu[i
iX):BVQaJH(Ig0MYH4Z,0A(^p(*)S,?-,A]AX.T`f9jD70[4]AMOfMCq`o8N2.T66$WM53.6>e
1^<gSj*o69dH5q(9t:.U_8kk![.!U*\R7^EN.AhKqr1P]A(SQlfG&OeC]ABd!g%c1g0Q^_p&O'
Hhm^prBen9p&\=Ma:(IPM`B4\r(t<MIkPQhJGG@\f\"g'FKHc_fC.R#E[HC*l4?"@0C&Hdf"
@&#(RV44'XO#3's<TlZIPI+jJ$]Ah4m/9c-c@INq4=c$.p-@,c8@3L9Qt2_3:[n2J]Agdbrkpg
!?WrtZRKdcN67logVH-#39&IeF=q$k`iD&r0;jFJpC53a<oSZpNL+84E;12IS-#(>5bPKh)3
=2\o(QVH)0iahlm!s'*^&LcYhU$_[CAZ?Hob,6EFa@=5"\$O9:J\"WfD._ofdg3Kj7WclFKP
QsHcKrRHE&5)+VAauLbbi+$o:A>6Qs(IZXk0J9^P#:WA3Fbog^R&(1#_?qjFn)rFX+L.QBt(
Qd\Eh#:B4^=KZBs6=OZ?=Q4e/]ALa:UFS+>S&I:sfHUg*_P8fL6BA=EO5sjX+P,W7(e`"oCh,
VO^&0:HKa/l%o?$qV_`JlQDd[7&0;iXbhMhS^<iCZ0Tb0:L%M="Nf:&Dod:,cSY@%OT]A3mAL
l-9@##Y[!<r*I8=7W]AKn*PC,;E3f7[*22@C?A\&A#[n__'3>mXM:.qu$]A$AR$f"X'-V28pE?
n9R`0\'[.+0s0kgr'#_F/oi/8dJ.(-B([gJ/rJsBqMGpe0VD8N8iVTI@D4R?5#\7FoU0W%3s
^!*CtiOF40eCeu/"\H`k)b-`!DGA*E?o>ouEqQTO)<S`TEsJ7]A\bmEMC3Y?IBVG(]A=[J&<`&
[6D:0=3=M4PmiS1"jMqNUDSkER4A.rXk%C3Ash*Y;d>i@)!MmFA7o6ZCSZqe6>+[c_ceUco4
1,sP_moWKB1]Ar`FW3%hckM7UI#1tn%Gg(m%5>i1tG2/d^3RC#+`0_?;inEO=2-XeEe[1Z7Ye
,ICJL\(<7CGOlk_3:^p>\\8#6!CIG^:a_C78f*KK=%i=k@i0_@jV\rYCAq%,2;X;Df>8X;Hl
LS4D!,-<(/m[rW,cDlnZdE4UOiB.GPO8<j`SO'oB-A??OWhI=d+'nXr6^d4S!<2U292`Ol<.
UDE)@fB,Eg?`cj$D:SE%uR\3d=oqPtP:ZTGNsOJRk-'Et4&8:-S^$Nr5P"2s/Q@NlY/Gl(=K
ITr(d=-[cOq>d]A_bgO1$DoXKfY\mEJ=k$#I@ZIn$<-i@P0Ae2Fm%H_TFMmq@G#qE!,-*LhER
i?GhODjc=<8O[=4K6(46\b)0.s_\_itG.dG1_-e;I7/k&#-(-,r>P'utXr5.dJ^JlO4n-O(U
JfQELZ,+5McjK`hL)j\gC8)^^B=6JHHK,f3QTFcUN,_+[46*0:MSKGkHC0h^($W5Sn#&TT(B
26ms`e)3:-kaOpK!Sa5+<>$n8jC2=>s&h69G:Yn'O7Q@%@8T7/FLLgYsaY*WLfYY]A;:!a5*X
/(2Mr.ula+<uNb3H<ZLij4Cl2`/CQL0ECp]AG=\'<7\bV*L^k'g=UrM!3CeDY;0@>R1Md<JS&
\,;mU]AS*uD(*cXkItC<#:\u#2IkS5UA1nBW;a#/WSj]A=9iJ_'o7g>4@%LG*qITV,TV`3>U\h
E.`AA\VHLs&^IjA'9@r-Y]AQW#>+Ap39-h9sP[neNqnKE2Qlh@uFj1YcC1GSnq06_8to&]Ags%
anW_1V7"2THg8,I)o5kK6g@tu4^#b=K]A3O!aI$&b^Uc2i%PKEc*.a.h.fR.R\+1[7#'H:)lF
qj&=qr>s/cWk32.jTPtfKj^+/pGAe#Pni&fbEtcnYfZ(V.2%b&uBJ/k8LDTh>&RfE^O9MAiU
T"O0)qM#]AVd>9(_j]A9/%A$,ZSJs*M[Thd*mC0?oRO:BqN''G/G.KN-<tgk+/]Ad0+aT^qNdH#
3dGK#m.`]A[N``DUj=k/<.$etB480aA4,[:CPCp4KD'S6@!lm;cUX*\IrN./bC`latU/1[2ni
f<02Z<9Kd'O,m8lj"Ss,9m\.Lp(9Y;bLZIg">0DuLRmhf&,"0A_sopChFTbd8B6+lBq^kZ9\
tgHQ1?A2"U,(4EIl?S_5(7=^4`C=.-V6jHo@10#NR'0-]A0>%Mj$q_!edkKcD8"XdisrQiM%T
lO2fK<$+979Bt#"!RKg77a>o^kLO:qrJc0(F,B"U7t))?J"+O'%B$:-ZF+HSr((,#`+&Nj`V
dm^$4Z8?k'uCn:2T!@S`4.:(T\@L@&ZjN>)JJnmuX==+dmjel[aYB>u241beS&]AN!Ms!1a,@
Hfqm1Nl5GSd".&EOc6f4bidqm)$lUtlTN-a[Pns%@oa`+[p%Yq&8c)2T!daJN^#kR]Apkgb:d
jc"on<WOFdsT_[!u9WKu^73(4Kh"D!R4^%HASN?WP)*$j?;M<q$"eLE$eD74l3<0JTGUnF/q
@)+gdb,p3nMWtS<o8Pir-k/2$8J^+"!ln:6"mLe[h%-_\5F6\P@f]AAM_H`$cK%t4dgG#ln-$
k39-5*(Sq1k+4_IsC@eTaMr%h!DT$!IA#F&-,Tm_<oY/2G'?f$R1u.]AEF=i.5#%lN&`/(o$n
Gi-:NPjd'l`oT0/i)2i4hu;WAZ7MM!BCD]A[5R8"e4d7hqaG&U/1E5+njN]And/ZVZFf$@dt34
F8:b/PTUAK4"E:?MMOG)M<t\-d_b6g#,CESjr;Worc%!mOLFqZNFIDS;G`UFjV@d/87<l`A.
(YUa)5oOJD)2*4#R72_*"Ea:*U[<UOoacD*0:-!&/j*+fY:KVZQufXS^+T#.V*_nk%kP%*#3
61DmG:KB<9E)Q[,;Tbb=tOD"Vuo:UFM@&iKWVO1Xcc@>/C]ALZQ0\aeK7fUi6C@-Qt?7he\6^
@YV[o%DX_#$KYVg*8CjYdbr-/mT#o+W@_(_6XUQ`c\f`jBHbQ1.#FPeT!G."`T(b+Q,V1%"Q
3&oUh7,j=Fri7LR:dA@Baj(&k.pPsA5!$G-%Xkshj]A)Al#Vm.\aah[/QmZi/732dqd!MWrOi
%,(ao>LpT(#k1.Vcda[=8EaG0<L+C/>5[<P+kJfJ+3*L=]AF<-l.LN@e0i^_/H*Eq]AUf]A";XK
`&j'ApIK2sn*)=tqXX/O8gc1\27lif[q-i2V>[JBGuYknfqsC5rgT)F5kc&quR+Y8':+&Zk&
rg^_U<?#^0`9#>KNUW"#sY1E48r.)hVg4)3Eh*:'T)o<NZ*Z=>GMp"a]A$).NriXG<980or1'
%H>eYR-\s?U.>oF1CM:kGpR6J<$1h_n<4ZQ3A2kAuZQUa_q:I*:?G^06BJ;r@e'S)4K&A`j6
.<n^.U9;)q]ANR"Wa]AqPQqHU]Ae=2i,[mO0]A]AR@31[-@PI-&oX##p`hgla5s+NUg$Dn/"P:eXl
JYQ]As;g&'%ZiRRY^'0H@bWRD9[Gc0C_WQ]A&np:@XL(CsWo<Hkn!TQDqN/rDIcs7R.V+*[)^&
o-P<l9b(-or#TJ]AE+T!dRU!EI!GD':5:"3oc#^JK*m<8F/.p4NIMF-UJ_2Fd#X3!=mDB=E)8
"\?9%1P:<,sq)_a\77^a'YBR\tK]AZDS:#'UKkauf325_U03<fp5"NU,PV^?E`M?PlkQjjm?T
hC]A7nJL1u)I,Ug0Ih`):fHDrrOuT6,42Rr1gOKPP$#g.QObI3.bbKO"uXj/+(4.YHVeEM<A9
6(0K]Aj+-J=9mm3ndFY;\.9b4K$YW3IV4!(<[L943oU@=[s]AOfZY)#Fd(^qp7HkG'5g77B=4@
@b0+%aH[Fgd_\S%772Db,c*)b0NFO)i;.=6T+g5]A`*r+S=F[5@]AYP))IE'8u']ApqsbP=7q-P
?h?S<515(;V'80D(&%pSObd^<YU,1."l#$+L=bi>*Q>FuGr0Up924V<L.>B66C@?R]A7W"''a
ac=+">!uW8]A!coBNUC(87AqoEI8p`5LdZ_I0/,uOR\/Y^Dd1*2)+GJC,QPBG7Ng=&q(i9s-@
d]An@h3St4M[#cQs#5,kYM;8MQ,Xa/)3Y9eL:G2H#7Z!*4%f2oI_QV`qj$Uq>m0?L62B,,A=u
Yr*Dc9Lqb$n9X9`fus448TpLXSHg]A%3Q~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="484" height="542"/>
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
<![CDATA[=if(len($type)=0,\"純收入\",\"  \"+$type)+\"的收益和損失\"]]></O>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
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
<FRFont name="SimSun" style="0" size="128" foreground="-13421773"/>
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
<OColor colvalue="-11284046"/>
<OColor colvalue="-861324"/>
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
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="5"/>
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
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
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
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="21.0" fixedWidth="true" columnWidth="40" filledWithImage="false" isBar="false"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
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
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
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
<DefinitionMap key="line">
<OneValueCDDefinition seriesName="cate" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds4]]></Name>
</TableData>
<CategoryName value="season"/>
</OneValueCDDefinition>
</DefinitionMap>
<DefinitionMap key="column">
<OneValueCDDefinition seriesName="cate" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds3]]></Name>
</TableData>
<CategoryName value="season"/>
</OneValueCDDefinition>
</DefinitionMap>
</DefinitionMapList>
</CustomDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="false" export="true" fullScreen="true"/>
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
<BoundsAttr x="484" y="36" width="479" height="199"/>
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
<![CDATA[=if(len($type)=0,"純收入","  "+$type)+"的收益和損失"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  纯收入",$type)+"的收益和损失"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
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
<FRFont name="Microsoft YaHei" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.PiePlot">
<Plot>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="true" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}${PERCENT}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
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
</AttrList>
</ConditionAttr>
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
<PieAttr subType="1" smallPercent="0.05"/>
</Plot>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="country" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="484" y="0" width="479" height="271"/>
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
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=if(len($type)=0,\"純收入\",\"  \"+$type)+\"的百分比\"]]></O>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
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
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"纯收入",$type)+"的百分比"]]></Attributes>
</O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.gauge.VanChartGaugePlot">
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
<Attr enable="false" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-342221"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="true"/>
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
<HtmlLabel customText="function(){ return this.percentage;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
<gaugeValueLabel class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-4210753"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
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
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
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
</gaugeValueLabel>
</AttrLabel>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
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
<OColor colvalue="-342221"/>
<OColor colvalue="-11184811"/>
<OColor colvalue="-342221"/>
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
<VanChartGaugePlotAttr gaugeStyle="slot"/>
<GaugeDetailStyle>
<GaugeDetailStyleAttr horizontalLayout="true" needleColor="-1" slotBackgroundColor="-1118482" antiClockWise="true"/>
<MapHotAreaColor>
<MC_Attr minValue="0.0" maxValue="100.0" useType="0" areaNumber="5" mainColor="-14374913"/>
<ColorList>
<AreaColor>
<AC_Attr minValue="=80" maxValue="=100" color="-14374913"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=60" maxValue="=80" color="-11486721"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=40" maxValue="=60" color="-8598785"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=20" maxValue="=40" color="-5776129"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=0" maxValue="=20" color="-2888193"/>
</AreaColor>
</ColorList>
</MapHotAreaColor>
</GaugeDetailStyle>
<gaugeAxis>
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
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="64" foreground="-10066330"/>
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
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
<VanChartGaugeAxisAttr mainTickColor="-4539718" secTickColor="-1907998"/>
</gaugeAxis>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<MeterTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<MeterTable201109 meterType="1" name="type" value="百分比"/>
</MeterTableDefinition>
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
<BoundsAttr x="484" y="36" width="479" height="199"/>
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
<![CDATA[=if(len($type)=0,"純收入","  "+$type)+"的百分比"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  纯收入",$type)+"的百分比"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
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
<FRFont name="Microsoft YaHei" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.Bar2DPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="true" plotStyle="0" combinedSize="50.0"/>
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
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
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
<BarAttr isHorizontal="false" overlap="-0.25" interval="1.0"/>
<Bar2DAttr isSimulation3D="false"/>
</CategoryPlot>
</Plot>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="484" y="271" width="479" height="271"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
<Widget widgetName="chart1"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="963" height="542"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="5"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="7a99eb56-914d-480b-87a9-2150cbedf1c0"/>
</TemplateIdAttMark>
</Form>
